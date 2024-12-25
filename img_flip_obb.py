import os
import cv2
import random
ori_path = './img_save/'
save_path = './new_pic/'

filenames = os.listdir(ori_path)

# Filter out only .jpg files
img_files = [f for f in filenames if f.endswith('.png') and os.path.isfile(os.path.join(ori_path, f))]


def img_flip(image,type_):
    if type_ == 'h':
        img_flip = cv2.flip(image, 1)
        ori_txt = open(f'{ori_path+txt_file}', 'r')
        ori_lines = ori_txt.readlines()
        save_name = rf'{save_path}/'+f'{file_[:-4]}_flip{type_}.txt'
        aft_txt = open(save_name, 'a+')
        for line in ori_lines :
            list_txt = line.split()
            list_txt[1] = str(round(1-float(list_txt[1]),6))
            list_txt[3] = str(round(1-float(list_txt[3]),6))
            list_txt[5] = str(round(1-float(list_txt[5]),6))
            list_txt[7] = str(round(1-float(list_txt[7]),6))
            txt_content = [x + ' ' for x in list_txt]
            txt_content[-1] = txt_content[-1][:-1]+'\n'
            aft_txt.writelines(txt_content)

    if type_ == 'v':
        img_flip = cv2.flip(image, 0)
        ori_txt = open(f'{ori_path+txt_file}', 'r')
        ori_lines = ori_txt.readlines()
        save_name = rf'{save_path}/'+f'{file_[:-4]}_flip{type_}.txt'
        aft_txt = open(save_name, 'a+')
        for line in ori_lines :
            list_txt = line.split()
            list_txt[2] = str(round(1 - float(list_txt[2]),6))
            list_txt[4] = str(round(1 - float(list_txt[4]),6))
            list_txt[6] = str(round(1 - float(list_txt[6]),6))
            list_txt[8] = str(round(1 - float(list_txt[8]),6))
            txt_content = [x + ' ' for x in list_txt]
            txt_content[-1] = txt_content[-1][:-1]+'\n'
            aft_txt.writelines(txt_content)


    if type_ == 'hv':
        img_flip = cv2.flip(image, -1)
        ori_txt = open(f'{ori_path+txt_file}', 'r')
        ori_lines = ori_txt.readlines()
        save_name = rf'{save_path}/'+f'{file_[:-4]}_flip{type_}.txt'
        aft_txt = open(save_name, 'a+')
        for line in ori_lines :
            list_txt = line.split()
            list_txt[1] = str(round(1 - float(list_txt[1]),6))
            list_txt[2] = str(round(1 - float(list_txt[2]),6))
            list_txt[3] = str(round(1 - float(list_txt[3]),6))
            list_txt[4] = str(round(1 - float(list_txt[4]),6))
            list_txt[5] = str(round(1 - float(list_txt[5]),6))
            list_txt[6] = str(round(1 - float(list_txt[6]),6))
            list_txt[7] = str(round(1 - float(list_txt[7]),6))
            list_txt[8] = str(round(1 - float(list_txt[8]),6))
            txt_content = [x + ' ' for x in list_txt]
            txt_content[-1] = txt_content[-1][:-1]+'\n'
            aft_txt.writelines(txt_content)
        
    return img_flip

for file_ in img_files :
    type_ = 'hv'
    txt_file = file_[:-4] + '.txt'
    img = cv2.imread(ori_path+file_)
    print(ori_path+file_)
    flip_img = img_flip(img,type_)
    save_name = rf'{save_path}/'+f'{file_[:-4]}_flip{type_}.png'
    cv2.imwrite(save_name,flip_img)
