#%%
from utilities.confusion_matrix import calc_ConfusionMatrix
from utilities.confusionMatrix_dependent_functions import *
import numpy as np
import shutil
from pathlib import Path
import nibabel as nib
import numpy as np

import os


#%%
data_path = Path("../../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch")
labels_human = data_path / "labels_reconstructed"
# pred_human_2d = data_path / "result_2d_reconstructed"
# pred_human_3d = data_path / "result_3d_reconstructed"
pred = Path("../../../../Documents/data/Adrian_chamba_strokes_data/RatHumanCombined/")
pred_human = pred / "Human Niftis"
pred_rat = pred / "Rat Niftis"

for i in pred_human.glob("*"):
    print(i.name)

#%%
dice_dict_human_2d = {}
dice_dict_human_3d = {}
dice_dict_rat_2d = {}
dice_dict_rat_3d = {}
for i in labels_human.glob("*.nii.gz"):
    print(i.name)

    label_data = nib.load(i).get_fdata()
    name = i.name
    pred_data_2d = nib.load(pred_human_2d / name).get_fdata()
    pred_data_3d = nib.load(pred_human_3d / name).get_fdata()
    print(label_data.shape)
    print(pred_data_2d.shape)
    print(pred_data_3d.shape)

    # flatten data
    label_data = label_data.flatten()
    pred_data_2d = pred_data_2d.flatten()
    pred_data_3d = pred_data_3d.flatten()

    # calculate all metrics FOR 2D
    tp, tn, fp, fn = calc_ConfusionMatrix(label_data, pred_data_2d, c=1)
    mcc = calc_MCC_CM(tp, tn, fp, fn)
    acc = calc_Accuracy_CM(tp, tn, fp, fn)
    sens = calc_Sensitivity_CM(tp, fn)
    spec = calc_Specificity_CM(tn, fp)
    prec = calc_Precision_CM(tp, fp)
    false_Discovery_Rate = calc_False_Discovery_Rate_CM(fp, tp)
    false_Positive_Rate = calc_False_Positive_Rate_CM(fp, tn)
    positive_predictive_value = calc_Positive_Predictive_Value_CM(tp, fn)
    negative_predictive_value = calc_Negative_Predictive_Value_CM(tn, fp)
    dice = calc_mismDice_CM(truth=label_data, pred=pred_data_2d, c=1)
    wspec = calc_Weighted_Specificity_CM(tn, tn, fp, fn)

    # calculate all metrics FOR 3D
    tp_3d, tn_3d, fp_3d, fn_3d = calc_ConfusionMatrix(label_data, pred_data_3d, c=1)
    mcc_3d = calc_MCC_CM(tp_3d, tn_3d, fp_3d, fn_3d)
    acc_3d = calc_Accuracy_CM(tp_3d, tn_3d, fp_3d, fn_3d)
    sens_3d = calc_Sensitivity_CM(tp_3d, fn_3d)
    spec_3d = calc_Specificity_CM(tn_3d, fp_3d)
    prec_3d = calc_Precision_CM(tp_3d, fp_3d)
    false_Discovery_Rate_3d = calc_False_Discovery_Rate_CM(fp_3d, tp_3d)
    false_Positive_Rate_3d = calc_False_Positive_Rate_CM(fp_3d, tn_3d)
    positive_predictive_value_3d = calc_Positive_Predictive_Value_CM(tp_3d, fn_3d)
    negative_predictive_value_3d = calc_Negative_Predictive_Value_CM(tn_3d, fp_3d)
    dice_3d = calc_mismDice_CM(truth=label_data, pred=pred_data_3d, c=1)
    wspec_3d = calc_Weighted_Specificity_CM(tn_3d, tn_3d, fp_3d, fn_3d)


    if "Rat" in i.name:
        print("rat")
        # add the results to the dictionary with
        dice_dict_rat_2d[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec, "precision": prec, \
            "false_Discovery_Rate": false_Discovery_Rate, "false_Positive_Rate": false_Positive_Rate,\
            "positive_predictive_value": positive_predictive_value, "negative_predictive_value": negative_predictive_value,\
            "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}
        dice_dict_rat_3d[i.name] = {"mcc": mcc_3d, "accuracy": acc_3d, "sensitivity": sens_3d, "specificity": spec_3d, "precision": prec_3d, \
            "false_Discovery_Rate": false_Discovery_Rate_3d, "false_Positive_Rate": false_Positive_Rate_3d,\
            "positive_predictive_value": positive_predictive_value_3d, "negative_predictive_value": negative_predictive_value_3d,\
            "dice": dice_3d, "wspec": wspec_3d, "tp": tp_3d, "tn": tn_3d, "fp": fp_3d, "fn": fn_3d}

    elif "Human" in i.name:
        print("human")
        # add the results to the dictionary with
        dice_dict_human_2d[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec, "precision": prec, \
            "false_Discovery_Rate": false_Discovery_Rate, "false_Positive_Rate": false_Positive_Rate,\
            "positive_predictive_value": positive_predictive_value, "negative_predictive_value": negative_predictive_value,\
            "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}
        dice_dict_human_3d[i.name] = {"mcc": mcc_3d, "accuracy": acc_3d, "sensitivity": sens_3d, "specificity": spec_3d, "precision": prec_3d, \
            "false_Discovery_Rate": false_Discovery_Rate_3d, "false_Positive_Rate": false_Positive_Rate_3d,\
            "positive_predictive_value": positive_predictive_value_3d, "negative_predictive_value": negative_predictive_value_3d,\
            "dice": dice_3d, "wspec": wspec_3d, "tp": tp_3d, "tn": tn_3d, "fp": fp_3d, "fn": fn_3d}

#%%
import pandas as pd
# convert the dictionaries to dataframes
df_dice_rat_2d = pd.DataFrame.from_dict(dice_dict_rat_2d, orient='index')
df_dice_rat_3d = pd.DataFrame.from_dict(dice_dict_rat_3d, orient='index')
df_dice_human_2d = pd.DataFrame.from_dict(dice_dict_human_2d, orient='index')
df_dice_human_3d = pd.DataFrame.from_dict(dice_dict_human_3d, orient='index')

#%%
# save the dataframes to csv files for task 646 human and rat for 2d and 3d
df_dice_rat_2d.to_csv("646_rat_2d.csv")
df_dice_rat_3d.to_csv("646_rat_3d.csv")
df_dice_human_2d.to_csv("646_human_2d.csv")
df_dice_human_3d.to_csv("646_human_3d.csv")


