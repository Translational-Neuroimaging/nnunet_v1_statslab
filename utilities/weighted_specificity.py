# External modules
# Internal modules
from utilities.confusion_matrix import calc_ConfusionMatrix


# -----------------------------------------------------#
#           Calculate : Weighted Specificity          #
# -----------------------------------------------------#
def calc_Specificity_Weighted(truth, pred, c=1, alpha=0.1):
    # Obtain confusion mat
    tp, tn, fp, fn = calc_ConfusionMatrix(truth, pred, c)
    # Compute weighted specificity
    if (fp + tn) != 0:
        wspec = (alpha * tn) / ((1 - alpha) * fp + alpha * tn)
    else:
        wspec = 0.0
    # Return weighted specificity
    return wspec
