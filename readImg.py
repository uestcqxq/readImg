# -*- coding: UTF-8 -*-
import time

import numpy as np
import os
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
from glob import glob
from PIL import Image


# 读取目录下所有的jpg图片
def load_image(image_path, image_size):
    file_name = glob(image_path + "/*jpg")
    sample = []
    for file in file_name:
        pic = imread(file).astype(np.float32)
        pic = imresize(pic, (image_size, image_size)).astype(np.float32)
        sample.append(pic)

    sample = np.array(sample)
    return sample


def openImg(img_path):
    img = Image.open(img_path)

    return img


if __name__ == '__main__':
    samples = load_image("./321201006", 300)
    # 显示第一张图片

    # pic = samples[:1, :, :, :]
    for i in range(100):
        pic=samples[i]
        pic = np.reshape(pic, (300, 300, 3)).astype(np.uint8)
        plt.imshow(pic)
        plt.show()
        print('显示第',i,'张二维码：')
        time.sleep(1)
        plt.close()
    # f_dir = r'.\321201006'
    # file_list = os.listdir(f_dir)
    # print(len(file_list))
    # print(file_list[0])
    #
    # for i in range(100):
    #     file_path = f_dir + '\\' + file_list[i]
    #     print(file_path)
    #
    #     img = openImg(file_path)
    #     img.show()
    #     time.sleep(2)
    #     img.
    # f_path = r'.\321201006\321201006SF0000052_周冬梅_刘琳.jpg'
    #     # openImg(f_path)
