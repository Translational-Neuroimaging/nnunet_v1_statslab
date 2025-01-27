# %% managing imports
from pathlib import Path
import nibabel as nib
import numpy as np
import os

import patchify as patchify

# %% import data from Documents/data/adrian_data
input_folder = Path("../../../Documents/data/adrian_data/Rats24h")
output_folder = "../nnUNet_raw_data_base/nnUNet_raw_data/Task630_Patch_2d_Rat24h/"


#%% print current working directory
print(os.getcwd())
print("start")

# %% write a function to create patches and append them to a list
def create_patches(img):
    patches_1 = patchify.patchify(img, (45, 45, 45), step=15)
    final_patch = patches_1.reshape(-1, 45, 45, 45)

    # extract the patches in 3d shape and save it in a list
    list_patches = []
    for z in range(final_patch.shape[0]):
        list_patches.append(final_patch[z, :, :, :])

    # for data_h in range(0, img.shape[0], patch_size - overlap):
    #     for data_w in range(0, img.shape[1], patch_size - overlap):
    #         for data_d in range(0, img.shape[2], patch_size - overlap):
    #             patch = img[data_h:data_h + patch_size, data_w:data_w + patch_size, data_d:data_d + patch_size]
    #             if patch.shape == (patch_size, patch_size, patch_size):
    #                 patch_list.append(patch)
    return list_patches


# %% save the patches in a folder as .nii.gz
def save_patches(patch_list_whole_img, destination_folder, file_type, counter):
    # if type is t2 or adc then output_folder is output_folder/imagesTs
    if counter < 37:
        if file_type == "t2" or file_type == "adc":
            destination_folder = destination_folder + "/imagesTr"
        elif file_type == "seg":
            destination_folder = destination_folder + "/labelsTr"
    else:
        if file_type == "t2" or file_type == "adc":
            destination_folder = destination_folder + "/imagesTs"
        elif file_type == "seg":
            destination_folder = destination_folder + "/labelsTs"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for element in range(len(patch_list_whole_img)):
        patch = patch_list_whole_img[element]
        nii_file = nib.Nifti1Image(patch, np.eye(4))
        if file_type == "t2":
            new_name = new_dir_name + '_' + str(element) + '_0001' + '.nii.gz'
        elif file_type == "adc":
            new_name = new_dir_name + '_' + str(element) + '_0000' + '.nii.gz'
            # new_name = new_dir_name + '_0000_' + str(element) + '.nii.gz'
        elif file_type == "seg":
            new_name = new_dir_name + '_' + str(element) + '.nii.gz'
            # new_name = new_dir_name + '_' + str(element) + '.nii.gz'
        nib.save(nii_file, destination_folder + '/' + new_name)
    print(new_dir_name + " " + file_type + ' saved')


# %% create a function to create patches and save them
def create_and_save_patches(input_file, output, type_file, tally):
    load_nifti = nib.load(input_file)
    input_image_array = np.array(load_nifti.dataobj)

    # if input_image_array has nan values then change it to 0
    if np.isnan(input_image_array).any():
        input_image_array[np.isnan(input_image_array)] = 0

    print(np.isnan(input_image_array).any())

    list_patches = create_patches(input_image_array)
    save_patches(list_patches, output, type_file, tally)


# %% trail run
folder = input_folder / "Rat085-24h"
output_fold = "patch_data/"
new_dir_name = "Rat081"
for i in folder.glob("*.nii"):
    if "Masked_ADC" in i.name:
        adc_file = i
        create_and_save_patches(adc_file, output_fold, "adc", 41)

    elif "Masked_T2" in i.name:
        t2_file = i
        create_and_save_patches(t2_file, output_fold, "t2", 41)

    elif "GroundTruth24h" in i.name:
        gt_file = i
        create_and_save_patches(gt_file, output_fold, "seg", 41)

# %% perfect run
count = 1
for i in input_folder.glob("*"):
    new_dir = i
    new_dir_name = i.name.replace("-24h", "")
    # print(new_dir_name)
    print(count)

    for j in new_dir.glob("*.nii"):
        if "Masked_ADC" in j.name:
            adc_file = j
            create_and_save_patches(adc_file, output_folder, "adc", count)

        elif "Masked_T2" in j.name:
            t2_file = j
            create_and_save_patches(t2_file, output_folder, "t2", count)

        elif "GroundTruth24h" in j.name:
            gt_file = j
            create_and_save_patches(gt_file, output_folder, "seg", count)

    count += 1

# %%
file_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task630_Patch_3d_Rat24h/")

#%%
def delete_files(file_path, file_name):
    file_imagesTr = file_path / "imagesTr"
    file_labelsTr = file_path / "labelsTr"
    file_imagesTs = file_path / "imagesTs"
    file_labelsTs = file_path / "labelsTs"

    for i in file_imagesTr.glob(file_name + "*"):
        print(i.name)
        # delete the file if it exists
        if i.exists():
            os.remove(i)
            print("deleted")
        else:
            print("file doesn't exist")

    # same code for labelsTr, imagesTs, labelsTs
    for i in file_labelsTr.glob(file_name + "*"):
        print(i.name)
        # delete the file if it exists
        if i.exists():
            os.remove(i)
            print("deleted")
        # if file doesn't exit print file doesn't exist
        else:
            print("file doesn't exist")


# %%
delete_files(file_path, "Rat121_78")

# %%
list_data_points = list_of_exceptions

# %%
print(len(list_data_points))

# %%
for i in list_data_points:
    delete_files(file_path, i)

# %%
print(list_data_points)

# %% removing all the empty patches in the dataset

target_folder = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task632_Patch")

for i in target_folder.glob("*"):
    print(i)

#%%
imagesTr = target_folder / "imagesTr"
labelsTr = target_folder / "labelsTr"
count = 0
list_of_empty_files = []
for i in imagesTr.glob("*.nii.gz"):
    load_nifti = nib.load(i)
    input_image_array = np.array(load_nifti.dataobj)

    # if input_image_array has only one unique value print the name of the file
    if len(np.unique(input_image_array)) == 1:
        print(i.name)
        count += 1
        # append all the files that have only one unique value to a list
        list_of_empty_files.append(i.name.split("_000")[0])
    # print(np.unique(input_image_array))
print(count)

#%%
print(list_of_empty_files)

#%%
for i in list_of_empty_files:
    delete_files(target_folder, i)

#%% compare list of empty files with list_data_points
print(list_of_empty_files == list_data_points)



#%% creating patches using patchify


patches = patchify.patchify(data_input, (31, 31, 31), step=15)
print(patches.shape)