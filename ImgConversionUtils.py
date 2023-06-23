from PIL import Image, ImageEnhance
import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def ImgEnhance_muti(img_pil,Mode_=["bright",],Factor=[1,]):
    """
    Mode：      颜色转换类型[bright,contrast,color,sharpness]
    Factor ：   倍数
    return:     多张图片拼接Image
    """
    rows_=1+(Mode_.__len__())//3
    row_i=-1
    new_img_= Image.new(img_pil.mode, (512*3, 512*rows_))
    image_=img_pil
    for i_,mode_ in enumerate(Mode_):
        if(mode_=="bright"):
            # 亮度调整
            image_ = ImageEnhance.Brightness(image_).enhance(Factor[i_])
        if(mode_=="contrast"):
            # 对比度调整
            image_ = ImageEnhance.Contrast(image_).enhance(Factor[i_])
        if(mode_=="color"):
            # 饱和度调整
            image_ = ImageEnhance.Color(image_).enhance(Factor[i_])
        if(mode_=="sharpness"):
            # 清晰度调整
            image_ = ImageEnhance.Sharpness(image_).enhance(Factor[i_])
        if i_%3==0:
            row_i+=1
        new_img_.paste(image_,(512*(i_%3), 512*row_i))
    return new_img_

def ImgEnhance_one(img_pil,Mode_=["bright",],Factor=[1,]):
    """
    Mode：      颜色转换类型[bright,contrast,color,sharpness]
    Factor ：   倍数
    return:     多张图片拼接Image
    """
    rows_=1+(Mode_.__len__())//3
    row_i=-1
    new_img_= Image.new(img_pil.mode, (512, 512))
    image_=img_pil
    for i_,mode_ in enumerate(Mode_):
        if(mode_=="bright"):
            # 亮度调整
            image_ = ImageEnhance.Brightness(image_).enhance(Factor[i_])
        if(mode_=="contrast"):
            # 对比度调整
            image_ = ImageEnhance.Contrast(image_).enhance(Factor[i_])
        if(mode_=="color"):
            # 饱和度调整
            image_ = ImageEnhance.Color(image_).enhance(Factor[i_])
        if(mode_=="sharpness"):
            # 清晰度调整
            image_ = ImageEnhance.Sharpness(image_).enhance(Factor[i_])
        # 
        new_img_.paste(image_,(0, 0))
    return new_img_

    
def Pil2cv(img_pil):
    """ pil to cv 
        return img_cv
    """
    img_cv=np.asarray(img_pil)
    return img_cv

def Cv2pil(img_cv):
    """ 
        cv to pil 
        return img_pil 
    """
    img_pil=Image.fromarray(cv2.cvtColor(img_cv,cv2.COLOR_BGR2RGB))
    return img_pil

def Imgcvlist2plt(img_list:list,name_list:list):
    """ 图像显示。传参：图像元组 返回值：无 """
    out_imgs=np.hstack(tuple(img_list))
    out_imgs = cv2.cvtColor(out_imgs,cv2.COLOR_RGBA2BGR)
    return out_imgs


# def BatchProcessImgs(processMethod,method_param:list,save_root="/home/wzc/zlt_self/CV_Work/ImgFold"):
#     """ 批处理文件夹 """
#     # 判断存储位置是否存在，没有则创建
#     if not os.path.exists(save_root):
#         os.mkdir(save_root)
#     # 获得所有img地址
#     # root_path=f"/home/wzc/zlt_self/ZNewMyModel/data/Drishti-GS/test/disc_small/image"
#     sub_dir=["Drishti-GS","refuge"]
#     next_dir=["train","test"]
#     for sub_dir_ in sub_dir:
#         for next_dir_ in next_dir:
#             img_dir=f"/home/wzc/zlt_self/ZNewMyModel/data/{sub_dir_}/{next_dir_}/disc_small/image"
#             if os.path.exists(img_dir):
#                 file_names=os.listdir(img_dir)
#                 print(f"length:{file_names.__len__()}---{sub_dir_}/{next_dir_}/disc_small/image")
#                 for file_name in file_names:
#                     img_path=os.path.join(img_dir,file_name)
#                     save_path=os.path.join(save_root,f"{sub_dir_}/{next_dir_}/disc_small/image",file_name)
#                     processMethod(method_param,img_path=img_path,save_path=save_path)
#             else:
#                     print(f"！！！不存在：{img_dir}！！！")


def Imgs_filepath_Dict() :
    """ img_root="/home/wzc/zlt_self/ZNewMyModel/data" """
    imgPathDict=dict()
    sub_dir=["Drishti-GS","refuge"]
    next_dir=["train","test"]
    for sub_dir_ in sub_dir:
        for next_dir_ in next_dir:
            img_dir=f"/home/wzc/zlt_self/ZNewMyModel/data/{sub_dir_}/{next_dir_}/disc_small/image"
            if os.path.exists(img_dir):
                file_names=os.listdir(img_dir)
                print(f"length:{file_names.__len__()}---{sub_dir_}/{next_dir_}/disc_small/image")
                imgPathDict[f'{sub_dir_}/{next_dir_}']=file_names
    return imgPathDict

def plt_show(rows_n,cols_n,img_with_index=None,img_list=None):
    if img_with_index !=None:
        plt.figure()
        img_index=0
        img_root="/home/wzc/zlt_self/ZNewMyModel/data"
        
        for row_ in range(rows_n):
            for col_ in range(cols_n):
                print(f"第{img_index+1}张")
                plt.subplot(rows_n,cols_n,img_index+1)
                img_in_plt=cv2.imread(os.path.join(img_root+"/Drishti-GS/test"+"/disc_small/image",imgs_list[img_index]))
                plt.imshow(img_in_plt)
                img_index+=1
        plt.show()
    elif img_list !=None:
        img_root="/home/wzc/zlt_self/ZNewMyModel/data"
        
        plt.figure()

        img_index=0
        for row_ in range(rows_n):
            for col_ in range(cols_n):
                plt.subplot(rows_n,cols_n,img_index+1)
                plt.xticks([])
                plt.yticks([])
                img_path=img_root+"/Drishti-GS/test/disc_small/image/"+img_list[img_index]
                print(f"第{img_index+1}张--{img_path}")
                img_in_plt=cv2.imread(img_path)
                img_in_plt = cv2.cvtColor(img_in_plt,cv2.COLOR_RGBA2BGR)
                plt.imshow(img_in_plt)
                img_index+=1
        plt.show()
    else:
        sys.exit(1)














