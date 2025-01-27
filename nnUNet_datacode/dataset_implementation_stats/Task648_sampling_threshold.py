#%%
# %% managing imports
import shutil
from pathlib import Path
import nibabel as nib
import numpy as np
import os


#%%

database = Path("../../../Documents/data/adrian_data/Rats24h")
count =0
for i in database.glob("*"):
    print(i.name)
    count += 1

print(count)

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

create_folder(path + "/Task648_sampling_threshold")
#%%
create_folder(path + "/Task648_sampling_threshold/imagesTr")
create_folder(path + "/Task648_sampling_threshold/imagesTs")
create_folder(path + "/Task648_sampling_threshold/labelsTr")
create_folder(path + "/Task648_sampling_threshold/labelsTs")


#%% function to save the files in targeet database with the new name
def save_files(img, target_database, new_name, flag,file_type):
    if flag <=9:
        output_training_dir = target_database + "/imagesTr"
        output_labels_dir = target_database + "/labelsTr"
        output_training_all = target_database + "/all_related_tr"
    else:
        output_training_dir = target_database + "/imagesTs"
        output_labels_dir = target_database + "/labelsTs"
        output_training_all = target_database + "/all_related_ts"

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

# %%
counter =0
for i in database.iterdir():
    new_database = Path(i)
    new_name = i.name.split("-24h")[0]
    print(new_database)

    adc_file = new_database / "Masked_ADC.nii"
    t2_file = new_database / "Masked_T2.nii"
    gt_file = new_database / "GroundTruth24h.nii"

    save_files(nib.load(adc_file), path + "/Task648_sampling_threshold", new_name, counter, "adc")
    save_files(nib.load(t2_file), path + "/Task648_sampling_threshold", new_name, counter, "t2")
    save_files(nib.load(gt_file), path + "/Task648_sampling_threshold", new_name, counter, "mask")

    counter +=1
