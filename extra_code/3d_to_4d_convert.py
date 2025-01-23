# %%
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd

#%%
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/for_exp")
human_pred_dir = database / "result_reconstructed/human"
rat_pred_dir = database / "result_reconstructed/rat"
human_gt_dir = database / "labelsTs_reconstructed/human"
rat_gt_dir = database / "labelsTs_reconstructed/rat"
human_adc_dir = database / "adc_files/human_adc"
rat_adc_dir = database / "adc_files/rat_adc"

#%% code for human data
patient_dict = {}
for i in human_gt_dir.glob("*.nii.gz"):
    print(i.name)
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

#%% code for rat data
patient_dict = {}
for i in rat_gt_dir.glob("*.nii.gz"):
    print(i.name)
    p_id = i.name.split(".nii")[0]
    # if p_id has 2 or 3 digits, add a 0 in front
    if len(p_id) == 2:
        p_id = "00" + p_id
    elif len(p_id) == 3:
        p_id = "0" + p_id
    gt_file = i
    pred_file = rat_pred_dir / i.name
    darkfluid_name = i.name.replace(".nii.gz", "-24h.nii.gz")
    darfluid_file = rat_adc_dir / darkfluid_name
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
nib.save(gt_4d_nii, "chamba_tasks/646_4ds/rat_gt_4d.nii.gz")
pred_4d_nii = nib.Nifti1Image(pred_4d, np.eye(4))
nib.save(pred_4d_nii, "chamba_tasks/646_4ds/rat_pred_4d.nii.gz")
darfluid_4d_nii = nib.Nifti1Image(darfluid_4d, np.eye(4))
nib.save(darfluid_4d_nii, "chamba_tasks/646_4ds/rat_adc_4d.nii.gz")

# # %%
# database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task510_BrainTumour/")
# pred_dir = database / "result_2d"
# gt_dir = database / "labelsTs"
# darfluid_dir = database / "imagesTs"
#
#
# #%% add all gt, pred and darfluid files to a patient dictionary with the patient id as key and the filepath as value
# patient_dict = {}
# for i in gt_dir.glob("*.nii.gz"):
#     p_id = i.name.split(".nii")[0]
#     # if p_id has 2 or 3 digits, add a 0 in front
#     if len(p_id) == 2:
#         p_id = "00" + p_id
#     elif len(p_id) == 3:
#         p_id = "0" + p_id
#     gt_file = i
#     pred_file = pred_dir / i.name
#     darkfluid_name = i.name.replace(".nii.gz", "_0000.nii.gz")
#     darfluid_file = darfluid_dir / darkfluid_name
#     patient_dict[p_id] = {"gt_file": gt_file, "pred_file": pred_file, "darfluid_file": darfluid_file}
#     print(p_id)
#
# #%% dict to df
# patient_df = pd.DataFrame.from_dict(patient_dict, orient="index")
# #sort_index
# patient_df = patient_df.sort_index()
#
# # %% get all the data, extract nii and add it to list of arrays
# gt_list = []
# pred_list = []
# darfluid_list = []
# for i in patient_df.index:
#     gt = nib.load(patient_df.loc[i, "gt_file"])
#     gt_data = gt.get_fdata()
#     gt_list.append(gt_data)
#     pred = nib.load(patient_df.loc[i, "pred_file"])
#     pred_data = pred.get_fdata()
#     pred_list.append(pred_data)
#     darfluid = nib.load(patient_df.loc[i, "darfluid_file"])
#     darfluid_data = darfluid.get_fdata()
#     darfluid_list.append(darfluid_data)
#
#
# # %% combined all the data using np.stack from list of arrays
# gt_4d = np.stack(gt_list, axis=3)
# pred_4d = np.stack(pred_list, axis=3)
# darfluid_4d = np.stack(darfluid_list, axis=3)
#
#
# #%% save the 4d data as nii files
# gt_4d_nii = nib.Nifti1Image(gt_4d, np.eye(4))
# nib.save(gt_4d_nii, "chamba_tasks/gt_4d.nii.gz")
# pred_4d_nii = nib.Nifti1Image(pred_4d, np.eye(4))
# nib.save(pred_4d_nii, "chamba_tasks/pred_4d.nii.gz")
# darfluid_4d_nii = nib.Nifti1Image(darfluid_4d, np.eye(4))
# nib.save(darfluid_4d_nii, "chamba_tasks/darfluid_4d.nii.gz")
#
