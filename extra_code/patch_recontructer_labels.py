# %% managing all the imports here only
from pathlib import Path
import nibabel as nib
import numpy as np
import pandas as pd
import patchify as patchify
import matplotlib.pyplot as plt

# %% create a function to process all the data using dictionary
def process_all_data(file, data_dict):
    main_name = i.name.split("_")[0]
    # if main name doesn't exist in dictionary then create a new key
    if main_name not in data_dict:
        data_dict[main_name] = {}
        print("dict created: %s" % main_name)

    get_patch = i.name.split("_")[1].split(".")[0]
    # if get_patch_no has one character then add 0 as prefix
    if len(get_patch) == 1:
        get_patch = "00" + get_patch
    elif len(get_patch) == 2:
        get_patch = "0" + get_patch
    # add the patch number to the dictionary
    data_dict[main_name][get_patch] = i
    # print patch added in main_name dictionary
    print("patch added in %s dictionary: %s" % (main_name, get_patch))

# create a function for upper code
def get_data_from_nifti(file_list, type):
    new_list = []
    for element in file_list:
        e_img = nib.load(element)
        e_data = np.array(e_img.dataobj)
        new_list.append(e_data)

    return new_list

# create a function for whole process
def reconstruct_patches(patches_list, type ):
    patches = np.array(patches_list)
    if type == "human":
        patches_reshaped = patches.reshape(7, 8, 7, 30, 30, 30)
        reconstructed_data = patchify.unpatchify(patches_reshaped, (120, 135, 120))
    elif type == "mcao_60":
        patches_reshaped = patches.reshape(5, 5, 7, 30, 30, 30)
        reconstructed_data = patchify.unpatchify(patches_reshaped, (90, 90, 120))
    elif type == "mcao_100":
        patches_reshaped = patches.reshape(4, 2, 1, 30, 30, 30)
        reconstructed_data = patchify.unpatchify(patches_reshaped, (75, 45, 30))
    return reconstructed_data

# create a function for upper code
def get_data_from_df_for_recontruct(df, type, output_path):
    for i in df.columns:
        # get the data from dataframe
        name = i
        df_data = df[i].tolist()
        # get the data from nifti files
        data_list = get_data_from_nifti(df_data, type)
        # reconstruct patches
        inverse_patch = reconstruct_patches(data_list, type)

        # save inverse_patch as nifti file
        img = nib.Nifti1Image(inverse_patch, np.eye(4))
        nib.save(img, output_path + "/" + name + ".nii.gz")
        print("saved: %s" % name)

        # save inverse_patch as nifti file
        img = nib.Nifti1Image(inverse_patch, np.eye(4))
        nib.save(img, output_path + "/" + name + ".nii.gz")
        print("saved: %s" % name)

#%%
list_path = Path("../../../Documents/data/adrian_data/Rats24h")
macao_60_list = []
for i in list_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    macao_60_list.append(new_name)

# %% get data from imagesTr
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data/")
output_path = "../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data/full_image_data"

gt_path = dataset_path / "labelsTs"
img_path = dataset_path / "imagesTs"
result_path = dataset_path / "result_3d"


#%% check if all path exists
if not dataset_path.exists():
    print("dataset_path doesn't exist")
if not gt_path.exists():
    print("gt_path doesn't exist")
if not img_path.exists():
    print("img_path doesn't exist")
if not result_path.exists():
    print("result_path doesn't exist")


#%% gt data
human_data_dict = {}
mcao_60_data_dict = {}
mcao_100_data_dict = {}

for i in gt_path.glob("*.nii.gz"):
    name = i.name.split("_")[0]
    print(name)
    if i.name.startswith("Human"):
        print(i.name)
        process_all_data(i, human_data_dict)
    elif name in macao_60_list:
        print(i.name)
        process_all_data(i, mcao_60_data_dict)
    else:
        print(i.name)
        process_all_data(i, mcao_100_data_dict)

# # %%
# # save the data in a dictionary
# data_dict = {}
# for i in dataset_path.glob("*.nii.gz"):
#     process_all_data(i)

#%% dict to dataframe
df_human_data = pd.DataFrame(human_data_dict)
df_mcao_60_data = pd.DataFrame(mcao_60_data_dict)
df_mcao_100_data = pd.DataFrame(mcao_100_data_dict)

# sort the dataframe by index
df_human_data = df_human_data.sort_index()
df_mcao_60_data = df_mcao_60_data.sort_index()
df_mcao_100_data = df_mcao_100_data.sort_index()

#%% check if any cell is empty in dataframe
print(df_human_data.isnull().values.any())
print(df_mcao_60_data.isnull().values.any())
print(df_mcao_100_data.isnull().values.any())

#%%
get_data_from_df_for_recontruct(df_human_data, "human", str(output_path + "/human/labelsTs"))
get_data_from_df_for_recontruct(df_mcao_60_data, "mcao_60", str(output_path + "/60/labelsTs"))
get_data_from_df_for_recontruct(df_mcao_100_data, "mcao_100", str(output_path + "/100/labelsTs"))


