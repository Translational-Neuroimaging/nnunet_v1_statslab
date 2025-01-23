#%% imports
import math
from pathlib import Path
import numpy as np
import nibabel as nib
import pandas as pd
from sklearn.metrics import matthews_corrcoef, roc_auc_score

#%%

database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/segmentation_results_adrian")


#%% function to calculate the dice scorw
def dice_score(gt_data, pred_data):
    temp_pred = np.zeros_like(pred_data)
    temp_gt = np.zeros_like(gt_data)

    temp_pred[pred_data == 1] = 1
    temp_gt[gt_data == 1] = 1

    intersection = np.sum(temp_pred * temp_gt)
    union = np.sum(temp_pred) + np.sum(temp_gt)
    dice = 2 * intersection / union
    return dice

#%% calcculate TP, FP, TN, FN
def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i] == y_hat[i] == 1:
            TP += 1
        if y_hat[i] == 1 and y_actual[i] != y_hat[i]:
            FP += 1
        if y_actual[i] == y_hat[i] == 0:
            TN += 1
        if y_hat[i] == 0 and y_actual[i] != y_hat[i]:
            FN += 1

    return TP, FP, TN, FN

# %% define function to calculate  , Area under Curve
def calculate_auc(gt_vector, pred_vector):
    auc = roc_auc_score(gt_vector, pred_vector)

    return auc


#%% function to compute states for all tasks
def calculate_terms(TP, FP, TN, FN):
    PPV = TP / (TP + FP)
    NPV = TN / (TN + FN)
    sensitivity = TP / (TP + FN)
    specificity = TN / (FP + TN)
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    FNR = FN / (TP + FN)
    FPR = FP / (FP + TN)
    FDR = FP / (TP + FP)
    FOR = FN / (FN + TN)
    F1 = 2 * PPV * NPV / (PPV + NPV)
    return accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1



#%%
task_name = "Task615"

pred_2d_dir = database / task_name / "2d_best"
gt_dir = database / task_name / "gt_files"
pred_3d_dir = database / task_name / "3d_fullres"

log_dict_2d = {}
log_dict_3d = {}

for i in gt_dir.glob("*.nii.gz"):
    gt_data = nib.load(i).get_fdata()
    gt_array = gt_data.flatten()

    pred_2d_path = pred_2d_dir / i.name.replace(".nii.gz", ".nii")
    pred_2d_data = nib.load(pred_2d_path).get_fdata()
    pred_2d_array = pred_2d_data.flatten()
    print(pred_2d_array.shape)




#%%

def extract_stats_save(database, task_name):
    pred_2d_dir = database / task_name / "resultTs"
    gt_dir = database / task_name / "labelsTs"
    pred_3d_dir = database / task_name / "resultTs_3d"

    log_dict_2d = {}
    log_dict_3d = {}
    for i in gt_dir.glob("*.nii.gz"):
        # print(i.name)
        gt_data = nib.load(i).get_fdata()
        gt_array = gt_data.flatten()

        # 2d
        pred_2d_path = pred_2d_dir / i.name
        pred_2d_data = nib.load(pred_2d_path).get_fdata()
        pred_2d_array = pred_2d_data.flatten()

        dice_2d = dice_score(gt_array, pred_2d_array)
        TP, FP, TN, FN = perf_measure(gt_array, pred_2d_array)
        accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1 = calculate_terms(TP, FP, TN, FN)
        auc = calculate_auc(gt_array, pred_2d_array)
        log_dict_2d[i.name] = { 'dice': dice_2d ,'accuracy': accuracy, 'PPV': PPV, 'NPV': NPV,
                                        'sensitivity': sensitivity,'specificity': specificity, 'FNR': FNR, 'FPR': FPR,
                                        'FDR': FDR, 'FOR': FOR, 'F1': F1, 'auc': auc}
        print(i.name, "2d dice:", dice_2d, "accuracy:", accuracy, "PPV:", PPV, "NPV:", NPV, "sensitivity:", sensitivity, "specificity:", specificity, "FNR:", FNR, "FPR:", FPR, "FDR:", FDR, "FOR:", FOR, "F1:", F1, "auc:", auc)
        # 3d
        pred_3d_path = pred_3d_dir / i.name
        pred_3d_data = nib.load(pred_3d_path).get_fdata()
        pred_3d_array = pred_3d_data.flatten()

        dice_3d = dice_score(gt_array, pred_3d_array)
        TP, FP, TN, FN = perf_measure(gt_array, pred_3d_array)
        accuracy, PPV, NPV, sensitivity, specificity, FNR, FPR, FDR, FOR, F1 = calculate_terms(TP, FP, TN, FN)
        auc = calculate_auc(gt_array, pred_3d_array)

        log_dict_3d[i.name] = {'dice': dice_3d, 'accuracy': accuracy, 'PPV': PPV, 'NPV': NPV,
                               'sensitivity': sensitivity, 'specificity': specificity, 'FNR': FNR, 'FPR': FPR,
                               'FDR': FDR, 'FOR': FOR, 'F1': F1, 'auc': auc}

    df_2d = pd.DataFrame.from_dict(log_dict_2d).T
    df_3d = pd.DataFrame.from_dict(log_dict_3d).T

    return df_2d, df_3d

