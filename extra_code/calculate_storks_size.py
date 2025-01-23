# %%
from pathlib import Path
import nibabel as nb
import numpy as np
import pandas as pd
from sklearn.metrics import matthews_corrcoef, roc_auc_score

# %%
target_base = Path("./../../../Documents/data/adrian_data")

data_24h = target_base / "Rats24h"
# pred_dir = target_base / "resultTs"


# %% create a list of

therapy_list = ["081", "086", "088", "091", "093", '095', '102', '110', '114', '115', '121', '152', '166', '168', '170',
                '171', '180']

# %%
log_dict = {}
log_therapy_list = {}
for i in data_24h.glob("*"):
    new_dir = i
    rat_label = str(i.name[3:6])

    for j in new_dir.glob("GroundTruth24h.nii"):
        gt_img = nb.load(j).get_fdata()

        pred_array = gt_img.ravel()
        total_values = pd.value_counts(pred_array)
        stroke_size = (total_values[1] / (total_values[0] + total_values[1])) * 100
        print(i.name + " : " + str(stroke_size))  # in percentage

        if rat_label in therapy_list:  # threshold = 1
            log_therapy_list[i.name] = {}
            log_therapy_list[i.name]["stroke_size"] = stroke_size
        else:  # threshold = 2.1
            log_dict[i.name] = {}
            log_dict[i.name]["stroke_size"] = stroke_size

# %% all dataframe to csv
df_log_dict = pd.DataFrame.from_dict(log_dict, orient='index')
df_log_therapy_dict = pd.DataFrame.from_dict(log_therapy_list, orient='index')

df_log_therapy_dict.to_csv('stroke_size_therapy.csv')
df_log_dict.to_csv('stroke_size_control.csv')

# %% also for theranostics data

theranostics_data = target_base / "Theranostics"

# %%
theranostics_dict = {}
for i in theranostics_data.glob("*"):
    # print(i.name)
    new_dir = i

    for j in new_dir.glob("Voi24.nii"):
        gt_img = nb.load(j).get_fdata()

        pred_array = gt_img.ravel()
        total_values = pd.value_counts(pred_array)
        stroke_size = (total_values[1] / (total_values[0] + total_values[1])) * 100
        print(i.name + " : " + str(stroke_size))  # in percentage

        theranostics_dict[i.name] = {}  # 12.24 is threshold
        theranostics_dict[i.name]["stroke_size"] = stroke_size

# %% all dataframe to csv
df_theranostics_dict = pd.DataFrame.from_dict(theranostics_dict, orient='index')



