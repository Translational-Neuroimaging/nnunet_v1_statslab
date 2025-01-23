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


#%%
dice_dict = {}
for i in labels_human.glob("*.nii.gz"):
    print(i.name)
    new_dir = i

    label_data = nib.load(i).get_fdata()
    name = i.name
    pred_data = nib.load(pred_human / name).get_fdata()
    print(label_data.shape)
    print(pred_data.shape)

    # flatten data
    label_data = label_data.flatten()
    pred_data = pred_data.flatten()

    # calculate all metrics
    tp, tn, fp, fn = calc_ConfusionMatrix(label_data, pred_data, c=1)
    mcc = calc_MCC_CM(tp, tn, fp, fn)
    acc = calc_Accuracy_CM(tp, tn, fp, fn)
    sens = calc_Sensitivity_CM(tp, fn)
    spec = calc_Specificity_CM(tn, fp)
    prec = calc_Precision_CM(tp, fp)
    false_Discovery_Rate = calc_False_Discovery_Rate_CM(fp, tp)
    false_Positive_Rate = calc_False_Positive_Rate_CM(fp, tn)
    positive_predictive_value = calc_Positive_Predictive_Value_CM(tp, fn)
    negative_predictive_value = calc_Negative_Predictive_Value_CM(tn, fp)
    dice = calc_mismDice_CM(truth=label_data, pred=pred_data, c=1)
    wspec = calc_Weighted_Specificity_CM(tn, tn, fp, fn)

    # add the results to the dictionary with
    # dice_dict[i.name] = {"normal_dice": normal_dice, "mism_dice": mism_dice}
    dice_dict[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec, "precision": prec, \
        "false_Discovery_Rate": false_Discovery_Rate, "false_Positive_Rate": false_Positive_Rate,\
        "positive_predictive_value": positive_predictive_value, "negative_predictive_value": negative_predictive_value,\
        "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}

#%% dict to dataframe
import pandas as pd
df = pd.DataFrame.from_dict(dice_dict, orient='index')

#%%
# save the dataframe as csv files in results folder
df.to_csv("results/605_rat.csv")

#%%
# ------------------------------610---------------------------------#


#%%
# ------------------------------645---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task645_Patch_2d_Rat24h")
labels_human = data_path / "Human_Patch_testing/labels_reconstructed"
pred_human = data_path / "Human_Patch_testing/result_reconstructed"
label_rat = data_path / "labels_reconstructed"
pred_rat = data_path / "rat_result_reconstructed"

#%%
dice_dict_human = {}
for i in labels_human.glob("*.nii.gz"):
    print(i.name)

    label_data = nib.load(i).get_fdata()
    name = i.name
    pred_data = nib.load(pred_human / name).get_fdata()
    print(label_data.shape)
    print(pred_data.shape)

    # flatten data
    label_data = label_data.flatten()
    pred_data = pred_data.flatten()

    # calculate all metrics
    tp, tn, fp, fn = calc_ConfusionMatrix(label_data, pred_data, c=1)
    mcc = calc_MCC_CM(tp, tn, fp, fn)
    acc = calc_Accuracy_CM(tp, tn, fp, fn)
    sens = calc_Sensitivity_CM(tp, fn)
    spec = calc_Specificity_CM(tn, fp)
    prec = calc_Precision_CM(tp, fp)
    false_Discovery_Rate = calc_False_Discovery_Rate_CM(fp, tp)
    false_Positive_Rate = calc_False_Positive_Rate_CM(fp, tn)
    positive_predictive_value = calc_Positive_Predictive_Value_CM(tp, fn)
    negative_predictive_value = calc_Negative_Predictive_Value_CM(tn, fp)
    dice = calc_mismDice_CM(truth=label_data, pred=pred_data, c=1)
    wspec = calc_Weighted_Specificity_CM(tn, tn, fp, fn)

    # add the results to the dictionary with
    # dice_dict[i.name] = {"normal_dice": normal_dice, "mism_dice": mism_dice}
    dice_dict_human[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec, "precision": prec, \
        "false_Discovery_Rate": false_Discovery_Rate, "false_Positive_Rate": false_Positive_Rate,\
        "positive_predictive_value": positive_predictive_value, "negative_predictive_value": negative_predictive_value,\
        "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}

#%%
dice_dict_rat = {}
for i in label_rat.glob("*.nii.gz"):
    print(i.name)

    label_data = nib.load(i).get_fdata()
    name = i.name
    pred_data = nib.load(pred_rat / name).get_fdata()
    print(label_data.shape)
    print(pred_data.shape)

    # flatten data
    label_data = label_data.flatten()
    pred_data = pred_data.flatten()

    # calculate all metrics
    tp, tn, fp, fn = calc_ConfusionMatrix(label_data, pred_data, c=1)
    mcc = calc_MCC_CM(tp, tn, fp, fn)
    acc = calc_Accuracy_CM(tp, tn, fp, fn)
    sens = calc_Sensitivity_CM(tp, fn)
    spec = calc_Specificity_CM(tn, fp)
    prec = calc_Precision_CM(tp, fp)
    false_Discovery_Rate = calc_False_Discovery_Rate_CM(fp, tp)
    false_Positive_Rate = calc_False_Positive_Rate_CM(fp, tn)
    positive_predictive_value = calc_Positive_Predictive_Value_CM(tp, fn)
    negative_predictive_value = calc_Negative_Predictive_Value_CM(tn, fp)
    dice = calc_mismDice_CM(truth=label_data, pred=pred_data, c=1)
    wspec = calc_Weighted_Specificity_CM(tn, tn, fp, fn)

    # add the results to the dictionary with
    # dice_dict[i.name] = {"normal_dice": normal_dice, "mism_dice": mism_dice}
    dice_dict_rat[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec, "precision": prec, \
        "false_Discovery_Rate": false_Discovery_Rate, "false_Positive_Rate": false_Positive_Rate,\
        "positive_predictive_value": positive_predictive_value, "negative_predictive_value": negative_predictive_value,\
        "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}

#%% dict to dataframe
import pandas as pd
df_human = pd.DataFrame.from_dict(dice_dict_human, orient='index')
df_rat = pd.DataFrame.from_dict(dice_dict_rat, orient='index')

#%%
# save the dataframe as csv files in results folder
df_human.to_csv("results/645_human.csv")
df_rat.to_csv("results/645_rat.csv")

#%%
# ------------------------------646---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch")
labels_human = data_path / "labels_reconstructed"
pred_human_2d = data_path / "result_2d_reconstructed"
pred_human_3d = data_path / "result_3d_reconstructed"

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


#%%
for i in Path("results").glob("*"):
    print(i.name)


    