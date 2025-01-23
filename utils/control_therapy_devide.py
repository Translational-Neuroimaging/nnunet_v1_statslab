# %%
from pathlib import Path

# %%
database = Path("../../../Documents/data/adrian_data")
output_dir = database / "devided"

# %% 24h rat
task_24h = database / "Christine_data_Rat24h_devided"

therapy_data = task_24h / "christine_therapy_data"
control_data = task_24h / "christine_control_data"

# %%
list_therapy = []
list_control = []
for i in therapy_data.glob("*"):
    # print(i.name)
    fold_name = i.name.split("-")[0]
    print(fold_name)
    # add name into list_therapy
    list_therapy.append(fold_name)
for i in control_data.glob("*"):
    # print(i.name)
    fold_name = i.name.split("-")[0]
    print(fold_name)
    # add name into list_control
    list_control.append(fold_name)

# %%
print(len(list_therapy))
print(len(list_control))




# %%
task_72h = database / "Rats72h"


# %% create a function for the upper code
def therapy_control_data_division(task_name):
    folder = database / task_name
    for m in folder.glob("*"):
        # print(i.name)
        if m.name.split('-')[0] in list_therapy:
            print("therapy")
            # create a folder if it does not exist in the output_dir and copy the data into it
            if not (output_dir / task_name / "therapy" / m.name).exists():
                (output_dir / task_name / "therapy" / m.name).mkdir(parents=True)
            for j in m.glob("*"):
                print(j.name)
                # copy the data
                (output_dir / task_name / "therapy" / m.name / j.name).write_bytes(j.read_bytes())
        elif m.name.split('-')[0] in list_control:
            print("control")
            # create a folder if it does not exist in the output_dir and copy the data into it
            if not (output_dir / task_name / "control" / m.name).exists():
                (output_dir / task_name / "control" / m.name).mkdir(parents=True)
            for j in m.glob("*"):
                print(j.name)
                # copy the data
                (output_dir / task_name / "control" / m.name / j.name).write_bytes(j.read_bytes())


# %%
therapy_control_data_division("Rats1m")

#%% print hello
print("hello")


#%% print hello
