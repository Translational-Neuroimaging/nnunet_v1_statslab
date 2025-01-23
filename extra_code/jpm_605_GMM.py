#%%managing imports
import numpy as np
from pathlib import Path
import nibabel as nib
import matplotlib.pyplot as plt
from utilities.confusion_matrix import calc_ConfusionMatrix
from utilities.confusionMatrix_dependent_functions import *


#%% load  the csv files
import  pandas as pd
mappinf_human =pd.read_csv("utils/Human_name_mapping.csv")
mapping = pd.read_csv("results/605_rat.csv")

#%% get all the columns as a list from mapping_human
columns = mappinf_human.columns.tolist()


#%%
mappinf_human[columns[0]].values

#%% get the first column of df as list
list = mapping.iloc[:,0].tolist()
#%%

#%%
list

#%%
rat_datapath = "../../../Documents/data/Adrian_chamba_strokes_data/Rat/Niftis"

datapath = "../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat/resultTs"


#%%
unet_list = []
for i in Path(datapath).glob("*.nii.gz"):
    print(i.name)
    data = nib.load(i).get_fdata()
    unet_list.append(data)


#%%
adc_list = []
gmm_list = []
gt_list = []

for i in Path(rat_datapath).glob("*"):
    new_name = i.name.split("-")[0]+".nii.gz"
    # print(new_name)
    if new_name in list:
        adc_data = nib.load(i/"Masked_ADC.nii").get_fdata()
        gmm_data = nib.load(i/"RF_Probmaps1.nii").get_fdata()
        gt_data = nib.load(i/"Voi_24h.nii").get_fdata()
        # append the data to the list
        adc_list.append(adc_data)
        gmm_list.append(gmm_data)
        gt_list.append(gt_data)

#%% get the average of the list
adc_avg = np.mean(adc_list, axis=0)
gmm_avg = np.mean(gmm_list, axis=0)
gt_avg = np.mean(gt_list, axis=0)

#%% get the average of the uneet list
unet_avg = np.mean(unet_list, axis=0)


#%% save the average data
adc_avg_nii = nib.Nifti1Image(adc_avg, np.eye(4))
nib.save(adc_avg_nii, "results/gmm_niftis/adc_avg.nii.gz")

gmm_avg_nii = nib.Nifti1Image(gmm_avg, np.eye(4))
nib.save(gmm_avg_nii, "results/gmm_niftis/gmm_avg.nii.gz")

gt_avg_nii = nib.Nifti1Image(gt_avg, np.eye(4))
nib.save(gt_avg_nii, "results/gmm_niftis/gt_avg.nii.gz")

#%% save the average data
unet_avg = nib.Nifti1Image(unet_avg, np.eye(4))
nib.save(unet_avg, "results/gmm_niftis/unet_avg.nii.gz")

#%% import all the niftis
adc_avg = nib.load("results/gmm_niftis/adc_avg.nii.gz").get_fdata()
gmm_avg = nib.load("results/gmm_niftis/gmm_avg.nii.gz").get_fdata()
gt_avg = nib.load("results/gmm_niftis/gt_avg.nii.gz").get_fdata()
unet_avg = nib.load("results/gmm_niftis/unet_avg.nii.gz").get_fdata()

#%% jpm

adc_rot = np.rot90(adc_avg, 3)
gt_rot = np.rot90(gt_avg, 3)
pred_rot = np.rot90(gmm_avg, 3)
unet_rot = np.rot90(unet_avg, 3)



# %% create a function plot subplots of the image and the masks

def plot_subplots(image, mask_img, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 40
    for _ in range(n_rows):
        for _ in range(n_cols):
            ax[n].imshow(image[:, :, slice_no], cmap='gray')
            ax[n].imshow(mask_img[:, :, slice_no], cmap='hot', alpha=0.7, vmin=0, vmax=1)
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice_no), color='r', fontsize=5)
            n += 1
            slice_no += 8
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig

def plot_subplots_single_modality(image, n_rows, n_cols):
    fig, ax = plt.subplots(n_rows, n_cols, figsize=(150, 50))

    n = 0
    slice_no = 40
    for _ in range(n_rows):
        for _ in range(n_cols):
            ax[n].imshow(image[:, :, slice_no], cmap='gray')
            ax[n].set_xticks([])
            ax[n].set_yticks([])
            # hider border of subplot
            ax[n].set_frame_on(False)
            ax[n].set_title('Slice {}'.format(slice_no), color='r', fontsize=5)
            n += 1
            slice_no += 8
    fig.subplots_adjust(wspace=0, hspace=0)
    # plt.show()
    return fig

#%%
fig = plot_subplots(adc_rot, gt_rot, 1, 8)
fig.savefig("results/gmm_niftis/adc_gt.pdf", bbox_inches='tight', dpi=300)

fig_adc = plot_subplots_single_modality(adc_rot, 1, 8)
fig_adc.savefig("results/gmm_niftis/adc.pdf", bbox_inches='tight', dpi=300)

