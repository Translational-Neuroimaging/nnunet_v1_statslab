# External modules
# Internal modules
from utilities.confusion_matrix import calc_ConfusionMatrix
from utilities.dice import calc_DSC_Sets
from utilities.weighted_specificity import calc_Specificity_Weighted

# -----------------------------------------------------#
#                Calculate : MISmetric                #
# -----------------------------------------------------#
"""
Combination of weighted Specificity for p=0 and Dice Similarity Coefficient
as Backbone for p>0.
Recommended for weak-labeled datasets.
References:
    Coming soon.
"""


def calc_MISm(truth, pred, c=1, alpha=0.1):
    # Obtain confusion mat
    tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
    # Identify metric wing
    p = tp + fn
    # Compute & return normal dice if p > 0
    if p > 0:
        return calc_DSC_Sets(truth, pred, c)
    # Compute & return weighted specificity if p = 0
    else:
        return calc_Specificity_Weighted(truth, pred, c, alpha)
