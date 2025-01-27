# %% managing all the imports here only
from pathlib import Path
import pandas as pd
from utilities.confusionMatrix_dependent_functions import *

#%%
mcao_100 = []
mcao_100_path = Path("../../../Documents/data/adrian_data/Theranostics/")
for k in mcao_100_path.glob("*"):
    # add it to list
    mcao_100.append(k.name)
print(mcao_100)

#%% 612
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat/testing")
rs_path = data_path
dict_605 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_605)

#%% dict to df 650
df_605 = pd.DataFrame.from_dict(dict_605, orient='index')

# save to csv 650
df_605.to_csv(str(rs_path / "605_3d") + ".csv")


#%% mean and median tversky print
print("mean tversky: ", df_605['tversky'].mean())
print("median tversky: ", df_605['tversky'].median())

#%% remove the .nii.gz from the index
df_605.index = df_605.index.str.replace('.nii.gz', '')

#%% if the data_name is in mcao_100 then add it to mcao_100 dict with key as data_name and value as all the data, else add it to rat_60 dict.. if data_name starts with human then add it to human dict
rat_60_dict = {}
rat_100_dict = {}
human_dict = {}

for i in df_605.index:
    if i.startswith("Human"):
        human_dict[i] = df_605.loc[i]
    elif i in mcao_100:
        rat_100_dict[i] = df_605.loc[i]
    else:
        rat_60_dict[i] = df_605.loc[i]

#%% dict to df
rat_60_605_df = pd.DataFrame.from_dict(rat_60_dict, orient='index')
rat_100_605_df = pd.DataFrame.from_dict(rat_100_dict, orient='index')
human_605_df = pd.DataFrame.from_dict(human_dict, orient='index')

#%% mean and median tversky print
print("mean tversky: ", rat_60_605_df['tversky'].mean())
print("median tversky: ", rat_60_605_df['tversky'].median())

print("mean tversky: ", rat_100_605_df['tversky'].mean())
print("median tversky: ", rat_100_605_df['tversky'].median())

print("mean tversky: ", human_605_df['tversky'].mean())
print("median tversky: ", human_605_df['tversky'].median())

#%% save to csv
rat_60_605_df.to_csv(str(rs_path / "rat_60_605_3d") + ".csv")
rat_100_605_df.to_csv(str(rs_path / "rat_100_605_3d") + ".csv")
human_605_df.to_csv(str(rs_path / "human_605_3d") + ".csv")


#%% 653 mcao_100 3d
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task653_mcao_100/testing")
rs_path = data_path

dict_653 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_653)

#%% dict to df 650
df_653 = pd.DataFrame.from_dict(dict_653, orient='index')

