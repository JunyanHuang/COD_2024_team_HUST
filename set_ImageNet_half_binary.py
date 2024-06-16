# -*- coding: utf-8 -*-
"""
@File    : set_ImageNet_half_binary.py
@Author  : Junyan Huang
@Date    : 2024/6/15
@Updated : 2024/6/15
@Stu ID  : U202115263
"""

import os
import cv2
from tqdm import tqdm


is_generate_dir = True
is_show_image = False
is_save_image_ImageNet = False
is_save_image_COD = True


if is_generate_dir:
    root, dirs, files = next(os.walk('matched_imagenet_15'))
    for dir_name in dirs:
        print(dir_name)
        os.makedirs(os.path.join('half_binary_COD_15' ,dir_name), exist_ok=True)
        os.makedirs(os.path.join('half_binary_ImageNet_15', dir_name), exist_ok=True)

##  保存ImageNet的半二值图像
_, class_names, _ = next(os.walk('half_binary_COD_15'))
image_id = 0
# for class_name in tqdm(class_names):
#     image_path_imagenet = os.path.join('matched_imagenet_15', class_name)
#     images = iter(os.listdir(os.path.join(image_path_imagenet, 'image')))
#     masks = iter(os.listdir(os.path.join(image_path_imagenet, 'mask')))
#
#     # 在15个子类中读取图像和掩码
#     while True:
#         try:
#             img = cv2.imread(
#                 os.path.join(image_path_imagenet, 'image', next(images))
#             )
#             msk = cv2.imread(
#                 os.path.join(image_path_imagenet, 'mask', next(masks))
#             )
#
#             # 生成半二值图像
#             img[msk == 0] = 0
#             if is_show_image:
#                 cv2.imshow('1', img)
#                 key = cv2.waitKey(0)
#
#             if is_save_image_ImageNet:
#                 image_id += 1
#                 cv2.imwrite(
#                     os.path.join('half_binary_ImageNet_15', class_name, str(image_id) + '.jpg'),
#                     img
#                 )
#
#         except StopIteration:
#             break


## 保存 COD 半二值图像
COD_train_path = 'half_binary_raw_COD/train'
COD_test_path = 'half_binary_raw_COD/test'

# 训练集
# train_files = os.listdir(COD_train_path)
# for train_file in tqdm(train_files):
#     try:
#         if len(train_file.split('-')) >= 6:
#             go_to_dir = str.lower(train_file.split('-')[5])
#             if go_to_dir == 'stickinsect':
#                 go_to_dir = 'stickInsect'
#             new_id = train_file.split('-')[6]
#             if go_to_dir in class_names:
#                 img = cv2.imread(os.path.join(COD_train_path, train_file))
#
#                 if is_show_image:
#                     cv2.imshow('1', img)
#                     key = cv2.waitKey(0)
#
#                 if is_save_image_COD:
#                     os.makedirs(
#                         os.path.join('half_binary_COD_15', go_to_dir, 'train'),
#                         exist_ok=True
#                     )
#                     cv2.imwrite(
#                         filename=os.path.join('half_binary_COD_15', go_to_dir, 'train', new_id),
#                         img=img
#                     )
#
#
#     except:
#         raise Exception(train_file.split('-'))

# 测试集
test_files = os.listdir(COD_test_path)
for test_file in tqdm(test_files):
    try:
        if len(test_file.split('-')) >= 6:
            go_to_dir = str.lower(test_file.split('-')[5])
            if go_to_dir == 'stickinsect':
                go_to_dir = 'stickInsect'
            new_id = test_file.split('-')[6]
            if go_to_dir in class_names:
                img = cv2.imread(os.path.join(COD_test_path, test_file))

                if is_show_image:
                    cv2.imshow('1', img)
                    key = cv2.waitKey(0)

                if is_save_image_COD:
                    os.makedirs(
                        os.path.join('half_binary_COD_15', go_to_dir, 'test'),
                        exist_ok=True
                    )
                    cv2.imwrite(
                        filename=os.path.join('half_binary_COD_15', go_to_dir, 'test', new_id),
                        img=img
                    )
    except:
        raise Exception(test_file.split('-'))







