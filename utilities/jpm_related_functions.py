# %%
import nibabel as nib
import numpy as np
from pathlib import Path
import copy
import matplotlib.pyplot as plt

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
def seg_list(seg_path):
    seg_list = []
    for i in seg_path.glob("*.nii.gz"):
        seg_list.append(i.name.split(".nii")[0])
    return seg_list

#%%
def create_dict_for_mean_jpm(data_path):
    dict_final_data = {}
    gt_path = data_path / "labelsTs"
    seg_path = data_path / "result"
    seg_path_3d = data_path / "result_3d"
    t2_path = data_path / "imagesTs"

    print("checking all the paths")
    # print the paths
    print("gt path : " + str(gt_path))
    print("seg path : " + str(seg_path))
    print("seg path 3d : " + str(seg_path_3d))

    for i in seg_path.glob("*.nii.gz"):
        # print(i.name)
        name = i.name.split(".nii")[0]
        print(name)
        dict_final_data[name] = {}

        if (t2_path / i.name.replace(".nii","_0001.nii")).exists():
            # print("t2 exists")
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["t2"] = extract_data(t2_path / i.name.replace(".nii","_0001.nii"))
        if (gt_path / i.name).exists():
            # print("seg exists")
            # dict_task[name]["gt"] = str(gt_path / i.name)
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["gt"] = extract_data(gt_path / i.name)
        dict_final_data[name]["seg"] = extract_data(seg_path / i.name)
        # dict_task[name]["seg"] = str(i)
        if (seg_path_3d / i.name).exists():
            # print("seg_3d exists")
            # dict_task[name]["seg_3d"] = str(seg_path_3d / i.name)
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["seg_3d"] = extract_data(seg_path_3d / i.name)

    print(" added all the extracted data to the dictionary")
    # print the dictionary
    # print(dict_task)

    return dict_final_data

#%%
def create_dict_for_mean_jpm_with_5_attr(data_path):
    dict_final_data = {}
    gt_path = data_path / "gt"
    nnUNet_seg_path = data_path / "nnUNet_results"
    spatGmm_seg_path = data_path / "SpatGmm_results"
    spatGmm_gt_path = data_path / "SpatGmm_gt"
    t2_path = data_path / "imagesTs"
    ADC_path = data_path / "imagesTs"

    print("checking all the paths")
    # if paths exist, print them
    if gt_path.exists():
        print("gt path : " + str(gt_path))
    if nnUNet_seg_path.exists():
        print("nnUNet_seg_path : " + str(nnUNet_seg_path))
    if spatGmm_seg_path.exists():
        print("spatGmm_seg_path : " + str(spatGmm_seg_path))
    if spatGmm_gt_path.exists():
        print("spatGmm_gt_path : " + str(spatGmm_gt_path))
    if t2_path.exists():
        print("t2_path : " + str(t2_path))
    if ADC_path.exists():
        print("ADC_path : " + str(ADC_path))


    for i in spatGmm_seg_path.glob("*.nii.gz"):
        # print(i.name)
        name = i.name.split(".nii")[0]
        print(name)
        dict_final_data[name] = {}

        if (t2_path / i.name.replace(".nii","_0001.nii")).exists():
            # print("t2 exists")
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["t2"] = extract_data(t2_path / i.name.replace(".nii","_0001.nii"))
        if (ADC_path / i.name.replace(".nii","_0000.nii")).exists():
            # print("ADC exists")
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["ADC"] = extract_data(ADC_path / i.name.replace(".nii","_0000.nii"))
        if (gt_path / i.name).exists():
            # print("seg exists")
            # dict_task[name]["gt"] = str(gt_path / i.name)
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["gt"] = extract_data(gt_path / i.name)
        if (spatGmm_gt_path / i.name).exists():
            # print("seg_3d exists")
            # dict_task[name]["seg_3d"] = str(seg_path_3d / i.name)
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["spatGmm_gt"] = extract_data(spatGmm_gt_path / i.name)
        if (nnUNet_seg_path / i.name).exists():
            # print("seg_3d exists")
            # dict_task[name]["seg_3d"] = str(seg_path_3d / i.name)
            # extract the data and add it to the dictionary dict_final_data
            dict_final_data[name]["nnUNet_seg"] = extract_data(nnUNet_seg_path / i.name)
        dict_final_data[name]["spatGmm_seg"] = extract_data(spatGmm_seg_path / i.name)

    print(" added all the extracted data to the dictionary")
    # print the dictionary
    # print(dict_task)

    return dict_final_data

