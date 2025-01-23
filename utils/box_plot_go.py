import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

#%% import csv from result
df_601 = pd.read_csv("results/601_human.csv")

#%% nan to 0
if df_601.isnull().values.any():
    df_601 = df_601.fillna(0)

#%% box plot for dice and accuracy
fig =go.Figure()
fig.add_trace(go.Box(y=df_601['dice'], name="dice"))
fig.add_trace(go.Box(y=df_601['accuracy'], name="accuracy"))
fig.update_layout(xaxis_title="human whole img", yaxis_title="dice range")
# font size
fig.update_layout(font=dict(size=18))
#y axis min range set to 0
fig.update_yaxes(range=[0.5, 1.02])
# fig.show()
fig.write_image("results/plots/601_dice_accuracy.pdf")

#%% for 605
df_605 = pd.read_csv("results/605_rat.csv")

#%% nan to 0
if df_605.isnull().values.any():
    df_605 = df_605.fillna(0)

#%% box plot for dice and accuracy
fig =go.Figure()
fig.add_trace(go.Box(y=df_605['dice'], name="dice"))
fig.add_trace(go.Box(y=df_605['accuracy'], name="accuracy"))
fig.update_layout(xaxis_title="rat whole img", yaxis_title="dice range")
fig.update_layout(font=dict(size=18))
#y axis min range set to 0
fig.update_yaxes(range=[0.5, 1.02])
# fig.show()
fig.write_image("results/plots/605_dice_accuracy.pdf")

#%% box plot for dice mcc and sensitivity
fig =go.Figure()
fig.add_trace(go.Box(y=df_605['dice'], name="dice"))
fig.add_trace(go.Box(y=df_605['positive_predictive_value'], name="positive_predictive_value"))
fig.add_trace(go.Box(y=df_605['sensitivity'], name="sensitivity"))
fig.update_layout(xaxis_title="rat whole img", yaxis_title="dice range")
fig.update_layout(font=dict(size=18))
#y axis min range set to 0
fig.update_yaxes(range=[0.5, 1.02])
# fig.show()
fig.write_image("results/plots/605_dice_mcc_sensitivity.pdf")

#%% box plot for all stats
fig =go.Figure()
fig.add_trace(go.Box(y=df_605['dice'], name="dice"))
fig.add_trace(go.Box(y=df_605['positive_predictive_value'], name="positive_predictive_value"))
fig.add_trace(go.Box(y=df_605['sensitivity'], name="sensitivity"))
fig.add_trace(go.Box(y=df_605['specificity'], name="specificity"))
fig.add_trace(go.Box(y=df_605['accuracy'], name="accuracy"))

#negetive predictive value
fig.add_trace(go.Box(y=df_605['negative_predictive_value'], name="negative_predictive_value"))
#false discovery rate
fig.add_trace(go.Box(y=df_605['false_Discovery_Rate'], name="false_discovery_rate"))

fig.update_layout(yaxis_title="range")
#plot color
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5)
fig.update_layout(font=dict(size=14))
#y axis min range set to 0
fig.update_yaxes(range=[0.5, 1.02])
#remove legend
fig.update_layout(showlegend=False)
# fig.show()
fig.write_image("results/plots/605_all_stats.pdf")

#%% box plot for 601 all stats
fig =go.Figure()
fig.add_trace(go.Box(y=df_601['dice'], name="dice"))
fig.add_trace(go.Box(y=df_601['positive_predictive_value'], name="positive_predictive_value"))
fig.add_trace(go.Box(y=df_601['sensitivity'], name="sensitivity"))
fig.add_trace(go.Box(y=df_601['specificity'], name="specificity"))
fig.add_trace(go.Box(y=df_601['accuracy'], name="accuracy"))
#negetive predictive value
fig.add_trace(go.Box(y=df_601['negative_predictive_value'], name="negative_predictive_value"))
#false positive rate
# fig.add_trace(go.Box(y=df_601['false_Positive_Rate'], name="false_positive_rate"))
#false discovery rate
fig.add_trace(go.Box(y=df_601['false_Discovery_Rate'], name="false_discovery_rate"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5)
fig.update_layout( yaxis_title="range")

fig.update_layout(font=dict(size=14))
#y axis min range set to 0
fig.update_yaxes(range=[0.5, 1.02])
fig.update_layout(showlegend=False)

# fig.show()
fig.write_image("results/plots/601_all_stats.pdf")

#%%605 rat vs 645 rat
df_645 = pd.read_csv("results/645_rat.csv")

#%% nan to 0
if df_645.isnull().values.any():
    df_645 = df_645.fillna(0)

#%% box plot for dice mcc and sensitivity
fig =go.Figure()
fig.add_trace(go.Box(y=df_605['dice'], name="dice"))
# dice 645
fig.add_trace(go.Box(y=df_645['dice'], name="dice_patch"))
fig.add_trace(go.Box(y=df_605['positive_predictive_value'], name="positive_predictive_value"))
#ppv 645
fig.add_trace(go.Box(y=df_645['positive_predictive_value'], name="ppv_patch"))
fig.add_trace(go.Box(y=df_605['sensitivity'], name="sensitivity"))
#sensitivity 645
fig.add_trace(go.Box(y=df_645['sensitivity'], name="sensitivity_patch"))
fig.add_trace(go.Box(y=df_605['specificity'], name="specificity"))
#specificity 645
fig.add_trace(go.Box(y=df_645['specificity'], name="specificity_patch"))
fig.add_trace(go.Box(y=df_605['accuracy'], name="accuracy"))
#accuracy 645
fig.add_trace(go.Box(y=df_645['accuracy'], name="accuracy_patch"))
fig.add_trace(go.Box(y=df_605['negative_predictive_value'], name="negative_predictive_value"))
#npv 645
fig.add_trace(go.Box(y=df_645['negative_predictive_value'], name="npv_patch"))
fig.add_trace(go.Box(y=df_605['false_Discovery_Rate'], name="false_discovery_rate"))
#fdr 645
fig.add_trace(go.Box(y=df_645['false_Discovery_Rate'], name="fdr_patch"))
fig.update_layout(yaxis_title="range")
fig.update_layout(font=dict(size=14))
fig.update_yaxes(range=[0.5, 1.02])
fig.update_layout(showlegend=False)

fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="dice"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="positive_predictive_value"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="sensitivity"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="specificity"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="accuracy"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="negative_predictive_value"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="false_discovery_rate"))

