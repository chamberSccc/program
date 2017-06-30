# -*- coding: utf-8 -*-
from PIL import Image
import random
import cv2 as cv
import numpy as np

imgName = '8.jpg'
imgDir = 'image/'
kernel_size1 = (3, 3)
kernel_size2 = (9, 9)
sigma = 200


def readImg(imgDir, imgName):
    img = cv.imread(imgDir + imgName)
    return img


def addGausNoise(img, param):
    # 读取图片并转为数组
    im = np.array(img)
    means = 0
    sigma = 100

    r = im[:, :, 0].flatten()
    g = im[:, :, 1].flatten()
    b = im[:, :, 2].flatten()
    # 计算新的像素值
    for i in range(im.shape[0] * im.shape[1]):
        pr = int(r[i]) + random.gauss(0, sigma)
        pg = int(g[i]) + random.gauss(0, sigma)
        pb = int(b[i]) + random.gauss(0, sigma)
        if (pr < 0):
            pr = 0
        if (pr > 255):
            pr = 255
        if (pg < 0):
            pg = 0
        if (pg > 255):
            pg = 255
        if (pb < 0):
            pb = 0
        if (pb > 255):
            pb = 255
        r[i] = pr
        g[i] = pg
        b[i] = pb
    im[:, :, 0] = r.reshape([im.shape[0], im.shape[1]])
    im[:, :, 1] = g.reshape([im.shape[0], im.shape[1]])
    im[:, :, 2] = b.reshape([im.shape[0], im.shape[1]])
    new_imgName = 'New_Noise' + str(means) + "_" + str(sigma) + "_" + imgName
    # 写入图片
    cv.imwrite(imgDir + new_imgName, im)
    return im


def GaussionFilter(img, kernel_size, sigma):
    img_Gaus = cv.GaussianBlur(img, kernel_size, sigma)

    # 写入图片
    new_imgName = "New_Gau" + str(kernel_size1[0]) + "_" + str(sigma) + "_" + imgName
    cv.imwrite(imgDir + new_imgName, img_Gaus)
    return img_Gaus


def DiffOfGaussion(img, kernel_size1, kernel_size2):
    img_kernel1 = GaussionFilter(img, kernel_size1, sigma)
    img_kernel2 = GaussionFilter(img, kernel_size2, sigma)

    new_imgName = 'New_Dog' + str(kernel_size1[0]) + "_" + str(kernel_size2[1]) + "_" + imgName

    img_DOG = img_kernel1 - img_kernel2
    cv.imwrite(imgDir + new_imgName, img_DOG)
    return


# 先采用canny算子
def GradientNorm(img, operator):
    if operator == 'canny':
        img_Grad = cv.Canny(img, 100, 150)
        # img_Grad = cv.Laplacian()
    new_imgName = 'New_Grad' + operator + "_" + imgName
    cv.imwrite(imgDir + new_imgName, img_Grad)
    return


img = cv.imread(imgDir + imgName)
# img1 = GaussionFilter(img, kernel_size, sigma)
# DiffOfGaussion(img,1,4)
# GradientNorm(img1, 'canny')
# img1 = addGausNoise(img,1)
# img2 = GaussionFilter(img1, kernel_size2, sigma)
a = 1
# DiffOfGaussion(img2,kernel_size1,kernel_size2)


