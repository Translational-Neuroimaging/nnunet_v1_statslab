# %% all the imports
import nibabel as nib
import numpy as np
from pathlib import Path
import copy
import numpy as np
import os

# %% pathlib import Path("../nnUNet_raw_data_base/nnUNet_raw_data")
from matplotlib import pyplot as plt

# from torchvision.io.video import av

database = Path("../../Documents/joint_p_map/for_maps")

task_name = "610"

img_dir = database / "christine"
label_610_dir = database / "610"
label_615_dir = database / "615_results"
gt_dir = database / "christine"

# %% create list for same test data experiments
list_gt = []
list_610 = []
list_615 = []
list_img = []
print("hello")
# %%
for i in img_dir.glob("*"):
    new_dir = i
    # print(i)

    for j in new_dir.glob("Masked_T2.nii.gz"):
        img_data = nib.load(j).get_fdata()
        list_img.append(img_data)

    for k in new_dir.glob("GroundTruth24h.nii.gz"):
        gt_data = nib.load(k).get_fdata()
        print(gt_data.shape)
        list_gt.append(gt_data)

# %%
for i in label_610_dir.glob("*.nii.gz"):
    label_610_data = nib.load(i).get_fdata()
    list_610.append(label_610_data)
    print(label_610_data.shape)

# %%
for i in label_615_dir.glob("*.nii.gz"):
    label_615_data = nib.load(i).get_fdata()
    list_615.append(label_615_data)
    print(label_615_data.shape)

# %% take average of all the images as the final image
join_img = np.mean(list_img, axis=0)
join_gt = np.mean(list_gt, axis=0)
join_610 = np.mean(list_610, axis=0)
join_615 = np.mean(list_615, axis=0)

# %%

type(join_img)

# %% rotate data
img_data_rot = np.rot90(join_img, 1)
gt_data_rot = np.rot90(join_gt, 1)
label_610_data_rot = np.rot90(join_610, 1)
label_615_data_rot = np.rot90(join_615, 1)


# %% create a function plot subplots of the image and the masks

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
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice), color='r', fontsize=5)
            n += 1
            slice += 5
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig


# %%
plt_5 = plot_subplots(img_data_rot, gt_data_rot, 1, 7)

# %% save the figure
plt_5.savefig("output2/615_gt.pdf", bbox_inches="tight", dpi=300)

# %%plot the final image
# plt.imshow(join_img[:, :, 78], cmap='gray')
# plt.show()

# %%
database2 = Path("../../Documents/joint_p_map")
dsc_625 = database2 / "625"

dsc_625_pred = dsc_625 / "cv_niftis_postprocessed"
dsc_625_gt = dsc_625 / "labelsTr"


# %% function to calculate dice score
def dice_score(pred, gt):
    intersection = np.sum(pred * gt)
    return (2. * intersection) / (np.sum(pred) + np.sum(gt))


# %%
list_dc = []
count = 0
for i in dsc_625_pred.glob("*.nii.gz"):
    pred_data = nib.load(i).get_fdata()

    for j in dsc_625_gt.glob("*.nii.gz"):
        if i.name == j.name:
            gt_data = nib.load(j).get_fdata()
            print(i.name)

            dc = dice_score(pred_data, gt_data)
            list_dc.append(dc)
            print(i.name + " : " + str(dc))


#%%
print("mean dice score: " + str(np.mean(list_dc)))
print("std dice score: " + str(np.std(list_dc)))