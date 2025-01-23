# %% managing all the imports here only
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd
import patchify as patchify
import matplotlib.pyplot as plt

# %% get data from imagesTr
dataset_path = Path("imagesTr")

# save the data in a dictionary
data_dict = {"adc": {}, "t2": {}}

for i in dataset_path.glob("*"):
    # get data using nib.
    img = nib.load(i)
    data = np.array(img.dataobj)

    # if suffix is _0000 then it is adc file else it is t2 file
    suffix = i.name[-12:]

    dict_name = i.name.split("_000")[0].split("_")[1]
    # dict name has one character then add 0 as prefix
    if len(dict_name) == 1:
        dict_name = "0" + dict_name
    if suffix == "_0000.nii.gz":
        # add the adc file to the dictionary
        data_dict["adc"][dict_name] = i
    elif suffix == "_0001.nii.gz":
        # add the t2 file to the dictionary
        data_dict["t2"][dict_name] = i

# %% dict to dataframe
df = pd.DataFrame(data_dict)

# %% sort df by index by Rat081_1 then Rat081_2 not Rat081_10
df = df.sort_index()

# %% get adc and t2 files from df as list
adc_files = df["adc"].tolist()
t2_files = df["t2"].tolist()


# %% create a function for upper code
def get_data_from_nifti(file_list):
    new_list = []
    for element in file_list:
        e_img = nib.load(element)
        e_data = np.array(e_img.dataobj)
        new_list.append(e_data)
    return new_list


# %%
adc_data_list = get_data_from_nifti(adc_files)
t2_data_list = get_data_from_nifti(t2_files)

# %% for adc_data_list

adc_patches = np.array(adc_data_list)
adc_patches_reshaped = adc_patches.reshape(4, 4, 6, 45, 45, 45)
reconstructed_adc = patchify.unpatchify(adc_patches_reshaped, (90, 90, 120))

# %%
original_adc = nib.load('input/Masked_ADC.nii')
original_adc_data = np.array(original_adc.dataobj)

modified_original_adc_data = original_adc_data[0:90, 0:90, 0:120]
modified_original_adc_data[np.isnan(modified_original_adc_data)] = 0

# %%check equality of reconstructed_adc and modified_original_adc_data
print(np.array_equal(reconstructed_adc, modified_original_adc_data))


# %% create a function for whole process
def reconstruct_patches(patches_list, original_data):
    patches = np.array(patches_list)
    patches_reshaped = patches.reshape(4, 4, 6, 45, 45, 45)
    reconstructed_data = patchify.unpatchify(patches_reshaped, (90, 90, 120))
    original_data = original_data[0:90, 0:90, 0:120]
    original_data[np.isnan(original_data)] = 0

    # check equality of reconstructed_adc and modified_original_adc_data
    if np.array_equal(reconstructed_data, original_data):
        print("True")
    return True

