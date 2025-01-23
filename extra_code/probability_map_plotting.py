# %%
import nibabel as nib
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt

#%%
def extract_data(img):
    # load nii data
    data = nib.load(img).get_fdata()
    # if img_data has nan values then replace them with 0
    if np.isnan(data).any():
        data[np.isnan(data)] = 0
    # return the data
    return data

#%%
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing")

#%%
task_name = "1m"

#%%
data_path = dataset_path / task_name
gt_path = data_path / "labelsTs"
seg_path = data_path / "result"
seg_path_3d = data_path / "result_3d"
t2_path = data_path / "imagesTs"

#%%
dict_task = {}

for i in seg_path.glob("*.nii.gz"):
    print(i.name)
    name = i.name.split(".nii")[0]
    print(name)
    dict_task[name] = {}

    if (t2_path / i.name.replace(".nii","_0001.nii")).exists():
        print("t2 exists")
        dict_task[name]["t2"] = str(t2_path / i.name.replace(".nii","_0001.nii"))
    if (gt_path / i.name).exists():
        print("seg exists")
        dict_task[name]["gt"] = str(gt_path / i.name)
    dict_task[name]["seg"] = str(i)
    if (seg_path_3d / i.name).exists():
        print("seg_3d exists")
        dict_task[name]["seg_3d"] = str(seg_path_3d / i.name)

#%% dict to df
import pandas as pd
df = pd.DataFrame.from_dict(dict_task, orient="index")

#%% extract data from dict and save it in another dict
dict_final_data = {}
for i in dict_task.keys():
    print(i)
    # task = dataset_path / i
    # print values of key
    print(dict_task[i])

    if "seg" in dict_task[i].keys():
        dict_final_data[i] = {"seg": extract_data(dict_task[i]["seg"])}
        if "t2" in dict_task[i].keys():
            dict_final_data[i]["t2"] = extract_data(dict_task[i]["t2"])
        if "gt" in dict_task[i].keys():
            dict_final_data[i]["gt"] = extract_data(dict_task[i]["gt"])
        if "seg_3d" in dict_task[i].keys():
            dict_final_data[i]["seg_3d"] = extract_data(dict_task[i]["seg_3d"])

#%% dict to df
# import pandas as pd
df_final_data = pd.DataFrame.from_dict(dict_final_data, orient="index")

#%% dict final data to separate lists
t2_list = []
gt_list = []
seg_list = []

print(" adding the data to the list...")
# add the data to the list from dict_final_data
for i in dict_final_data.keys():
    # print(i)
    seg_list.append(dict_final_data[i]["seg"])
    # check if there is nan values in the t2 data and if there is then replace them with 0 and add it to the list,
    # if not add to list directly
    if np.isnan(dict_final_data[i]["t2"]).any():
        dict_final_data[i]["t2"][np.isnan(dict_final_data[i]["t2"])] = 0
        t2_list.append(dict_final_data[i]["t2"])
    else:
        t2_list.append(dict_final_data[i]["t2"])
    gt_list.append(dict_final_data[i]["gt"])
print("list created")

#%%
print("saving final images for jpm")
# save the final data for therapy and control
nib.save(nib.Nifti1Image(np.mean(t2_list, axis=0), np.eye(4)), dataset_path / "jpm_&_mean_files/1m/final_t2.nii.gz")
nib.save(nib.Nifti1Image(np.mean(gt_list, axis=0), np.eye(4)), dataset_path / "jpm_&_mean_files/1m/final_gt.nii.gz")
nib.save(nib.Nifti1Image(np.mean(seg_list, axis=0), np.eye(4)), dataset_path / "jpm_&_mean_files/1m/final_seg_unet.nii.gz")

print("final images saved in folder" + str(dataset_path / "jpm_&_mean_files/1m"))









