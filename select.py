# -*- coding: utf-8 -*-
"""
@File    : select.py
@Author  : Junyan Huang
@Date    : 2024/6/4
@Updated : 2024/6/4
@Stu ID  : U202115263
"""
import cv2
import json
import os



## match by jason and txt
json_path = 'COD-ImageNet.json'
txt_path = 'LOC_synset_mapping.txt'
selected_dataset_path = 'selected_ImageNet'


## match the subclasses of COD and ImageNet
with open(json_path, 'r') as json_file:
    COD_ImageNet_match: dict = json.load(json_file)


## match the subclass names of ImageNet with their IDs
with open(txt_path, 'r') as txt_file:
    ImageNet_ID_match: dict = {}
    def collect_key(key_list):
        sub_class = ''
        for _key in key_list:

            sub_class = sub_class + _key + ' '
        return sub_class.strip(' ')

    for line in txt_file.readlines():
        key, value = collect_key(line.strip('\n').split(' ')[1:]), line.strip('\n').split(' ')[0]
        ImageNet_ID_match[key] = value


## count matched subclasses and images
num_class = 0
num_image = 0


## generate selected dataset
for key, value in COD_ImageNet_match.items():
    num_class += 1
    os.makedirs(os.path.join(selected_dataset_path, key), exist_ok=True)
    print(f"match:  COD-10K:{key}  ImageNet-1K:{value}")

    for subclass_ImageNet in value:
        try:
            assert os.path.exists(os.path.join('ILSVRC', 'train', ImageNet_ID_match[subclass_ImageNet]))
        except:
            raise Exception(f'{subclass_ImageNet}不存在')

        # read and store image
        images_path = [os.path.join('ILSVRC', 'train', ImageNet_ID_match[subclass_ImageNet], image)
                       for image in os.listdir(os.path.join('ILSVRC', 'train', ImageNet_ID_match[subclass_ImageNet]))]
        for _img in images_path:
            num_image += 1
            img = cv2.imread(_img)
            cv2.imwrite(os.path.join(selected_dataset_path, key, str(num_image) + '.jpg'), img)




## show matched subclasses and images number
print(f'\n{num_class} classes match between ImageNet and COD-10K in total')
print(f'{num_image} images match in total')


