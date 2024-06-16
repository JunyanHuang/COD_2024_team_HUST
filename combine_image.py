# -*- coding: utf-8 -*-
"""
@File    : combine_image.py
@Author  : Junyan Huang
@Date    : 2024/6/14
@Updated : 2024/6/14
@Stu ID  : U202115263
"""
import numpy as np

"""
    用于将 COD-10K 和 ImageNet中对应的图像合并
    随机裁剪-拼接
"""

import os
import cv2
import random


# 设置图像大小
size = (680, 512)           # 宽度， 高度
size_half = (340, 256)      # 宽度 / 2， 高度 / 2
size_hole = (128, 128)      # 最大空洞

# 是否展示图像 是否生成文件 是否保存图片
is_show_image: bool = False
is_generate_dir: bool = False
is_save_image: bool = True
is_save_mask: bool = True


## 匹配 COD-10K和ImageNet文件名
if is_generate_dir:
    root, dirs, files = next(os.walk('matched_imagenet_15'))
    for dir_name in dirs:
        print(dir_name)
        os.makedirs(os.path.join('Image-COD' ,dir_name), exist_ok=True)

    for root, dirs_imagenet, files in os.walk('Image-COD'):
        for file_name in  files:
            try:
                go_to_dir = str.lower(file_name.split('-')[5])
                if go_to_dir == 'stickinsect':
                    go_to_dir = 'stickInsect'
                new_id = file_name.split('-')[6]
                if go_to_dir in dirs:
                    print(go_to_dir)
                    img = cv2.imread(os.path.join(root, file_name))
                    cv2.imwrite(filename= os.path.join('Image-COD', go_to_dir, new_id + '.jpg'), img=img)
            except:
                print(" false file name ",file_name)


_, subclass_names , _ = next(os.walk('matched_imagenet_15'))
new_img_id = 0
for subclass in subclass_names:
    print('\n\n')
    print("processing: ", subclass)

    # image     ImageNet
    root_image, dirs, files_images = next(os.walk(os.path.join('matched_imagenet_15', subclass, 'image')))

    # mask      ImageNet
    root_mask, _, files_masks = next(os.walk(os.path.join('matched_imagenet_15', subclass, 'mask')))

    # image     COD
    root_COD = os.path.join('Image-COD', subclass)
    files_images_COD = os.listdir(root_COD)

    # 读取 imagenet 数据
    files_images = iter(files_images)
    files_masks = iter(files_masks)

    # 新建保存新数据集的文件夹
    os.makedirs(os.path.join('image_for_repair', subclass, 'image'), exist_ok=True)
    os.makedirs(os.path.join('image_for_repair', subclass, 'mask'), exist_ok=True)

    ## 读取imagenet图像
    while True:
        try:
            image_name = next(files_images)
            mask_name = next(files_masks)

            # 确保image 和 mask 匹配
            try:
                assert image_name.split('.')[0] == mask_name.split('.')[0]
            except:
                raise Exception("not matched")

            # 读取image mask
            img = cv2.imread(os.path.join(root_image, image_name))
            msk = cv2.imread(os.path.join(root_mask, mask_name))

            # 为图像修复做处理
            img[msk == 0] = 255
            img = cv2.resize(img, size_hole, interpolation=cv2.INTER_AREA)
            msk = cv2.resize(msk, size_hole, interpolation=cv2.INTER_AREA)
            reverse_msk = np.zeros_like(msk)
            reverse_msk[msk == 0] = 255
            cod_msk = np.zeros_like(msk)



            # 随机挑选COD图像
            rand_cod_image_name = random.choice(files_images_COD)
            rand_cod_img = cv2.imread(os.path.join(root_COD, rand_cod_image_name))
            rand_cod_img = cv2.resize(rand_cod_img, size_half, interpolation=cv2.INTER_AREA)

            # 合并图像
            # new_image = np.concatenate((img, rand_cod_img), axis=1)
            new_image = np.concatenate((
                    np.concatenate((rand_cod_img, rand_cod_img), axis=0),
                    np.concatenate((rand_cod_img, rand_cod_img), axis=0)
                ),
                axis=1
            )


            # 随机放置
            x_offset = np.random.randint(0, size_hole[0])
            y_offset = np.random.randint(0, size_hole[1])
            new_image[y_offset : y_offset + size_hole[1], x_offset : x_offset + size_hole[0]] = img

            # 生成掩码
            new_mask = np.zeros_like(new_image)
            new_mask[y_offset : y_offset + size_hole[1],x_offset : x_offset + size_hole[0]] = cv2.bitwise_not(msk)

            # 展示图像
            if is_show_image:
                # cv2.imshow('imgnet', img)
                # key = cv2.waitKey(0)
                # cv2.imshow('cod', rand_cod_img)
                # key = cv2.waitKey(0)
                cv2.imshow('new_image', new_image)
                cv2.imshow('new_mask', new_mask)
                key = cv2.waitKey(0)
                pass

            if is_save_image:
                new_img_id += 1
                print('id: ', new_img_id)
                cv2.imwrite(os.path.join('image_for_repair', subclass, 'image', str(new_img_id) + '.jpg'), new_image)
                if is_save_mask:
                    cv2.imwrite(os.path.join('image_for_repair', subclass, 'mask', str(new_img_id) + '.jpg'), new_mask)








        except StopIteration:
            break


## 显示生成多少图片
print(f'{new_img_id} new images are generated')
