import os
import nibabel as nib
from pathlib import Path

# %%  function to create new folder at nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results/


def create_folder(target_database, new_folder_name):
    if not os.path.exists(target_database + "/" + new_folder_name):
        os.makedirs(target_database + "/" + new_folder_name)
        print("The new directory is created!")
    else:
        print("The new directory is already exist!")


# %%
path = "../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results/Task615/"

create_folder(path, "2d")
create_folder(path, "3d_fullres")
create_folder(path, "2d_best")

# %% import data from segmentation_results/
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results/")

for i in database.iterdir():
    print(i)


# %% create a function to check whether the folder contains the folders
def folder_contains_folders(folder_path):
    for i in folder_path.iterdir():
        if i.is_dir():
            return True
        else:
            return False


# %% create a function to check whether the folder contains the files
def folder_contains_files(folder_path):
    for i in folder_path.iterdir():
        if i.is_file():
            return True
        else:
            return False


# %% create function to crete a folder only if it doesn't exist
def create_folder_if_not_exist(folder_path, new_folder_name):
    if not os.path.exists(folder_path + "/" + new_folder_name):
        os.makedirs(folder_path + "/" + new_folder_name)
        print("The new directory is created!")
    else:
        print("The new directory is already exist!")


# %% for separate tasks
def convert_files(base_fold, target_datab, t_name):
    for i in base_fold.iterdir():
        new_dir = i
        for j in new_dir.glob("*.nii.gz"):
            new_name = j.name.replace(".nii.gz", ".nii")
            print(new_name)
            img_data = nib.load(j)
            redirected_path = target_datab + "/" + t_name + "/" + i.name + "/" + new_name
            create_folder_if_not_exist(target_datab + "/" + t_name, i.name)
            nib.save(img_data, redirected_path)

    return "done"


# %%
task_name = "Task625"
base_folder = database / task_name
target_database = "../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian"

convert_files(base_folder, target_database, task_name)
