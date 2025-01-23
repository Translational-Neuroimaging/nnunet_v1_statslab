# External modules
import numpy as np
# Internal modules
from utilities.confusion_matrix import calc_ConfusionMatrix


# -----------------------------------------------------#
#              Calculate : DSC Enhanced               #
# -----------------------------------------------------#
def calc_DSC_Enhanced(truth, pred, c=1):
    # Obtain sets with associated class
    gt = np.equal(truth, c)
    pd = np.equal(pred, c)
    # Calculate Dice
    if gt.sum() == 0 and pd.sum() == 0:
        dice = 1.0
    elif (pd.sum() + gt.sum()) != 0:
        dice = 2 * np.logical_and(pd, gt).sum() / (pd.sum() + gt.sum())
    else:
        dice = 0.0
    # Return computed Dice
    return dice


# -----------------------------------------------------#
#              Calculate : DSC via Sets               #
# -----------------------------------------------------#
def calc_DSC_Sets(truth, pred, c=1):
    # Obtain sets with associated class
    gt = np.equal(truth, c)
    pd = np.equal(pred, c)
    # Calculate Dice
    if (pd.sum() + gt.sum()) != 0:
        dice = 2 * np.logical_and(pd, gt).sum() / (pd.sum() + gt.sum())
    else:
        dice = 0.0
    # Return computed Dice
    return dice


# -----------------------------------------------------#
#             Calculate : DSC via ConfMat             #
# -----------------------------------------------------#
def calc_DSC_CM(truth, pred, c=1):
    # Obtain confusion mat
    tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
    # Calculate Dice
    if (2 * tp + fp + fn) != 0:
        dice = 2 * tp / (2 * tp + fp + fn)
    else:
        dice = 0.0
    # Return computed Dice
    return dice
