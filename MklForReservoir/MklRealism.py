# -*- coding: utf-8 -*-
import numpy as np
import modshogun as shogun

#获取核函数的组合实例
def getCombinKernel():
    kernel_Dog_1 = shogun.GaussianKernel(1.0)
    kernel_Grad_1 = shogun.GaussianKernel(1.0)
    kernel_DirX = shogun.GaussianKernel(1.0)
    kernel_DirY = shogun.GaussianKernel(1.0)
    combined_kernel = shogun.CombinedKernel()
    combined_kernel.append_kernel(kernel_Dog_1)
    combined_kernel.append_kernel(kernel_Grad_1)
    combined_kernel.append_kernel(kernel_DirX)
    combined_kernel.append_kernel(kernel_DirY)
    return combined_kernel

def reshapeData():
    features_train = shogun.RealFeatures()
    features_test  = shogun.RealFeatures()
    return

def trainData():
    return