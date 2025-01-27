#%%
import os
from pathlib import Path
import numpy as np
import nibabel as nib
import random

#%% function to create new folder if it doesn't exist
def create_folder(folder_path, new_folder_name):
    isExist = os.path.exists(folder_path)
    print(isExist)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(folder_path)
        print("The new directory is created!")
        os.makedirs(folder_path + "/" + new_folder_name)
        print("The new directory is created!")
    else:
        os.makedirs(folder_path + "/" + new_folder_name)
        print("The new directory is created!")

#%% create new folder at nnUnet_raw_data_base/nnUNet_raw_data
path = "../nnUNet_raw_data_base/nnUNet_raw_data"
# create_folder(path, "Task620_Control")
create_folder(path + "/Task620_Control", "/imagesTr")
create_folder(path + "/Task620_Control", "/labelsTr")
create_folder(path + "/Task620_Control", "/imagesTs")
create_folder(path + "/Task620_Control", "/labelsTs")

#%%
create_folder(path + "/Task620_Control", "/all_related_ts")
create_folder(path + "/Task620_Control", "/all_related_tr")

# %%
database = Path("../../../Documents/data/adrian_data/Rats24h")

target_database = "../nnUNet_raw_data_base/nnUNet_raw_data/Task620_Control"

# %% list
therapy_list = ["Rat081", "Rat086", "Rat088", "Rat091", "Rat093", "Rat095", "Rat102", "Rat110", "Rat114", "Rat115",
                "Rat121", "Rat152", "Rat166", "Rat168", "Rat170", "Rat171"]

#%% function to save the files in targeet database with the new name
def save_files(img, target_database, new_name, class_name):
    if class_name == "control":
        output_training_dir = target_database + "/imagesTr"
        output_labels_dir = target_database + "/labelsTr"
        output_training_all = target_database + "/all_related_tr"
    else:
        output_training_dir = target_database + "/imagesTs"
        output_labels_dir = target_database + "/labelsTs"
        output_training_all = target_database + "/all_related_ts"

    if j.name == "Masked_ADC.nii":
        label_name = new_name + "_0000.nii.gz"
        print(label_name)
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif j.name == "Masked_T2.nii":
        label_name = new_name + "_0001.nii.gz"
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif j.name == "GroundTruth24h.nii":
        label_name = new_name + ".nii.gz"
        print(output_labels_dir + "/" + label_name)
        nib.save(img, output_labels_dir + "/" + label_name)

    else:
        label_name =new_name + "_" + j.name
        # print(output_training_all + "/" + label_name)
        nib.save(img, output_training_all + "/" + label_name)

# %%
for i in database.iterdir():
    new_database = Path(i)
    new_name = i.name.split("-24h")[0]

    if i.name.split("-24h")[0] in therapy_list:
        # print(i.name)

        for j in new_database.glob("*.nii"):
            print(j.name)
            img = nib.load(j)
            save_files(img, target_database, new_name, "therapy")
    else:
        for j in new_database.glob("*.nii"):
            print(j.name)
            img = nib.load(j)
            save_files(img, target_database, new_name, "control")

