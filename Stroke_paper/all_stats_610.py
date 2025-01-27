#%%
from pathlib import Path
import pandas as pd

# from Stroke_paper.tp_based_csv_modification import control_dict
from utilities.confusionMatrix_dependent_functions import *

#%% 646 2d and 3d
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch")
rs_path =dataset_path
dict_646_2d = {}
dict_646_3d = {}
segmentation_path = rs_path / "result_2d_reconstructed"
gt_path = rs_path / "labels_reconstructed"
segmentation_path_3d = rs_path / "result_3d_reconstructed"

#%% create a function to load nii.gz file
def load_nii(file_path):
    return nib.load(file_path).get_fdata()


#%%
segmentation_path_original = rs_path / "result_2d"
for i in segmentation_path_original.glob("*.nii.gz"):

    #load segmentation
    seg = load_nii(i)
    # print shape of gt
    print(seg.shape)


#%%
calc_stats(gt_path, segmentation_path, dict_646_2d)
calc_stats(gt_path, segmentation_path_3d, dict_646_3d)

#%% dict to df 646_2d
df_646_2d = pd.DataFrame.from_dict(dict_646_2d, orient='index')
df_646_3d = pd.DataFrame.from_dict(dict_646_3d, orient='index')

#%% remove .nii.gz from index
df_646_2d.index = df_646_2d.index.str.replace(".nii.gz", "")
df_646_3d.index = df_646_3d.index.str.replace(".nii.gz", "")

#%% if tversky is nan remove the whole raw
df_646_2d = df_646_2d.dropna(subset=['tversky'])
df_646_3d = df_646_3d.dropna(subset=['tversky'])


#%% if index name starts with Human add it new to Human dict for both df
df_human_2d = df_646_2d[df_646_2d.index.str.startswith("Human")]
df_human_3d = df_646_3d[df_646_3d.index.str.startswith("Human")]

#%%
# create list of tuples containing the dataframes and their names
dfs = [(df_646_2d, "646_2d"), (df_human_2d, "human_2d"), (df_646_3d, "646_3d"), (df_human_3d, "human_3d")]

# loop through the list of dataframes and names
for df, name in dfs:
    print(f"mean dice {name}: ", df["dice"].mean())
    print(f"mean tversky {name}: ", df["tversky"].mean())
    print(f"median dice {name}: ", df["dice"].median())
    print(f"median tversky {name}: ", df["tversky"].median())
    print("....")





#%% 650
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data")
rs_path =dataset_path
dict_650 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_650)

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')

#%% remove .nii.gz from index
df_650.index = df_650.index.str.replace(".nii.gz", "")

#%%
df_650.to_csv(str(rs_path / "650_testing_data") + ".csv")

#%% remove the whole raw if tversky is nan
df_650 = df_650.dropna(subset=['tversky'])




#%%
dataset_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch")
rs_path =dataset_path
dict_650_1 = {}
segmentation_path = rs_path / "result"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_650_1)

#%% dict to df 650_1
df_650_1 = pd.DataFrame.from_dict(dict_650_1, orient='index')

#%% remove .nii.gz from index
df_650_1.index = df_650_1.index.str.replace(".nii.gz", "")

#%%
df_650_1.to_csv(str(rs_path / "650_1") + ".csv")

#%% remove the whole raw if tversky is nan
df_650_1 = df_650_1.dropna(subset=['tversky'])

#%% print mean dice, mism and tversky also median dice, mism and tversky
print("mean dice: ", df_650_1["dice"].mean())
print("mean mism: ", df_650_1["mism"].mean())
print("mean tversky: ", df_650_1["tversky"].mean())

print("median dice: ", df_650_1["dice"].median())
print("median mism: ", df_650_1["mism"].median())
print("median tversky: ", df_650_1["tversky"].median())



#%% 613
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task613_mcao60_spatGmm")

#%%
rs_path = data_path
dict_613 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_613)

#%% dict to df 613
df_613 = pd.DataFrame.from_dict(dict_613, orient='index')

#%% remove .nii.gz from index
df_613.index = df_613.index.str.replace(".nii.gz", "")