# %% control therapy separate mean files foe jpm
def create_dict_for_mean_jpm_control_therapy(filepath):
    dict_final_data_therapy = {}
    dict_final_data_control = {}

    # get the list of all the control files
    control_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
    control_data_list = []
    for i in control_path.iterdir():
        print(i.name)
        control_data_name = i.name.split("-")[0]
        print(control_data_name)
        # add it to list
        control_data_list.append(control_data_name)

    gt_path = filepath / "labelsTs"
    seg_path = filepath / "result"
    t2_path = filepath / "imagesTs"

    print("checking all the paths")
    # print the paths
    print("gt path : " + str(gt_path))
    print("seg path : " + str(seg_path))

    for i in seg_path.glob("*.nii.gz"):
        # print(i.name)
        name = i.name.split(".nii")[0]
        print(name)

        if name in control_data_list:
            print(i.name  + "  control")
            dict_final_data_control[name] = {}

            if (t2_path / i.name.replace(".nii", "_0001.nii")).exists():
                # print("t2 exists")
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data_control[name]["t2"] = extract_data(t2_path / i.name.replace(".nii", "_0001.nii"))
            if (gt_path / i.name).exists():
                # print("seg exists")
                # dict_task[name]["gt"] = str(gt_path / i.name)
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data_control[name]["gt"] = extract_data(gt_path / i.name)
            dict_final_data_control[name]["seg"] = extract_data(seg_path / i.name)
        else:
            print(i.name + "  therapy")
            dict_final_data_therapy[name] = {}

            if (t2_path / i.name.replace(".nii", "_0001.nii")).exists():
                # print("t2 exists")
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data_therapy[name]["t2"] = extract_data(t2_path / i.name.replace(".nii", "_0001.nii"))
            if (gt_path / i.name).exists():
                # print("seg exists")
                # dict_task[name]["gt"] = str(gt_path / i.name)
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data_therapy[name]["gt"] = extract_data(gt_path / i.name)
            dict_final_data_therapy[name]["seg"] = extract_data(seg_path / i.name)

    print(" added all the extracted data to the dictionary")
    # print the dictionary
    # print(dict_task)

    return dict_final_data_control, dict_final_data_therapy

#%% from list fro gmm
def create_dict_for_mean_jpm_with_list(data_path, seg_list):
    dict_final_data = {}
    gt_path = data_path / "labelsTs"
    seg_path = data_path / "result"
    seg_path_3d = data_path / "result_3d"
    t2_path = data_path / "imagesTs"

    print("checking all the paths")
    # print the paths
    print("gt path : " + str(gt_path))
    print("seg path : " + str(seg_path))
    print("seg path 3d : " + str(seg_path_3d))

    for i in seg_path.glob("*.nii"):
        # print(i.name)
        name = i.name.split(".nii")[0]
        print(name)
        if name in seg_list:
            dict_final_data[name] = {}

            if (t2_path / i.name.replace(".nii","_0001.nii")).exists():
                # print("t2 exists")
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data[name]["t2"] = extract_data(t2_path / i.name.replace(".nii","_0001.nii"))
            if (gt_path / i.name).exists():
                # print("seg exists")
                # dict_task[name]["gt"] = str(gt_path / i.name)
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data[name]["gt"] = extract_data(gt_path / i.name)
            dict_final_data[name]["seg"] = extract_data(seg_path / i.name)
            # dict_task[name]["seg"] = str(i)
            if (seg_path_3d / i.name).exists():
                # print("seg_3d exists")
                # dict_task[name]["seg_3d"] = str(seg_path_3d / i.name)
                # extract the data and add it to the dictionary dict_final_data
                dict_final_data[name]["seg_3d"] = extract_data(seg_path_3d / i.name)
        else:
            print(name  + " not in the list")

    print(" added all the extracted data to the dictionary")
    # print the dictionary
    # print(dict_task)

    return dict_final_data



#%% code 123
def create_mean_img_jpm(dict_final_data, jpm_img_path):
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
        # if dict_final_data has t2 data
        if "t2" in dict_final_data[i].keys():
            if np.isnan(dict_final_data[i]["t2"]).any():
                dict_final_data[i]["t2"][np.isnan(dict_final_data[i]["t2"])] = 0
                t2_list.append(dict_final_data[i]["t2"])
            else:
                t2_list.append(dict_final_data[i]["t2"])
        # if dict_final_data has gt data
        if "gt" in dict_final_data[i].keys():
            gt_list.append(dict_final_data[i]["gt"])
    print("list created")

    print("saving final images for jpm")
    # save the final images
    #if list exists
    if len(t2_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(t2_list, axis=0), np.eye(4)), jpm_img_path / "final_t2.nii.gz")
    if len(gt_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(gt_list, axis=0), np.eye(4)), jpm_img_path / "final_gt.nii.gz")
    nib.save(nib.Nifti1Image(np.mean(seg_list, axis=0), np.eye(4)), jpm_img_path / "final_seg.nii.gz")

    # if final seg nii.gz exists in jpm_img_path then print the message
    if (jpm_img_path / "final_seg.nii.gz").exists():
        print("final images saved in folder" + str(jpm_img_path))


