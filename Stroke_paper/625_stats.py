#%%
import shutil
from pathlib import Path
import pandas as pd
from utilities.confusionMatrix_dependent_functions import *


#%% control list
data_path = Path("../../../Documents/data/adrian_data/Rats24h/")
mcao_60_list = []

for i in data_path.glob("*"):
    print(i.name)
    new_name = i.name.split("-")[0]
    print(new_name)
    #add new name to list
    mcao_60_list.append(new_name)




#%% data path 650_patch gmm testing data
data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task653_mcao_100")


for i in data_path.iterdir():
    print(i)

#%%
# task_name = "mcao_100"
rs_path = data_path
seg_path = rs_path / "result"
gt_path = rs_path / "labelsTs"
dict_653 = {}

calc_stats(gt_path, seg_path, dict_653)

#%% dict to df 650
df_653 = pd.DataFrame.from_dict(dict_653, orient='index')

#%%
df_653.index = df_653.index.str.replace('.nii.gz', '')

#%% if index name is in list add it to mcao_60_df  and if not then add it to mcao_100_df
mcao_60_df = pd.DataFrame()
mcao_100_df = pd.DataFrame()

for i in df_653.index:
    print(i)
    name = i
    #if str is in index_list, add to dict
    if name in mcao_60_list:
        mcao_60_df = mcao_60_df.append(df_653.loc[i])
    else:
        mcao_100_df = mcao_100_df.append(df_653.loc[i])

#%%
mcao_60_df.to_csv(str(rs_path / "mcao_60" ) + ".csv")
mcao_100_df.to_csv(str(rs_path / "mcao_100") + ".csv")
# save to csv 650
# df_650.to_csv(str(rs_path / task_name) + ".csv")

#%%
testing_data_input = rs_path / "testing"
testing_data_output = rs_path / "testing_data"