#%% save to csv 613
df_613.to_csv(str(rs_path / "613_spatgt_compare") + ".csv")

#%%  testing on other timepoints
task_name = "testing_tp/72h"
rs_path = data_path / task_name
dict_613_72h = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_613_72h)

#%% dict to df 613_72h
df_613_72h = pd.DataFrame.from_dict(dict_613_72h, orient='index')

#%% remove .nii.gz from index
df_613_72h.index = df_613_72h.index.str.replace(".nii.gz", "")

#%% save to csv 613_72h
df_613_72h.to_csv(str(rs_path / "613_72h") + ".csv")

#%% testing on other timepoints
task_name = "testing_tp/1w"
rs_path = data_path / task_name
dict_613_1w = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_613_1w)

#%% dict to df 613_1w
df_613_1w = pd.DataFrame.from_dict(dict_613_1w, orient='index')

#%% remove .nii.gz from index
df_613_1w.index = df_613_1w.index.str.replace(".nii.gz", "")

#%% save to csv 613_1w
df_613_1w.to_csv(str(rs_path / "613_1w") + ".csv")

#%% testing on other timepoints
task_name = "testing_tp/1m"
rs_path = data_path / task_name
dict_613_1m = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_613_1m)

#%% dict to df 613_1m
df_613_1m = pd.DataFrame.from_dict(dict_613_1m, orient='index')

#%% remove .nii.gz from index
df_613_1m.index = df_613_1m.index.str.replace(".nii.gz", "")

#%% save to csv 613_1m
df_613_1m.to_csv(str(rs_path / "613_1m") + ".csv")


#%% 612
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task612_mcao60_gmmLabels")

#%%
rs_path = data_path
dict_612 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "testing/labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_612)

#%% compare gt and segmentation
rs_path = data_path
dict_612 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_612)

#%% dict to df 612
df_612 = pd.DataFrame.from_dict(dict_612, orient='index')

# save to csv 612
df_612.to_csv(str(rs_path / "612_gmm_labels_compare") + ".csv")

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_612, orient='index')

# save to csv 650
df_650.to_csv(str(rs_path / "612_gmm_gt_compare") + ".csv")

#%% testing on other timepoints
task_name = "testing_tp/72h"
rs_path = data_path / task_name
dict_612_72h = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_612_72h)

#%% dict to df 612_72h
df_612_72h = pd.DataFrame.from_dict(dict_612_72h, orient='index')

# save to csv 612_72h
df_612_72h.to_csv(str(rs_path / "612_72h") + ".csv")

#%% testing on other timepoints
task_name = "testing_tp/1w"
rs_path = data_path / task_name
dict_612_1w = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_612_1w)

#%% dict to df 612_1w
df_612_1w = pd.DataFrame.from_dict(dict_612_1w, orient='index')

# save to csv 612_1w
df_612_1w.to_csv(str(rs_path / "612_1w") + ".csv")

#%% testing on other timepoints
task_name = "testing_tp/1m"
rs_path = data_path / task_name
dict_612_1m = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

calc_stats(gt_path, segmentation_path, dict_612_1m)

#%% dict to df 612_1m
df_612_1m = pd.DataFrame.from_dict(dict_612_1m, orient='index')

# save to csv 612_1m
df_612_1m.to_csv(str(rs_path / "612_1m") + ".csv")

#%% testing on other timepoints




#%% mean and median tvwrsky print
print("mean tversky: ", df_650["tversky"].mean())
print("median tversky: ", df_650["tversky"].median())

#%% data path 650_patch gmm testing data
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/gmm_testing/data")


#%%
task_name = "mcao_100"
rs_path = data_path / task_name
seg_path = rs_path / "result"
gt_path = rs_path / "labelsTs"
dict_650 = {}

calc_stats(gt_path, seg_path, dict_650)

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')

# save to csv 650
df_650.to_csv(str(rs_path / task_name) + ".csv")
#%% 605 24h

data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task601_human")

for i in data_path.iterdir():
    print(i)

