import cv2
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import math

ori_path = './img_save/'
save_path = './new_pic/'

filenames = os.listdir(ori_path)

# Filter out only .jpg files
img_files = [f for f in filenames if f.endswith('.png') and os.path.isfile(os.path.join(ori_path, f))]


def rotate_image(image, angle):
    global M,h,w
    (h, w) = canvas.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h), borderValue=(125,125,125))
    return rotated_image

def rotate_txt(txt_,rotate_matrix):
    b_x1 = float(txt_[1])*old_w+x_offset; b_y1 = float(txt_[2])*old_h+y_offset; b_x2 = float(txt_[3])*old_w+x_offset; b_y2 = float(txt_[4])*old_h+y_offset
    b_x3 = float(txt_[5])*old_w+x_offset; b_y3 = float(txt_[6])*old_h+y_offset; b_x4 = float(txt_[7])*old_w+x_offset; b_y4 = float(txt_[8])*old_h+y_offset
    b_left_top = [b_x1,b_y1]; b_right_top = [b_x2,b_y2]; b_right_bottom = [b_x3,b_y3]; b_left_bottom = [b_x4,b_y4]

    left_top_matrix = np.matrix(b_left_top+[1]) ;a_left_top = (rotate_matrix*left_top_matrix.T).flatten().tolist()
    left_bottom_matrix = np.matrix(b_left_bottom+[1]) ;a_left_bottom = (rotate_matrix*left_bottom_matrix.T).flatten().tolist()
    right_top_matrix = np.matrix(b_right_top+[1]) ;a_right_top = (rotate_matrix*right_top_matrix.T).flatten().tolist()
    right_bottom_matrix = np.matrix(b_right_bottom+[1]) ;a_right_bottom = (rotate_matrix*right_bottom_matrix.T).flatten().tolist()
    x1 = np.clip(round(a_left_top[0][0]/w,3),0,1); y1 = np.clip(round(a_left_top[0][1]/h,3),0,1)
    x2 = np.clip(round(a_right_top[0][0]/w,3),0,1); y2 = np.clip(round(a_right_top[0][1]/h,3),0,1)
    x3 = np.clip(round(a_right_bottom[0][0]/w,3),0,1); y3 = np.clip(round(a_right_bottom[0][1]/h,3),0,1)
    x4 = np.clip(round(a_left_bottom[0][0]/w,3),0,1); y4 = np.clip(round(a_left_bottom[0][1]/h,3),0,1)
    txt_content = f'{txt_[0]} {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n'
    return txt_content

def expend_img(img):
    global canvas, x_offset, y_offset, old_h, old_w
    (old_h, old_w) = img.shape[:2] 
    max_diagonal = math.ceil(math.sqrt(old_h ** 2 + old_w ** 2))
    (new_h, new_w) = (max_diagonal,max_diagonal)
    canvas = np.ones((new_h, new_w, 3), dtype=np.uint8)*50
    x_offset = (new_w - old_w) // 2
    y_offset = (new_h - old_h) // 2
    canvas[y_offset:y_offset+old_h, x_offset:x_offset+old_w] = img
    #cv2.imwrite("output.png", canvas)



for file_ in img_files :
    angle = 320
    img = cv2.imread(ori_path+file_)
    print(ori_path+file_)
    expend_img(img)
    rotated_image = rotate_image(canvas, angle)
    save_name = rf'{save_path}/'+f'{file_[:-4]}_rotate{angle}.png'
    cv2.imwrite(save_name,rotated_image)

    txt_file = file_[:-4] + '.txt'
    ori_txt = open(f'{ori_path+txt_file}', 'r')
    ori_lines = ori_txt.readlines()
    aft_txt = open(save_name[:-4]+'.txt', 'a+')
    for line in ori_lines :
        list_txt = line.split()
        after_txt = rotate_txt(list_txt,M)
        aft_txt.writelines(after_txt)
#cv2.imshow('rotated_image', rotated_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
