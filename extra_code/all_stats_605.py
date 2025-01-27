#%%
from utilities.confusion_matrix import calc_ConfusionMatrix
from utilities.confusionMatrix_dependent_functions import *
import numpy as np
import shutil
from pathlib import Path
import pandas as pd
import nibabel as nib
import numpy as np
from utilities.confusionMatrix_dependent_functions import *
import os

#%%

data_path = Path("../../../Documents/data/adrian_data/Data_Paper_12092022")
gmm_1w = data_path / "GMM/GMM_1w/Niftis"
gmm_24h = data_path / "GMM/GMM_24h/Niftis"

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
segmentation_path = data_path / "resultTs"
gt_path = data_path / "labelsTs"

#%%
calc_stats(segmentation_path, gt_path, dict_24h)

#%% dict to df
df_24h = pd.DataFrame.from_dict(dict_24h, orient='index')

#%% save to csv
df_24h.to_csv(str(data_path) + "/24h.csv")

#%% 605 24h 3d
segmentation_path = data_path / "resultTs_3d"
gt_path = data_path / "labelsTs"

#%%
dict_24h_3d = {}
calc_stats(segmentation_path, gt_path, dict_24h_3d)

#%% dict to df
df_24h_3d = pd.DataFrame.from_dict(dict_24h_3d, orient='index')

df_24h_3d.to_csv(str(data_path) + "/24h_3d.csv")

#%%
# ------------------------------605---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat/testing")
data_72h = data_path / "72h"
data_1w = data_path / "1w"
data_1m = data_path / "1m"


#%%
dict_72h = {}
segmentation_path = data_72h / "result"
ground_truth_path = data_72h / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_72h)

#%% dict to df
df_72h = pd.DataFrame.from_dict(dict_72h, orient='index')
# save df to csv

df_72h.to_csv(str(data_72h) +"/2d_72h.csv")

#%% 72h 3d
dict_72h_3d = {}
segmentation_path = data_72h / "result_3d"
ground_truth_path = data_72h / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_72h_3d)


#%% dict to df
df_72h_3d = pd.DataFrame.from_dict(dict_72h_3d, orient='index')

# save df to csv
df_72h_3d.to_csv(str(data_72h) +"/3d_72h.csv")


#%% 1w 2d
dict_1w = {}
segmentation_path = data_1w / "result"
ground_truth_path = data_1w / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1w)

#%% dict to df
df_1w = pd.DataFrame.from_dict(dict_1w, orient='index')

# save df to csv
df_1w.to_csv(str(data_1w) +"/2d_1w.csv")

#%% 1w 3d
dict_1w_3d = {}
segmentation_path = data_1w / "result_3d"
ground_truth_path = data_1w / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1w_3d)

#%% dict to df
df_1w_3d = pd.DataFrame.from_dict(dict_1w_3d, orient='index')

# save df to csv
df_1w_3d.to_csv(str(data_1w) +"/3d_1w.csv")


#%% 1m 2d
dict_1m = {}
segmentation_path = data_1m / "result"
ground_truth_path = data_1m / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1m)

#%% dict to df
df_1m = pd.DataFrame.from_dict(dict_1m, orient='index')

# save df to csv
df_1m.to_csv(str(data_1m) +"/2d_1m.csv")

#%% 1m 3d
dict_1m_3d = {}
segmentation_path = data_1m / "result_3d"
ground_truth_path = data_1m / "labelsTs"
calc_stats(ground_truth_path, segmentation_path, dict_1m_3d)

#%% dict to df
df_1m_3d = pd.DataFrame.from_dict(dict_1m_3d, orient='index')

# save df to csv
df_1m_3d.to_csv(str(data_1m) +"/3d_1m.csv")

#%% 648 calc_stats
# ------------------------------648---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task648_sampling_threshold")
segmentation_path = data_path / "result_2d"
ground_truth_path = data_path / "labelsTs"

dict_648 = {}
calc_stats(ground_truth_path, segmentation_path, dict_648)

#%% dict to df
df_648 = pd.DataFrame.from_dict(dict_648, orient='index')

# save df to csv
df_648.to_csv(str(data_path) +"/2d_648.csv")

#%% 649
# ------------------------------649---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task649_sampling_threshold_2")
segmentation_path = data_path / "result_2d"
ground_truth_path = data_path / "labelsTs"

dict_649 = {}
calc_stats(ground_truth_path, segmentation_path, dict_649)

#%% dict to df
df_649 = pd.DataFrame.from_dict(dict_649, orient='index')

# save df to csv
df_649.to_csv(str(data_path) +"/2d_649.csv")

#%%





#%% mean and median dice of dict_648
print(np.mean(df_648['dice']))
print(np.median(df_648['dice']))
print(np.std(df_648['dice']))

#%% mean and median dice of dict_649
print(np.mean(df_649['dice']))
print(np.median(df_649['dice']))
print(np.std(df_649['dice']))


#%%sklearn balaced_accuracy_score
from sklearn.metrics import balanced_accuracy_score

dice_bal_acc = {}
for i in segmentation_path.glob("*.nii.gz"):
    print(i.name)
    segmentation = nib.load(str(i)).get_fdata()
    ground_truth = nib.load(str(ground_truth_path / i.name)).get_fdata()
    print(segmentation.shape)
    print(ground_truth.shape)

    # flatten data
    pred_data = segmentation.flatten()
    label_data = ground_truth.flatten()

    stats = calc_all_metrics_CM(label_data, pred_data, c=1)
    bal_acc = balanced_accuracy_score(label_data, pred_data)
    bal_acc_1 = balanced_accuracy_score(label_data, pred_data, adjusted=True)
    # balanced_accuracy_score
    dice_bal_acc[i.name] = {'dice': stats[9], 'acc': stats[4], 'balanced_accuracy_score': bal_acc,
                            'balanced_accuracy_score_1': bal_acc_1}

    # # calculate all metrics using function calc_all_metrics_CM
    # stats = calc_all_metrics_CM(label_data, pred_data, c=1)
    # dict[i.name] = {'mcc': stats[0], 'sens': stats[1], 'spec': stats[2], 'prec': stats[3], 'acc': stats[4],
    #                 'FDR': stats[5], 'FPR': stats[6], 'PPV': stats[7], 'NPV': stats[8], 'dice': stats[9],
    #                 'wspec': stats[10]}

#%% dict to df
df_dice_bal_acc = pd.DataFrame.from_dict(dice_bal_acc, orient='index')

