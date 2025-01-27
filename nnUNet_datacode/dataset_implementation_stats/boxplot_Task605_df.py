# %%
from pathlib import Path
import nibabel as nb
from rdflib.tools.csv2rdf import column

import calculate_mcc
from sklearn.metrics import matthews_corrcoef
import pandas as pd

# %%
# target_base = Path("..")
target_base = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat")

gt_dir = target_base / "labelsTs"
pred_dir = target_base / "resultTs"
pred_3d_dir = target_base / "resultTs_3d"

# %% for 2d unet result dataset
log_dict = {}
for i in gt_dir.glob("*.nii.gz"):
    new_name = i.name.split(".nii.gz")[0]
    log_dict[new_name] = {}
    gt_data = nb.load(i).get_fdata()
    gt_array = gt_data.flatten()

    for j in pred_dir.glob(i.name):
        pred_data = nb.load(j).get_fdata()
        pred_array = pred_data.flatten()

        mcc = matthews_corrcoef(gt_array, pred_array)
        print(new_name + " : " + str(mcc))
        log_dict[new_name]["mcc"] = mcc

        TP, FP, TN, FN = calculate_mcc.perf_measure(gt_array, pred_array)
        log_dict[new_name]["TP"] = TP
        log_dict[new_name]["FP"] = FP
        log_dict[new_name]["TN"] = TN
        log_dict[new_name]["FN"] = FN

        accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate = calculate_mcc. \
            calculate_all_terms(TP, FP, TN, FN)
        log_dict[new_name]["accuracy"] = accuracy
        log_dict[new_name]["precision"] = precision
        log_dict[new_name]["recall"] = recall
        log_dict[new_name]["f1score"] = f1score
        log_dict[new_name]["sensitivity"] = sensitivity
        log_dict[new_name]["specificity"] = specificity
        log_dict[new_name]["false_omission_rate"] = false_omission_rate
        print("precision : " + str(precision))

        auc = calculate_mcc.calculate_auc(gt_array, pred_array)
        log_dict[new_name]["auc"] = auc

# %%
df = pd.DataFrame.from_dict(log_dict).T

# %%
df.to_csv('boxplot_calculation_2d.csv')

# %% for 3d unet result_files
log_dict_3d = {}
for i in gt_dir.glob("*.nii.gz"):
    new_name = i.name.split(".nii.gz")[0]
    log_dict_3d[new_name] = {}
    gt_data = nb.load(i).get_fdata()
    gt_array = gt_data.flatten()

    for j in pred_3d_dir.glob(i.name):
        pred_data = nb.load(j).get_fdata()
        pred_array = pred_data.flatten()

        mcc = matthews_corrcoef(gt_array, pred_array)
        print(new_name + " : " + str(mcc))
        log_dict_3d[new_name]["mcc"] = mcc

        TP, FP, TN, FN = calculate_mcc.perf_measure(gt_array, pred_array)
        log_dict_3d[new_name]["TP"] = TP
        log_dict_3d[new_name]["FP"] = FP
        log_dict_3d[new_name]["TN"] = TN
        log_dict_3d[new_name]["FN"] = FN

        accuracy, precision, recall, f1score, sensitivity, specificity, false_omission_rate = calculate_mcc. \
            calculate_all_terms(TP, FP, TN, FN)
        log_dict_3d[new_name]["accuracy"] = accuracy
        log_dict_3d[new_name]["precision"] = precision
        log_dict_3d[new_name]["recall"] = recall
        log_dict_3d[new_name]["f1score"] = f1score
        log_dict_3d[new_name]["sensitivity"] = sensitivity
        log_dict_3d[new_name]["specificity"] = specificity
        log_dict_3d[new_name]["false_omission_rate"] = false_omission_rate
        print("precision : " + str(precision))

        auc = calculate_mcc.calculate_auc(gt_array, pred_array)
        log_dict_3d[new_name]["auc"] = auc

# %%
df_3d = pd.DataFrame.from_dict(log_dict_3d).T

# %%
df_3d.to_csv('boxplot_calculation_3d.csv')

# %%
import matplotlib.pyplot as plt

boxplot = df.boxplot(column=['accuracy'])
plt.show()



#%% save dataframe to csv