#guve green color to all 645 box plot
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="dice_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="ppv_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="sensitivity_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="specificity_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="accuracy_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="npv_patch"))
fig.update_traces(marker_color='green', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="fdr_patch"))



# fig.show()
fig.write_image("results/plots/605_645_dice_mcc_sensitivity.pdf")
#y axis min range set to 0

#%% 654 human vs 601 human
df_654 = pd.read_csv("results/645_human.csv")

#%% nan to 0
if df_654.isnull().values.any():
    df_654 = df_654.fillna(0)

#%% box plot for all stats
fig =go.Figure()
fig.add_trace(go.Box(y=df_601['dice'], name="dice"))
# dice 654
fig.add_trace(go.Box(y=df_654['dice'], name="dice_patch"))
# fig.add_trace(go.Box(y=df_601['positive_predictive_value'], name="positive_predictive_value"))
# #ppv 654
# fig.add_trace(go.Box(y=df_654['positive_predictive_value'], name="ppv_patch"))
# fig.add_trace(go.Box(y=df_601['sensitivity'], name="sensitivity"))
# #sensitivity 654
# fig.add_trace(go.Box(y=df_654['sensitivity'], name="sensitivity_patch"))
# fig.add_trace(go.Box(y=df_601['specificity'], name="specificity"))
# #specificity 654
# fig.add_trace(go.Box(y=df_654['specificity'], name="specificity_patch"))
# fig.add_trace(go.Box(y=df_601['accuracy'], name="accuracy"))
# #accuracy 654
# fig.add_trace(go.Box(y=df_654['accuracy'], name="accuracy_patch"))
# fig.add_trace(go.Box(y=df_601['negative_predictive_value'], name="negative_predictive_value"))
# #npv 654
# fig.add_trace(go.Box(y=df_654['negative_predictive_value'], name="npv_patch"))
# fig.add_trace(go.Box(y=df_601['false_Discovery_Rate'], name="false_discovery_rate"))
# #fdr 654
# fig.add_trace(go.Box(y=df_654['false_Discovery_Rate'], name="fdr_patch"))
fig.update_layout(yaxis_title="range")
fig.update_layout(font=dict(size=14))
fig.update_yaxes(range=[0, 1.02])
fig.update_layout(showlegend=False)

fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="dice"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="positive_predictive_value"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="sensitivity"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="specificity"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="accuracy"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="negative_predictive_value"))
fig.update_traces(marker_color='blue', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="false_discovery_rate"))

#guve yellow color to all 645 box plot
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="dice_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="ppv_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="sensitivity_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="specificity_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="accuracy_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="npv_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="fdr_patch"))

# fig.show()
fig.write_image("results/plots/601_645_human_all.pdf")

#%% import 646 all csv files
df_646_human_2d = pd.read_csv("results/646_human_2d.csv")
df_646_human_3d = pd.read_csv("results/646_human_3d.csv")
df_646_rat_2d = pd.read_csv("results/646_rat_2d.csv")
df_646_rat_3d = pd.read_csv("results/646_rat_3d.csv")

#%% nan to 0
if df_646_human_2d.isnull().values.any():
    df_646_human_2d = df_646_human_2d.fillna(0)
if df_646_human_3d.isnull().values.any():
    df_646_human_3d = df_646_human_3d.fillna(0)
if df_646_rat_2d.isnull().values.any():
    df_646_rat_2d = df_646_rat_2d.fillna(0)
