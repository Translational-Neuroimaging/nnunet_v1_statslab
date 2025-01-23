#%%
import os
from pathlib import Path

import nibabel as nib
import numpy as np

#%%
input_database = "../../Documents/WSIC/data WSIC/Rats24h"
output_database = "../../Documents/WSIC/data WSIC/Trail_task"


#%% import the ground truth from the nifti_store
gt_path =  Path("nifti_store/GroundTruth24h.nii")
output_path = 'nifti_store'
print(type(output_path))
#%%
gt_nifti = nib.load(gt_path)
print("gt_nifti shape: ", gt_nifti.shape)
gt_data = np.array(gt_nifti.dataobj)
gt_data[gt_data != 0] = 0
print(np.unique(gt_data))
#%%
nii_file = nib.Nifti1Image(gt_data, np.eye(4))


#%%
nib.save(nii_file, output_path + '/GroundTruth24h_modified.nii')
nib.save(gt_nifti, output_path + '/GroundTruth24h_normal.nii')
#%% save


#%% get and save the main nifti files
def get_and_save_nifti(input_file, destination_folder, file_type, counter):

    if counter < 37:
        if file_type == "t2" or file_type == "adc":
            destination_folder = destination_folder + "/imagesTr"
        elif file_type == "seg":
            destination_folder = destination_folder + "/labelsTr"
    else:
        if file_type == "t2" or file_type == "adc":
            destination_folder = destination_folder + "/imagesTs"
        elif file_type == "seg":
            destination_folder = destination_folder + "/labelsTs"

    load_nifti = nib.load(input_file)

    if file_type == "seg":
        seg_data = load_nifti.get_fdata()
        seg_data[seg_data != 0] = 0
        nii_file = nib.Nifti1Image(seg_data, np.eye(4))
    else:
        nii_file = load_nifti

    if file_type == "t2":
        new_name = new_dir_name + '_0001' + '.nii.gz'
    elif file_type == "adc":
        new_name = new_dir_name + '_0000' + '.nii.gz'
    elif file_type == "seg":
        new_name = new_dir_name + '.nii.gz'
        # new_name = new_dir_name + '_' + str(element) + '.nii.gz'

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    file_name  = destination_folder + '/' + new_name
    # print(type(file_name))
    nib.save(nii_file, file_name)
    print(new_dir_name + " " + file_type + ' saved')


#%%import data using Pathlib
input_folder = Path(input_database)
count = 0
for file in input_folder.iterdir():
    new_dir = file
    new_dir_name = new_dir.name.replace("-24h", "")
    print(type(new_dir_name))

    for i in new_dir.glob("*.nii"):
        if i.name == "Masked_ADC.nii":
            get_and_save_nifti(i, str(output_database), "adc", count)
        elif i.name == "Masked_T2.nii":
            get_and_save_nifti(i, str(output_database), "t2", count)
        elif i.name == "GroundTruth24h.nii":
            get_and_save_nifti(i, str(output_database), "seg", count)
    count += 1
