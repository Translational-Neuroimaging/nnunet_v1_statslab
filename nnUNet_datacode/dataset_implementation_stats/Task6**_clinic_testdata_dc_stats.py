import math
from pathlib import Path
import numpy as np
import nibabel as nib

# %% for loop to import data from nnUNet_raw_data_base/nnUNet_raw_data/Task6**_clinic_testdata
path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task6**_clinic_testdata")

gt_database = path / "labelsTs"

pred_2d_db = path / "results_test/Task615_2d_5fold"


# %% function to compute the dice coefficient
def dc(pred, gt):
    # calculate dice score
    intersection = np.sum(pred * gt)
    union = np.sum(pred) + np.sum(gt)
    dice = 2 * intersection / union
    return dice


# %%
def dc_from_data(pred, gt):
    gt_data = nib.load(gt).get_fdata()
    gt_array = gt_data.flatten()

    pred_data = nib.load(pred).get_fdata()
    pred_array = pred_data.flatten()

    # calculate dise score and add it in dict
    temp_pred = np.zeros_like(pred_data)
    temp_gt = np.zeros_like(gt_data)

    temp_pred[pred_data == 1] = 1
    temp_gt[gt_data == 1] = 1
    dice = dc(temp_pred, temp_gt)

    return dice


# %%
dice_all = []
for i in pred_2d_db.glob("*.nii.gz"):
    # print(i.name)

    for j in gt_database.glob("*.nii.gz"):
        if i.name == j.name:
            # print(j.name)
            dice = dc_from_data(i, j)
            print(i.name.replace(".nii.gz", "") + " : " + str(dice))
            # break
            dice_all.append(dice)

#%% mean of all dice
print("mean of all dice : " + str(np.mean(dice_all)))
