# -*- coding: utf-8 -*-
"""
@File    : imagenet_selection.py
@Author  : Junyan Huang
@Date    : 2024/5/26
@Updated : 2024/5/26
@Stu ID  : U202115263
"""

import os
import shutil
import json
import cv2


json_path = 'COD-ImageNet.json'
raw_path = 'imagenet1k'
selected_path = 'imagenet1K_selected'


## 读取COD-ImageNet.json
with open(json_path, 'r') as json_file:
    COD_ImageNet_match: dict = json.load(json_file)


num_class = 0   # 统计匹配的类数量
num_image = 0
for key, value in COD_ImageNet_match.items():
    num_class += 1
    os.makedirs(os.path.join(selected_path, key), exist_ok=True)

    for imagenet_class in value:
        try:
            assert os.path.exists(os.path.join(raw_path, imagenet_class))
        except:
            raise Exception(f'在{raw_path}中{imagenet_class}不存在')
        images_path = [os.path.join(raw_path, imagenet_class, image)
                       for image in os.listdir(os.path.join(raw_path, imagenet_class))]

        for img_path in images_path:
            image = cv2.imread(img_path)
            cv2.imwrite(os.path.join(selected_path, key, str(num_image)+'.jpg' ), image)
            num_image += 1


    print(f"match:  COD-10K:{key}  ImageNet-1K:{value}")

print(f'\n{num_class} classes match between ImageNet and COD-10K in total')
print(f'{num_image} images match in total')