#%%
dict_24h = {}
segmentation_path = data_path / "result_3d"
gt_path = data_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_24h)

#%% dict to df
df_24h = pd.DataFrame.from_dict(dict_24h, orient='index')


# get the index of df as a list
index_list = df_24h.index.tolist()
# remove .nii.gz from the index
index_list = [i.split(".nii.gz")[0] for i in index_list]

#%% remove .nii.gz from the index name of df
df_24h.index = df_24h.index.str.replace('.nii.gz', '')

#%% sort the index
df_24h = df_24h.sort_index()


#%% if tversky is nan, remove the row with index
for i in index_list:
    if np.isnan(df_24h.loc[i, 'tversky']):
        df_24h = df_24h.drop(i)
# df_24h = df_24h.dropna()

#%% save to csv
df_24h.to_csv(str(data_path) + "/human.csv")

#%% get mean of dice and tversky  and msism
print(np.mean(df_24h['dice']))
print(np.mean(df_24h['tversky']))
print(np.mean(df_24h['mism']))
#%% remove the raw with nan in tversky
df_24h = df_24h.dropna()

#%% 24h 1w gt
dict_24h_1w = {}
segmentation_path = data_path / "result"
gt_path = data_path / "testing/1w/labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_24h_1w)

#%% dict to df
df_24h_1w = pd.DataFrame.from_dict(dict_24h_1w, orient='index')

#%% save to csv
df_24h_1w.to_csv(str(data_path) + "/24h_1w_gt.csv")










#%%
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/")


#%% 610 24h 3d
segmentation_path = data_path / "result"
gt_path = data_path / "labelsTs"

#%%
dict_24h_3d = {}
calc_stats(gt_path, segmentation_path, dict_24h_3d)

#%% dict to df
df_24h_3d = pd.DataFrame.from_dict(dict_24h_3d, orient='index')

# mean tversky
print(np.mean(df_24h_3d['tversky']))
# median tversky
print(np.median(df_24h_3d['tversky']))
#%%
df_24h_3d.to_csv(str(data_path) + "/24h.csv")


#%% control list
data_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
control_list = []
for i in data_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    #add new name to list
    control_list.append(new_name)

#%% remove 'therapy_gt1w_gt24h'.csv from control_list
control_list.remove('therapy_gt1w_gt24h.csv')

#%%
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")

#%% open csv file tested_data_gt_volume_seg_vol.csv
df = pd.read_csv(data_path / "tested_data_gt_volume_seg_vol.csv", index_col=0)

#%% remove nii.gz from df index
df.index = df.index.str.replace(".nii.gz", "")


#%%
control_dict = {}
therapy_dict = {}
for i in df.index:
    print(i)
    str = i
    #if str is in index_list, add to dict
    if str in control_list:
        control_dict[i] = df.loc[i]
    else:
        therapy_dict[i] = df.loc[i]

#%% dict to df
df_control = pd.DataFrame.from_dict(control_dict, orient='index')
df_therapy = pd.DataFrame.from_dict(therapy_dict, orient='index')

#%% save to csv
df_control.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w/control.csv")
df_therapy.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w/therapy.csv")
# df_therapy.to_csv(str(data_path) + "/therapy.csv")


#%% remove nii.gz from df_24h_3d index
# df.index = df.index.str.replace(".nii.gz", "")
df_24h_3d.index = df_24h_3d.index.str.replace(".nii.gz", "")
df = df_24h_3d

#%%
w1_index_list

#%% #%%
dict = {}
for i in df_24h_3d.index:
    print(i)
    str = i
    #if str is in index_list, add to dict
    if str in w1_index_list:
        dict[i] = df_24h_3d.loc[i]

#%% dict to df
df_24h = pd.DataFrame.from_dict(dict, orient='index')

#%% save to csv
df_24h.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/24h_3d.csv")

#%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df = df_24h
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df.loc[i])
    else:
        df_control = df_control.append(df.loc[i])

#%% save to csv
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")
df_therapy.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/24h_3d_therapy.csv")
df_control.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/24h_3d_control.csv")

