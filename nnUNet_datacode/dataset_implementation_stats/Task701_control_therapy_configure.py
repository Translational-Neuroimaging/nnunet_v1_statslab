#%%
import os
from pathlib import Path
import numpy as np
import nibabel as nib
import random


#%%
database_folder = Path("../nnUNet_raw_data_base/nnUNet_raw_data/christine_theranostics_data_folder")

therapy_folder = database_folder / "christine_therapy_data"
control_folder = database_folder / "christine_control_data"
theranoctics_folder = database_folder / "theranostics_data"

#%% find total number of data we have
small_count =0
big_count = 0
for i in control_folder.glob("*"):
    new_dir = i

    for j in new_dir.glob("*"):
        if i.name == "small_strokes_data":
            small_count += 1
        elif i.name == "big_strokes_data":
            big_count += 1

#%%
# small_count
big_count


#%% function to create empty folder
def create_folder(folder_path):
    isExist = os.path.exists(folder_path)
    print(isExist)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(folder_path)
        print("The new directory is created!")

#%%
folder = "../nnUNet_raw_data_base/nnUNet_raw_data/task615_data_prep/"
create_folder(folder + "christine_therapy_data")
create_folder(folder + "christine_therapy_data/small_strokes_data")
create_folder(folder + "christine_therapy_data/big_strokes_data")
create_folder(folder + "christine_control_data")
create_folder(folder + "christine_control_data/small_strokes_data")
create_folder(folder + "christine_control_data/big_strokes_data")
create_folder(folder + "theranostics_data")
create_folder(folder + "theranostics_data/small_strokes_data")
create_folder(folder + "theranostics_data/big_strokes_data")



#%% nii to nii.gz conversion

for i in theranoctics_folder.glob("*"):
    print(i.name)
    new_dir = i

    for j in new_dir.glob("*"):
        new_dir_2 = j

        for k in new_dir_2.glob("*"):
            print(k.name)
    #     img = nib.load(j)
    #     print(j.name)

    #
    #     label_name = str(j).replace("christine_theranostics_data_folder","task615_data_prep") + ".gz"
    #     print(label_name)
        # nib.save(img, label_name)


#%% craete Task 615 data
folder = "../nnUNet_raw_data_base/nnUNet_raw_data/Task615_ControlTherapy/"
create_folder(folder)
create_folder(folder + "imagesTs")
create_folder(folder + "labelsTs")
create_folder(folder + "imagesTr")
create_folder(folder + "labelsTr")
create_folder(folder + "results")
create_folder(folder + "results_3d")
create_folder(folder + "all_related_tr")
create_folder(folder + "all_related_ts")

#%% delete folder with data and create new one
import os
import shutil

folder = "../nnUNet_raw_data_base/nnUNet_raw_data/Task615_ControlTherapy/"
dir = folder

if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)


#%%
def sort_files(img ,target_database, count_small, threshold, new_name):
    if count_small < threshold:
        output_training_dir = target_database + "/imagesTr"
        output_labels_dir = target_database + "/labelsTr"
        output_training_all = target_database + "/all_related_tr"
    else:
        output_training_dir = target_database + "/imagesTs"
        output_labels_dir = target_database + "/labelsTs"
        output_training_all = target_database + "/all_related_ts"

    if k.name == "60.gz":
        label_name = new_name + "_0000.nii.gz"
        print(label_name)
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif k.name == "Masked_T2.nii.gz":
        label_name = new_name + "_0001.nii.gz"
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif k.name == "GroundTruth24h.nii.gz":
        label_name = new_name + ".nii.gz"
        print(output_labels_dir + "/" + label_name)
        nib.save(img, output_labels_dir + "/" + label_name)

    else:
        label_name =new_name + "_" + k.name
        # print(output_training_all + "/" + label_name)
        nib.save(img, output_training_all + "/" + label_name)

#%% function to sort theranstics data
def sort_theranostics_data(img ,target_database, count_small, threshold, new_name):
    if count_small < threshold:
        output_training_dir = target_database + "/imagesTr"
        output_labels_dir = target_database + "/labelsTr"
        output_training_all = target_database + "/all_related_tr"
    else:
        output_training_dir = target_database + "/imagesTs"
        output_labels_dir = target_database + "/labelsTs"
        output_training_all = target_database + "/all_related_ts"

    if k.name == "human.nii.gz":
        label_name = new_name + "_0000.nii.gz"
        print(label_name)
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif k.name == "T2W_c.nii.gz":
        label_name = new_name + "_0001.nii.gz"
        print(output_training_dir + "/" + label_name)
        nib.save(img, output_training_dir + "/" + label_name)

    elif k.name == "Voi24.nii.gz":
        label_name = new_name + ".nii.gz"
        print(output_labels_dir + "/" + label_name)
        nib.save(img, output_labels_dir + "/" + label_name)

    else:
        label_name =new_name + "_" + k.name
        # print(output_training_all + "/" + label_name)
        nib.save(img, output_training_all + "/" + label_name)


#%%  data split and move to task615_ControlTherapy folder
count_small = 0
count_big = 0

for i in control_folder.glob("*"):
    # print(i.name)
    new_dir = i
    target_database = str(database_folder).replace("christine_theranostics_data_folder", "Task615_ControlTherapy")

    for j in new_dir.glob("*"):
        new_dir_2 = j
        new_name = j.name.replace("-24h", "")
        # print(j.name)
        for k in new_dir_2.glob("*"):
            print(k.name)
        if i.name == "small_strokes_data":

            for k in new_dir_2.glob("*"):
                print(k.name)
                img = nib.load(k)
                sort_files(img, target_database, count_small, 6, new_name)
                # sort_theranostics_data(img, target_database, count_small, 12, new_name)
            count_small += 1

        elif i.name == "big_strokes_data":
            for k in new_dir_2.glob("*"):
                print(k.name)
                img = nib.load(k)
                sort_files(img, target_database, count_big, 5, new_name)
                # sort_theranostics_data(img, target_database, count_big, 11, new_name)
            count_big += 1


            # if i.name == "small_strokes_data":
            #     sort_files(img, target_database, count_small, 6, new_name)

        # count_small += 1

        # if i.name == "small_strokes_data" and count_small < 6:
        #     count_small += 1
        #     print(j.name)
        #
        # elif i.name == "small_strokes_data" and count_small >= 6:
        #     print()
        #
        # elif i.name == "big_strokes_data" and count_big < 6:
        #     print()
        #     count_big += 1
        # elif i.name == "big_strokes_data" and count_big >= 6:
        #     print()

print("count_big  = " + str(count_big))
print("count_small = " + str(count_small))


#%%
#
# theranstics data
#small_strokes_data 18
#big_strokes_data 17



#%%

target_database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task615_ControlTherapy")

for i in target_database.glob("*"):
    print(i)
