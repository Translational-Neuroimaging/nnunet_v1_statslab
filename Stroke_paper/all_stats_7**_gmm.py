#%%
from pathlib import Path
import pandas as pd
from utilities.confusionMatrix_dependent_functions import *


#%% 705

data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/sampling_threshold_gmm/old/data")

#%%
task_name = "5"
rs_path = data_path / task_name

dict_05 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_05)

#%% dict to df 05
df_05 = pd.DataFrame.from_dict(dict_05, orient='index')

#%%  mean of df_705 dice
np.mean(df_05['tversky'])


#%% save to csv 705
df_05.to_csv(str(data_path) + "/05.csv")

#%% 10
task_name = "10"
rs_path = data_path / task_name

dict_10 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_10)

#%% dict to df 10
df_10 = pd.DataFrame.from_dict(dict_10, orient='index')

df_10.to_csv(str(data_path) + "/10.csv")


#%% 15
task_name = "15"
rs_path = data_path / task_name

dict_15 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_15)

#%% dict to df 15
df_15 = pd.DataFrame.from_dict(dict_15, orient='index')

df_15.to_csv(str(data_path) + "/15.csv")

#%% 20
task_name = "20"
rs_path = data_path / task_name

dict_20 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_20)

#%% dict to df 20
df_20 = pd.DataFrame.from_dict(dict_20, orient='index')

df_20.to_csv(str(data_path) + "/20.csv")

#%% 25
task_name = "25"
rs_path = data_path / task_name

dict_25 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_25)

#%% dict to df 25
df_25 = pd.DataFrame.from_dict(dict_25, orient='index')

df_25.to_csv(str(data_path) + "/25.csv")

#%% print mean of tversky
print(np.mean(df_05['tversky']))
print(np.mean(df_10['tversky']))
print(np.mean(df_15['tversky']))
print(np.mean(df_20['tversky']))
print(np.mean(df_25['tversky']))