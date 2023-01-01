import glob
import cv2
import os
import cv2
import numpy as np

INPUT1 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_0"
INPUT2 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_15"
INPUT3 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_30"
INPUT4 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_45"

INPUT5 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_30_Nov"
INPUT6 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_30_Oct"
#INPUT7 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_45_Nov"
#INPUT8 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_all_45_Oct"
INPUT9 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_0_First"
INPUT10 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_15_First"
INPUT11 = "/Users/kitihh/vehid/START/Image_Splits_Current/images_split_45_First"

OUTPUT_DIR = "/Users/kitihh/vehid/START/Image_Splits_Current_Mirrored/"

input = INPUT4
mir = "mir"

out_folder = os.path.basename(input)
img_paths = glob.glob(f"{input}{os.sep}*.png")

for img_path in img_paths:
    img_name = os.path.basename(img_path)
    y1 = img_name.split('_')[0]
    y2 = img_name.split('_')[1]
    y3 = img_name.split('_')[2]
    y4 = img_name.split('_')[3]
    y5 = img_name.split('_')[4]
    y6 = img_name.split('_')[5]
    slice_number = img_name.split('_')[6]
    img_basename = img_name.split(f"{y1}_{y2}_{y3}_{y4}_{y5}_{y6}_{slice_number}_")[1]
    img_basename = img_basename.split('.')[0]
    print(y1, y2, y3, y4, y5, y6, slice_number, img_basename)
    
    img = cv2.imread((img_path), cv2.IMREAD_COLOR)
    #cv2.imshow('Image', img)
    img_mir = np.fliplr(img)
    #cv2.imshow('Mirrored image', img_mir)
    #cv2.waitKey(0)

    cv2.imwrite(f"{OUTPUT_DIR}/{out_folder}/{y4}_{y5}_{y6}_{y1}_{y2}_{y3}_{slice_number}_{img_basename}mir.png", img_mir)
print(out_folder)