#%%
Task615_log_2d, Task615_log_3d = extract_stats_save(database, "Task615")

#%%
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

#%%
# indian = df[df['Nationality']=="Indian"]
# overseas = df[df['Nationality']=="Overseas"]

fig =go.Figure()
fig.add_trace(go.Box(y=Task615_log_2d['dice'], name="dice_2d"))
fig.add_trace(go.Box(y=Task615_log_2d['auc'], name="auc_2d"))
fig.add_trace(go.Box(y=Task615_log_2d['accuracy'], name="accuracy_2d"))
fig.add_trace(go.Box(y=Task615_log_3d['dice'], name="dice_3d"))
fig.add_trace(go.Box(y=Task615_log_3d['auc'], name="auc_3d"))
fig.add_trace(go.Box(y=Task615_log_3d['accuracy'], name="accuracy_3d"))
fig.update_layout(xaxis_title="model", yaxis_title="dice range", title="dice comparison")
fig.show()
fig.write_image("output/615_all3.pdf")


#%%
# import plotly.express as px
# df = px.data.tips()
# fig = px.box(Task615_log_2d, y="dice")
# fig.show()

#%%
Task620_log_2d, Task620_log_3d = extract_stats_save(database, "Task620")

#%%
fig =go.Figure()
fig.add_trace(go.Box(y=Task620_log_2d['dice'], name="dice_2d"))
fig.add_trace(go.Box(y=Task620_log_2d['auc'], name="auc_2d"))
fig.add_trace(go.Box(y=Task620_log_3d['accuracy'], name="accuracy_3d"))
fig.add_trace(go.Box(y=Task620_log_3d['dice'], name="dice_3d"))
fig.add_trace(go.Box(y=Task620_log_3d['auc'], name="auc_3d"))
fig.add_trace(go.Box(y=Task620_log_3d['accuracy'], name="accuracy_3d"))
fig.update_layout(xaxis_title="model", yaxis_title="dice range", title="dice comparison")
fig.show()
fig.write_image("output/620_all3.pdf")

#%%
Task625_log_2d, Task625_log_3d = extract_stats_save(database, "Task625")

#%%
fig =go.Figure()
fig.add_trace(go.Box(y=Task625_log_2d['dice'], name="dice_2d"))
fig.add_trace(go.Box(y=Task625_log_2d['accuracy'], name="accuracy_2d"))
fig.add_trace(go.Box(y=Task625_log_2d['auc'], name="auc_2d"))
fig.add_trace(go.Box(y=Task625_log_3d['dice'], name="dice_3d"))
fig.add_trace(go.Box(y=Task625_log_3d['accuracy'], name="accuracy_3d"))
fig.add_trace(go.Box(y=Task625_log_3d['auc'], name="auc_3d"))
fig.update_layout(xaxis_title="model", yaxis_title="dice range", title="dice comparison")
fig.show()
fig.write_image("output/625_all3.pdf")

#%%

database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/")

task_name = "Task610_rat"

pred_2d_dir = database / task_name / "resultTs"
gt_dir = database / task_name / "labelsTs"
pred_3d_dir = database / task_name / "resultTs_3d"

log_dict_2d = {}
log_dict_3d = {}

for i in gt_dir.glob("*.nii.gz"):
    gt_data = nib.load(i).get_fdata()
    gt_array = gt_data.flatten()
    # print(i.name)

    pred_2d_path = pred_2d_dir / i.name
    pred_2d_data = nib.load(pred_2d_path).get_fdata()
    pred_2d_array = pred_2d_data.flatten()
    # print(pred_2d_array.shape)

#%%
database = Path("../nnUNet_raw_data_base/nnUNet_raw_data/")

Task610_log_2d, Task610_log_3d = extract_stats_save(database, "Task610_rat")


#%%
fig =go.Figure()
fig.add_trace(go.Box(y=Task610_log_2d['dice'], name="dice_2d"))
# fig.add_trace(go.Box(y=Task610_log_2d['accuracy'], name="accuracy_2d"))
fig.add_trace(go.Box(y=Task610_log_2d['auc'], name="auc_2d"))
fig.add_trace(go.Box(y=Task610_log_3d['dice'], name="dice_3d"))
# fig.add_trace(go.Box(y=Task610_log_3d['accuracy'], name="accuracy_3d"))
fig.add_trace(go.Box(y=Task610_log_3d['auc'], name="auc_3d"))
fig.update_layout(xaxis_title="model", yaxis_title="range")
fig.show()
fig.write_image("output/610_dice_auc.pdf")

# fig.add_trace(go.Box(y=Task625_log_2d['dice'], name="dice_2d"))
# fig.add_trace(go.Box(y=Task625_log_2d['accuracy'], name="accuracy_2d"))
# fig.add_trace(go.Box(y=Task625_log_2d['auc'], name="auc_2d"))
# fig.add_trace(go.Box(y=Task625_log_3d['dice'], name="dice_3d"))
# fig.add_trace(go.Box(y=Task625_log_3d['accuracy'], name="accuracy_3d"))
# fig.add_trace(go.Box(y=Task625_log_3d['auc'], name="auc_3d"))
# fig.update_layout(xaxis_title="model", yaxis_title="dice range", title="dice comparison")
# fig.show()
# fig.write_image("output/625_all3.pdf")

