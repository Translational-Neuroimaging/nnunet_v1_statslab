# %% Managing all the imports here
# Importing necessary libraries for handling file paths, medical imaging (NIfTI), data manipulation, 
# patch creation, and visualization
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd
import patchify as patchify
import matplotlib.pyplot as plt

# %% Paths for the dataset and output
# Define the dataset path for 3D images and output path for reconstructed data
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/result_3d")
output_path = "../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/result_3d_reconstructed"

# %% Identify and filter files based on naming conventions
# Iterate through all .nii.gz files in the dataset folder
# Print names of files starting with "Human"
for i in dataset_path.glob("*.nii.gz"):
    if i.name.startswith("Human"):
        print(i.name)

# %% Function to process data and organize it into dictionaries based on file names
def process_all_data(file):
    if i.name.startswith("Human"):
        # Process files for Human dataset
        Human_name = i.name.split("_")[0]
        if Human_name not in Human_dict:
            Human_dict[Human_name] = {}
            print("dict created: %s" % Human_name)

        get_patch = i.name.split("_")[1].split(".")[0]
        Human_dict[Human_name][get_patch] = i
        print("patch added in %s dictionary: %s" % (Human_name, get_patch))
    elif i.name.startswith("Rat"):
        # Process files for Rat dataset
        Rat_name = i.name.split("_")[0]
        if Rat_name not in Rat_dict:
            Rat_dict[Rat_name] = {}
            print("dict created: %s" % Rat_name)

        get_patch = i.name.split("_")[1].split(".")[0]
        Rat_dict[Rat_name][get_patch] = i
        print("patch added in %s dictionary: %s" % (Rat_name, get_patch))

# %% Initialize dictionaries for storing Human and Rat data
Human_dict = {}
Rat_dict = {}

# Process all NIfTI files in the dataset folder
for i in dataset_path.glob("*.nii.gz"):
    process_all_data(i)

# %% Convert dictionaries to DataFrames
# Human and Rat data are converted into Pandas DataFrames for easier manipulation and analysis
human_df = pd.DataFrame(Human_dict)
rat_df = pd.DataFrame(Rat_dict)

# %% Sort DataFrames by their indices
human_df = human_df.sort_index()
rat_df = rat_df.sort_index()

# %% Function to extract data arrays from NIfTI files
def get_data_from_nifti(file_list):
    new_list = []
    for element in file_list:
        e_img = nib.load(element)
        e_data = np.array(e_img.dataobj)
        new_list.append(e_data)
    return new_list

# %% Function to reconstruct patches for Rat dataset
def reconstruct_patches_rat(patches_list):
    patches = np.array(patches_list)
    patches_reshaped = patches.reshape(4, 4, 6, 45, 45, 45)
    reconstructed_data = patchify.unpatchify(patches_reshaped, (90, 90, 120))
    return reconstructed_data

# %% Function to reconstruct patches for Human dataset
def reconstruct_patches_human(patches_list):
    patches = np.array(patches_list)
    patches_reshaped = patches.reshape(6, 7, 6, 45, 45, 45)
    reconstructed_data = patchify.unpatchify(patches_reshaped, (120, 135, 120))
    return reconstructed_data

# %% Process and save reconstructed data for Human and Rat datasets
# For Human dataset
for i in human_df.columns:
    name = i
    df_data = human_df[i].tolist()
    data_list = get_data_from_nifti(df_data)
    inverse_patch = reconstruct_patches_human(data_list)
    img = nib.Nifti1Image(inverse_patch, np.eye(4))
    nib.save(img, output_path + "/" + name + ".nii.gz")
    print("saved: %s" % name)

# For Rat dataset
for i in rat_df.columns:
    name = i
    df_data = rat_df[i].tolist()
    data_list = get_data_from_nifti(df_data)
    inverse_patch = reconstruct_patches_rat(data_list)
    img = nib.Nifti1Image(inverse_patch, np.eye(4))
    nib.save(img, output_path + "/" + name + ".nii.gz")
    print("saved: %s" % name)

# %% Process a specific NIfTI file
# Load, crop, and preprocess data from an ADC NIfTI file
original_adc = nib.load('input/Masked_ADC.nii')
original_adc_data = np.array(original_adc.dataobj)

# Crop data and handle NaN values
modified_original_adc_data = original_adc_data[0:90, 0:90, 0:120]
modified_original_adc_data[np.isnan(modified_original_adc_data)] = 0

# %% Check equality between reconstructed and modified data
# # Validate that the reconstructed data matches the modified original data
# print(np.array_equal(reconstructed_adc, modified_original_adc_data))