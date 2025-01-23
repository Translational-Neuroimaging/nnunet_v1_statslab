#%%  managing all the imports here only
from pathlib import Path
import numpy as np
import pandas as pd
import os
import shutil

#%%
human_data = Path("../../../Documents/data/adrian_data/Human_copy")
output_path = "../../../Documents/data/adrian_data/Human_labelled"

#%% change the name of the folders and all add to dictionary
data_dict = {}
count = 0

for i in human_data.glob("*"):
    folder_name = i.name

    if len(str(count)) == 1:
        new_name = "Human0" + str(count)
    else:
        new_name = "Human" + str(count)
    print(new_name)

    # add to dictionary with old name as key and new name as value
    data_dict[folder_name] = new_name

    # create a new folder with new name with output_path if not exist
    if not os.path.exists(output_path + "/" + new_name):
        os.makedirs(output_path + "/" + new_name)

    new_folder_name = output_path + "/" + new_name
    src_files = os.listdir(str(i))

    for file_name in src_files:
        full_file_name = os.path.join(str(i), file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, new_folder_name)

    count += 1


#%% data_dict to dataframe
df_labels = pd.DataFrame(data_dict, index=[0])

#%% save it to csv
df_labels.to_csv(output_path + "/Human_name_mapping.csv", index=False)
