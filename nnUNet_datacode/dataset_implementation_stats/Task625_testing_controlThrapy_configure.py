import os
import shutil


# %% create function copy files from source to target

def copy_files(src, trg):
    files = os.listdir(src)

    for fname in files:
        # copying the files to the
        # destination directory
        shutil.copy2(os.path.join(src, fname), trg)

    return 1

#%%
path = "../nnUNet_raw_data_base/nnUNet_raw_data/"
copy_files(path + "Task620_Control/imagesTr", path + "Task625_Theranostics/test_data_controlTherapy")
copy_files(path + "Task620_Control/labelsTr", path + "Task625_Theranostics/labels_test_data")
copy_files(path + "Task625_Theranostics/imagesTs", path + "Task625_Theranostics/test_data_controlTherapy")
copy_files(path + "Task625_Theranostics/labelsTs", path + "Task625_Theranostics/labels_test_data")