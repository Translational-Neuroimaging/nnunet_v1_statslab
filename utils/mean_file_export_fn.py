# %%
from shutil import copytree

import nibabel as nib
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt

# %%
database = Path("../../../Documents/data/adrian_data/devided")


# %% create a function to extract all the data from img and add in to the list
def extract_data(img):
    # load nii data
    data = nib.load(img).get_fdata()
    # if img_data has nan values then replace them with 0
    # if np.isnan(data).any():
    #     data[np.isnan(data)] = 0
    # return the data
    return data


# %% create a function for the upper code
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


# %% updated code
def extract_data_from_folder_1(folder):
    # create a list for all the data
    list_adc = []
    list_t2 = []
    list_gt = []
    for i in folder.glob("*"):
        # print(i.name)
        new_dir = i
        for j in new_dir.glob("*.nii"):
            # print(j.name)
            for j in new_dir.glob("*.nii"):
                # print(j.name)
                if j.name == "Masked_ADC.nii":
                    adc_data = extract_data(j)
                elif j.name == "Masked_T2.nii":
                    t2_data = extract_data(j)
                elif j.name == "GroundTruth24h.nii" or j.name == "Voi_1w.nii" or j.name == "Voi_72h.nii" or j.name == \
                        "Voi_1m.nii":
                    gt_data = extract_data(j)
                # if adc data has more than 1 unique values then add all the data to the corresponding list
                if len(np.unique(adc_data)) > 1:
                    list_adc.append(adc_data)
                    list_t2.append(t2_data)
                    list_gt.append(gt_data)
    return list_adc, list_t2, list_gt


# %%
task = database / "Rats1m"
therapy_adc, therapy_t2, therapy_gt = extract_data_from_folder_1(task / "therapy")
control_adc, control_t2, control_gt = extract_data_from_folder_1(task / "control")

# %% print length of the list
print(len(therapy_adc))
print(len(therapy_t2))
print(len(therapy_gt))
print(len(control_gt))
print(len(control_adc))
print(len(control_t2))


# %% create a function for code 5


# %% create a function for code 1 to 4
def create_final_data(task):
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


# %%
create_final_data(database / "Rats24h")

# %%
create_final_data(database / "Rats72h")

# %%
create_final_data(database / "Rats1w")

# %%
create_final_data(database / "Rats1m")

# %%

therapy_1m_folder = database / "Rats1w" / "therapy"
adc_list = []
t2_list = []
gt_list = []
for i in therapy_1m_folder.glob("*"):
    # print(i.name)

    new_dir = i
    # for adc
    for j in new_dir.glob("Masked_T2.nii"):
        print(i.name)

        img = nib.load(j)
        img_data = np.array(img.dataobj)
        # if data is an empty array the don't append the i.name in list
        if len(np.unique(img_data)) > 1:
            adc_list.append(i.name)

    # for t2
    for j in new_dir.glob("Masked_T2.nii"):
        print(i.name)

        img = nib.load(j)
        img_data = np.array(img.dataobj)
        # if data is an empty array the don't append the i.name in list
        if len(np.unique(img_data)) > 1:
            t2_list.append(i.name)

    # for gt
    for j in new_dir.glob("Voi_1w.nii"):
        print(i.name)

        img = nib.load(j)
        img_data = np.array(img.dataobj)
        # if data is an empty array the don't append the i.name in list
        if len(np.unique(img_data)) > 1:
            gt_list.append(i.name)

# %%
print(adc_list)
print(t2_list)
print(len(gt_list))

# %%
for i in therapy_1m_folder.glob("*"):
    print(i.name)
    if i.name in adc_list:
        src = therapy_1m_folder / i.name
        dst = database / "rearranged" / "Rats1w" / "therapy" / i.name
        copytree(src, dst)


# %%
def img_to_array(data):
    img = nib.load(data)
    img_data = np.array(img.dataobj)
    # if img data had nan values then replace it with 0
    img_data[np.isnan(img_data)] = 0
    return img_data


# %%
new_fold = database / "rearranged" / "Rats1m" / "therapy"
# list
adc_list = []
t2_list = []
gt_list = []
for i in new_fold.glob("*"):
    new_dir = i

    for j in new_dir.glob("*.nii"):
        if j.name == "Masked_ADC.nii":
            print(j.name)
            adc_data = img_to_array(j)
            adc_list.append(adc_data)
        elif j.name == "Masked_T2.nii":
            t2_data = img_to_array(j)
            t2_list.append(t2_data)
        elif j.name == "GroundTruth24h.nii" or j.name == "Voi_1w.nii" or j.name == "Voi_72h.nii" or j.name == \
                "Voi_1m.nii":
            gt_data = img_to_array(j)
            gt_list.append(gt_data)

# %%
print(len(adc_list))
print(len(t2_list))
print(len(gt_list))


#%% get mean of all the data
adc_mean = np.mean(adc_list, axis=0)
t2_mean = np.mean(t2_list, axis=0)
gt_mean = np.mean(gt_list, axis=0)

# %%
# save this data in a new folder
final_data = database / "rearranged_final_data"
if not final_data.exists():
    final_data.mkdir(parents=True)
#save the data as nifiti file
nib.save(nib.Nifti1Image(adc_mean, np.eye(4)), final_data / "1m_adc_therapy.nii.gz")
nib.save(nib.Nifti1Image(t2_mean, np.eye(4)), final_data / "1m_t2_therapy.nii.gz")
nib.save(nib.Nifti1Image(gt_mean, np.eye(4)), final_data / "1m_gt_therapy.nii.gz")


#%%