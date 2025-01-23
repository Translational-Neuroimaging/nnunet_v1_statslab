# %% managing imports
from pathlib import Path
import nibabel as nib
import numpy as np
import os

import patchify as patchify

# %% import data from Documents/data/adrian_data
input_Human_folder = Path("../../../Documents/data/adrian_data/Human_labelled")
input_rat_folder = Path("../../../Documents/data/adrian_data/Christine_data_Rat24h_devided")
rat_test_folder = input_rat_folder / "christine_therapy_data"

#%%
output_human = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/human_adc")
output_rat = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/rat_adc")

#%% code 1
for i in input_Human_folder.glob("*"):
    print(i.name)
    new_dir = i
    new_dir_name = i.name
    for j in new_dir.glob("Masked_ADC.nii"):
        print(j.name)
        adc = nib.load(j)
        adc_data = adc.get_fdata()
        print(adc_data.shape)

        # reshape to 120,135,120
        adc_data = adc_data[0:120,0:135,0:120]
        print(adc_data.shape)

        # save the reshaped data to output folder human
        nii_file = nib.Nifti1Image(adc_data, np.eye(4))
        file_name = new_dir_name + '.nii.gz'
        file_path = output_human / file_name
        nib.save(nii_file, file_path)

#%% code 1 for rat data for 90,90,120
for i in rat_test_folder.glob("*"):
    print(i.name)
    new_dir = i
    new_dir_name = i.name
    for j in new_dir.glob("60.gz"):
        print(j.name)
        adc = nib.load(j)
        adc_data = adc.get_fdata()
        print(adc_data.shape)

        # reshape to 90,90,120
        adc_data = adc_data[0:90,0:90,0:120]
        print(adc_data.shape)

        # save the reshaped data to output folder human
        nii_file = nib.Nifti1Image(adc_data, np.eye(4))
        file_name = new_dir_name + '.nii.gz'
        file_path = output_rat / file_name
        nib.save(nii_file, file_path)


#%%
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/result_2d_reconstructed")
out = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/for_exp/result_reconstructed")

#%%
for i in database.glob("*"):
    print(i.name)
    # if name starts with Human then savbe it in human folder else save it in rat folder
    if i.name.startswith("Human"):
        new_path = out / "human"
        # copy the file to the new path
        os.system(f"cp {i} {new_path}")
    elif i.name.startswith("Rat"):
        new_path = out / "rat"
        # copy the file to the new path
        os.system(f"cp {i} {new_path}")


# %%
import pandas as pd


#%%
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/for_exp")
human_pred_dir = database / "result_reconstructed/human"
rat_pred_dir = database / "result_reconstructed/rat"
human_gt_dir = database / "labels_reconstructed/human"
rat_gt_dir = database / "labels_reconstructed/rat"
human_adc_dir = database / "adc_files/human"
rat_adc_dir = database / "adc_files/rat"


#%% add all gt, pred and darfluid files to a patient dictionary with the patient id as key and the filepath as value
# code 1
patient_dict = {}
for i in human_gt_dir.glob("*.nii.gz"):
    p_id = i.name.split(".nii")[0]
    # if p_id has 2 or 3 digits, add a 0 in front
    if len(p_id) == 2:
        p_id = "00" + p_id
    elif len(p_id) == 3:
        p_id = "0" + p_id
    gt_file = i
    pred_file = human_pred_dir / i.name
    # darkfluid_name = i.name.replace(".nii.gz", "_0000.nii.gz")
    darfluid_file = human_adc_dir / i.name
    patient_dict[p_id] = {"gt_file": gt_file, "pred_file": pred_file, "darfluid_file": darfluid_file}
    print(p_id)

#%% dict to df
patient_df = pd.DataFrame.from_dict(patient_dict, orient="index")
#sort_index
patient_df = patient_df.sort_index()

# %% get all the data, extract nii and add it to list of arrays
gt_list = []
pred_list = []
darfluid_list = []
for i in patient_df.index:
    gt = nib.load(patient_df.loc[i, "gt_file"])
    gt_data = gt.get_fdata()
    gt_list.append(gt_data)
    pred = nib.load(patient_df.loc[i, "pred_file"])
    pred_data = pred.get_fdata()
    pred_list.append(pred_data)
    darfluid = nib.load(patient_df.loc[i, "darfluid_file"])
    darfluid_data = darfluid.get_fdata()
    darfluid_list.append(darfluid_data)


# %% combined all the data using np.stack from list of arrays
gt_4d = np.stack(gt_list, axis=3)
pred_4d = np.stack(pred_list, axis=3)
darfluid_4d = np.stack(darfluid_list, axis=3)


#%% save the 4d data as nii files
gt_4d_nii = nib.Nifti1Image(gt_4d, np.eye(4))
nib.save(gt_4d_nii, "chamba_tasks/gt_4d.nii.gz")
pred_4d_nii = nib.Nifti1Image(pred_4d, np.eye(4))
nib.save(pred_4d_nii, "chamba_tasks/pred_4d.nii.gz")
darfluid_4d_nii = nib.Nifti1Image(darfluid_4d, np.eye(4))
nib.save(darfluid_4d_nii, "chamba_tasks/darfluid_4d.nii.gz")






#%%
path = Path("../../../Downloads")

output_data = path / "data"

for i in path.glob("Human31.nii"):
    print(i.name)
    img = nib.load(i)
    nib.save(img, str(path / i.name) + ".gz")






# img = nib.load(i)
# nib.save(img, i.with_suffix(".nii.gz"))
