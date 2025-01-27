#%%
from pathlib import Path
import pandas as pd

# from Stroke_paper.tp_based_csv_modification import control_dict
from utilities.confusionMatrix_dependent_functions import *

#%%
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data")

for i in dataset_path.glob("*"):
    print(i)

#%% 705
task_name = "705"
rs_path =dataset_path / task_name
dict_705 = {}
dict_705_3d = {}
segmentation_path = rs_path / "result"
segmentation_path_3d = rs_path / "result_3d"
gt_path = rs_path / "gt_niftis"

#%%
calc_stats(gt_path, segmentation_path, dict_705)
calc_stats(gt_path, segmentation_path_3d, dict_705_3d)

#%% dict to df 705
df_705 = pd.DataFrame.from_dict(dict_705, orient='index')
df_705_3d = pd.DataFrame.from_dict(dict_705_3d, orient='index')

#%% df to csv
df_705.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}.csv")
df_705_3d.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}_3d.csv")



#%% 710
task_name = "710"
rs_path =dataset_path / task_name
dict_710 = {}
dict_710_3d = {}
segmentation_path = rs_path / "result"
segmentation_path_3d = rs_path / "result_3d"
gt_path = rs_path / "gt_niftis"

#%%
calc_stats(gt_path, segmentation_path, dict_710)
calc_stats(gt_path, segmentation_path_3d, dict_710_3d)

#%% dict to df 710
df_710 = pd.DataFrame.from_dict(dict_710, orient='index')
df_710_3d = pd.DataFrame.from_dict(dict_710_3d, orient='index')

#%% df to csv
df_710.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}.csv")
df_710_3d.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}_3d.csv")


#%% 715
task_name = "715"
rs_path =dataset_path / task_name
dict_715 = {}
dict_715_3d = {}
segmentation_path = rs_path / "result"
segmentation_path_3d = rs_path / "result_3d"
gt_path = rs_path / "gt_niftis"

#%%
calc_stats(gt_path, segmentation_path, dict_715)
calc_stats(gt_path, segmentation_path_3d, dict_715_3d)

#%% dict to df 715
df_715 = pd.DataFrame.from_dict(dict_715, orient='index')
df_715_3d = pd.DataFrame.from_dict(dict_715_3d, orient='index')

#%% df to csv
df_715.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}.csv")
df_715_3d.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}_3d.csv")

#%% 720
task_name = "720"
rs_path =dataset_path / task_name
dict_720 = {}
dict_720_3d = {}
segmentation_path = rs_path / "result"
segmentation_path_3d = rs_path / "result_3d"
gt_path = rs_path / "gt_niftis"

#%%
calc_stats(gt_path, segmentation_path, dict_720)
calc_stats(gt_path, segmentation_path_3d, dict_720_3d)

#%% dict to df 720
df_720 = pd.DataFrame.from_dict(dict_720, orient='index')
df_720_3d = pd.DataFrame.from_dict(dict_720_3d, orient='index')

#%% df to csv
df_720.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}.csv")
df_720_3d.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}_3d.csv")

#%% 725
task_name = "725"
rs_path =dataset_path / task_name
dict_725 = {}
dict_725_3d = {}
segmentation_path = rs_path / "result"
segmentation_path_3d = rs_path / "result_3d"
gt_path = rs_path / "gt_niftis"

#%%
calc_stats(gt_path, segmentation_path, dict_725)
calc_stats(gt_path, segmentation_path_3d, dict_725_3d)

#%% dict to df 725
df_725 = pd.DataFrame.from_dict(dict_725, orient='index')
df_725_3d = pd.DataFrame.from_dict(dict_725_3d, orient='index')

#%% df to csv
df_725.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}.csv")
df_725_3d.to_csv(f"../nnUNet_raw_data_base/nnUNet_raw_data/threshold_validation_data/{task_name}/{task_name}_3d.csv")







