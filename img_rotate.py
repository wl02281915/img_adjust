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
    txt_x, txt_y, txt_w, txt_h = float(txt_[1])*old_w, float(txt_[2])*old_h, float(txt_[3])*old_w, float(txt_[4])*old_h 
    b_left_top = [txt_x-txt_w/2+x_offset, txt_y-txt_h/2+y_offset]; b_left_bottom = [txt_x-txt_w/2+x_offset, txt_y+txt_h/2+y_offset]
    b_right_top = [txt_x+txt_w/2+x_offset, txt_y-txt_h/2+y_offset]; b_right_bottom = [txt_x+txt_w/2+x_offset ,txt_y+txt_h/2+y_offset]

    left_top_matrix = np.matrix(b_left_top+[1]) ;a_left_top = (rotate_matrix*left_top_matrix.T).flatten().tolist()
    left_bottom_matrix = np.matrix(b_left_bottom+[1]) ;a_left_bottom = (rotate_matrix*left_bottom_matrix.T).flatten().tolist()
    right_top_matrix = np.matrix(b_right_top+[1]) ;a_right_top = (rotate_matrix*right_top_matrix.T).flatten().tolist()
    right_bottom_matrix = np.matrix(b_right_bottom+[1]) ;a_right_bottom = (rotate_matrix*right_bottom_matrix.T).flatten().tolist()
    left_top = [max(0,int(min([a_left_top[0][0],a_left_bottom[0][0],a_right_top[0][0],a_right_bottom[0][0]]))),
        max(0,int(min([a_left_top[0][1],a_left_bottom[0][1],a_right_top[0][1],a_right_bottom[0][1]])))]

    right_bottom = [min(w,int(max([a_left_top[0][0],a_left_bottom[0][0],a_right_top[0][0],a_right_bottom[0][0]]))),
        min(h,int(max([a_left_top[0][1],a_left_bottom[0][1],a_right_top[0][1],a_right_bottom[0][1]])))]
    a_x, a_y, a_w, a_h = (left_top[0]+right_bottom[0])/2/w, (left_top[1]+right_bottom[1])/2/h, (right_bottom[0]-left_top[0])/w, (right_bottom[1]-left_top[1])/h
    if min(a_x,a_y)<=0 or max(a_x,a_y)>=1 :
        flag_= False
    else :
        flag_ = True


    return flag_, [str(round(a_x,6)), str(round(a_y,6)), str(round(a_w,6)), str(round(a_h,6))]

def expend_img(img):
    global canvas, x_offset, y_offset, old_h, old_w
    (old_h, old_w) = img.shape[:2] 
    max_diagonal = math.ceil(math.sqrt(old_h ** 2 + old_w ** 2))
    (new_h, new_w) = (max_diagonal,max_diagonal)
    canvas = np.ones((new_h, new_w, 3), dtype=np.uint8)*255
    x_offset = (new_w - old_w) // 2
    y_offset = (new_h - old_h) // 2
    canvas[y_offset:y_offset+old_h, x_offset:x_offset+old_w] = img
    #cv2.imwrite("output.png", canvas)



for file_ in img_files :
    angle = 50
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
        flag_, after_txt = rotate_txt(list_txt,M)
        if flag_ == True :
            for i in range(len(after_txt)):
                list_txt[i+1] = after_txt[i]
            txt_content = [x + ' ' for x in list_txt]
            txt_content[-1] = txt_content[-1][:-1]+'\n'
            aft_txt.writelines(txt_content)
#cv2.imshow('rotated_image', rotated_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
