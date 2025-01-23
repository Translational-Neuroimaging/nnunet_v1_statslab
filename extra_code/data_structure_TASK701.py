# %%
from pathlib import Path
import nibabel as nb
import numpy as np
import pandas as pd

# %% craete new folder on nnUNet_raw_data
import os

output_folder = '../nnUNet_raw_data_base/nnUNet_raw_data/christine_theranostics_data_folder'


def create_folder(folder_path):
    isExist = os.path.exists(folder_path)
    print(isExist)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(folder_path)
        print("The new directory is created!")


# %%
target_base = Path("./../../../Documents/data/adrian_data")

data_24h = target_base / "Rats24h"

# %% create a list of

therapy_list = ["081", "086", "088", "091", "093", '095', '102', '110', '114', '115', '121', '152', '166', '168', '170',
                '171', '180']

# %% craeted 4 list and saved all the index based on strokes size
control_big = []
control_small = []

therapy_big = []
therapy_small = []

for i in data_24h.glob("*"):
    # print(i.name)
    new_dir = i
    rat_label = str(i.name[3:6])
    #
    for j in new_dir.glob("*.nii"):
        img = nb.load(j)

        if j.name == "GroundTruth24h.nii":
            gt_img = nb.load(j).get_fdata()

            pred_array = gt_img.ravel()
            total_values = pd.value_counts(pred_array)
            stroke_size = (total_values[1] / (total_values[0] + total_values[1])) * 100
            print(i.name + " : " + str(stroke_size))  # in percentage

            if rat_label in therapy_list:  # threshold = 1
                if stroke_size <= 1:
                    therapy_small.append(i.name)
                else:
                    therapy_big.append(i.name)
            else:  # threshold = 2.1
                if stroke_size <= 2.1:
                    control_small.append(i.name)
                else:
                    control_big.append(i.name)

# %%
for i in data_24h.glob("*"):
    new_dir = i

    for j in new_dir.glob("*.nii"):
        img = nb.load(j)
        # print(j.name)

        if i.name in control_big:
            updated_path = output_folder + '/christine_control_data/big_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)

        elif i.name in control_small:
            updated_path = output_folder + '/christine_control_data/small_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)

        elif i.name in therapy_big:
            updated_path = output_folder + '/christine_therapy_data/big_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)

        elif i.name in therapy_small:
            updated_path = output_folder + '/christine_therapy_data/small_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)

# %%
control_big

# %% also for theranostics data

theranostics_data = target_base / "Theranostics"

# %%
theranostics_small = []
theranostics_big = []

for i in theranostics_data.glob("*"):
    # print(i.name)
    new_dir = i

    for j in new_dir.glob("Voi24.nii"):
        gt_img = nb.load(j).get_fdata()

        pred_array = gt_img.ravel()
        total_values = pd.value_counts(pred_array)
        stroke_size = (total_values[1] / (total_values[0] + total_values[1])) * 100
        print(i.name + " : " + str(stroke_size))  # in percentage

        if stroke_size <= 12.24:
            theranostics_small.append(i.name)
        else:
            theranostics_big.append(i.name)

        # theranostics_dict[i.name] = {}  # 12.24 is threshold
        # theranostics_dict[i.name]["stroke_size"] = stroke_size

# %% all dataframe to csv
theranostics_small

# %% structuring the data

for i in theranostics_data.glob("*"):
    new_dir = i

    for j in new_dir.glob("*.nii"):
        img = nb.load(j)
        print(j.name)
        if i.name in theranostics_small:
            updated_path = output_folder + '/christine_theranostics_data/small_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)

        elif i.name in theranostics_big:
            updated_path = output_folder + '/christine_theranostics_data/big_strokes_data/' + i.name
            create_folder(updated_path)
            label_name = j.name + ".gz"
            nb.save(img, updated_path + "/" + label_name)



#%%