#%% img data
human_data_dict_adc = {}
human_data_dict_t2 = {}
mcao_60_data_dict_adc = {}
mcao_60_data_dict_t2 = {}
mcao_100_data_dict_adc = {}
mcao_100_data_dict_t2 = {}

for i in img_path.glob("*.nii.gz"):
    name = i.name.split("_")[0]
    print(name)
    suffix = i.name.split("_")[2]
    print(suffix)
    if i.name.startswith("Human"):
        print(i.name)
        if suffix == "0000.nii.gz":
            process_all_data(i, human_data_dict_adc)
        elif suffix == "0001.nii.gz":
            process_all_data(i, human_data_dict_t2)
    elif name in macao_60_list:
        print(i.name)
        if suffix == "0000.nii.gz":
            process_all_data(i, mcao_60_data_dict_adc)
        elif suffix == "0001.nii.gz":
            process_all_data(i, mcao_60_data_dict_t2)
    else:
        print(i.name)
        if suffix == "0000.nii.gz":
            process_all_data(i, mcao_100_data_dict_adc)
        elif suffix == "0001.nii.gz":
            process_all_data(i, mcao_100_data_dict_t2)

# # %%
# # save the data in a dictionary
# data_dict = {}
# for i in dataset_path.glob("*.nii.gz"):
#     process_all_data(i)

#%% dict to dataframe
df_human_data_adc = pd.DataFrame(human_data_dict_adc)
df_human_data_t2 = pd.DataFrame(human_data_dict_t2)
df_mcao_60_data_adc = pd.DataFrame(mcao_60_data_dict_adc)
df_mcao_60_data_t2 = pd.DataFrame(mcao_60_data_dict_t2)
df_mcao_100_data_adc = pd.DataFrame(mcao_100_data_dict_adc)
df_mcao_100_data_t2 = pd.DataFrame(mcao_100_data_dict_t2)


# sort the dataframe by index
df_human_data_adc = df_human_data_adc.sort_index()
df_human_data_t2 = df_human_data_t2.sort_index()
df_mcao_60_data_adc = df_mcao_60_data_adc.sort_index()

#%% check if any cell is empty in dataframe
print(df_human_data_adc.isnull().values.any())
print(df_human_data_t2.isnull().values.any())
print(df_mcao_60_data_adc.isnull().values.any())
print(df_mcao_60_data_t2.isnull().values.any())
print(df_mcao_100_data_adc.isnull().values.any())
print(df_mcao_100_data_t2.isnull().values.any())

#%%
get_data_from_df_for_recontruct(df_human_data_adc, "human", str(output_path + "/human/ADC"))
get_data_from_df_for_recontruct(df_human_data_t2, "human", str(output_path + "/human/T2"))
get_data_from_df_for_recontruct(df_mcao_60_data_adc, "mcao_60", str(output_path + "/60/ADC"))
get_data_from_df_for_recontruct(df_mcao_60_data_t2, "mcao_60", str(output_path + "/60/T2"))
get_data_from_df_for_recontruct(df_mcao_100_data_adc, "mcao_100", str(output_path + "/100/ADC"))
get_data_from_df_for_recontruct(df_mcao_100_data_t2, "mcao_100", str(output_path + "/100/T2"))

#%% result data
human_data_dict_result = {}
mcao_60_data_dict_result = {}
mcao_100_data_dict_result = {}

for i in result_path.glob("*.nii.gz"):
    name = i.name.split("_")[0]
    print(name)
    if i.name.startswith("Human"):
        print(i.name)
        process_all_data(i, human_data_dict_result)
    elif name in macao_60_list:
        print(i.name)
        process_all_data(i, mcao_60_data_dict_result)
    else:
        print(i.name)
        process_all_data(i, mcao_100_data_dict_result)

#%%
df_human_data_result = pd.DataFrame(human_data_dict_result)
df_mcao_60_data_result = pd.DataFrame(mcao_60_data_dict_result)
df_mcao_100_data_result = pd.DataFrame(mcao_100_data_dict_result)

# sort the dataframe by index
df_human_data_result = df_human_data_result.sort_index()
df_mcao_60_data_result = df_mcao_60_data_result.sort_index()
df_mcao_100_data_result = df_mcao_100_data_result.sort_index()


#%% check the length of the indexes of the dataframes
print(len(df_human_data_result.index))
print(len(df_mcao_60_data_result.index))
print(len(df_mcao_100_data_result.index))

