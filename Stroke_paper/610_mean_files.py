# %%
import nibabel as nib
import numpy as np
from pathlib import Path
import copy
import matplotlib.pyplot as plt
from utilities.jpm_related_functions import *


#%%
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing")

#%%
task_name = "1w"

#%%
data_path = dataset_path / task_name

#%%

dict = create_dict_for_mean_jpm(data_path)

#%%
img_path = dataset_path / "jpm_&_mean_files" / task_name
create_mean_img_jpm(dict, img_path)

#%%
task_name = "72h"
data_path = dataset_path / task_name

#%%
dict_72h = create_dict_for_mean_jpm(data_path)

#%%
img_path = dataset_path / "jpm_&_mean_files" / task_name
create_mean_img_jpm(dict_72h, img_path)

#%% 24h
task_name = "24h"
data_path = Path("../../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")

#%%
dict_24h = create_dict_for_mean_jpm(data_path)

#%%
img_path = dataset_path / "jpm_&_mean_files" / task_name
create_mean_img_jpm(dict_24h, img_path)

# ------------------------------getting the list ---------------------------------------------
#%%
data_path =  dataset_path / "72h" / "result"
list_72h = seg_list(data_path)

#%%
data_path =  dataset_path / "1w" / "result"
list_1w = seg_list(data_path)

#%%
data_path =  dataset_path / "1m" / "result"
list_1m = seg_list(data_path)

#%% 24h
data_path =  Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/result")
list_24h = seg_list(data_path)

#%%gmm files
dataset_path =  Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files")

#%%
task_name = "24h"
data_path = dataset_path / task_name

#%%
dict_24h = create_dict_for_mean_jpm_with_list(data_path, list_24h)

#%%
img_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/jpm_&_mean_files/gmm") / task_name
create_mean_img_jpm(dict_24h, img_path)

#%% 72h
task_name = "72h"
data_path = dataset_path / task_name

dict_72h = create_dict_for_mean_jpm_with_list(data_path, list_72h)

#%%
img_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/jpm_&_mean_files/gmm") / task_name
create_mean_img_jpm(dict_72h, img_path)

#%% 1w
task_name = "1w"
data_path = dataset_path / task_name

dict_1w = create_dict_for_mean_jpm_with_list(data_path, list_1w)

#%%
img_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/jpm_&_mean_files/gmm") / task_name
create_mean_img_jpm(dict_1w, img_path)

#%% 1m
task_name = "1m"
data_path = dataset_path / task_name

dict_1m = create_dict_for_mean_jpm_with_list(data_path, list_1m)

#%%
img_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/jpm_&_mean_files/gmm") / task_name
create_mean_img_jpm(dict_1m, img_path)






#%% 24h
task_name = "24h"
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")

#%%
dict_24h_control, dict_24h_therapy = create_dict_for_mean_jpm_control_therapy(data_path)

#%%
img_path = dataset_path / "jpm_&_mean_files/Task4/control"
create_mean_img_jpm(dict_24h_control, img_path)

#%% for therapy
img_path = dataset_path / "jpm_&_mean_files/Task4/therapy"
create_mean_img_jpm(dict_24h_therapy, img_path)


#%%
testing_data_list = []
testing_data = data_path / "labelsTs"
for i in testing_data.iterdir():
    # print(i.name)
    testing_data_name = i.name.split(".nii.gz")[0]
    print(testing_data_name)
    # add the name to the list
    testing_data_list.append(testing_data_name)


#%%
filepath = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")

for i in filepath.iterdir():
    print(i.name)

#%%
dict_1w_gt =  create_dict_for_mean_jpm_with_list(filepath, testing_data_list)
# create_dict_for_mean_jpm_with_list

#%% dict to df
import pandas as pd
df_1w_gt = pd.DataFrame.from_dict(dict_1w_gt, orient='index')

#%% sort df by index
df_1w_gt = df_1w_gt.sort_index()

#%% get df index as list
possible_files = df_1w_gt.index.tolist()

#%% sort list by index
testing_data_list.sort()


#%% 24h
task_name = "24h"
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")

#%%
dict_24h_task1 = create_dict_for_mean_jpm_with_list(data_path, possible_files)

#%%
img_path = dataset_path / "jpm_&_mean_files/Task1/24h/"
create_mean_img_jpm(dict_24h_task1, img_path)

#%% gmm 24h
file_path = data_path / "testing/gmm_files/24h"
dict_24h_gmm = create_dict_for_mean_jpm_with_list(file_path, possible_files)

#%%
img_path = dataset_path / "jpm_&_mean_files/Task1/gmm/"
create_mean_img_jpm(dict_24h_gmm, img_path)

#%% 1w
task_name = "1w"
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")

#%%
dict_1w_task1 = create_dict_for_mean_jpm_with_list(data_path, possible_files)

#%%
img_path = dataset_path / "jpm_&_mean_files/Task1/1w_gt/"
create_mean_img_jpm(dict_1w_task1, img_path)


#%% Task 4 24h
task_name = "24h"
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")

#%%
dict_24h_control, dict_24h_therapy = create_dict_for_mean_jpm_control_therapy(data_path)

#%% dict to df
import pandas as pd
df_24h_control = pd.DataFrame.from_dict(dict_24h_control, orient='index')
df_24h_therapy = pd.DataFrame.from_dict(dict_24h_therapy, orient='index')

#%% get the index as list
possible_files_control = df_24h_control.index.tolist()
possible_files_therapy = df_24h_therapy.index.tolist()

# #%%
# img_path = dataset_path / "jpm_&_mean_files/Task4/control"
# create_mean_img_jpm(dict_24h_control, img_path)
#
# #%% for therapy
# img_path = dataset_path / "jpm_&_mean_files/Task4/therapy"
# create_mean_img_jpm(dict_24h_therapy, img_path)

#
# #%%
# testing_data_list = []
# testing_data = data_path / "labelsTs"
# for i in testing_data.iterdir():
#     # print(i.name)
#     testing_data_name = i.name.split(".nii.gz")[0]
#     print(testing_data_name)
#     # add the name to the list
#     testing_data_list.append(testing_data_name)


#%%
filepath = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h")

for i in filepath.iterdir():
    print(i.name)

#%%
dict_24h_gmm_control =  create_dict_for_mean_jpm_with_list(filepath, possible_files_control)
dict_24h_gmm_therapy =  create_dict_for_mean_jpm_with_list(filepath, possible_files_therapy)
# create_dict_for_mean_jpm_with_list

# #%% dict to df
# import pandas as pd
# df_1w_gt = pd.DataFrame.from_dict(dict_1w_gt, orient='index')
#
# #%% sort df by index
# df_1w_gt = df_1w_gt.sort_index()
#
# #%% get df index as list
# possible_files = df_1w_gt.index.tolist()
#
# #%% sort list by index
# testing_data_list.sort()
#
#
# #%% 24h
# task_name = "24h"
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")
#
# #%%
# dict_24h_task1 = create_dict_for_mean_jpm_with_list(data_path, possible_files)

#%%
img_path = dataset_path / "jpm_&_mean_files/Task4/gmm/control"
create_mean_img_jpm(dict_24h_gmm_control, img_path)

#%% for therapy
img_path = dataset_path / "jpm_&_mean_files/Task4/gmm/therapy"
create_mean_img_jpm(dict_24h_gmm_therapy, img_path)

#%%


