import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

ori_path = './img_save/'
save_path = './new_pic'

filenames = os.listdir(ori_path)

# Filter out only .txt files
txt_files = [f for f in filenames if f.endswith('.txt') and os.path.isfile(os.path.join(ori_path, f))]

#print(txt_files)


for file_ in txt_files :
    img_file = file_[:-4] + '.png'
    print(ori_path+img_file)
    img = Image.open(ori_path+img_file)

    brightness = ImageEnhance.Brightness(img) # 調整亮度
    contrast = ImageEnhance.Contrast(img)     # 調整對比
    color = ImageEnhance.Color(img)           # 調整飽和度
    sharpness = ImageEnhance.Sharpness(img)   # 調整銳利度

    output_b5 = brightness.enhance(2)       # 提高亮度
    save_name = rf'{save_path}/{file_[:-4]}_brightup'
    output_b5.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' ) 

    output_b05 = brightness.enhance(0.5)      # 降低亮度
    save_name = rf'{save_path}/{file_[:-4]}_brightdown'
    output_b05.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )
    
    output_c5 = contrast.enhance(5)           # 提高對比
    save_name = rf'{save_path}/{file_[:-4]}_constrastup'
    output_c5.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )

    output_c05 = contrast.enhance(0.5)        # 降低對比
    save_name = rf'{save_path}/{file_[:-4]}_constrastdown'
    output_c05.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )
    
    output_color5 = color.enhance(5)          # 提高飽和度
    save_name = rf'{save_path}/{file_[:-4]}_colorup'
    output_color5.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )

    output_color05 = color.enhance(0.5)       # 降低飽和度
    save_name = rf'{save_path}/{file_[:-4]}_colordown'
    output_color05.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )

    output_s5 = sharpness.enhance(10)        # 提高銳利度
    save_name = rf'{save_path}/{file_[:-4]}_sharpup'
    output_s5.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )

    output_s05 = sharpness.enhance(0.5)          # 降低銳利度
    save_name = rf'{save_path}/{file_[:-4]}_sharpdown'
    output_s05.save(save_name+'.png')
    save_txt = shutil.copy(ori_path+file_, save_name+'.txt' )
