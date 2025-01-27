import math

import numpy as np
from  pathlib import Path
import nibabel as nib

#%% craete a function to calculate dice score


# def dc(pred_data, gt_data):
#     """
#     calculate dice score
#     """
#     temp_pred = np.zeros_like(pred_data)
#     temp_gt = np.zeros_like(gt_data)
#
#     temp_pred[pred_data == 1] = 1
#     temp_gt[gt_data == 1] = 1
#     dice = 2 * np.sum(temp_pred * temp_gt) / (np.sum(temp_pred) + np.sum(temp_gt))
#     return dice


#%% import data of segmematation_results_adrian/
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian")

gt_dir = database / "Task620" / "gt_files"
pred_dir = database / "Task620" / "3d_fullres"
list_dc = []

for i in pred_dir.glob("*.nii"):

    for j in gt_dir.glob("*.nii.gz"):
         if j.name.replace(".nii.gz", ".nii") == i.name:
             gt_data = nb.load(j).get_fdata()
             gt_array = gt_data.flatten()

             pred_data = nb.load(i).get_fdata()
             pred_array = pred_data.flatten()

             dice = dc(pred_array, gt_array)
             list_dc.append(dice)
             print(dice)


#%%
np.mean(list_dc)

#%%
np.std(list_dc)

#%% find the no of data in the list
len(list_dc)




#%%

# %%
database = Path("../../Documents/exp_results/")

task_name = "Task610"

label_dir = database / task_name / "labelsTs"
result_2d_dir = database / task_name / "resultTs"
result_3d_dir = database / task_name / "resultTs_3d"


# %% craete a function to calculate the dice score
def dc(p, g):
    dice = np.sum(p[g == 1]) * 2.0 / (np.sum(p) + np.sum(g))
    if math.isnan(dice):
        dice = 0.0
    # print('Dice similarity score is {}'.format(dice))
    return dice

# %% Task 610
dice_2d = []
dice_3d = []
for i in label_dir.glob("*.nii.gz"):
    # print(i.name)
    label_data = nib.load(i).get_fdata()
    # label_array = label_data.flatten()
    # print(label_array.shape)

    for j in result_3d_dir.glob("*.nii.gz"):

        if i.name == j.name:
            pred_data = nib.load(j).get_fdata()
            # pred_array = pred_data.flatten()

            # calculate dice score and add it in dict
            dice = dc(pred_data, label_data)
            print(i.name + " " + "  dice 2d : " + " " + str(dice))
            dice_2d


    for k in result_3d_dir.glob("*.nii.gz"):

        if i.name == k.name:
            pred_3d_data = nib.load(k).get_fdata()
            # pred_3d_array = pred_3d_data.flatten()

            # calculate dice score and add it in dict
            dice_3d = dc(pred_3d_data, label_data)
            print(i.name + " " + "  dice 3d : " + " " + str(dice_3d))
            dice_3d.append(dice_3d)



# %%
dice