for i in testing_data_input.iterdir():
    new_dir  = i
    print(i.name)
    for j in new_dir.glob("*"):
        # print(j)
        # if name starts with "Human" copy it to testing_data_output
        if j.name.startswith("Human"):
            shutil.copy(j, testing_data_output / i.name)
            print("copying")




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
#
# #%% get mean of dice and tversky  and msism
# print(np.mean(df_24h['dice']))
# print(np.mean(df_24h['tversky']))
# print(np.mean(df_24h['mism']))
# #%% remove the raw with nan in tversky
# df_24h = df_24h.dropna()
#
# #%% 24h 1w gt
# dict_24h_1w = {}
# segmentation_path = data_path / "result"
# gt_path = data_path / "testing/1w/labelsTs"
#
# #%%
# calc_stats(gt_path, segmentation_path, dict_24h_1w)
#
# #%% dict to df
# df_24h_1w = pd.DataFrame.from_dict(dict_24h_1w, orient='index')
#
# #%% save to csv
# df_24h_1w.to_csv(str(data_path) + "/24h_1w_gt.csv")
#
#
# #%% 610 24h 3d
# segmentation_path = data_path / "resultTs_3d"
# gt_path = data_path / "labelsTs"
#
# #%%
# dict_24h_3d = {}
# calc_stats(gt_path, segmentation_path, dict_24h_3d)
#
# #%% dict to df
# df_24h_3d = pd.DataFrame.from_dict(dict_24h_3d, orient='index')
#
# df_24h_3d.to_csv(str(data_path) + "/24h_3d.csv")
#
# #%%
# # ------------------------------605---------------------------------#
# data_path = Path("../../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing")
# data_72h = data_path / "72h"
# data_1w = data_path / "1w"
# data_1m = data_path / "1m"
#
#
# #%%
# dict_72h = {}
# segmentation_path = data_72h / "result"
# ground_truth_path = data_72h / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_72h)
#
# #%% dict to df
# df_72h = pd.DataFrame.from_dict(dict_72h, orient='index')
# # save df to csv
#
# df_72h.to_csv(str(data_72h) +"/2d_72h.csv")
#
# #%% 72h 3d
# dict_72h_3d = {}
# segmentation_path = data_72h / "result_3d"
# ground_truth_path = data_72h / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_72h_3d)
#
#
# #%% dict to df
# df_72h_3d = pd.DataFrame.from_dict(dict_72h_3d, orient='index')
#
# # save df to csv
# df_72h_3d.to_csv(str(data_72h) +"/3d_72h.csv")
#
#
# #%% 1w 2d
# dict_1w = {}
# segmentation_path = data_1w / "result"
# ground_truth_path = data_1w / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_1w)
#
# #%% dict to df
# df_1w = pd.DataFrame.from_dict(dict_1w, orient='index')
#
# # save df to csv
# df_1w.to_csv(str(data_1w) +"/2d_1w.csv")
#
# #%% 1w 3d
# dict_1w_3d = {}
# segmentation_path = data_1w / "result_3d"
# ground_truth_path = data_1w / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_1w_3d)
#
# #%% dict to df
# df_1w_3d = pd.DataFrame.from_dict(dict_1w_3d, orient='index')
#
# # save df to csv
# df_1w_3d.to_csv(str(data_1w) +"/3d_1w.csv")
#
#
# #%% 1m 2d
# dict_1m = {}
# segmentation_path = data_1m / "result"
# ground_truth_path = data_1m / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_1m)
#
# #%% dict to df
# df_1m = pd.DataFrame.from_dict(dict_1m, orient='index')
#
# # save df to csv
# df_1m.to_csv(str(data_1m) +"/2d_1m.csv")
#
# #%% 1m 3d
# dict_1m_3d = {}
# segmentation_path = data_1m / "result_3d"
# ground_truth_path = data_1m / "labelsTs"
# calc_stats(ground_truth_path, segmentation_path, dict_1m_3d)
#
# #%% dict to df
# df_1m_3d = pd.DataFrame.from_dict(dict_1m_3d, orient='index')
#
# # save df to csv
# df_1m_3d.to_csv(str(data_1m) +"/3d_1m.csv")
#
#
# #%%
# data_path = Path("../../../../Documents/data/adrian_data/Data_Paper_12092022")
# gmm_1w = data_path / "GMM/GMM_1w/Niftis"
# gmm_24h = data_path / "GMM/GMM_24h/Niftis"
#
# #%%
# dict_gmm_1w = {}
# calc_stats3(gmm_1w, "Voi_1w.nii", gmm_24h, "RF_Probmaps1.nii", dict_gmm_1w)
#
# #%% dict to df and save to csv
# df_gmm_1w = pd.DataFrame.from_dict(dict_gmm_1w, orient='index')
# df_gmm_1w.to_csv(str(data_path) + "/gmm_1w_voi_24h_mask.csv")
#
# #%%
# dict_gmm1w = {}
# calc_stats2(gmm_1w, "Voi_1w.nii", "RF_Probmaps1.nii", dict_gmm1w)
#
# #%% dict to df
# df_gmm1w = pd.DataFrame.from_dict(dict_gmm1w, orient='index')
#
# #%% save to csv
# df_gmm1w.to_csv(str(gmm_1w) + "/GMM_1w.csv")
#
# #%%
# dict_gmm24h = {}
# calc_stats2(gmm_24h, "Voi_24h.nii", "RF_Probmaps1.nii", dict_gmm24h)
#
# #%% dict to df
# df_gmm24h = pd.DataFrame.from_dict(dict_gmm24h, orient='index')
#
# #%% save to csv
# df_gmm24h.to_csv(str(gmm_24h) + "/GMM_24h.csv")
#
#
#
# #%%
# segmentation_path = data_path / "resultTs"
# gt_path = data_path / "testing/1w" / "labelsTs"
#
# #%%
# dict_24h_seg_1w_mask = {}
# # calc_stats3(gmm_1w, "Voi_1w.nii", gmm_24h, "RF_Probmaps1.nii", dict_gmm_1w)
# for i in segmentation_path.glob("*.nii.gz"):
#     print(i.name)
#     # file_name = i.name.replace("-1w", "")
#     # # print(file_name)
#     #
#     # if path exists, then continue
#     # new_filename = file_name + "-24h"
#     if (gt_path / i.name).exists():
#         print(str(gt_path / i.name) + "  path exists")
#         seg_file_name = i
#         gt_file_name = gt_path / i.name
#
#         segmentation = nib.load(str(seg_file_name)).get_fdata()
#         ground_truth = nib.load(str(gt_file_name)).get_fdata()
#         print(segmentation.shape)
#         print(ground_truth.shape)
#
#         # flatten data
#         pred_data = segmentation.flatten()
#         label_data = ground_truth.flatten()
#
#         name = i.name.replace(".nii.gz", "")
#         # calculate all metrics using function calc_all_metrics_CM
#         stats = calc_all_metrics_CM(label_data, pred_data)
#         dict_24h_seg_1w_mask[name] = {'mcc': stats[0], 'sens': stats[1], 'spec': stats[2], 'prec': stats[3], 'acc': stats[4],
#                         'FDR': stats[5], 'FPR': stats[6], 'PPV': stats[7], 'NPV': stats[8], 'dice': stats[9],
#                         'wspec': stats[10], 'tversky': stats[11], 'balanced_acc': stats[12]}
#
# #%% dict to df and save to csv
# df = pd.DataFrame.from_dict(dict_24h_seg_1w_mask, orient='index')
# df.to_csv(str(data_path) + "/24h_pred_1w_gt.csv")
#
# #%% 645 Patch 2d Rat24h
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task645_Patch_2d_Rat24h/")
# segmentation_path = data_path / "rat_result_reconstructed"
# gt_path = data_path / "labels_reconstructed"
# dict_645_2d = {}
#
# #%% 610
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
# segmentation_path = data_path / "24h_gt"
# gt_path = data_path / "labelsTs"
# dict_610_gt1w_gt24h = {}
# calc_stats(gt_path, segmentation_path, dict_610_gt1w_gt24h)
#
# #%% dict to df and save to csv
# df = pd.DataFrame.from_dict(dict_610_gt1w_gt24h, orient='index')
# df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")
#
# #%% control list
# data_path = Path("../../../Documents/data/adrian_data/devided/Rats24h/control")
# control_list = []
# for i in data_path.glob("*"):
#     print(i.name)
#     new_name = i.name.split("-")[0]
#     print(new_name)
#     #add new name to list
#     control_list.append(new_name)
#
# #%% remove nii.gz from df index
# df.index = df.index.str.replace(".nii.gz", "")
#
#
#
# #%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
# df_therapy = pd.DataFrame()
# df_control = pd.DataFrame()
#
# for i in df.index:
#     if i not in control_list:
#         df_therapy = df_therapy.append(df.loc[i])
#     else:
#         df_control = df_control.append(df.loc[i])
#
# #%% save to csv
# df_therapy.to_csv(str(data_path) + "/therapy_gt1w_gt24h.csv")
# df_control.to_csv(str(data_path) + "/control_gt1w_gt14h.csv")
#
# #%% 610_rat read csv
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
#
# df_24h = pd.read_csv(str(data_path) + "/610_gt1w_gt24h.csv", index_col=0)
#
# #%% remove nii.gz from df index
# # df_24h.index = df_24h.index.str.replace(".nii.gz", "")
# # remove unnamed column
# # df_24h = df_24h.drop(columns=["Unnamed: 0"])
# # drop raw if tversly is noy zero add to new_df
# new_df = pd.DataFrame()
# for i in df_24h.index:
#     if df_24h.loc[i, "tversky"] != 0:
#         new_df = new_df.append(df_24h.loc[i])
#
# #%% #%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
# df_therapy = pd.DataFrame()
# df_control = pd.DataFrame()
#
# for i in df_24h.index:
#     if i not in control_list:
#         df_therapy = df_therapy.append(df_24h.loc[i])
#     else:
#         df_control = df_control.append(df_24h.loc[i])
#
# #%% save to csv
# new_df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")
# # df_control.to_csv(str(data_path) + "/control_gmm_24h_1w_gt_with_same_testing_data.csv")
#
# #%% 610 rat testing 1w
# data_path = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/testing/1w")
# segmentation_path = data_path / "24h_gt"
# gt_path = data_path / "labelsTs"
#
# dict_610_gt1w_gt24h = {}
# calc_stats(gt_path, segmentation_path, dict_610_gt1w_gt24h)
#
# #%% dict to df and save to csv
# df = pd.DataFrame.from_dict(dict_610_gt1w_gt24h, orient='index')
#
# #%%
# new_df = pd.DataFrame()
# for i in df.index:
#     if df.loc[i, "tversky"] != 0:
#         new_df = new_df.append(df.loc[i])
#
# #%% save to csv
# new_df.to_csv(str(data_path) + "/610_gt1w_gt24h.csv")
#
# #%% new df remove nii.gz from df index
# new_df.index = new_df.index.str.replace(".nii.gz", "")
#
# #%% #%% if df index not in control_list then add it to df_therapy and if in control_list add to df_control
# df_therapy = pd.DataFrame()
# df_control = pd.DataFrame()
#
# for i in new_df.index:
#     if i not in control_list:
#         df_therapy = df_therapy.append(new_df.loc[i])
#     else:
#         df_control = df_control.append(new_df.loc[i])
#
# #%% save to csv
# df_therapy.to_csv(str(data_path) + "/therapy_gt1w_gt24h.csv")
# df_control.to_csv(str(data_path) + "/control_gt1w_gt14h.csv")
#
