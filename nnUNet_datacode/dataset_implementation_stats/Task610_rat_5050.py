# %% training data will bne used for testing
from pathlib import Path
import nibabel as nb
import numpy as np

#%%
img_dir = Path("../../../Documents/data/Adrian_chamba_strokes_data/Rats24h")

output_dir = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task610_rat/")
#
output_training_dir = output_dir / "imagesTr"
output_labels_tr = output_dir / "labelsTr"
output_training_all =  output_dir / "all_about_training"
output_testing_dir = output_dir / "imagesTs"
output_labels_ts = output_dir / "labelsTs"
output_testing_all = output_dir / "all_other_images_connected_ts"

#%%
count = 0
for i in img_dir.glob("*"):
    # print(i.name)
    new_name = i.name.replace("-24h", "")
    # print(new_name)
    new_dir = img_dir/i.name

    for j in new_dir.glob("*"):
        # print(j.name)

        img = nb.load(j)

        if count < 27:
            if j.name == "Masked_ADC.nii":
                label_name = new_name + "_0000.nii.gz"
                print(label_name)
                nb.save(img, output_training_dir / label_name)

            elif j.name == "Masked_T2.nii":
                label_name = new_name + "_0001.nii.gz"
                nb.save(img, output_training_dir / label_name)

            elif j.name == "GroundTruth24h.nii":
                label_name = new_name + ".nii.gz"
                nb.save(img, output_labels_tr / label_name)

            else:
                label_name = new_name + "_" + j.name + ".gz"
                nb.save(img, output_training_all / label_name)
                # print(label_name)

        else:
            if j.name == "Masked_ADC.nii":
                # print(i.name)
                label_name = new_name + "_0000.nii.gz"
                print(label_name)
                nb.save(img, output_testing_dir / label_name)

            elif j.name == "Masked_T2.nii":
                label_name = new_name + "_0001.nii.gz"
                nb.save(img, output_testing_dir / label_name)

            elif j.name == "GroundTruth24h.nii":
                label_name = new_name + ".nii.gz"
                nb.save(img, output_labels_ts / label_name)
                print(count)

            else:
                label_name = new_name + "_" + j.name + ".gz"
                nb.save(img, output_testing_all / label_name)

    count += 1