fig_1 = plot_subplots(adc_rot, pred_rot, 1, 8)
fig_1.savefig("results/gmm_niftis/adc_gmm.pdf", bbox_inches='tight', dpi=300)

fig_2 = plot_subplots(adc_rot, unet_rot, 1, 8)
fig_2.savefig("results/gmm_niftis/adc_unet.pdf", bbox_inches='tight', dpi=300)

#%%

import pandas as pd
mapping_human =pd.read_csv("utils/Human_name_mapping.csv")

#%% get all the columns as a list from mapping_human
columns = mapping_human.columns.tolist()

#%%
columns

#%% create a diction with the columns are values and mapping_human values as keys
mapping_human_dict = {mapping_human[col].values[0]:col for col in columns}

#%% dict to df
mapping_human_df = pd.DataFrame.from_dict(mapping_human_dict, orient='index')

#%%
mapping_human_df['Human09']

#%%
list_test_names= []
database_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/labels_reconstructed")
for i in database_path.glob("*"):
    # print(i.name)
    if "Human" in i.name:
        print("yes")
        name = i.name.split(".")[0]

        print(mapping_human_dict[name])
        list_test_names.append(mapping_human_dict[name])
        # print(name)
        # get the column name of mapping_human using the val


#%%
len(list_test_names)


#%%
human_datapath = "../../../Documents/data/Adrian_chamba_strokes_data/RatHumanCombined/Human Niftis"


#%%
dice_dict_human = {}
for i in Path(human_datapath).glob("*"):
    if i.name in list_test_names:
        print(i.name)
        new_dir = i

        #RF_Probmaps1.nii
        #Final_manual.nii

        pred_data = nib.load(new_dir / "RF_Probmaps1.nii").get_fdata()
        gt_data = nib.load(new_dir / "Final_manual.nii").get_fdata()

        print(gt_data.shape)
        print(pred_data.shape)

        # flatten data
        label_data = gt_data.flatten()
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
        dice_dict_human[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec,
                                 "precision": prec, \
                                 "false_Discovery_Rate": false_Discovery_Rate,
                                 "false_Positive_Rate": false_Positive_Rate, \
                                 "positive_predictive_value": positive_predictive_value,
                                 "negative_predictive_value": negative_predictive_value, \
                                 "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}

#%%dict to df and save
df_human = pd.DataFrame.from_dict(dice_dict_human, orient='index')
df_human.to_csv("results/gmm_niftis/combined_human.csv")


#%% nan to 0
if df_human.isnull().values.any():
    df_human = df_human.fillna(0)


#%%  calculate mean dice median dice and std dice
mean_dice = df_human["dice"].mean()
median_dice = df_human["dice"].median()
std_dice = df_human["dice"].std()
print(mean_dice, median_dice, std_dice)



#%%  rat


list_test_names= []
database_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task646_combined_patch/labels_reconstructed")
for i in database_path.glob("*"):
    # print(i.name)
    if "Rat" in i.name:
        print("yes")
        name = i.name.split(".")[0]

        # print(mapping_human_dict[name])
        # list_test_names.append(mapping_human_dict[name])
        print(name)
        list_test_names.append(name)
        # get the column name of mapping_human using the val


#%%
len(list_test_names)


#%%
rat_datapath = "../../../Documents/data/Adrian_chamba_strokes_data/RatHumanCombined/Rat Niftis"

#%%
dice_dict_rat = {}
for i in Path(rat_datapath).glob("*"):
    print(i.name)
    name = i.name.split("-")[0]
    if name in list_test_names:
        print(name)
        new_dir = i
        pred_data = nib.load(new_dir / "RF_Probmaps1.nii").get_fdata()
        gt_data = nib.load(new_dir / "Voi_24h.nii").get_fdata()

        print(gt_data.shape)
        print(pred_data.shape)

        # flatten data
        label_data = gt_data.flatten()
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
        dice_dict_rat[i.name] = {"mcc": mcc, "accuracy": acc, "sensitivity": sens, "specificity": spec,
                                 "precision": prec, \
                                 "false_Discovery_Rate": false_Discovery_Rate,
                                 "false_Positive_Rate": false_Positive_Rate, \
                                 "positive_predictive_value": positive_predictive_value,
                                 "negative_predictive_value": negative_predictive_value, \
                                 "dice": dice, "wspec": wspec, "tp": tp, "tn": tn, "fp": fp, "fn": fn}

#%%dict to df and save
import pandas as pd
df_human = pd.DataFrame.from_dict(dice_dict_rat, orient='index')
df_human.to_csv("results/gmm_niftis/combined_rat.csv")


#%% nan to 0
if df_human.isnull().values.any():
    df_human = df_human.fillna(0)


#%%  calculate mean dice median dice and std dice
mean_dice = df_human["dice"].mean()
median_dice = df_human["dice"].median()
std_dice = df_human["dice"].std()
print(mean_dice, median_dice, std_dice)



