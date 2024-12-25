import cv2
import numpy as np
import os
import shutil
import random

def guass_noise(img, mean = 0, sigma = 10) :
    gauss = np.random.normal(mean,sigma,(img.shape[0],img.shape[1],img.shape[2]))
    noise_img = img+gauss
    noise_img = np.clip(noise_img,a_min=0,a_max=255)
    return noise_img


def saltpepper_noise(img, s_p_percent = 0.05) :
    noise_img = np.copy(img)
    s_vs_p = 0.5
    # 添加Salt噪声
    num_salt = np.ceil(s_p_percent * img.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
    noise_img[coords[0], coords[1], :] = [255, 255, 255]

# 添加Pepper噪声
    num_pepper = np.ceil(s_p_percent * img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
    noise_img[coords[0], coords[1], :] = [0, 0, 0]
    return noise_img

ori_path = './img_save/'
save_path = './new_pic'

filenames = os.listdir(ori_path)

# Filter out only .txt files
img_files = [f for f in filenames if f.endswith('.png') and os.path.isfile(os.path.join(ori_path, f))]
#print(txt_files)


for file_ in img_files :
    txt_file = file_[:-4] + '.txt'
    img = cv2.imread(ori_path+file_)
    print(file_)
    img_noise = guass_noise(img,0,5)
    save_name = rf'{save_path}/{file_[:-4]}_guassnoise'
    save_txt = shutil.copy(ori_path+txt_file, save_name+'.txt' )
    cv2.imwrite(save_name+'.png',img_noise)
'''
    img_noise = saltpepper_noise(img,0.01)
    save_name = rf'{save_path}/{file_[:-4]}_saltpeppernoise'
    cv2.imwrite(save_name+'.png',img_noise)
    #save_txt = shutil.copy(ori_path+txt_file, save_name+'.txt' )
'''
