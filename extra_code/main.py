#%%
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np

mri_file = 'input/imageT/BRATS_001.nii.gz'
img = nib.load(mri_file)
#%%
print(type(img))
img_hdr = img.header
print(img_hdr)
img_hdr.keys()

#%%
print(img.shape)
print(img.header.get_zooms())
print(img.header.get_xyzt_units())

#%%
img_data = img.get_fdata()
print(img_data.shape)
type(img_data)

print(np.min(img_data))
np.max(img_data)

#%%
print(img_data[118:121, 118:121, 75:78,0])

#%%
mid_slice_x = img_data[118, :, :, 0] # x= 118 and t =0
print(mid_slice_x.shape)

#%% ploting

plt.imshow(mid_slice_x.T, cmap='gray', origin='lower')
plt.xlabel('first axis')
plt.ylabel('second axis')
plt.colorbar(label='signal intensity')
plt.show()

#%%
print(img_data.shape)

img_data = np.rot90(img_data.squeeze(),1)
print(img_data.shape)

fig, axes = plt.subplots(1,14,figsize=[50,5])

n=0
slice =0
for _ in range(14):
    axes[n].imshow(img_data[:,:,slice,0],'gray')
    axes[n].set_xticks([])
    axes[n].set_yticks([])
    axes[n].set_title('slice number : {}'.format(slice), color='r')
    n +=1
    slice +=10

fig.subplots_adjust(wspace=0, hspace=0)
plt.show()
plt.savefig('output/plot1.png')

#%% reshaping preparation
colonal = np.transpose(img_data, [1, 3, 2, 0])
colonal = np.rot90(colonal, 1)

trnsversal = np.transpose(img_data, [2,1,3,0])
trnsversal = np.rot90(trnsversal, 2)

sagital = np.transpose(img_data, [2,3,1,0])
sagital = np.rot90(sagital, 1)

#%%
# fig, axes = plt.subplots(3,10,figsize=[55,30])
#
# n=5
# for i in range(10):
#     axes[n].imshow(colonal[:, :, n, 0], 'gray')
#     axes[n].set_xticks([])
#     axes[n].set_yticks([])
#     axes[n].set_title('slice number : {}'.format(slice), color='blue')
#     if i == 0:
#         axes[0][i].set_ylabel('colonal', color='blue')
#     n +=15
#
# fig.subplots_adjust(wspace=0, hspace=0)
# plt.show()