#%% function to check if dataframe has all data - function 01
# def check_df(df, type):
#     if type == "human":
#         for i in range(0, 392):
#             if str(i).zfill(3) not in df.index:
#                 print("missing data for human", i)
#     elif type == "mcao_60":
#         for i in range(0, 175):
#             if str(i).zfill(3) not in df.index:
#                 print("missing data for mcao_60", i)
#     elif type == "mcao_100":
#         for i in range(0, 8):
#             if str(i).zfill(3) not in df.index:
#                 print("missing data for mcao_100", i)
#
# #%%
# check_df(df_human_data_result, "human")
# check_df(df_mcao_60_data_result, "mcao_60")
# check_df(df_mcao_100_data_result, "mcao_100")

#%% code 001 to 006
# new_df = df_human_data_result
# #%% create an empty dataframe 002
# final_df = pd.DataFrame()
#
# final_df.index = pd.RangeIndex(start=1, stop=393).astype(str).str.zfill(3)
#
# final_df = pd.DataFrame(index= final_df.index , columns=df_human_data_result.columns)
#
#
# # %% copy the values of df_human_data_result to new_df for available index 003
# for index, row in new_df.iterrows():
#     for column in new_df.columns:
#         final_df.loc[index, column] = new_df.loc[index, column]
#
# #%% 004
# empty_array = "../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data/result_3d/Human07_001.nii.gz"
#
# #%% fill the empty cells with final_df 005
# for index, row in final_df.iterrows():
#     for column in final_df.columns:
#         if pd.isnull(final_df.loc[index, column]):
#             final_df.loc[index, column] = empty_array
#             #print the index and column of the empty cell
#             print(index, column)


# #%% write a function for 001 to 005 for the missing data filling and return new dataframe
# # function 02
# def fill_missing_data(df, type, string_to_fill_nan_values):
#     updated_df = pd.DataFrame()
#     if type == "human":
#         end_range = 392
#     elif type == "mcao_60":
#         end_range = 175
#     elif type == "mcao_100":
#         end_range = 8
#
#     updated_df.index = pd.RangeIndex(start=1, stop=end_range).astype(str).str.zfill(3)
#     updated_df = pd.DataFrame(index= updated_df.index , columns=df.columns)
#
#     for index, row in df.iterrows():
#         for column in df.columns:
#             updated_df.loc[index, column] = df.loc[index, column]
#
#     for index, row in updated_df.iterrows():
#         for column in updated_df.columns:
#             if pd.isnull(updated_df.loc[index, column]):
#                 updated_df.loc[index, column] = string_to_fill_nan_values
#                 #print the index and column of the empty cell
#                 print(index, column)
#     return updated_df


#%% create a function to replace function 01 and 02
# function 03
def check_df_and_fill_missing_data(df, type, string_to_fill_nan_values):
    data_missing = False
    if type == "human":
        for i in range(0, 392):
            if str(i).zfill(3) not in df.index:
                print("missing data for human", i)
            data_missing = True
    elif type == "mcao_60":
        for i in range(0, 175):
            if str(i).zfill(3) not in df.index:
                print("missing data for mcao_60", i)
            data_missing = True
    elif type == "mcao_100":
        for i in range(0, 8):
            if str(i).zfill(3) not in df.index:
                print("missing data for mcao_100", i)
            data_missing = True
    else:
        print("wrong type")

    if data_missing:
        updated_df = pd.DataFrame()
        if type == "human":
            end_range = 392
        elif type == "mcao_60":
            end_range = 175
        elif type == "mcao_100":
            end_range = 8

        updated_df.index = pd.RangeIndex(start=0, stop=end_range).astype(str).str.zfill(3)
        updated_df = pd.DataFrame(index= updated_df.index , columns=df.columns)

        for index, row in df.iterrows():
            for column in df.columns:
                updated_df.loc[index, column] = df.loc[index, column]

        for index, row in updated_df.iterrows():
            for column in updated_df.columns:
                if pd.isnull(updated_df.loc[index, column]):
                    updated_df.loc[index, column] = string_to_fill_nan_values
                    #print the index and column of the empty cell
                    print(index, column)
    else:
        updated_df = df
    return updated_df

#%%
empty_array = "../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data/result_3d/Human07_001.nii.gz"
df_human_data_result_final = check_df_and_fill_missing_data(df_human_data_result, "human", empty_array)
df_mcao_60_data_result_final = check_df_and_fill_missing_data(df_mcao_60_data_result, "mcao_60", empty_array)
df_mcao_100_data_result_final = check_df_and_fill_missing_data(df_mcao_100_data_result, "mcao_100", empty_array)


#%% check if any cell is empty in dataframe
print(df_human_data_result.isnull().values.any())
print(df_mcao_60_data_result.isnull().values.any())
print(df_mcao_100_data_result.isnull().values.any())


#%%
get_data_from_df_for_recontruct(df_human_data_result_final, "human", str(output_path + "/human/result_3d"))
get_data_from_df_for_recontruct(df_mcao_60_data_result_final, "mcao_60", str(output_path + "/60/result_3d"))
get_data_from_df_for_recontruct(df_mcao_100_data_result_final, "mcao_100", str(output_path + "/100/result_3d"))

