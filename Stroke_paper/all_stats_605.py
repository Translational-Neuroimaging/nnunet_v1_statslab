#%%
from pathlib import Path
import pandas as pd
from utilities.confusionMatrix_dependent_functions import *

#%%

data_path = Path("../../../Documents/data/adrian_data/Data_Paper_12092022")
gmm_1w = data_path / "GMM/GMM_1w/Niftis"
gmm_24h = data_path / "GMM/GMM_24h/Niftis"
gmm_72h = data_path / "GMM/GMM_72h"
gmm_1m = data_path / "GMM/GMM_1m"

rfc_1m = data_path / "RFC/RFC_24h Train 1m Test/Niftis"
rfc_1w = data_path / "RFC/RFC_24h Train 1w Test/Niftis"
rfc_72h = data_path / "RFC/RFC_24h Train 72h Test/Niftis"

#%%
dict_gmm1w = {}
calc_stats2(gmm_1w, "Voi_1w.nii", "RF_Probmaps1.nii", dict_gmm1w)

#%% dict to df
df_gmm1w = pd.DataFrame.from_dict(dict_gmm1w, orient='index')

#%% save to csv
df_gmm1w.to_csv(str(gmm_1w) + "/GMM_1w.csv")

#%%
dict_gmm24h = {}
calc_stats2(gmm_24h, "Voi_24h.nii", "RF_Probmaps1.nii", dict_gmm24h)

#%% dict to df
df_gmm24h = pd.DataFrame.from_dict(dict_gmm24h, orient='index')

#%% save to csv
df_gmm24h.to_csv(str(gmm_24h) + "/GMM_24h.csv")

#%% 72h
dict_gmm72h = {}
calc_stats2(gmm_72h, "Voi_72h.nii", "RF_Probmaps1.nii", dict_gmm72h)

#%% dict to df
df_gmm72h = pd.DataFrame.from_dict(dict_gmm72h, orient='index')

#%% save to csv
df_gmm72h.to_csv(str(gmm_72h) + "/GMM_72h.csv")

#%% 1m
dict_gmm1m = {}

calc_stats2(gmm_1m, "Voi_1m.nii", "RF_Probmaps1.nii", dict_gmm1m)

#%% dict to df
df_gmm1m = pd.DataFrame.from_dict(dict_gmm1m, orient='index')

#%% save to csv
df_gmm1m.to_csv(str(gmm_1m) + "/GMM_1m.csv")

#%%
dict_rfc1m = {}
calc_stats2(rfc_1m, "Voi_1m.nii", "RF_Probmaps1.nii", dict_rfc1m)

#%% dict to df
df_rfc1m = pd.DataFrame.from_dict(dict_rfc1m, orient='index')

df_rfc1m.to_csv(str(rfc_1m) + "/RFC_1m.csv")

#%%
dict_rfc1w = {}
calc_stats2(rfc_1w, "Voi_1w.nii", "RF_Probmaps1.nii", dict_rfc1w)

#%% dict to df
df_rfc1w = pd.DataFrame.from_dict(dict_rfc1w, orient='index')

df_rfc1w.to_csv(str(rfc_1w) + "/RFC_1w.csv")


#%%
dict_rfc72h = {}
calc_stats2(rfc_72h, "Voi_72h.nii", "RF_Probmaps1.nii", dict_rfc72h)

#%% dict to df
df_rfc72h = pd.DataFrame.from_dict(dict_rfc72h, orient='index')

df_rfc72h.to_csv(str(rfc_72h) + "/RFC_72h.csv")

#%% 605 24h

data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat")

#%%
dict_24h = {}
segmentation_path = data_path / "resultTs_3d"
gt_path = data_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_24h)

#%% dict to df
df_24h = pd.DataFrame.from_dict(dict_24h, orient='index')

#%%mean tversky
print("mean tversky: ", df_24h["tversky"].mean())


#%% save to csv
df_24h.to_csv(str(data_path) + "/24h_3d.csv")


#%%
# ------------------------------605---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat/testing_tp")
data_72h = data_path / "72h"
data_1w = data_path / "1w"
data_1m = data_path / "1m"

for i in  data_path.glob("*"):
    print(i)

#%% 72h 3d
dict_72h_3d = {}
segmentation_path = data_72h / "result_3d"
ground_truth_path = data_72h / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_72h_3d)


#%% dict to df
df_72h_3d = pd.DataFrame.from_dict(dict_72h_3d, orient='index')

# save df to csv
df_72h_3d.to_csv(str(data_72h) +"/3d_72h.csv")


#%% 1w 3d
dict_1w_3d = {}
segmentation_path = data_1w / "result_3d"
ground_truth_path = data_1w / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1w_3d)

#%% dict to df
df_1w_3d = pd.DataFrame.from_dict(dict_1w_3d, orient='index')

# save df to csv
df_1w_3d.to_csv(str(data_1w) +"/3d_1w.csv")


#%% 1m 3d
dict_1m_3d = {}
segmentation_path = data_1m / "result_3d"
ground_truth_path = data_1m / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1m_3d)

#%% dict to df
df_1m_3d = pd.DataFrame.from_dict(dict_1m_3d, orient='index')

# save df to csv
df_1m_3d.to_csv(str(data_1m) +"/3d_1m.csv")
