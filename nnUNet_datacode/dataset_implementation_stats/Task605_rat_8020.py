# %% training data will bne used for testing
from pathlib import Path
import nibabel as nb
import numpy as np

#%%
img_dir = Path("../../../Documents/data/Adrian_chamba_strokes_data/Rats24h")

output_dir = Path("../nnUNet_raw_data_base/nnUNet_raw_data/Task605_rat/")

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
    new_dir = img_dir / i.name

    for j in new_dir.glob("*"):
        # print(j.name)
        img = nb.load(j)

        if count < 37:
            if j.name == "Masked_ADC.nii":
                # print(i.name)
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

#%%
for i in img_dir.glob("*"):
    new_name = i.name.split("-24h")[0]
    new_dir = img_dir / i.name
    # print(new_dir)

    for k in new_dir.glob("*"):
        # print(k.name)

        if (k.name == "Masked_ADC.nii"):
            img = nb.load(k)
            label_name = new_name + "_0000.nii.gz"
            print(label_name)
            nb.save(img, output_training_dir / label_name)

        if (k.name == "Masked_T2.nii"):
            img = nb.load(k)
            label_name = new_name + "_0001.nii.gz"
            print(label_name)
            nb.save(img, output_training_dir / label_name)

        if (k.name == "GroundTruth24h.nii"):
            img = nb.load(k)
            label_name = new_name + ".nii.gz"
            print(label_name)
            nb.save(img, output_labels_tr / label_name)

# %% testing parrt
output_testing_dir = output_dir / "images_ts"
output_all_testing_dir = output_dir / "all_other_images_connected_ts"

count = 0
for i in img_dir.glob("*"):
    new_name = i.name.split("-24h")[0]
    new_dir = img_dir / i.name
    # print(new_dir)
    new_name = new_name[3:]
    # print(new_name)  # for giving new index for testing data

    for k in new_dir.glob("*"):

        if (count < 20):
            if (k.name == "Masked_ADC.nii"):
                img = nb.load(k)
                label_name = "Rat0" + new_name + "_0000.nii.gz"
                print(label_name)
                nb.save(img, output_testing_dir / label_name)

            elif(k.name == "Masked_T2.nii"):
                img = nb.load(k)
                label_name = "Rat0" + new_name + "_0001.nii.gz"
                print(label_name)
                nb.save(img, output_testing_dir / label_name)

            else:
                img = nb.load(k)
                label_name = "Rat0" + new_name + "_" + k.name + ".gz"
                print(label_name)
                nb.save(img, output_all_testing_dir / label_name)
    count += 1

