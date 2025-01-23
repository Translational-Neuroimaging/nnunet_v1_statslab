from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from scipy.ndimage import interpolation

img_dir = Path("../nnUNet_raw_data_base/nnUNet_raw_data/main_training_data_for_testing")

# %%
original_data = img_dir / "images_tr_converted"
labels = img_dir / "labels"
predicted_dir = img_dir / "prediction_files_for_dc"

# %%

img = nib.load(original_data / "BRATS_1020_0002.nii.gz")
epi_img_data = img.get_fdata()
epi_img_data.shape


# %%
def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    # fig.tight_layout()
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, origin="lower")
        axes[i].axis('off')


slice_0 = epi_img_data[:, 75, :]
slice_1 = epi_img_data[:, 110, :]
slice_2 = epi_img_data[:, 125, :]
show_slices([slice_0, slice_1, slice_2])
plt.suptitle("Center slices for EPI image")
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

# %% labels
label_img = nib.load(labels / "BRATS_1020.nii.gz")
lbl_img_data = label_img.get_fdata()
lbl_img_data.shape


# %% mask
def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    # fig.tight_layout()
    for i, slice in enumerate(slices):
        str_0 = "background_slice_" + str(i)

        # axes[i].imshow(str_0.T, origin="lower")
        axes[i].imshow(slice.T, origin="lower")
        axes[i].axis('off')


#%%
slice_0 = lbl_img_data[:, 75, :]
slice_1 = lbl_img_data[:, 110, :]
slice_2 = lbl_img_data[:, 125, :]

background_slice_0 = epi_img_data[:, 75, :]
background_slice_1 = epi_img_data[:, 110, :]
background_slice_2 = epi_img_data[:, 125, :]

type(slice_0)
# show_slices([slice_0, slice_1, slice_2])
# plt.suptitle("Center slices for EPI image")
# plt.subplots_adjust(wspace=0, hspace=0)
# plt.show()

# %%
background_slices = [background_slice_0, background_slice_1, background_slice_2]
slices = [slice_0, slice_1, slice_2]
background_slice_2

# %%

plt.figure()
j = 1
for i in range(2):
    plt.subplot(1, 2, j)
    plt.imshow(slices[i].T, origin="lower", interpolation='none')
    plt.imshow(background_slices[i].T, cmap='gray', origin="lower", interpolation='none', alpha=0.4)
    plt.axis('off')
    j += 1
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

# %%

import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color


def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols)
    ax.imshow(image, cmap='gray')
    # ax.imshow(image)
    ax.axis('off')
    fig.show()
    return fig, ax


# %%
image_show(color.rgb2gray(slice_0.T))
# image_show(color.gray2rgb(slice_0.T))

slice_0.max()

#%%

#%%
# print(imageInput.GetDimensions())

# %%
import pylab

xy = np.zeros((2, 10))
xy[0] = range(10)
xy[1] = range(10)
colors = [int(i % 3) for i in xy[0]]
# pylab.scatter(xy[0], xy[1], c=colors)
# pylab.scatter(xy[0], xy[1], c=colors, cmap = pylab.cm.cool)
# pylab.show()
xy[0]
# %%
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 3, 3, 4, 4]
labels = [1.0, 2.0, 3.0]
# colors = ['red', 'blue', 'green']
# olors = [int(i % 3) for i in xy[0]]
plt.imshow(slice_0.T)
# color = ['red' if l == 0 else 'green' for l in labl]
# plt.scatter(arr1, arr2, color=color)
plt.show()
# %%
def class_labels(label):
    label = label.T
    # print(type(label))
    all_classes = [0, 1.0, 2.0, 3.0]
    colors = ['red', 'green', 'blue', 'gray']
    loc = np.arange(0, max(all_classes), max(all_classes) / float(len(colors)))
    print(loc)
    # print(type(label))
    return label, loc


class_labels(slice_0)[1]

# %%
import matplotlib

# img = class_labels(slice_0)[0]
# loc = class_labels(slice_0)[1]
# print(type(loc))
# plt.imshow(img, cmap=matplotlib.colors.ListedColormap(loc), origin="lower",
#            interpolation='none')
plt.imshow(background_slices[i].T, cmap='gray', origin="lower", interpolation='none', alpha=0.4)
plt.axis('off')
# j += 1
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

# %%
from nilearn import plotting

display = plotting.plot_anat(main_img_dir_ + 'BRATS_1020_0002.nii.gz')
display.add_overlay(lbl_img_dir_ + 'BRATS_1020.nii.gz', colorbar=True)
display.savefig('output/plotting1.png')
# plotting.show()

# %%

#
# import SimpleITK as sitk
#
# img1 = slice_0
#
# # sitk.Show(img1)
#
# img = sitk.GetImageFromArray(slice_0.T)
# label_img= sitk.GetImageFromArray()
# print(img.GetSize())
#
#
# # %%
# def plot(image):
#     plt.imshow(image.T, origin='lower')
#     plt.show()
#
#
# # %%
# array = sitk.GetArrayFromImage(img)
# spacing = img.GetSpacing()
# print(spacing)
#
# # %%
# plot(slice_1)
# #%%
# image = sitk.GetImageFromArray(lbl_img_data)
# plot(sitk.LabelToRGB(image))
#
# #%%
