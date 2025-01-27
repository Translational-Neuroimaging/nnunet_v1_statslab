import ast
import math
from pathlib import Path

import nibabel as nib
import numpy as np
import pandas as pd
from sklearn.metrics import matthews_corrcoef, roc_auc_score

#%%

base_database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian/Task625")

#%% function to compute the dice coefficient
def dc(p, g):
    dice = np.sum(p[g == 1]) * 2.0 / (np.sum(p) + np.sum(g))
    if math.isnan(dice):
        dice = 0.0
    # print('Dice similarity score is {}'.format(dice))
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
log_dict_625 = {}
for i in base_database.glob("*"):
    if i.name != "gt_files":
        pred_dir = i
    task_name = pred_dir.name
    log_dict_625[task_name] = {}
    gt_dir = base_database / "gt_files"

    for j in gt_dir.glob("*.nii.gz"):
        gt_data = nib.load(j).get_fdata()
        gt_array = gt_data.flatten()

        for k in pred_dir.glob("*.nii"):
            print(k.name)

            pred_data = nib.load(k).get_fdata()
            pred_array = pred_data.flatten()

            if k.name == j.name.replace(".nii.gz", ".nii"):

                temp_pred = np.zeros_like(pred_data)
                temp_gt = np.zeros_like(gt_data)

                temp_pred[pred_data == 1] = 1
                temp_gt[gt_data == 1] = 1

                dice = dc(temp_pred, temp_gt)

                # calculate mcc and add it in dict
                mcc = matthews_corrcoef(gt_array, pred_array)
                print(task_name + " mcc : " + str(mcc))

                TP, FP, TN, FN = perf_measure(gt_array, pred_array)
                accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1 = calculate_terms(TP, FP, TN, FN)
                auc = calculate_auc(gt_array, pred_array)
                log_dict_625[task_name][k.name] = {'accuracy': accuracy, 'PPV': PPV, 'NPV': NPV, 'sensitivity': sensitivity,
                                               'specificity': specificity, 'FNR': FNR, 'FPR': FPR, 'FDR': FDR, 'FOR':
                                                   FOR, 'F1': F1, 'auc': auc, 'Dice': dice, 'mcc': mcc}
                print(log_dict_625[task_name][k.name])


                break


df_625 = pd.DataFrame.from_dict(log_dict_625).T

df_625.to_csv('log_dict_625.csv')


#%%
# save_dict = {
#     'log_dict_615': log_dict_625
# }

# #%% piuckle dump
# import pickle
# with open('log_dict.pickle', 'wb') as handle:
#     pickle.dump(save_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# #%% load pickle
# with open('log_dict.pickle', 'rb') as handle:
#     b = pickle.load(handle)
#

#%% read csv df file
df_615 = pd.read_csv('log_dict_615.csv')
df_620 = pd.read_csv('log_dict_620.csv')
df_625 = pd.read_csv('log_dict_625.csv')