# save to csv 650
df_653.to_csv(str(rs_path / "653_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_653['tversky'].mean())
print("median tversky: ", df_653['tversky'].median())

#%% remove the .nii.gz from the index
df_653.index = df_653.index.str.replace('.nii.gz', '')

#%% if the data_name is in mcao_100 then add it to mcao_100 dict with key as data_name and value as all the data, else add it to rat_60 dict.. if data_name starts with human then add it to human dict
rat_60_dict = {}
rat_100_dict = {}
human_dict = {}

for i in df_653.index:
    if i.startswith("Human"):
        human_dict[i] = df_653.loc[i]
    elif i in mcao_100:
        rat_100_dict[i] = df_653.loc[i]
    else:
        rat_60_dict[i] = df_653.loc[i]

#%% dict to df
rat_60_653_df = pd.DataFrame.from_dict(rat_60_dict, orient='index')
rat_100_653_df = pd.DataFrame.from_dict(rat_100_dict, orient='index')
human_653_df = pd.DataFrame.from_dict(human_dict, orient='index')

#%% mean and median tversky print fo all
print("mean tversky: ", rat_60_653_df['tversky'].mean())
print("median tversky: ", rat_60_653_df['tversky'].median())

print("mean tversky: ", rat_100_653_df['tversky'].mean())
print("median tversky: ", rat_100_653_df['tversky'].median())

print("mean tversky: ", human_653_df['tversky'].mean())
print("median tversky: ", human_653_df['tversky'].median())

#%% save to csv
rat_60_653_df.to_csv(str(rs_path / "rat_60_653_3d") + ".csv")
rat_100_653_df.to_csv(str(rs_path / "rat_100_653_3d") + ".csv")
human_653_df.to_csv(str(rs_path / "human_653_3d") + ".csv")


#%% 652 mcao 3d testing folder
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task652_mcao/testing")
rs_path = data_path

dict_652 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_652)

#%% dict to df 650
df_652 = pd.DataFrame.from_dict(dict_652, orient='index')

# save to csv 650
df_652.to_csv(str(rs_path / "652_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_652['tversky'].mean())
print("median tversky: ", df_652['tversky'].median())

#%% remove the .nii.gz from the index
df_652.index = df_652.index.str.replace('.nii.gz', '')

#%% if the data_name is in mcao_100 then add it to mcao_100 dict with key as data_name and value as all the data, else add it to rat_60 dict.. if data_name starts with human then add it to human dict
rat_60_dict = {}
rat_100_dict = {}
human_dict = {}

for i in df_652.index:
    if i.startswith("Human"):
        human_dict[i] = df_652.loc[i]
    elif i in mcao_100:
        rat_100_dict[i] = df_652.loc[i]
    else:
        rat_60_dict[i] = df_652.loc[i]

#%% dict to df
rat_60_652_df = pd.DataFrame.from_dict(rat_60_dict, orient='index')
rat_100_652_df = pd.DataFrame.from_dict(rat_100_dict, orient='index')
human_652_df = pd.DataFrame.from_dict(human_dict, orient='index')

#%% mean and median tversky print fo all
print("mean tversky: ", rat_60_652_df['tversky'].mean())
print("median tversky: ", rat_60_652_df['tversky'].median())

print("mean tversky: ", rat_100_652_df['tversky'].mean())
print("median tversky: ", rat_100_652_df['tversky'].median())

print("mean tversky: ", human_652_df['tversky'].mean())
print("median tversky: ", human_652_df['tversky'].median())

#%% save to csv
rat_60_652_df.to_csv(str(rs_path / "rat_60_652_3d") + ".csv")
rat_100_652_df.to_csv(str(rs_path / "rat_100_652_3d") + ".csv")
human_652_df.to_csv(str(rs_path / "human_652_3d") + ".csv")



#%% 651 mcao 3d testing folder
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task651_rat/")
rs_path = data_path

dict_651 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_651)

#%% dict to df 650
df_651 = pd.DataFrame.from_dict(dict_651, orient='index')

# save to csv 650
df_651.to_csv(str(rs_path / "651_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_651['tversky'].mean())
print("median tversky: ", df_651['tversky'].median())

#%% remove the .nii.gz from the index
df_651.index = df_651.index.str.replace('.nii.gz', '')

#%% if the data_name is in mcao_100 then add it to mcao_100 dict with key as data_name and value as all the data, else add it to rat_60 dict.. if data_name starts with human then add it to human dict
rat_60_dict = {}
rat_100_dict = {}
human_dict = {}

for i in df_651.index:
    if i.startswith("Human"):
        human_dict[i] = df_651.loc[i]
    elif i in mcao_100:
        rat_100_dict[i] = df_651.loc[i]
    else:
        rat_60_dict[i] = df_651.loc[i]

#%% dict to df
rat_60_651_df = pd.DataFrame.from_dict(rat_60_dict, orient='index')
rat_100_651_df = pd.DataFrame.from_dict(rat_100_dict, orient='index')
human_651_df = pd.DataFrame.from_dict(human_dict, orient='index')

#%% mean and median tversky print fo all
print("mean tversky: ", rat_60_651_df['tversky'].mean())
print("median tversky: ", rat_60_651_df['tversky'].median())

print("mean tversky: ", rat_100_651_df['tversky'].mean())
print("median tversky: ", rat_100_651_df['tversky'].median())

print("mean tversky: ", human_651_df['tversky'].mean())
print("median tversky: ", human_651_df['tversky'].median())

#%% remove the rows if tversky = nan for human_651_df
human_651_df_final = human_651_df[human_651_df['tversky'].notna()]

#%% mean and median tversky print for human_651_df_final
print("mean tversky: ", human_651_df_final['tversky'].mean())
print("median tversky: ", human_651_df_final['tversky'].median())


#%% save to csv
rat_60_651_df.to_csv(str(rs_path / "rat_60_651_3d") + ".csv")
rat_100_651_df.to_csv(str(rs_path / "rat_100_651_3d") + ".csv")
human_651_df_final.to_csv(str(rs_path / "human_651_3d") + ".csv")


#%% 650 patch individual testing folder
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task650_patch/testing_data/full_image_data")

#%%
task_name = "60"
rs_path = data_path / task_name
dict_650 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_650)

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')


#%% remove the .nii.gz from the index
df_650.index = df_650.index.str.replace('.nii.gz', '')

# save to csv 650
df_650.to_csv(str(rs_path / "650_60_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_650['tversky'].mean())
print("median tversky: ", df_650['tversky'].median())

#%%
task_name = "100"
rs_path = data_path / task_name
dict_650 = {}
segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_650)

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')


#%% remove the .nii.gz from the index
df_650.index = df_650.index.str.replace('.nii.gz', '')

# save to csv 650
df_650.to_csv(str(rs_path / "650_100_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_650['tversky'].mean())
print("median tversky: ", df_650['tversky'].median())

#%%
task_name = "human"
rs_path = data_path / task_name
dict_650 = {}

segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_650)

#%% dict to df 650
df_650 = pd.DataFrame.from_dict(dict_650, orient='index')


#%% remove the .nii.gz from the index
df_650.index = df_650.index.str.replace('.nii.gz', '')

#%% remove Human10, Human21 and Human44 from df_650 and save it as df_650_final
df_650_final = df_650.drop(['Human10', 'Human21', 'Human44'])

#%% save to csv 650_final
df_650_final.to_csv(str(rs_path / "650_human_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_650_final['tversky'].mean())
print("median tversky: ", df_650_final['tversky'].median())

#%% 601_human_3d
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task601_human/testing")

#%%
rs_path = data_path
dict_601 = {}

segmentation_path = rs_path / "result_3d"
gt_path = rs_path / "labelsTs"

#%%
calc_stats(gt_path, segmentation_path, dict_601)

#%% dict to df 601
df_601 = pd.DataFrame.from_dict(dict_601, orient='index')

#%% remove the .nii.gz from the index
df_601.index = df_601.index.str.replace('.nii.gz', '')

#%% save to csv 601
df_601.to_csv(str(rs_path / "601_3d") + ".csv")

#%% mean and median tversky print
print("mean tversky: ", df_601['tversky'].mean())
print("median tversky: ", df_601['tversky'].median())

#%% if the data_name is in mcao_100 then add it to mcao_100 dict with key as data_name and value as all the data, else add it to rat_60 dict.. if data_name starts with human then add it to human dict
rat_60_dict = {}
rat_100_dict = {}
human_dict = {}

for i in df_601.index:
    if i.startswith("Human"):
        human_dict[i] = df_601.loc[i]
    elif i in mcao_100:
        rat_100_dict[i] = df_601.loc[i]
    else:
        rat_60_dict[i] = df_601.loc[i]

#%% dict to df
rat_60_df = pd.DataFrame.from_dict(rat_60_dict, orient='index')
rat_100_df = pd.DataFrame.from_dict(rat_100_dict, orient='index')
human_df = pd.DataFrame.from_dict(human_dict, orient='index')

#%% mean and median tversky print fo all
print("mean tversky: ", df_601['tversky'].mean())
print("median tversky: ", df_601['tversky'].median())

#%% mean and median tversky print for rat_60_df
print("mean tversky: ", rat_60_df['tversky'].mean())
print("median tversky: ", rat_60_df['tversky'].median())

#%% mean and median tversky print for rat_100_df
print("mean tversky: ", rat_100_df['tversky'].mean())
print("median tversky: ", rat_100_df['tversky'].median())

#%% remove the rows if tversky = nan for human_651_df
human_601_df_final = human_df.drop(['Human10', 'Human21', 'Human44'])
# df_650_final = df_650.drop(['Human10', 'Human21', 'Human44'])

#%% mean and median tversky print for human_601_df_final
print("mean tversky: ", human_601_df_final['tversky'].mean())
print("median tversky: ", human_601_df_final['tversky'].median())


#%% save to csv
rat_60_df.to_csv(str(rs_path / "rat_60_3d") + ".csv")
rat_100_df.to_csv(str(rs_path / "rat_100_3d") + ".csv")
human_601_df_final.to_csv(str(rs_path / "human_601_3d") + ".csv")