#%% % 24h 1w gt
dict_24h_1w = {}
segmentation_path = data_path / "result_3d"
gt_path = data_path / "testing/1w/labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_24h_1w)

#%% dict to df
df_24h_1w = pd.DataFrame.from_dict(dict_24h_1w, orient='index')

print(np.mean(df_24h_1w['tversky']))
# print(np.mean(df_24h_1w['dice']))

#%% remove the raw with 0 in tversky in df_24h_1w
df_610 = df_24h_1w
df_610 = df_610[df_610['tversky'] != 0]

#%% get df_24h_1w index as a list
w1_index_list = df_610.index.tolist()

#%% save to csv
df_610.to_csv(str(data_path) + "/24h_1w_gt.csv")


#%% remove nii.gz from df_24h_1w index
df_610.index = df_610.index.str.replace(".nii.gz", "")
df = df_610


#%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df.loc[i])
    else:
        df_control = df_control.append(df.loc[i])

#%% save to csv
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")
df_therapy.to_csv(str(data_path) + "/therapy_24h_1w_gt_final.csv")
df_control.to_csv(str(data_path) + "/control_24h_1w_gt_final.csv")

#%% 610 testing 1w
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")

#%% 610 testing 1w
segmentation_path = data_path / "result_3d"
gt_path = data_path / "labelsTs"

#%%
dict_610_1w = {}
calc_stats(gt_path, segmentation_path, dict_610_1w)

#%% dict to df
df_610_1w = pd.DataFrame.from_dict(dict_610_1w, orient='index')

# mean tversky
print(np.mean(df_610_1w['tversky']))

#%% remove the .nii.gz from df_610_1w index
df_610_1w.index = df_610_1w.index.str.replace(".nii.gz", "")

#%% save to csv
df_610_1w.to_csv(str(data_path) + "/610_1w_3d.csv")

#%%
control_dict = {}
therapy_dict = {}

for i in df_610_1w.index:
    if i in control_list:
        control_dict[i] = df_610_1w.loc[i]
    else:
        therapy_dict[i] = df_610_1w.loc[i]

#%% dict to df
df_control = pd.DataFrame.from_dict(control_dict, orient='index')
df_therapy = pd.DataFrame.from_dict(therapy_dict, orient='index')

#%% save to csv
df_control.to_csv(str(data_path) + "/control_610_1w_3d.csv")
df_therapy.to_csv(str(data_path) + "/therapy_610_1w_3d.csv")





#%% gmm 610
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h")


#%% gmmm 24h
segmentation_path = data_path / "result"
gt_path = data_path / "labelsTs"

#%%
dict_24h_gmm = {}
calc_stats(gt_path, segmentation_path, dict_24h_gmm)

#%% dict to df
df_24h_gmm = pd.DataFrame.from_dict(dict_24h_gmm, orient='index')

# mean tversky
print(np.mean(df_24h_gmm['tversky']))
#%%
# df_24h_gmm.to_csv(str(data_path) + "/24h_gmm.csv")


#%% remove the .nii.gz from df_24h_gmm index
df_24h_gmm.index = df_24h_gmm.index.str.replace(".nii.gz", "")

#%%
dict = {}
for i in df_24h_gmm.index:
    print(i)
    str = i
    #if str is in index_list, add to dict
    if str in w1_index_list:
        dict[i] = df_24h_gmm.loc[i]

#%% dict to df
df_24h_gmm_3d = pd.DataFrame.from_dict(dict, orient='index')

#%% save to csv
df_24h_gmm_3d.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/gmm_24h.csv")

#%% control list
data_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
control_list = []
for i in data_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    #add new name to list
    control_list.append(new_name)

#%% remove nii.gz from  index
# df_24h_gmm_3d.index = df_24h_gmm_3d.index.str.replace(".nii.gz", "")
df = df_24h_gmm_3d

#%%  mean tversky
print(np.mean(df['tversky']))
# median tversky
print(np.median(df['tversky']))

#%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df.loc[i])
    else:
        df_control = df_control.append(df.loc[i])

#%% save to csv
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h")
df_therapy.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/therapy_24h_gmm.csv")
df_control.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/control_24h_gmm.csv")


