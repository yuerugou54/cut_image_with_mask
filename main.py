#-*-coding:utf-8-*-
from skimage import data, util
import skimage
import cv2
import numpy as np
import skimage as skimage
from skimage import morphology
import copy
import os
def split_with_bbox(image,label,save_path):
	#(min_row, min_col, max_row, max_col)
    laebl = label>0
    connect_label = skimage.measure.label(label, connectivity=1)
    area_list= skimage.measure.regionprops(connect_label)
    for index,area in enumerate(area_list):
        cur_box = area.bbox
        print(cur_box)
        target_image = copy.copy(image[cur_box[0]:cur_box[2],cur_box[1]:cur_box[3]])
        target_label = copy.copy(label[cur_box[0]:cur_box[2],cur_box[1]:cur_box[3]])
        target_label[target_label>0]=255
        target_label[target_label==0]=0
        cv2.imwrite(os.path.join(save_path, str(index)+".png"),target_label)
        cv2.imwrite(os.path.join(save_path, str(index)+".jpg"),target_image)

#imread image
img = cv2.imread("image.jpg")
#imread label
label = cv2.imread("label.png")[:,:,0]
label=255-label
#imread label
save_path = "result"
split_with_bbox(img,label,save_path)