#%% create a function uaing code 123 with 6 attributes t2, adc, gt, nnUNet_seg, spatGmm_seg, spatGmm_gt
def create_mean_img_jpm_with_6_attr(dict_final_data, jpm_img_path):
    t2_list = []
    gt_list = []
    ADC_list = []
    nnUNet_seg_list = []
    spatGmm_seg_list = []
    spatGmm_gt_list = []

    print(" adding the data to the list...")

    # add the data to the list from dict_final_data
    for i in dict_final_data.keys():
        print(i)
        # check if there is nan values in the t2 data and if there is then replace them with 0 and add it to the list,
        # if not add to list directly
        # if dict_final_data has t2 data
        if "t2" in dict_final_data[i].keys():
            if np.isnan(dict_final_data[i]["t2"]).any():
                dict_final_data[i]["t2"][np.isnan(dict_final_data[i]["t2"])] = 0
                t2_list.append(dict_final_data[i]["t2"])
            else:
                t2_list.append(dict_final_data[i]["t2"])
        # if dict_final_data has gt data
        if "gt" in dict_final_data[i].keys():
            gt_list.append(dict_final_data[i]["gt"])
        # if dict_final_data has ADC data
        if "ADC" in dict_final_data[i].keys():
            ADC_list.append(dict_final_data[i]["ADC"])
        # if dict_final_data has nnUNet_seg data
        if "nnUNet_seg" in dict_final_data[i].keys():
            nnUNet_seg_list.append(dict_final_data[i]["nnUNet_seg"])
        # if dict_final_data has spatGmm_seg data
        if "spatGmm_seg" in dict_final_data[i].keys():
            spatGmm_seg_list.append(dict_final_data[i]["spatGmm_seg"])
        # if dict_final_data has spatGmm_gt data
        if "spatGmm_gt" in dict_final_data[i].keys():
            spatGmm_gt_list.append(dict_final_data[i]["spatGmm_gt"])
    print("list created")

    # spatGmm_gt_list has more than 1 unique values print the message
    if len(np.unique(spatGmm_gt_list)) > 1:
        print("spatGmm_gt_list has more than 1 unique values")

    print("saving final images for jpm")
    # save the final images
    #if list exists
    if len(t2_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(t2_list, axis=0), np.eye(4)), jpm_img_path / "final_t2.nii.gz")
    if len(gt_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(gt_list, axis=0), np.eye(4)), jpm_img_path / "final_gt.nii.gz")
    if len(ADC_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(ADC_list, axis=0), np.eye(4)), jpm_img_path / "final_ADC.nii.gz")
    if len(nnUNet_seg_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(nnUNet_seg_list, axis=0), np.eye(4)), jpm_img_path / "final_nnUNet_seg.nii.gz")
    if len(spatGmm_seg_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(spatGmm_seg_list, axis=0), np.eye(4)), jpm_img_path / "final_spatGmm_seg.nii.gz")
    if len(spatGmm_gt_list) > 0:
        nib.save(nib.Nifti1Image(np.mean(spatGmm_gt_list, axis=0), np.eye(4)), jpm_img_path / "final_spatGmm_gt.nii.gz")

    # if final seg nii.gz exists in jpm_img_path then print the message
    if (jpm_img_path / "final_spatGmm_gt.nii.gz").exists():
        print("final images saved in folder" + str(jpm_img_path))


# %% create a function plot subplots of the image and the masks

def plot_subplots(image, mask_img, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 45
    for _ in range(n_rows):
        for _ in range(n_cols):
            ax[n].imshow(image[:, :, slice_no], cmap='gray')
            ax[n].imshow(mask_img[:, :, slice_no], cmap='hot', alpha=0.7, vmin=0, vmax=1)
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice_no), color='r', fontsize=5)
            n += 1
            slice_no += 10
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig


#%%
def plot_subplots_single_modality(image, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 45
    for _ in range(n_rows):
        for _ in range(n_cols):
            ax[n].imshow(image[:, :, slice_no], cmap='gray')
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice_no), color='r', fontsize=5)
            n += 1
            slice_no += 10
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig






#%% old functions
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