#%% % 24h 1w gt
dict_24h_1w = {}
segmentation_path = data_path / "result"
gt_path = data_path / "1w_labels"

#%%
calc_stats(gt_path, segmentation_path, dict_24h_1w)

#%% dict to df
df_24h_1w = pd.DataFrame.from_dict(dict_24h_1w, orient='index')

print(np.mean(df_24h_1w['tversky']))
# print(np.mean(df_24h_1w['dice']))

#%% remove .nii.gz from index
df_24h_1w.index = df_24h_1w.index.str.replace(".nii.gz", "")

#%% save index as list
index_list = df_610.index.tolist()

#%% save to csv
df_24h_1w.to_csv(str(data_path) + "/24h_1w_gt.csv")

#%%
dict = {}
for i in df_24h_1w.index:
    print(i)
    str = i
    #if str is in index_list, add to dict
    if str in w1_index_list:
        dict[i] = df_24h_1w.loc[i]

#%% dict to df
df_24h_1w_3d = pd.DataFrame.from_dict(dict, orient='index')

# #%% remove the raw with 0 in tversky in df_24h_1w
# df_610 = df_24h_1w
# df_610 = df_610[df_610['tversky'] != 0]


#%% save to csv
df_24h_1w_3d.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/gmm_24h_1w.csv")

#%%
df = df_24h_1w_3d
#%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df.loc[i])
    else:
        df_control = df_control.append(df.loc[i])

#%% save to csv
df_therapy.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/therapy_24h_1w_gmm.csv")
df_control.to_csv("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/gmm_files/24h/control_24h_1w_gmm.csv")

















#%%
# ------------------------------605---------------------------------#
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing")
data_72h = data_path / "72h"
data_1w = data_path / "1w"
data_1m = data_path / "1m"

for i in data_path.glob("*"):
    print(i.name)


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

#%%
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat")
data_24h = data_path

#%% 24h seg 1w gt
dict_24h_1w = {}
segmentation_path = data_24h / "result_3d"
ground_truth_path = data_24h / "testing/1w/labelsTs"

calc_stats(ground_truth_path, segmentation_path, dict_24h_1w)

#%% dict to df
df_24h_1w = pd.DataFrame.from_dict(dict_24h_1w, orient='index')

# save df to csv
df_24h_1w.to_csv(str(data_24h) +"/24h_1w.csv")

#%%
data_path = Path("../../../Documents/data/adrian_data/Data_Paper_12092022")
gmm_1w = data_path / "GMM/GMM_1w/Niftis"
gmm_24h = data_path / "GMM/GMM_24h/Niftis"

#%%
dict_gmm_1w = {}
calc_stats3(gmm_1w, "Voi_1w.nii", gmm_24h, "RF_Probmaps1.nii", dict_gmm_1w)

#%% dict to df and save to csv
df_gmm_1w = pd.DataFrame.from_dict(dict_gmm_1w, orient='index')
df_gmm_1w.to_csv(str(data_path) + "/gmm_1w_voi_24h_mask.csv")

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
segmentation_path = data_path / "resultTs"
gt_path = data_path / "testing/1w" / "labelsTs"

#%%
dict_24h_seg_1w_mask = {}
# calc_stats3(gmm_1w, "Voi_1w.nii", gmm_24h, "RF_Probmaps1.nii", dict_gmm_1w)
for i in segmentation_path.glob("*.nii.gz"):
    print(i.name)
    # file_name = i.name.replace("-1w", "")
    # # print(file_name)
    #
    # if path exists, then continue
    # new_filename = file_name + "-24h"
    if (gt_path / i.name).exists():
        print(str(gt_path / i.name) + "  path exists")
        seg_file_name = i
        gt_file_name = gt_path / i.name

        segmentation = nib.load(str(seg_file_name)).get_fdata()
        ground_truth = nib.load(str(gt_file_name)).get_fdata()
        print(segmentation.shape)
        print(ground_truth.shape)

        # flatten data
        pred_data = segmentation.flatten()
        label_data = ground_truth.flatten()

        name = i.name.replace(".nii.gz", "")
        # calculate all metrics using function calc_all_metrics_CM
        stats = calc_all_metrics_CM(label_data, pred_data)
        dict_24h_seg_1w_mask[name] = {'mcc': stats[0], 'sens': stats[1], 'spec': stats[2], 'prec': stats[3], 'acc': stats[4],
                        'FDR': stats[5], 'FPR': stats[6], 'PPV': stats[7], 'NPV': stats[8], 'dice': stats[9],
                        'wspec': stats[10], 'tversky': stats[11], 'balanced_acc': stats[12]}

