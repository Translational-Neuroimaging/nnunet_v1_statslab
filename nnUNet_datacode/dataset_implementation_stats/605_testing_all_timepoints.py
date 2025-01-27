# %% managing imports
import shutil
from pathlib import Path
import nibabel as nib
import numpy as np
import os


#%%

database = Path("../../../Documents/data/adrian_data/")


#%%
path = "../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat"

for i in Path(path).glob("*"):
    print(i.name)


#%% function to create folder if not exists
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(folder_name + " created")
    else:
        print(folder_name + " already exists")

#%%

create_folder(path + "/testing/72h")
create_folder(path + "/testing/1w")
create_folder(path + "/testing/1m")

#%% create_folder imagesTs and labelsTs for 72h and 1w and 1m
create_folder(path + "/testing/72h/imagesTs")
create_folder(path + "/testing/72h/labelsTs")
create_folder(path + "/testing/1w/imagesTs")
create_folder(path + "/testing/1w/labelsTs")
create_folder(path + "/testing/1m/imagesTs")
create_folder(path + "/testing/1m/labelsTs")
#%% create_folder result & result_3d for 72h and 1w and 1m
create_folder(path + "/testing/72h/result")
create_folder(path + "/testing/72h/result_3d")
create_folder(path + "/testing/1w/result")
create_folder(path + "/testing/1w/result_3d")
create_folder(path + "/testing/1m/result")
create_folder(path + "/testing/1m/result_3d")


#%% function to save the files in targeet database with the new name
def save_files(img, target_database, new_name,file_type):

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

# %% 72h
database_72h = database / "Rats72h"
for i in database_72h.iterdir():
    # print(i.name)
    new_database = Path(i)
    new_name = i.name.split("-72h")[0]
    print(new_database)

    adc_file = new_database / "Masked_ADC.nii"
    t2_file = new_database / "Masked_T2.nii"
    gt_file = new_database / "Voi_72h.nii"
    # print(gt_file)

    save_files(nib.load(adc_file), path + "/testing/72h", new_name, "adc")
    save_files(nib.load(t2_file), path + "/testing/72h", new_name, "t2")
    save_files(nib.load(gt_file), path + "/testing/72h", new_name, "mask")

#%% 1w
database_1w = database / "Rats1w"
for i in database_1w.iterdir():
    # print(i.name)
    new_database = Path(i)
    new_name = i.name.split("-1w")[0]
    print(new_database)

    adc_file = new_database / "Masked_ADC.nii"
    t2_file = new_database / "Masked_T2.nii"
    gt_file = new_database / "Voi_1w.nii"
    # print(gt_file)

    save_files(nib.load(adc_file), path + "/testing/1w", new_name, "adc")
    save_files(nib.load(t2_file), path + "/testing/1w", new_name, "t2")
    save_files(nib.load(gt_file), path + "/testing/1w", new_name, "mask")

#%% 1m
database_1m = database / "Rats1m"
for i in database_1m.iterdir():
    # print(i.name)
    new_database = Path(i)
    new_name = i.name.split("-1m")[0]
    print(new_database)

    adc_file = new_database / "Masked_ADC.nii"
    t2_file = new_database / "Masked_T2.nii"
    gt_file = new_database / "Voi_1m.nii"
    # print(gt_file)

    save_files(nib.load(adc_file), path + "/testing/1m", new_name, "adc")
    save_files(nib.load(t2_file), path + "/testing/1m", new_name, "t2")
    save_files(nib.load(gt_file), path + "/testing/1m", new_name, "mask")