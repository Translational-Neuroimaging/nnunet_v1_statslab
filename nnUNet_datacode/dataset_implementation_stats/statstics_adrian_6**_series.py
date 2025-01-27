#%% imports
import math
from pathlib import Path
import numpy as np
import nibabel as nib
import pandas as pd
from sklearn.metrics import matthews_corrcoef, roc_auc_score

#%%

database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian")

#%% function to calculate the dice scorw
def dice_score(gt_data, pred_data):
    temp_pred = np.zeros_like(pred_data)
    temp_gt = np.zeros_like(gt_data)

    temp_pred[pred_data == 1] = 1
    temp_gt[gt_data == 1] = 1

    intersection = np.sum(temp_pred * temp_gt)
    union = np.sum(temp_pred) + np.sum(temp_gt)
    dice = 2 * intersection / union
    return dice

#%% calcculate TP, FP, TN, FN
def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i] == y_hat[i] == 1:
            TP += 1
        if y_hat[i] == 1 and y_actual[i] != y_hat[i]:
            FP += 1
        if y_actual[i] == y_hat[i] == 0:
            TN += 1
        if y_hat[i] == 0 and y_actual[i] != y_hat[i]:
            FN += 1

    return TP, FP, TN, FN

# %% define function to calculate  , Area under Curve
def calculate_auc(gt_vector, pred_vector):
    auc = roc_auc_score(gt_vector, pred_vector)

    return auc


#%% function to compute states for all tasks
def calculate_terms(TP, FP, TN, FN):
    PPV = TP / (TP + FP)
    NPV = TN / (TN + FN)
    sensitivity = TP / (TP + FN)
    specificity = TN / (FP + TN)
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    FNR = FN / (TP + FN)
    FPR = FP / (FP + TN)
    FDR = FP / (TP + FP)
    FOR = FN / (FN + TN)
    F1 = 2 * PPV * NPV / (PPV + NPV)
    return accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1

#%%
def extract_stats_save(database, task_name):

    pred_2d_dir = database / task_name / "2d_best"
    gt_dir = database / task_name / "gt_files"
    pred_3d_dir = database / task_name / "3d_fullres"

    log_dict_2d = {}
    log_dict_3d = {}
    for i in gt_dir.glob("*.nii.gz"):
        # print(i.name)
        gt_data = nib.load(i).get_fdata()
        gt_array = gt_data.flatten()

        for j in pred_2d_dir.glob("*.nii"):
            print(j.name)
            pred_data = nib.load(j).get_fdata()
            pred_array = pred_data.flatten()

            if j.name == i.name.replace(".nii.gz", ".nii"):
                dice = dice_score(gt_array, pred_array)
                TP, FP, TN, FN = perf_measure(gt_array, pred_array)
                accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1 = calculate_terms(TP, FP, TN, FN)
                auc = calculate_auc(gt_array, pred_array)
                log_dict_2d[j.name] = { 'dice': dice ,'accuracy': accuracy, 'PPV': PPV, 'NPV': NPV,
                                        'sensitivity': sensitivity,'specificity': specificity, 'FNR': FNR, 'FPR': FPR,
                                        'FDR': FDR, 'FOR': FOR, 'F1': F1, 'auc': auc}

        for k in pred_3d_dir.glob("*.nii"):
            print(k.name)
            pred_data = nib.load(k).get_fdata()
            pred_array = pred_data.flatten()

            if k.name == i.name.replace(".nii.gz", ".nii"):
                dice = dice_score(gt_array, pred_array)
                TP, FP, TN, FN = perf_measure(gt_array, pred_array)
                accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1 = calculate_terms(TP, FP, TN, FN)
                auc = calculate_auc(gt_array, pred_array)
                log_dict_3d[k.name] = { 'dice': dice ,'accuracy': accuracy, 'PPV': PPV, 'NPV': NPV,
                                        'sensitivity': sensitivity,'specificity': specificity, 'FNR': FNR, 'FPR': FPR,
                                        'FDR': FDR, 'FOR': FOR, 'F1': F1, 'auc': auc}

    df_2d = pd.DataFrame.from_dict(log_dict_2d).T
    df_3d = pd.DataFrame.from_dict(log_dict_3d).T

    df_2d.to_csv(database / task_name / "2d_stats.csv")
    df_3d.to_csv(database / task_name / "3d_stats.csv")

    return df_2d, df_3d

#%%
Task615_log_2d, Task615_log_3d = extract_stats_save(database, "Task615")

#%%
Task620_log_2d, Task620_log_3d = extract_stats_save(database, "Task620")

#%%
Task625_log_2d, Task625_log_3d = extract_stats_save(database, "Task625")

