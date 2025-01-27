#%%
import os
from pathlib import Path
import numpy as np
import nibabel as nib
import random


#%%
database_folder = Path("../../../Documents/data/adrian_data/devided/Rats24h")

therapy_folder = database_folder / "therapy"
control_folder = database_folder / "control"

#%% function to create empty folder
def create_folder(folder_path):
    isExist = os.path.exists(folder_path)
    print(isExist)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(folder_path)
        print("The new directory is created!")


#%% task 1  for Task802
folder = "../nnUNet_raw_data_base/nnUNet_raw_data/Task802_therapy_training/"
create_folder(folder)
create_folder(folder + "/imagesTr")
create_folder(folder + "/labelsTr")
create_folder(folder + "/imagesTs")
create_folder(folder + "/labelsTs")

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
path = "../nnUNet_raw_data_base/nnUNet_raw_data"
database = control_folder
count = 1
for i in database.glob("*"):
    # print(i.name)
    new_dir = i
    new_name = i.name.split("-")[0]
    # print(new_name)

    if count == 0:
        flag_type = "train"
        adc_file = new_dir / "Masked_ADC.nii"
        t2_file = new_dir / "Masked_T2.nii"
        gt_file = new_dir / "GroundTruth24h.nii"

        save_files(nib.load(adc_file), path + "/Task802_therapy_training", new_name, flag_type, "adc")
        save_files(nib.load(t2_file), path + "/Task802_therapy_training", new_name, flag_type, "t2")
        save_files(nib.load(gt_file), path + "/Task802_therapy_training", new_name, flag_type, "mask")

    else:
        flag_type = "test"
        adc_file = new_dir / "Masked_ADC.nii"
        t2_file = new_dir / "Masked_T2.nii"
        gt_file = new_dir / "GroundTruth24h.nii"

        save_files(nib.load(adc_file), path + "/Task802_therapy_training", new_name, flag_type, "adc")
        save_files(nib.load(t2_file), path + "/Task802_therapy_training", new_name, flag_type, "t2")
        save_files(nib.load(gt_file), path + "/Task802_therapy_training", new_name, flag_type, "mask")
