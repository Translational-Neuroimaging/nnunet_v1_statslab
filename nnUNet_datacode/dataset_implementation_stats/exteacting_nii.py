import os
from pathlib import Path
import nibabel as nib

# %%

database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian/")


# %% function to create a folder only if it doesn't exist
def create_folder_if_not_exist(folder_path):
    folder_path = str(folder_path)
    if not os.path.exists(folder_path + "/" + "labels"):
        os.makedirs(folder_path + "/" + "labels")
        print("The new directory is created!")
    else:
        print("The new directory is already exist!")


# %% create a function to extract_nii_gz_files nii.gz files from the folder
def extract_nii_gz_files(task_name):
    gt_database = database / task_name / "gt_files"

    for i in gt_database.glob("*.nii.gz"):
        new_name = i.name.replace(".nii.gz", ".nii")
        print(new_name)
        img_data = nib.load(i)
        redirected_path = database / task_name / "labels"

        create_folder_if_not_exist(database / task_name)

        nib.save(img_data, redirected_path / new_name)

    return "done"


# %%
extract_nii_gz_files("Task625")


#%%

new_dir = database / "Task620"
oned_dir = new_dir / "2d_best"
twod_dir = new_dir / "3d_fullres"

for i in oned_dir.glob("*.nii"):
    # print(i.name)
    for j in twod_dir.glob(str(i.name)):
        print(i.name)
