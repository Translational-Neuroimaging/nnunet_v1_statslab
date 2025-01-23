import numpy as np
from sklearn.metrics import confusion_matrix


# -----------------------------------------------------#
#            Calculate : Confusion Matrix             #
# -----------------------------------------------------#
def calc_ConfusionMatrix(truth, pred):
    c = 1
    dtype = np.int64
    # Obtain predicted and actual condition
    gt = np.equal(truth, c)
    pd = np.equal(pred, c)
    not_gt = np.logical_not(gt)
    not_pd = np.logical_not(pd)
    # Compute Confusion Matrix
    tp = np.logical_and(pd, gt).sum()
    tn = np.logical_and(not_pd, not_gt).sum()
    fp = np.logical_and(pd, not_gt).sum()
    fn = np.logical_and(not_pd, gt).sum()
    # Convert to desired numpy type to avoid overflow
    tp = tp.astype(dtype)
    tn = tn.astype(dtype)
    fp = fp.astype(dtype)
    fn = fn.astype(dtype)
    # Return Confusion Matrix
    return tp, tn, fp, fn


# def calc_ConfusionMatrix(truth, pred):
#     tn, fp, fn, tp = confusion_matrix(truth, pred).ravel()
#     return tp, tn, fp, fn