#%% dict to df and save to csv
df = pd.DataFrame.from_dict(dict_24h_seg_1w_mask, orient='index')
df.to_csv(str(data_path) + "/24h_pred_1w_gt.csv")

#%% 645 Patch 2d Rat24h
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task645_Patch_2d_Rat24h/")
segmentation_path = data_path / "rat_result_reconstructed"
gt_path = data_path / "labels_reconstructed"
dict_645_2d = {}

#%% 610
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
segmentation_path = data_path / "24h_gt"
gt_path = data_path / "labelsTs"
dict_610_gt1w_gt24h = {}
calc_stats(gt_path, segmentation_path, dict_610_gt1w_gt24h)

#%% dict to df and save to csv
df = pd.DataFrame.from_dict(dict_610_gt1w_gt24h, orient='index')

# mean tversky
print(df["tversky"].mean())

#%%
df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")

#%% control list
data_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
control_list = []
for i in data_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    #add new name to list
    control_list.append(new_name)

#%% remove nii.gz from df index
df.index = df.index.str.replace(".nii.gz", "")



#%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df.loc[i])
    else:
        df_control = df_control.append(df.loc[i])

#%% save to csv
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
df_therapy.to_csv(str(data_path) + "/therapy_gt1w_gt24h.csv")
df_control.to_csv(str(data_path) + "/control_gt1w_gt14h.csv")

#%% 610_rat read csv
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")

df_24h = pd.read_csv(str(data_path) + "/610_gt1w_gt24h.csv", index_col=0)

#%% remove nii.gz from df index
# df_24h.index = df_24h.index.str.replace(".nii.gz", "")
# remove unnamed column
# df_24h = df_24h.drop(columns=["Unnamed: 0"])
# drop raw if tversly is noy zero add to new_df
new_df = pd.DataFrame()
for i in df_24h.index:
    if df_24h.loc[i, "tversky"] != 0:
        new_df = new_df.append(df_24h.loc[i])

#%% #%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in df_24h.index:
    if i not in control_list:
        df_therapy = df_therapy.append(df_24h.loc[i])
    else:
        df_control = df_control.append(df_24h.loc[i])

#%% save to csv
new_df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")
# df_control.to_csv(str(data_path) + "/control_gmm_24h_1w_gt_with_same_testing_data.csv")

#%% 610 rat testing 1w
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
segmentation_path = data_path / "24h_gt"
gt_path = data_path / "labelsTs"

dict_610_gt1w_gt24h = {}
calc_stats(gt_path, segmentation_path, dict_610_gt1w_gt24h)

#%% dict to df and save to csv
df = pd.DataFrame.from_dict(dict_610_gt1w_gt24h, orient='index')

#%%
new_df = pd.DataFrame()
for i in df.index:
    if df.loc[i, "tversky"] != 0:
        new_df = new_df.append(df.loc[i])

#%% save to csv
new_df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")

#%% new df remove nii.gz from df index
new_df.index = new_df.index.str.replace(".nii.gz", "")

#%% #%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
df_therapy = pd.DataFrame()
df_control = pd.DataFrame()

for i in new_df.index:
    if i not in control_list:
        df_therapy = df_therapy.append(new_df.loc[i])
    else:
        df_control = df_control.append(new_df.loc[i])

#%% save to csv
df_therapy.to_csv(str(data_path) + "/therapy_gt1w_gt24h.csv")
df_control.to_csv(str(data_path) + "/control_gt1w_gt14h.csv")

