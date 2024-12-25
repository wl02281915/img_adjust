import numpy
import os, cv2
 
data_path = './img_save/'
save_train = './data/train/'
save_val = './data/val/'
save_test = './data/test/'
 
choose_path = ['train','val','test']
 
filenames = os.listdir(data_path)
img_files = [f for f in filenames if f.endswith('.png') and os.path.isfile(os.path.join(data_path, f))]
for file_ in img_files :
    print(file_)
    img = cv2.imread(data_path+file_)
    save_ = numpy.random.choice(choose_path,p=[0.7,0.1,0.2])
    if save_ == 'train' :
        cv2.imwrite(save_train+'images/'+file_,img)
        os.popen(f'cp {data_path}{file_[:-4]}.txt {save_train}/labels')
    elif save_ == 'test' :
        cv2.imwrite(save_test+'images/'+file_,img)
        os.popen(f'cp {data_path}{file_[:-4]}.txt {save_test}/labels')
    else :
        cv2.imwrite(save_val+'images/'+file_,img)
        os.popen(f'cp {data_path}{file_[:-4]}.txt {save_val}/labels')

