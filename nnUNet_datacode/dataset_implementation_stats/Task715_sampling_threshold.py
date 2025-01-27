# %% managing imports
import shutil
from pathlib import Path
import nibabel as nib
import numpy as np
import os

#%%
data_path = Path("../../../Documents/data/adrian_data/")

#%% import csv file
import pandas as pd
df = pd.read_csv(data_path / "rat_24h_gt_percentage.csv")
df = df.sort_values(by=['percentage'], ascending=True)

#%% get first 5 rows of df of first columns as list
rat_list = df.iloc[:15, 0].tolist()

#%%
path = "../nnUNet_raw_data_base/nnUNet_raw_data"

#%% function to create folder if not exists
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(folder_name + " created")
    else:
        print(folder_name + " already exists")

#%%

create_folder(path + "/Task715_sampling_threshold")

#%%
create_folder(path + "/Task715_sampling_threshold/imagesTr")
create_folder(path + "/Task715_sampling_threshold/imagesTs")
create_folder(path + "/Task715_sampling_threshold/labelsTr")
create_folder(path + "/Task715_sampling_threshold/labelsTs")

#%% function to save the files in target database with the new name
def save_files(img, target_database, new_name, flag_type ,file_type):
    if flag_type == "train":
        output_training_dir = target_database + "/imagesTr"
        output_labels_dir = target_database + "/labelsTr"
    else:
        output_training_dir = target_database + "/imagesTs"
        output_labels_dir = target_database + "/labelsTs"

    print(img.shape)
    if file_type == "adc":
        label_name = new_name + "_0000.nii.gz"
        print(label_name)
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif file_type == "t2":
        label_name = new_name + "_0001.nii.gz"
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif file_type == "mask":
        label_name = new_name + ".nii.gz"
        print(output_labels_dir + "/" + label_name)
        nib.save(img, output_labels_dir + "/" + label_name)


#%%
database = data_path / "Rats24h"

for i in database.glob("*"):
    # print(i.name)
    new_dir = i
    new_name = i.name.split("-")[0]
    # print(new_name)

    if new_name in rat_list:
        flag_type = "train"
        adc_file = new_dir / "Masked_ADC.nii"
        t2_file = new_dir / "Masked_T2.nii"
        gt_file = new_dir / "GroundTruth24h.nii"

        save_files(nib.load(adc_file), path + "/Task715_sampling_threshold", new_name, flag_type, "adc")
        save_files(nib.load(t2_file), path + "/Task715_sampling_threshold", new_name, flag_type, "t2")
        save_files(nib.load(gt_file), path + "/Task715_sampling_threshold", new_name, flag_type, "mask")


    else:
        flag_type = "test"
        adc_file = new_dir / "Masked_ADC.nii"
        t2_file = new_dir / "Masked_T2.nii"
        gt_file = new_dir / "GroundTruth24h.nii"

        save_files(nib.load(adc_file), path + "/Task715_sampling_threshold", new_name, flag_type, "adc")
        save_files(nib.load(t2_file), path + "/Task715_sampling_threshold", new_name, flag_type, "t2")
        save_files(nib.load(gt_file), path + "/Task715_sampling_threshold", new_name, flag_type, "mask")