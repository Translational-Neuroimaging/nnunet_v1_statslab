# %% all the imports
import nibabel as nib
import numpy as np
from pathlib import Path

# %% pathlib import Path("../nnUNet_raw_data_base/nnUNet_raw_data")
from matplotlib import pyplot as plt

database = Path("../nnUNet_raw_data_base/nnUNet_raw_data")

task_name = "Task610_rat"

# %% for 610 and 620 task
label_dir610 = database / task_name / "labelsTs"
label_dir620 = database / "segmentation_results_adrian/final_segmentation_Task6**/Task620/labels"

# %% create list for same test data experiments
list = []

# %%
for i in label_dir610.glob("*"):

    for j in label_dir620.glob("*"):
        if i.name == j.name.replace(".nii", ".nii.gz"):
            list.append(i.name.replace(".nii.gz", ""))

# %%
list_img = []
img_dir = database / task_name / "imagesTs"

for i in img_dir.glob("*_0001.nii.gz"):
    # print(i.name)

    if i.name.replace("_0001.nii.gz", "") in list:
        print(i.name)

        # import nii.gz
        img_data = nib.load(i).get_fdata()
        # print(type(img_data))
        list_img.append(img_data)

# %% take average of all the
# images as the final image
final_img = np.mean(list_img, axis=0)

# %%plot the final image
plt.imshow(final_img[:, :, 78], cmap='gray')
plt.show()



#%% get the labels for the final image
gt_dir = label_dir610

list_gt = []
for i in gt_dir.glob("*"):

    if i.name.replace(".nii.gz", "") in list:
        print(i.name)

        # import nii.gz
        gt_data = nib.load(i).get_fdata()
        # print(type(img_data))
        list_gt.append(gt_data)


#%% take average of all the labels array as the final array
final_gt = np.mean(list_gt, axis=0)

#%% plot the final array
plt.imshow(final_gt[:, :, 78], cmap='gray')
plt.show()

#%% save the final image and final array
nib.save(nib.Nifti1Image(final_img, np.eye(4)), "output/final_img.nii.gz")
nib.save(nib.Nifti1Image(final_gt, np.eye(4)), "output/final_gt.nii.gz")

# %% segmentation files for 610 and 620 task
segmentation_dir_620 = database / "segmentation_results_adrian/final_segmentation_Task6**/Task620/2d_best"
segmentation_dir_610 = database / task_name / "resultTs"

segmentation_dir_610_list = []
segmentation_dir_620_list = []
for i in segmentation_dir_620.glob("*"):

    if i.name.replace(".nii", "") in list:
        print(i.name)

        # import nii.gz
        gt_data = nib.load(i).get_fdata()
        # print(type(img_data))
        segmentation_dir_620_list.append(gt_data)

# %%

for i in segmentation_dir_610.glob("*.nii.gz"):
    # print(i.name)

    if i.name.replace(".nii.gz", "") in list:
        print(i.name)

        # import nii.gz
        gt_data = nib.load(i).get_fdata()
        # print(type(img_data))
        segmentation_dir_610_list.append(gt_data)

# %% average the segmentation files for 610 and 620 task
final_segmentation_620 = np.mean(segmentation_dir_620_list, axis=0)
final_segmentation_610 = np.mean(segmentation_dir_610_list, axis=0)

# %% save the final segmentation files for 610 and 620 task
nib.save(nib.Nifti1Image(final_segmentation_620, np.eye(4)), "output/final_segmentation_620.nii.gz")
nib.save(nib.Nifti1Image(final_segmentation_610, np.eye(4)), "output/final_segmentation_610.nii.gz")







#%% for task 615
task_name = "Task615_ControlTherapy"
gt_dir_615 = database / task_name / "labelsTs"
img_dir_615 = database / task_name / "imagesTs"
segmentation_dir_615 = database / task_name / "2d_best"

#list for all directories
gt_dir_615_list = []
img_dir_615_list = []
segmentation_dir_615_list = []

for i in gt_dir_615.glob("*"):
    # print(i.name)

    #import nii.gz`
    gt_data = nib.load(i).get_fdata()
    #print(type(img_data))
    if gt_data.shape == (93, 93, 120):
        gt_dir_615_list.append(gt_data)

#%%
for i in img_dir_615.glob("*_0001.nii.gz"):
    print(i.name)

    #import nii.gz`
    img_data = nib.load(i).get_fdata()
    #print(type(img_data))
    # if the shape is 93*93*120 then add it to the list
    if img_data.shape == (93, 93, 120):
        img_dir_615_list.append(img_data)
    # img_dir_615_list.append(img_data)

#%%
for i in segmentation_dir_615.glob("*"):
    print(i.name)

    #import nii.gz`
    gt_data = nib.load(i).get_fdata()
    #print(type(img_data))
    if gt_data.shape == (93, 93, 120):
        segmentation_dir_615_list.append(gt_data)

#%% average the files of task 615
final_gt_615 = np.mean(gt_dir_615_list, axis=0)
final_img_615 = np.mean(img_dir_615_list, axis=0)
final_segmentation_615 = np.mean(segmentation_dir_615_list, axis=0)

#%% save the final files of task 615
nib.save(nib.Nifti1Image(final_gt_615, np.eye(4)), "output/final_gt_615.nii.gz")
nib.save(nib.Nifti1Image(final_img_615, np.eye(4)), "output/final_img_615.nii.gz")
nib.save(nib.Nifti1Image(final_segmentation_615, np.eye(4)), "output/final_segmentation_615.nii.gz")



#%% for task 625
task_name = "Task625_Theranostics"
gt_dir_625 = database / task_name / "labels"
img_dir_625 = database / task_name / "test_data_controlTherapy"
segmentation_dir_625 = database / task_name / "2d_best"

#list for all directories
gt_dir_625_list = []
img_dir_625_list = []
segmentation_dir_625_list = []

for i in gt_dir_625.glob("*"):
    print(i.name)

    #import nii.gz`
    gt_data = nib.load(i).get_fdata()
    #print(type(img_data))
    gt_dir_625_list.append(gt_data)

#%%
for i in img_dir_625.glob("*_0001.nii.gz"):
    print(i.name)

    #import nii.gz`
    img_data = nib.load(i).get_fdata()
    #print(type(img_data))
    img_dir_625_list.append(img_data)


#%%
for i in segmentation_dir_625.glob("*"):
    print(i.name)

    #import nii.gz`
    gt_data = nib.load(i).get_fdata()
    #print(type(img_data))
    segmentation_dir_625_list.append(gt_data)

#%% average the files of task 625
final_gt_625 = np.mean(gt_dir_625_list, axis=0)
final_img_625 = np.mean(img_dir_625_list, axis=0)
final_segmentation_625 = np.mean(segmentation_dir_625_list, axis=0)

#%% save the final files of task 625
nib.save(nib.Nifti1Image(final_gt_625, np.eye(4)), "output/final_gt_625.nii.gz")
nib.save(nib.Nifti1Image(final_img_625, np.eye(4)), "output/final_img_625.nii.gz")
nib.save(nib.Nifti1Image(final_segmentation_625, np.eye(4)), "output/final_segmentation_625.nii.gz")




