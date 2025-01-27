#%% loading data
from pathlib import Path
import numpy as np
import math
import nibabel as nib

#%%
database_dir = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat")
img_dir = database_dir / "imagesTs"
label_dir = database_dir / "labelsTs"


#%%

twod_result_dir = database_dir / "resultTs"
threed_result_dir = database_dir / "resultTs_3d"

#%% function to compute the dice coefficient
def dc(p, g):
    dice = np.sum(p[g == 1]) * 2.0 / (np.sum(p) + np.sum(g))
    if math.isnan(dice):
        dice = 0.0
    # print('Dice similarity score is {}'.format(dice))
    return dice


# %%
dice_all = []
for i in label_dir.glob("*"):
    # print(i.name)

    for j in twod_result_dir.glob("*.nii.gz"):
        # print(j.name)

        if i.name == j.name:
            pred_data = nib.load(i).get_fdata()
            gt_data = nib.load(j).get_fdata()

            # print(np.unique(gt_data))
            temp_pred = np.zeros_like(pred_data)
            temp_gt = np.zeros_like(gt_data)

            temp_pred[pred_data == 1] = 1
            temp_gt[gt_data == 1] = 1
            dice = dc(temp_pred, temp_gt)
            dice_all.append(dice)

            print("for " + i.name + "  dc : " + str(dice))

        # print(dice_all)
        # np.mean(dice_all)

# %% dice for 3d
dice_3d = []
for i in label_dir.glob("*"):
    # print(i.name)

    for j in threed_result_dir.glob("*.nii.gz"):
        # print(j.name)

        if i.name == j.name:
            pred_data = nib.load(i).get_fdata()
            gt_data = nib.load(j).get_fdata()

            # print(np.unique(gt_data))
            temp_pred = np.zeros_like(pred_data)
            temp_gt = np.zeros_like(gt_data)

            temp_pred[pred_data == 1] = 1
            temp_gt[gt_data == 1] = 1
            dice = dc(temp_pred, temp_gt)
            dice_3d.append(dice)

            print( i.name + "  " + str(dice))

        # print(dice_all)
        # np.mean(dice_all)


#%%
print(np.mean(dice_all))
print(np.mean(dice_3d))