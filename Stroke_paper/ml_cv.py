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
list_tr = []
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/labelsTr")

for i in data_path.glob("*"):
    # print(i.name)
    new_name = i.name.split(".nii")[0]
    print(new_name)
    # add the name to the list
    list_tr.append(new_name)
    # save it as lis