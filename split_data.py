# import os
import cv2
# import numpy as np
import pandas as pd

# IMG_HEIGHT = 740
# IMG_WIDTH = 596
SLICE_SIZE = 60
OFFSET = 45 #choose 0/15/30/45
DATA_DIR = "/Users/kitihh/vehid/START/images/All_CNN/" #"./images/images/"
FILE_NAME = f"./START/preparation_rene_{SLICE_SIZE}_{OFFSET}_TRY.csv" #delete Nov if not Nov
# OUTPUT_DIR = f"images_split_test"
OUTPUT_DIR = f"images_split_all_{OFFSET}" #Usually instead of all are split names to be used

data_csv = pd.read_csv(FILE_NAME, delimiter=",\s*", header = 0, engine='python') #_rene_60_45
print(data_csv)
#data_csv = data_csv.query('`Slice number` != 9')


name_old = ""
img = []

for i in data_csv.to_numpy():
    name_current, slice_number, y1, y2, y3, y4, y5, y6 = i
    a = SLICE_SIZE * slice_number + OFFSET
    b = a + SLICE_SIZE
    if name_old != name_current:
        print(name_current)
        img = cv2.imread((DATA_DIR + name_current), cv2.IMREAD_COLOR)
    cv2.imwrite(f"./START/{OUTPUT_DIR}/{y1}_{y2}_{y3}_{y4}_{y5}_{y6}_{slice_number}_{name_current}", img[:,a:b,:])
    name_old = name_current
    