#%%
def extract_data_from_folder(folder):
    # create a list for all the data
    list_adc = []
    list_t2 = []
    list_gt = []
    for i in folder.glob("*"):
        # print(i.name)
        new_dir = i
        for j in new_dir.glob("*.nii"):
            # print(j.name)
            if j.name == "Masked_ADC.nii":
                # print(j.name)
                # extract the data
                img_data = extract_data(j)
                # if data has more than 1 unique values then add it to the list
                if len(np.unique(img_data)) > 1:
                    list_adc.append(img_data)
            elif j.name == "Masked_T2.nii":
                # print(j.name)
                # extract the data
                img_data = extract_data(j)
                # if data has more than 1 unique values then add it to the list
                if len(np.unique(img_data)) > 1:
                    list_t2.append(img_data)
            elif j.name == "GroundTruth24h.nii" or j.name == "Voi_1w.nii" or j.name == "Voi_72h.nii" or j.name == \
                    "Voi_1m.nii":
                # print(j.name)
                # extract the data
                img_data = extract_data(j)
                # print unique values
                # if data has more than 1 unique values then add it to the list
                if len(np.unique(img_data)) > 1:
                    list_gt.append(img_data)
    return list_adc, list_t2, list_gt


# %%
# task = database / "Rats1m"
# therapy_adc, therapy_t2, therapy_gt = extract_data_from_folder_1(task / "therapy")
# control_adc, control_t2, control_gt = extract_data_from_folder_1(task / "control")



# %% create a function for code 1 to 4
def create_final_data(task, database):
    # extract the data from the therapy folder
    therapy_adc, therapy_t2, therapy_gt = extract_data_from_folder(task / "therapy")
    # extract the data from the control folder
    control_adc, control_t2, control_gt = extract_data_from_folder(task / "control")

    # create a new folder for the final data
    final_data = database / "final_data" / task.name
    # if the folder does not exist then create it
    if not final_data.exists():
        final_data.mkdir(parents=True)

    # save the final data for therapy and control
    nib.save(nib.Nifti1Image(np.mean(therapy_adc, axis=0), np.eye(4)), final_data / "final_adc_therapy.nii.gz")
    nib.save(nib.Nifti1Image(np.mean(therapy_t2, axis=0), np.eye(4)), final_data / "final_t2_therapy.nii.gz")
    nib.save(nib.Nifti1Image(np.mean(therapy_gt, axis=0), np.eye(4)), final_data / "final_gt_therapy.nii.gz")

    nib.save(nib.Nifti1Image(np.mean(control_adc, axis=0), np.eye(4)), final_data / "final_adc_control.nii.gz")
    nib.save(nib.Nifti1Image(np.mean(control_t2, axis=0), np.eye(4)), final_data / "final_t2_control.nii.gz")
    nib.save(nib.Nifti1Image(np.mean(control_gt, axis=0), np.eye(4)), final_data / "final_gt_control.nii.gz")

#%%


#%%
database = Path("output")

for i in database.glob("*.nii.gz"):
    print(i)


#%% print current working directory
import os
print(os.getcwd())


#%%
img_path = database / "final_img_625.nii.gz"
img_data = nib.load(img_path).get_fdata()

gt_path = database / "final_gt_625.nii.gz"
gt_data = nib.load(gt_path).get_fdata()

segmentation_path_615 = database / "final_segmentation_625.nii.gz"
segmentation_data_610 = nib.load(segmentation_path_615).get_fdata()

# segmentation_path_620 = database / "final_segmentation_620.nii.gz"
# segmentation_data_620 = nib.load(segmentation_path_620).get_fdata()


#%%
print(gt_data.shape)

#%% rotate data
img_data_rot = np.rot90(img_data, 1)
gt_data_rot = np.rot90(gt_data, 1)
segmentation_data_610_rot = np.rot90(segmentation_data_610, 1)

#%% create a function plot subplots of the image and the masks

def plot_subplots(image, mask_img, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    my_cmap = copy.copy(plt.cm.get_cmap('gray'))  # get a copy of the gray color map
    my_cmap.set_bad(alpha=0)

    n = 0
    slice = 60
    for _ in range(n_rows):
        for _ in range(n_cols):

            # ax[n].imshow(image[:, :, slice])
            ax[n].imshow(image[:, :, slice], cmap='gray')
            ax[n].imshow(mask_img[:, :, slice], cmap='Greens', alpha=0.7)
            # ax[n].imshow(mask_img[:, :, slice], cmap='Purples', alpha=0.7)
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            #hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice), color='r', fontsize=5)
            n += 1
            slice += 5
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig

#%%
plt_5 = plot_subplots(img_data_rot, segmentation_data_610_rot, 1, 7)

#%% save the figure
plt_5.savefig("output1/625_segmentation.pdf", bbox_inches="tight", dpi=300)