if df_646_rat_3d.isnull().values.any():
    df_646_rat_3d = df_646_rat_3d.fillna(0)


#%% get dice mean and median and std for all df
#human 2d
dice_646_human_2d_mean = df_646_human_2d['dice'].mean()
print("dice_646_human_2d_mean: ", dice_646_human_2d_mean)
dice_646_human_2d_median = df_646_human_2d['dice'].median()
print("dice_646_human_2d_median: ", dice_646_human_2d_median)
dice_646_human_2d_std = df_646_human_2d['dice'].std()
print("dice_646_human_2d_std: ", dice_646_human_2d_std)
print("............................................")
#human 3d
dice_646_human_3d_mean = df_646_human_3d['dice'].mean()
print("dice_646_human_3d_mean: ", dice_646_human_3d_mean)
dice_646_human_3d_median = df_646_human_3d['dice'].median()
print("dice_646_human_3d_median: ", dice_646_human_3d_median)
dice_646_human_3d_std = df_646_human_3d['dice'].std()
print("dice_646_human_3d_std: ", dice_646_human_3d_std)
print("............................................")
#rat 2d
dice_646_rat_2d_mean = df_646_rat_2d['dice'].mean()
print("dice_646_rat_2d_mean: ", dice_646_rat_2d_mean)
dice_646_rat_2d_median = df_646_rat_2d['dice'].median()
print("dice_646_rat_2d_median: ", dice_646_rat_2d_median)
dice_646_rat_2d_std = df_646_rat_2d['dice'].std()
print("dice_646_rat_2d_std: ", dice_646_rat_2d_std)
print("............................................")

#rat 3d
dice_646_rat_3d_mean = df_646_rat_3d['dice'].mean()
print("dice_646_rat_3d_mean: ", dice_646_rat_3d_mean)
dice_646_rat_3d_median = df_646_rat_3d['dice'].median()
print("dice_646_rat_3d_median: ", dice_646_rat_3d_median)
dice_646_rat_3d_std = df_646_rat_3d['dice'].std()
print("dice_646_rat_3d_std: ", dice_646_rat_3d_std)



#%% 601 human dice box plot vs 646 human 3d dice box plot
fig = go.Figure()
fig.add_trace(go.Box(y=df_601['dice'], name="human_dice"))
fig.add_trace(go.Box(y=df_646_human_3d['dice'], name="human_dice_patch"))
fig.update_traces(marker_color='rebeccapurple', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="human_dice_patch"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="human_dice"))

# fig.update_layout(yaxis_title="range")
# fig.update_layout(font=dict(size=18))
# fig.update_yaxes(range=[0.5, 1.02])
# fig.update_layout(showlegend=False)
# # fig.show()
# fig.write_image("results/plots/601_646_human_dice.pdf")
#
# #%% 605 rat dice box plot vs 646 rat 3d dice box plot
# fig = go.Figure()
fig.add_trace(go.Box(y=df_605['dice'], name="mcao_dice"))
fig.add_trace(go.Box(y=df_646_rat_3d['dice'], name="mcao_dice_patch"))
fig.update_traces(marker_color='rebeccapurple', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="mcao_dice_patch"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="mcao_dice"))

fig.update_layout(yaxis_title="range")
fig.update_layout(font=dict(size=18))
fig.update_yaxes(range=[0.5, 1.02])
fig.update_layout(showlegend=False)
# fig.show()
fig.write_image("results/plots/605_646_rat_dice.pdf")




#%% import combined rat and combined human from results/gmm_niftis
df_rat = pd.read_csv("results/gmm_niftis/combined_rat.csv")
df_human = pd.read_csv("results/gmm_niftis/combined_human.csv")


#%% box plot dice accuracy for combined rat and combined human seprarately
fig = go.Figure()
fig.add_trace(go.Box(y=df_human['dice'], name="human_dice"))
# accuracy df_human
fig.add_trace(go.Box(y=df_human['accuracy'], name="human_accuracy"))

fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="human_dice"))
fig.update_traces(marker_color='yellow', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="human_accuracy"))

fig.update_layout(yaxis_title="range")
fig.update_layout(font=dict(size=18))
# fig.show()
fig.write_image("results/plots/combined_human_dice_accuracy.pdf")

#%% same for rat data
fig = go.Figure()
fig.add_trace(go.Box(y=df_rat['dice'], name="rat_dice"))
# accuracy df_rat
fig.add_trace(go.Box(y=df_rat['accuracy'], name="rat_accuracy"))

fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="rat_dice"))
fig.update_traces(marker_color='firebrick', marker_line_color='rgb(8,48,107)',
                    marker_line_width=1.5, selector=dict(name="rat_accuracy"))

fig.update_layout(yaxis_title="range")
fig.update_layout(font=dict(size=18))
fig.update_layout(showlegend=False)
# fig.show()
fig.write_image("results/plots/combined_rat_dice_accuracy.pdf")


