# -*- coding: utf-8 -*-
"""
@File    : train.py
@Author  : Junyan Huang
@Date    : 2024/6/15
@Updated : 2024/6/15
@Stu ID  : U202115263
"""


import os
import timm
import torch
from tqdm import tqdm
import cv2
from torch.utils.data import Dataset, DataLoader


class half_binary_dataset(Dataset):
    """
        半二值图像数据集
    """

    def __init__(self, add_imagenet=False, train=True, transform=None):
        super().__init__()

        ## set classes
        self.classes = os.listdir('half_binary_COD_15')
        self.Train = train
        self.transform = transform

        ## load dataset
        self.train_data = []
        self.test_data = []
        self.labels = []

        # load COD train
        if self.Train:
            for label, class_name in enumerate(self.classes):
                image_path = os.path.join('half_binary_COD_15', class_name, 'train')
                images = os.listdir(image_path)
                for img in images:
                    self.train_data.append(
                        os.path.join(image_path, img)
                    )
                    self.labels.append(label)

            # load imageNet
            if add_imagenet:
                for label, class_name in enumerate(self.classes):
                    image_path = os.path.join('half_binary_ImageNet_15', class_name)
                    images = os.listdir(image_path)
                    for img in images:
                        self.train_data.append(
                            os.path.join(image_path, img)
                        )
                        self.labels.append(label)

        # load COD test
        else:
            for label, class_name in enumerate(self.classes):
                image_path = os.path.join('half_binary_COD_15', class_name, 'test')
                images = os.listdir(image_path)
                for img in images:
                    self.test_data.append(
                        os.path.join(image_path, img)
                    )
                    self.labels.append(label)

    def __len__(self):
        return len(self.train_data) if self.Train else len(self.test_data)

    def __getitem__(self, idx):
        if self.Train:
            img = cv2.imread(
                self.train_data[idx]
            )
            if self.transform:
                img = self.transform(img)
            return img, self.labels[idx]
        else:
            img = cv2.imread(
                self.test_data[idx]
            )
            if self.transform:
                img = self.transform(img)
            return img, self.labels[idx]


if __name__ == "__main__":
    dataset = half_binary_dataset(add_imagenet=True)


