#%%
from pathlib import Path
import pandas as pd
from utilities.confusionMatrix_dependent_functions import *

#%% 705

data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data")

#%% 705
rs_path = data_path / "Task705_sampling_threshold"
dict_705 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

for i in segmentation_path.glob("*.nii.gz"):
    print(i.name)

#%%
calc_stats(gt_path, segmentation_path, dict_705)

#%% dict to df 705
df_705 = pd.DataFrame.from_dict(dict_705, orient='index')

#%%  mean of df_705 dice
np.mean(df_705['tversky'])


#%% save to csv 705
df_705.to_csv(str(rs_path) + "/705_new.csv")

#%% 710
rs_path = data_path / "Task710_sampling_threshold"
dict_710 = {}

segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_710)

#%% dict to df 710
df_710 = pd.DataFrame.from_dict(dict_710, orient='index')

#%%  mean of df_705 dice
np.mean(df_710['tversky'])

#%% save to csv 710
df_710.to_csv(str(rs_path) + "/710_new.csv")

#%% 715
rs_path = data_path / "Task715_sampling_threshold"
dict_715 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_715)

#%% dict to df 715
df_715 = pd.DataFrame.from_dict(dict_715, orient='index')

#%%  mean of df_705 dice
np.mean(df_715['tversky'])

#%% save to csv 715
df_715.to_csv(str(rs_path) + "/715_new.csv")


#%% 720
rs_path = data_path / "Task720_sampling_threshold"
dict_720 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_720)

#%% dict to df 720
df_720 = pd.DataFrame.from_dict(dict_720, orient='index')

#%%  mean of df_705 dice
np.mean(df_720['tversky'])

#%% save to csv 720
df_720.to_csv(str(rs_path) + "/720_new.csv")

#%% 725
rs_path = data_path / "Task725_sampling_threshold"
dict_725 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_725)

#%% dict to df 725
df_725 = pd.DataFrame.from_dict(dict_725, orient='index')

#%%  mean of df_705 dice
np.mean(df_725['tversky'])

#%% save to csv 725
df_725.to_csv(str(rs_path) + "/725_new.csv")


#%% 705 to 725 mean tversky print
print("705: ", np.mean(df_705['tversky']))
print("710: ", np.mean(df_710['tversky']))
print("715: ", np.mean(df_715['tversky']))
print("720: ", np.mean(df_720['tversky']))
print("725: ", np.mean(df_725['tversky']))

#%% print mean dice 705 to 725
print("705: ", np.mean(df_705['dice']))
print("710: ", np.mean(df_710['dice']))
print("715: ", np.mean(df_715['dice']))
print("720: ", np.mean(df_720['dice']))
print("725: ", np.mean(df_725['dice']))

#%% median tversky 705 to 725
print("705: ", np.median(df_705['tversky']))
print("710: ", np.median(df_710['tversky']))
print("715: ", np.median(df_715['tversky']))
print("720: ", np.median(df_720['tversky']))
print("725: ", np.median(df_725['tversky']))


#%% 801
rs_path = data_path / "Task801_control_training"
dict_801 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_801)

#%% dict to df 801 & save to csv 801
df_801 = pd.DataFrame.from_dict(dict_801, orient='index')

#%%

df_801.to_csv(str(rs_path) + "/801.csv")

#%% 802
rs_path = data_path / "Task802_therapy_training"
dict_802 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_802)

#%% dict to df 802 & save to csv 802
df_802 = pd.DataFrame.from_dict(dict_802, orient='index')

df_802.to_csv(str(rs_path) + "/802.csv")


#%% 610 rat
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/")


rs_path = data_path / "Task610_rat"
dict_24h_3d = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

for i in segmentation_path.glob("*"):
    print(i)

calc_stats(gt_path, segmentation_path, dict_24h_3d)

#%%
df_24h_3d = pd.DataFrame.from_dict(dict_24h_3d, orient='index')

#%% remove .nii from index
df_24h_3d.index = df_24h_3d.index.str.replace('.nii.gz', '')

#%% save to csv
df_24h_3d.to_csv(str(rs_path) + "/24h_3d.csv")

#%% GMM stats 24h
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/")


rs_path = data_path / "Task610_rat/testing/gmm_files/24h"
dict_gmm_24h = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

for i in segmentation_path.glob("*"):
    print(i)

calc_stats(gt_path, segmentation_path, dict_gmm_24h)

#%% dict to df gmm 24h & save to csv gmm 24h
df_gmm_24h = pd.DataFrame.from_dict(dict_gmm_24h, orient='index')

#%% remove .nii from index
df_gmm_24h.index = df_gmm_24h.index.str.replace('.nii.gz', '')

#%% save to csv
df_gmm_24h.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/gmm_24h.csv")

#%% get index list from df_24h_3d index
index_list = df_24h_3d.index.tolist()

#%% remove .nii from index_list items
index_list = [i.replace('.nii.gz', '') for i in index_list]

#%%
dict = {}
for i in df_gmm_24h.index:
    print(i)
    str = i
    #if str is in index_list, add to dict
    if str in index_list:
        dict[i] = df_gmm_24h.loc[i]

#%% dict to df
df_gmm_same_testing = pd.DataFrame.from_dict(dict, orient='index')
#%%
df_gmm_same_testing.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/gmm_24h_with_same_testing_data.csv")

#%% mean tversky of df_gmm_same_testing
np.mean(df_gmm_same_testing['tversky'])
#%% GMM stats 72h
rs_path = data_path / "Task610_rat/testing/gmm_files/72h"
dict_gmm_72h = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_gmm_72h)

#%% dict to df gmm 72h & save to csv gmm 72h
df_gmm_72h = pd.DataFrame.from_dict(dict_gmm_72h, orient='index')

df_gmm_72h.to_csv(str(rs_path) + "/gmm_72h.csv")

#%% GMM stats 1w
rs_path = data_path / "Task610_rat/testing/gmm_files/1w"
dict_gmm_1w = {}

segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_gmm_1w)

#%% dict to df gmm 1w & save to csv gmm 1w
df_gmm_1w = pd.DataFrame.from_dict(dict_gmm_1w, orient='index')

df_gmm_1w.to_csv(str(rs_path) + "/gmm_1w.csv")

#%% GMM stats 1m
rs_path = data_path / "Task610_rat/testing/gmm_files/1m"
dict_gmm_1m = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_gmm_1m)

#%% dict to df gmm 1m & save to csv gmm 1m
df_gmm_1m = pd.DataFrame.from_dict(dict_gmm_1m, orient='index')

df_gmm_1m.to_csv(str(rs_path) + "/gmm_1m.csv")



#%% 651_rat
rs_path = data_path / "Task651_rat"

for i in rs_path.iterdir():
    print(i)
dict_651 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_651)

#%% dict to df 651 & save to csv 651
df_651 = pd.DataFrame.from_dict(dict_651, orient='index')

df_651.to_csv(str(rs_path) + "/651_twersky.csv")

#%%
np.mean(df_651['tversky'])

#%% 650_patch
rs_path = data_path / "Task650_patch"
dict_650 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

calc_stats(segmentation_path, gt_path, dict_650)

#%% dict to df 650 & save to csv 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')

df_650.to_csv(str(rs_path) + "/650.csv")

#%%
np.mean(df_650['dice'])

#%% 651_patch
rs_path = data_path / "Task651_patch"
dict_651 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"
