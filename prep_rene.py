#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import cv2
import glob


# In[2]:


import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['savefig.dpi'] = 300


# In[3]:


labels = ["Carleft1", "Carleft2", "Carleft3", "Carright1", "Carright2", "Carright3"]


# In[4]:


OFFSET = 45 #choose 0/15/30/45
SLICE_SIZE = 60


# In[5]:


DIR_LABELS = "/Users/kitihh/vehid/START/masks/All" #"./masks"
DIR_INPUT = "/Users/kitihh/vehid/START/images/All" #"./images/images"

DIR_OUTPUT = "./"
FILE_OUT = f"preparation_rene_{SLICE_SIZE}_{OFFSET}_TRY.csv" #Delete _Oct
#FILE_OUT = f"preparation_rene_{SLICE_SIZE}_{OFFSET}.csv"


# In[6]:


files_inputs = glob.glob(f"{DIR_INPUT}{os.sep}*.png")
print(len(files_inputs))


# In[7]:


files_labels = {}
for i in labels:
    f = glob.glob(f"{DIR_LABELS}{os.sep}{i}{os.sep}*.png")
    t = {}
    for k in f:
        t[os.path.basename(k)] = k
    files_labels[i] = t


# In[9]:


with open(f"{DIR_OUTPUT}{FILE_OUT}", "a") as fw:
    fw.write("Image name, Slice number, Carleft1, Carleft2, Carleft3, Carright1, Carright2, Carright3\n")
    for f in files_inputs:
        f_b = os.path.basename(f)
        img_f = cv2.imread(f, cv2.IMREAD_COLOR)
        labels_dict = {}
        for k in files_labels:
            if f_b in files_labels[k]:
                labels_dict[k] = files_labels[k][f_b]
        images_dict = {}
        for k in labels_dict:
            images_dict[k] = cv2.imread(labels_dict[k], cv2.IMREAD_GRAYSCALE)
#             plt.figure()
#             plt.imshow(images_dict[k], cmap="gray")
        slice_list = []
        j = 0
        if len(labels_dict) > 0:
            for i in np.arange(OFFSET, img_f.shape[1], SLICE_SIZE):
                if img_f.shape[1] - i < SLICE_SIZE:
                    break
                a = i
                b = a + SLICE_SIZE
                cars_list = []
                for k in labels:
                    if k in images_dict:
                        current_image = images_dict[k][:,a:b]
                        test_image = (current_image < 255)
                        # plt.figure()
                        # plt.imshow(np.hstack((current_image, test_image.astype(np.uint8)*255)), cmap="gray")
                        # plt.title(f"{f_b}_{k}_{a}:{b}")
                        # plt.show()
                        pixel_count = np.sum(test_image.astype(np.uint8))
                        #print(pixel_count)
                        if pixel_count > 700:
                            cars_list.append(1)
                        else:
                            cars_list.append(0)
                    else:
                        cars_list.append(0)
                    #     if np.any(test_image.astype(np.uint8)):
                    #         cars_list.append(1)
                    #     else:
                    #         cars_list.append(0)
                    # else:
                    #     cars_list.append(0)
                slice_list.append(cars_list)
                j = j + 1
            for i in np.arange(len(slice_list)):
                txt = f"{f_b}, {i}"
                for j in slice_list[i]:
                    txt = f"{txt}, {j}"
                fw.write(f"{txt}\n")


# In[ ]:
# %%
