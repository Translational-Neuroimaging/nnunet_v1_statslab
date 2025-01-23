# %%
from pathlib import Path
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# %%
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/for_exp")
human_pred_dir = database / "result_reconstructed/human"
rat_pred_dir = database / "result_reconstructed/rat"
human_gt_dir = database / "labelsTs_reconstructed/human"
rat_gt_dir = database / "labelsTs_reconstructed/rat"
human_adc_dir = database / "adc_files/human_adc"
rat_adc_dir = database / "adc_files/rat_adc"

# %%
human11_adc = nib.load(rat_adc_dir / "Rat095-24h.nii.gz").get_fdata()
human11_pred = nib.load(rat_pred_dir / "Rat095.nii.gz").get_fdata()
human11_gt = nib.load(rat_gt_dir / "Rat095.nii.gz").get_fdata()
print(human11_adc.shape)
print(human11_pred.shape)
print(human11_gt.shape)

#%%
np.unique(human11_pred)

# %% rotate by 3
human11_adc_rot = np.rot90(human11_adc, 3)
human11_pred_rot = np.rot90(human11_pred, 3)
human11_gt_rot = np.rot90(human11_gt, 3)


# %% create a function plot subplots of the image and the masks

def plot_subplots(image, mask_img, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 40
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
            slice_no += 8
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig


# %% create a function plot subplots of the images only

def plot_subplots_single_modality(image, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 40
    for _ in range(n_rows):
        for _ in range(n_cols):
            ax[n].imshow(image[:, :, slice_no], cmap='gray')
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice_no), color='r', fontsize=5)
            n += 1
            slice_no += 8
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig


# %% # if the data hads nan values, the nan values are replaced with 0
if np.isnan(human11_adc_rot).any():
    human11_adc_rot[np.isnan(human11_adc_rot)] = 0
if np.isnan(human11_pred_rot).any():
    human11_pred_rot[np.isnan(human11_pred_rot)] = 0
if np.isnan(human11_gt_rot).any():
    human11_gt_rot[np.isnan(human11_gt_rot)] = 0


#%% mirror the data along the axis 1
human11_adc_rot = np.flip(human11_adc_rot, axis=1)
human11_pred_rot = np.flip(human11_pred_rot, axis=1)
human11_gt_rot = np.flip(human11_gt_rot, axis=1)


# %% folder to save the plots
plot_path = "new_plots"
# craete a folder if it does not exist
if not Path(plot_path).exists():
    Path(plot_path).mkdir()


#%%
plt_adc = plot_subplots_single_modality(human11_adc_rot, 1, 8)
plt_adc_gt = plot_subplots(human11_adc_rot, human11_gt_rot, 1, 8)
plt_adc_pred = plot_subplots(human11_adc_rot, human11_pred_rot, 1, 8)

#%%
plt_adc.savefig(plot_path + "/human11_adc_rot.png", bbox_inches='tight')
plt_adc_gt.savefig(plot_path + "/human11_adc_gt_rot.png", bbox_inches='tight')
plt_adc_pred.savefig(plot_path + "/human11_adc_pred_rot.png", bbox_inches='tight')

# %% plot the subplots of the t2 therapy data and the mask data same for the adc data
plt_t2_gt = plot_subplots(therapy_t2, therapy_gt, 1, 5)
plt_adc_gt = plot_subplots(therapy_adc, therapy_gt, 1, 5)

# %% folder to save the plots
plot_path = "new_plots/" + task.name
# craete a folder if it does not exist
if not Path(plot_path).exists():
    Path(plot_path).mkdir()

# %% save the figure
plt_t2_gt.savefig(plot_path + "/therapy_t2_gt.pdf", bbox_inches="tight", dpi=300)
plt_adc_gt.savefig(plot_path + "/therapy_adc_gt.pdf", bbox_inches="tight", dpi=300)

# %% plot only adc and ony t2
plt_t2 = plot_subplots_single_modality(therapy_t2, 1, 5)
plt_adc = plot_subplots_single_modality(therapy_adc, 1, 5)

# %% save the figure
plt_t2.savefig(plot_path + "/therapy_t2.pdf", bbox_inches="tight", dpi=300)
plt_adc.savefig(plot_path + "/therapy_adc.pdf", bbox_inches="tight", dpi=300)

# %% re-run the code for the control data
control_t2, control_adc, control_gt = get_data_jpm_plotting(task, "control")

# %%
# if the data hads nan values, the nan values are replaced with 0
if np.isnan(control_t2).any():
    control_t2[np.isnan(control_t2)] = 0
if np.isnan(control_adc).any():
    control_adc[np.isnan(control_adc)] = 0
if np.isnan(control_gt).any():
    control_gt[np.isnan(control_gt)] = 0

# %% code 1
control_t2 = control_t2[15:75, 5:87, :]
control_adc = control_adc[15:75, 5:87, :]
control_gt = control_gt[15:75, 5:87, :]
# mirror the data
control_t2 = np.flip(control_t2, axis=1)
control_adc = np.flip(control_adc, axis=1)
control_gt = np.flip(control_gt, axis=1)

# %% plot the subplots of the t2 therapy data and the mask data same for the adc data
plt_t2_gt = plot_subplots(control_t2, control_gt, 1, 5)
plt_adc_gt = plot_subplots(control_adc, control_gt, 1, 5)

# %% save the figure
plt_t2_gt.savefig(plot_path + "/control_t2_gt.pdf", bbox_inches="tight", dpi=300)
plt_adc_gt.savefig(plot_path + "/control_adc_gt.pdf", bbox_inches="tight", dpi=300)

# %% plot only adc and ony t2
plt_t2 = plot_subplots_single_modality(control_t2, 1, 5)
plt_adc = plot_subplots_single_modality(control_adc, 1, 5)

# %% save the figure
plt_t2.savefig(plot_path + "/control_t2.pdf", bbox_inches="tight", dpi=300)
plt_adc.savefig(plot_path + "/control_adc.pdf", bbox_inches="tight", dpi=300)
#
# #%% plot t2 and gt from therapy data
# plt.imshow(therapy_t2[:, :, 78], cmap='gray')
# plt.show()
