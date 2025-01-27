# %%
import math
from pathlib import Path

import nibabel as nib
import numpy as np
from sklearn.metrics import matthews_corrcoef, roc_auc_score
import pandas as pd

# %%
target_database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat")

gt_dir = target_database / "labelsTs"
pred_dir = target_database / "resultTs"
pred_dir_3d = target_database / "resultTs_3d"


# %% function to compute the dice coefficient
def dc(p, g):
    dice = np.sum(p[g == 1]) * 2.0 / (np.sum(p) + np.sum(g))
    if math.isnan(dice):
        dice = 0.0
    # print('Dice similarity score is {}'.format(dice))
    return dice


# %% calcculate TP, FP, TN, FN
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


# %% define function to calculate accuracy, precision, recall, f1score, sensitivity, specificity,
# false omission rate
def calculate_all_terms(TP, FP, TN, FN):
    accuracy = (TP + TN) / (TP + TN + FN + FP)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1score = 2 * (precision * recall) / (precision + recall)
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    false_omission_rate = FN / (FN + TN)
    npv = 1 - false_omission_rate
    fnr = 1 - sensitivity
    false_positive_rate = 1 - specificity
    fdr = 1 - precision

    return accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate, \
           npv, fnr, false_positive_rate, fdr


# %% define function to calculate  , Area under Curve
def calculate_auc(gt_vector, pred_vector):
    auc = roc_auc_score(gt_vector, pred_vector)

    return auc


# %% for 2d
log_dict = {}
for i in gt_dir.glob("*.nii.gz"):
    new_name = i.name.split(".nii.gz")[0]
    # print(new_name)
    log_dict[new_name] = {}
    gt_data = nib.load(i).get_fdata()
    gt_array = gt_data.flatten()

    for k in pred_dir.glob(i.name):
        pred_data = nib.load(k).get_fdata()
        pred_array = pred_data.flatten()

        # calculate dise score and add it in dict
        temp_pred = np.zeros_like(pred_data)
        temp_gt = np.zeros_like(gt_data)

        temp_pred[pred_data == 1] = 1
        temp_gt[gt_data == 1] = 1
        dice = dc(temp_pred, temp_gt)
        log_dict[new_name]["Dice"] = dice

        # calculate mcc and add it in dict
        mcc = matthews_corrcoef(gt_array, pred_array)
        print(new_name + " : " + str(mcc))
        log_dict[new_name]["mcc"] = mcc

        # calculate TP, FP, TN, FN
        TP, FP, TN, FN = perf_measure(gt_array, pred_array)

        # calculate accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate
        # and add it in dict
        # accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate = \
        #     calculate_all_terms(TP, FP, TN, FN)

        accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate, \
        npv, fnr, false_positive_rate, fdr = calculate_all_terms(TP, FP, TN, FN)

        log_dict[new_name]["PPV"] = precision
        log_dict[new_name]["NPV"] = npv
        log_dict[new_name]["sensitivity"] = sensitivity
        log_dict[new_name]["specificity"] = specificity
        log_dict[new_name]["accuracy"] = accuracy
        log_dict[new_name]["FNR"] = fnr
        log_dict[new_name]["FPR"] = false_positive_rate
        log_dict[new_name]["FDR"] = fdr
        log_dict[new_name]["FOR"] = false_omission_rate
        log_dict[new_name]["F1"] = f1score
        log_dict[new_name]["AUC"] = calculate_auc(gt_array, pred_array)

        print("precision : " + str(precision))

        # calculate auc and add in dict
        auc = calculate_auc(gt_array, pred_array)
        log_dict[new_name]["auc"] = auc

    for j in pred_dir_3d.glob(i.name):
        pred_data = nib.load(j).get_fdata()
        pred_array = pred_data.flatten()

        # calculate dise score and add it in dict
        temp_pred = np.zeros_like(pred_data)
        temp_gt = np.zeros_like(gt_data)

        temp_pred[pred_data == 1] = 1
        temp_gt[gt_data == 1] = 1
        dice = dc(temp_pred, temp_gt)
        log_dict[new_name]["Dice_3d"] = dice

        # calculate mcc and add it in dict
        mcc = matthews_corrcoef(gt_array, pred_array)
        print(new_name + " : " + str(mcc))
        log_dict[new_name]["mcc_3d"] = mcc

        # calculate TP, FP, TN, FN
        TP, FP, TN, FN = perf_measure(gt_array, pred_array)

        # calculate accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate
        # and add it in dict
        # accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate = \
        #     calculate_all_terms(TP, FP, TN, FN)
        # log_dict[new_name]["accuracy_3d"] = accuracy
        # log_dict[new_name]["PPV_3d"] = precision
        # log_dict[new_name]["recall_3d"] = recall
        # log_dict[new_name]["f1score_3d"] = f1score
        # log_dict[new_name]["sensitivity_3d"] = sensitivity
        # log_dict[new_name]["specificity_3d"] = specificity
        # log_dict[new_name]["false_omission_rate_3d"] = false_omission_rate

        accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate, \
        npv, fnr, false_positive_rate, fdr = calculate_all_terms(TP, FP, TN, FN)

        log_dict[new_name]["PPV_3d"] = precision
        log_dict[new_name]["NPV_3d"] = npv
        log_dict[new_name]["sensitivity_3d"] = sensitivity
        log_dict[new_name]["specificity_3d"] = specificity
        log_dict[new_name]["Accuracy_3d"] = accuracy
        log_dict[new_name]["FNR_3d"] = fnr
        log_dict[new_name]["FPR_3d"] = false_positive_rate
        log_dict[new_name]["FDR_3d"] = fdr
        log_dict[new_name]["FOR_3d"] = false_omission_rate
        log_dict[new_name]["F1_3d"] = f1score
        log_dict[new_name]["AUC_3d"] = calculate_auc(gt_array, pred_array)

        print("precision : " + str(precision))

        # calculate auc and add in dict
        auc = calculate_auc(gt_array, pred_array)
        log_dict[new_name]["auc_3d"] = auc

#%%
df = pd.DataFrame.from_dict(log_dict).T

#%%
df.to_csv('Task605_all_calculation.csv')
