# %% managing all the imports here only
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd
import patchify as patchify
import matplotlib.pyplot as plt

# %% get data from imagesTr
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/result_3d")
output_path = "../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/result_3d_reconstructed"

# %%
for i in dataset_path.glob("*.nii.gz"):
    # print(i.name)
    # if i.name starts with Human the add it to humna_dict else add it to rat_dict
    if i.name.startswith("Human"):
        print(i.name)


# %% create a function to process all the data using dictionary
def process_all_data(file):
    if i.name.startswith("Human"):
        # use the normal code for Human_name and Human_dict
        Human_name = i.name.split("_")[0]
        if Human_name not in Human_dict:
            Human_dict[Human_name] = {}
            print("dict created: %s" % Human_name)

        get_patch = i.name.split("_")[1].split(".")[0]
        Human_dict[Human_name][get_patch] = i
        print("patch added in %s dictionary: %s" % (Human_name, get_patch))
    elif i.name.startswith("Rat"):
        # use the normal code for Rat_name and Rat_dict
        Rat_name = i.name.split("_")[0]
        if Rat_name not in Rat_dict:
            Rat_dict[Rat_name] = {}
            print("dict created: %s" % Rat_name)

        get_patch = i.name.split("_")[1].split(".")[0]
        Rat_dict[Rat_name][get_patch] = i
        print("patch added in %s dictionary: %s" % (Rat_name, get_patch))

    # # normal code
    # main_name = i.name.split("_")[0]
    # # if main name doesn't exist in dictionary then create a new key
    # if main_name not in data_dict:
    #     data_dict[main_name] = {}
    #     print("dict created: %s" % main_name)
    #
    # get_patch = i.name.split("_")[1].split(".")[0]
    # # if get_patch_no has one character then add 0 as prefix
    # if len(get_patch) == 1:
    #     get_patch = "0" + get_patch
    # # add the patch number to the dictionary
    # data_dict[main_name][get_patch] = i
    # # print patch added in main_name dictionary
    # print("patch added in %s dictionary: %s" % (main_name, get_patch))


# # %% create a function to process all the data using dictionary
# def process_all_data(file):
#     main_name = i.name.split("_")[0]
#     # if main name doesn't exist in dictionary then create a new key
#     if main_name not in data_dict:
#         data_dict[main_name] = {}
#         print("dict created: %s" % main_name)
#
#     get_patch = i.name.split("_")[1].split(".")[0]
#     # if get_patch_no has one character then add 0 as prefix
#     if len(get_patch) == 1:
#         get_patch = "0" + get_patch
#     # add the patch number to the dictionary
#     data_dict[main_name][get_patch] = i
#     # print patch added in main_name dictionary
#     print("patch added in %s dictionary: %s" % (main_name, get_patch))


# %%
# save the data in a dictionary
Human_dict = {}
Rat_dict = {}
# data_dict = {}
for i in dataset_path.glob("*.nii.gz"):
    process_all_data(i)

# %% dict to dataframe
human_df = pd.DataFrame(Human_dict)
rat_df = pd.DataFrame(Rat_dict)

# %% sort the dataframe by index
human_df = human_df.sort_index()
rat_df = rat_df.sort_index()


# %% create a function for upper code
def get_data_from_nifti(file_list):
    new_list = []
    for element in file_list:
        e_img = nib.load(element)
        e_data = np.array(e_img.dataobj)
        new_list.append(e_data)
    return new_list


# %% create a function for whole process for rat
def reconstruct_patches_rat(patches_list, ):
    patches = np.array(patches_list)
    patches_reshaped = patches.reshape(4, 4, 6, 45, 45, 45)
    reconstructed_data = patchify.unpatchify(patches_reshaped, (90, 90, 120))
    return reconstructed_data


# %% create a function for whole process for human
def reconstruct_patches_human(patches_list, ):
    patches = np.array(patches_list)
    patches_reshaped = patches.reshape(6, 7, 6, 45, 45, 45)
    reconstructed_data = patchify.unpatchify(patches_reshaped, (120, 135, 120))
    return reconstructed_data


# %% access all the colums of dataframe and get the data # code 5
# for i in df.columns:
#     # get the data from dataframe
#     name = i
#     df_data = df[i].tolist()
#     # get the data from nifti files
#     data_list = get_data_from_nifti(df_data)
#     # reconstruct patches
#     inverse_patch = reconstruct_patches(data_list)
#
#     # save inverse_patch as nifti file
#     img = nib.Nifti1Image(inverse_patch, np.eye(4))
#     nib.save(img, output_path + "/" + name + ".nii.gz")
#     print("saved: %s" % name)

# %% access all the columns of dataframe and get the data for human and rat using code 5
for i in human_df.columns:
    # get the data from dataframe
    name = i
    df_data = human_df[i].tolist()
    # get the data from nifti files
    data_list = get_data_from_nifti(df_data)
    # reconstruct patches
    inverse_patch = reconstruct_patches_human(data_list)

    # save inverse_patch as nifti file
    img = nib.Nifti1Image(inverse_patch, np.eye(4))
    nib.save(img, output_path + "/" + name + ".nii.gz")
    print("saved: %s" % name)

for i in rat_df.columns:
    # get the data from dataframe
    name = i
    df_data = rat_df[i].tolist()
    # get the data from nifti files
    data_list = get_data_from_nifti(df_data)
    # reconstruct patches
    inverse_patch = reconstruct_patches_rat(data_list)

    # save inverse_patch as nifti file
    img = nib.Nifti1Image(inverse_patch, np.eye(4))
    nib.save(img, output_path + "/" + name + ".nii.gz")
    print("saved: %s" % name)


















# %%
original_adc = nib.load('input/Masked_ADC.nii')
original_adc_data = np.array(original_adc.dataobj)

modified_original_adc_data = original_adc_data[0:90, 0:90, 0:120]
modified_original_adc_data[np.isnan(modified_original_adc_data)] = 0

# %%check equality of reconstructed_adc and modified_original_adc_data
print(np.array_equal(reconstructed_adc, modified_original_adc_data))
