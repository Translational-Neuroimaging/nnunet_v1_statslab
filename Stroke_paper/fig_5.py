# %%
import nibabel as nib
import numpy as np
from pathlib import Path
import copy
import matplotlib.pyplot as plt
from utilities.jpm_related_functions import *


#%%
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/for_new_jpm_fig_5")

#%%
count = 0
for i in dataset_path.iterdir():
    print(i.name)
    count += 1

print(count)


#%%
data_path = dataset_path

#%%
dict = create_dict_for_mean_jpm_with_5_attr(data_path)

#%% dict to df
import pandas as pd
df = pd.DataFrame.from_dict(dict, orient='index')

#%%
img_path = dataset_path / "mean_files"

#%%
create_mean_img_jpm_with_6_attr(dict, img_path)


#%%

unet_path = img_path

for i in unet_path.iterdir():
    print(i.name)


#%%

t2_file = unet_path / "final_t2.nii.gz"
adc_file = unet_path / "final_ADC.nii.gz"
gt_file = unet_path / "final_gt.nii.gz"
spatGMM_gt_file = unet_path / "final_spatGmm_gt.nii.gz"
spatGmm_seg_file = unet_path / "final_spatGmm_seg.nii.gz"
nnUNet_seg_file = unet_path / "final_nnUNet_seg.nii.gz"


#%% check if this path exists
spatGMM_gt_file.exists()

#%% load the same file using nibabel
data = nib.load(spatGmm_seg_file).get_fdata()

#%% check if the data has more than one unique value
np.unique(data)

#%%
t2_data = nib.load(t2_file).get_fdata()
gt_data = nib.load(gt_file).get_fdata()
spatGmm_seg_data = nib.load(spatGmm_seg_file).get_fdata()
spatGMM_gt_data = nib.load(spatGMM_gt_file).get_fdata()
nnUNet_seg_data = nib.load(nnUNet_seg_file).get_fdata()
adc_data = nib.load(adc_file).get_fdata()

#%%

t2_data_rot = np.rot90(t2_data, 3)
gt_data_rot = np.rot90(gt_data, 3)
spatGmm_seg_data_rot = np.rot90(spatGmm_seg_data, 3)
spatGMM_gt_data_rot = np.rot90(spatGMM_gt_data, 3)
nnUNet_seg_data_rot = np.rot90(nnUNet_seg_data, 3)
adc_data_rot = np.rot90(adc_data, 3)


#%% plot using plot_subplots
plot_t2 = plot_subplots_single_modality(t2_data_rot, 1, 6)
plot_adc = plot_subplots_single_modality(adc_data_rot, 1, 6)
plot_gt = plot_subplots_single_modality(gt_data_rot, 1, 6)
plot_spatGmm_seg = plot_subplots_single_modality(spatGmm_seg_data_rot, 1, 6)
plot_spatGMM_gt = plot_subplots_single_modality(spatGMM_gt_data_rot, 1, 6)
plot_nnUNet_seg = plot_subplots_single_modality(nnUNet_seg_data_rot, 1, 6)

data_path = dataset_path / "jpm_files"

# save the figure
plot_t2.savefig(str(data_path) + "/t2.pdf", bbox_inches="tight")
plot_adc.savefig(str(data_path) + "/adc.pdf", bbox_inches="tight")
plot_gt.savefig(str(data_path) + "/gt.pdf", bbox_inches="tight")
plot_spatGmm_seg.savefig(str(data_path) + "/spatGmm_seg.pdf", bbox_inches="tight")
plot_spatGMM_gt.savefig(str(data_path) + "/spatGMM_gt.pdf", bbox_inches="tight")
plot_nnUNet_seg.savefig(str(data_path) + "/nnUNet_seg.pdf", bbox_inches="tight")

#%%
plt_t2_nnUNet = plot_subplots(t2_data_rot, nnUNet_seg_data_rot, 1, 6)
plt_t2_spatGmm_seg = plot_subplots(t2_data_rot, spatGmm_seg_data_rot, 1, 6)
plt_t2_spatGMM_gt = plot_subplots(t2_data_rot, spatGMM_gt_data_rot, 1, 6)
plt_t2_gt = plot_subplots(t2_data_rot, gt_data_rot, 1, 6)

# save the figure
plt_t2_nnUNet.savefig(str(data_path) + "/t2_nnUNet.pdf", bbox_inches="tight")
plt_t2_spatGmm_seg.savefig(str(data_path) + "/t2_spatGmm_seg.pdf", bbox_inches="tight")
plt_t2_spatGMM_gt.savefig(str(data_path) + "/t2_spatGMM_gt.pdf", bbox_inches="tight")
plt_t2_gt.savefig(str(data_path) + "/t2_gt.pdf", bbox_inches="tight")

#%% plot using plot_subplots
plt_t2_gt = plot_subplots(t2_data_rot, gt_data_rot, 1, 6)


# %% save the figure
plt_t2_gt.savefig(str(unet_path / task_name) + "/t2_gt.pdf", bbox_inches="tight", dpi=300)
plt_t2_unet.savefig(str(unet_path / task_name) + "/t2_unet.pdf", bbox_inches="tight", dpi=300)
plt_t2_gmm.savefig(str(unet_path / task_name) + "/tt2_gmm.pdf", bbox_inches="tight", dpi=300)
# #%% plot using plot_subplots
# plot_t2 = plot_subplots_single_modality(t2_data_changed, 1, 6)
# # save the figure
# plot_t2.savefig(str(data_path) + "/t2.pdf", bbox_inches="tight", dpi=300)


#%% plot using plot_subplots
plt_t2_gt = plot_subplots(t2_data_rot, gt_data_rot, 1, 6)
plt_t2_unet = plot_subplots(t2_data_rot, unet_data_rot, 1, 6)
plt_t2_gmm = plot_subplots(t2_data_rot, gmm_data_rot, 1, 6)

# %% save the figure
plt_t2_gt.savefig(str(unet_path / task_name) + "/t2_gt.pdf", bbox_inches="tight", dpi=300)
plt_t2_unet.savefig(str(unet_path / task_name) + "/t2_unet.pdf", bbox_inches="tight", dpi=300)
plt_t2_gmm.savefig(str(unet_path / task_name) + "/tt2_gmm.pdf", bbox_inches="tight", dpi=300)
