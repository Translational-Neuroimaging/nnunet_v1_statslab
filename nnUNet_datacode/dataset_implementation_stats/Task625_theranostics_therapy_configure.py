#%%
import os
from pathlib import Path
import numpy as np
import nibabel as nib
import random
import shutil

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
create_folder(path, "task625_Theranostics")
create_folder(path + "/Task625_Theranostics", "/imagesTr")
create_folder(path + "/Task625_Theranostics", "/labelsTr")
create_folder(path + "/Task625_Theranostics", "/imagesTs")
create_folder(path + "/Task625_Theranostics", "/labelsTs")
create_folder(path + "/Task625_Theranostics", "/all_related_tr")
create_folder(path + "/Task625_Theranostics", "/all_related_ts")


#%%
def copy_files(src, trg):
    files = os.listdir(src)

    for fname in files:
        # copying the files to the
        # destination directory
        shutil.copy2(os.path.join(src, fname), trg)

#%%
path = "../nnUNet_raw_data_base/nnUNet_raw_data/"
copy_files(path + "Task620_Control/all_related_ts", path + "Task625_Theranostics/all_related_ts")

# %%
database = Path("../../../Documents/data/adrian_data/Theranostics/")

target_database = "../nnUNet_raw_data_base/nnUNet_raw_data/Task625_Theranostics"

#%% function to save the files in target database with the new name
def save_files(img, target_database, new_name, ):
    output_training_dir = target_database + "/imagesTr"
    output_labels_dir = target_database + "/labelsTr"
    output_training_all = target_database + "/all_related_tr"

    if j.name == "human.nii":
        label_name = new_name + "_0000.nii.gz"
        print(label_name)
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif j.name == "T2W_c.nii":
        label_name = new_name + "_0001.nii.gz"
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif j.name == "Voi24.nii":
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
    new_name = i.name

    for j in new_database.glob("*.nii"):
        print(j.name)
        img = nib.load(j)
        save_files(img, target_database, new_name)

#%%
count = 0
for i in database.iterdir():
    count += 1

print(count)