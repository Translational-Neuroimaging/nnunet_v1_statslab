#%%
from pathlib import Path
import pandas as pd

from utilities.confusionMatrix_dependent_functions import *


#%% control list
data_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
control_list = []
for i in data_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    #add new name to list
    control_list.append(new_name)


#%% 613
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task613_mcao60_spatGmm")

#%%
rs_path = data_path
dict_613 = {}
segmentation_path = "result_3d"
gt_path = rs_path / "labelsTs"

#%% import csv file
csv_path = data_path / "613_spatgt_compare.csv"

df = pd.read_csv(csv_path)


#%% give the name to 1st column name
df.rename(columns={df.columns[0]: "name"}, inplace=True)

#%% if df name is in control list, then add control_df else add it to therapy_df
control_df = pd.DataFrame()
therapy_df = pd.DataFrame()

for i in df["name"]:
    if i in control_list:
        control_df = control_df.append(df[df["name"] == i])
    else:
        therapy_df = therapy_df.append(df[df["name"] == i])


#%% df to csv
control_df.to_csv(data_path / "613_control_gmmspat.csv", index=False)
therapy_df.to_csv(data_path / "613_therapy_gmmspat.csv", index=False)

#%%
csv_path = data_path / "613_control_gmmspat.csv"

df = pd.read_csv(csv_path)