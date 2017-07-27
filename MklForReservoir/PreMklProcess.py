# -*- coding: utf-8 -*-
import numpy as np
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import modshogun as shogun


#获取核函数的组合实例 combin_kernel
def getCombinKernel(kernelWidth,trainDataList):
    for x in trainDataList:
        x = shogun.RealFeatures(x)
    kernel_X_Y = shogun.GaussianKernel(trainDataList[0], trainDataList[0], kernelWidth[0])
    kernel_Gau_R1 = shogun.GaussianKernel(trainDataList[1],trainDataList[1],kernelWidth[1])
    kernel_Gau_R2 = shogun.GaussianKernel(trainDataList[2],trainDataList[2],kernelWidth[2])
    kernel_Gau_R4 = shogun.GaussianKernel(trainDataList[3],trainDataList[3],kernelWidth[3])
    kernel_Grad_R1 = shogun.GaussianKernel(trainDataList[4],trainDataList[4],kernelWidth[4])
    kernel_Grad_R2 = shogun.GaussianKernel(trainDataList[5],trainDataList[5],kernelWidth[5])
    kernel_Grad_R4 = shogun.GaussianKernel(trainDataList[6],trainDataList[6],kernelWidth[6])
    kernel_Dir_R1_X = shogun.GaussianKernel(trainDataList[7],trainDataList[7],kernelWidth[7])
    kernel_Dir_R2_X = shogun.GaussianKernel(trainDataList[8],trainDataList[8],kernelWidth[8])
    kernel_Dir_R4_X = shogun.GaussianKernel(trainDataList[9],trainDataList[9],kernelWidth[9])
    kernel_Dir_R1_Y = shogun.GaussianKernel(trainDataList[10],trainDataList[10],kernelWidth[10])
    kernel_Dir_R2_Y = shogun.GaussianKernel(trainDataList[11],trainDataList[11],kernelWidth[11])
    kernel_Dir_R4_Y = shogun.GaussianKernel(trainDataList[12],trainDataList[12],kernelWidth[12])
    kernel_Dog_R2_R1 = shogun.GaussianKernel(trainDataList[13],trainDataList[13],kernelWidth[13])
    kernel_Dog_R4_R2 = shogun.GaussianKernel(trainDataList[14],trainDataList[14],kernelWidth[14])
    kernel_Dog_R8_R6 = shogun.GaussianKernel(trainDataList[15],trainDataList[15],kernelWidth[15])

    kernel_train_list = [kernel_X_Y,kernel_Gau_R1,kernel_Gau_R2,kernel_Gau_R4,kernel_Grad_R1,kernel_Grad_R2,kernel_Grad_R4,
                         kernel_Dir_R1_X,kernel_Dir_R2_X,kernel_Dir_R4_X,kernel_Dir_R1_Y,kernel_Dir_R2_Y,kernel_Dir_R4_Y,
                         kernel_Dog_R2_R1,kernel_Dog_R4_R2,kernel_Dog_R8_R6]

    combined_kernel = shogun.CombinedKernel()
    for kernel in kernel_train_list:
        combined_kernel.append_kernel(kernel)
    return combined_kernel
#得到shogun复合特征 combin_feature
def getShogunFeature(trainDataList):
    combin_feature = shogun.CombinedFeatures()
    for x in trainDataList:
        combin_feature.append_feature_obj(shogun.RealFeatures(x))
    return combin_feature

#训练MKL
def getMkl(kernel,label):
    svm_solver = shogun.SVRLight()
    mkl = shogun.MKLRegression(svm_solver)
    mkl.set_kernel(kernel)
    mkl.set_labels(label)
    return mkl

# train_data = np.array([[1,2,3],[1.1,2.1,3.1]],dtype=float)
# train_data1 = shogun.RealFeatures(np.array([[1.2,2.2,3.2],[1.3,2.3,3.3],[1.4,2.4,3.4]],dtype=float))
# train_label = np.array([1,2,3],dtype=float)
# test_data = np.array([[2,3,4],[2.1,3.1,4.1]],dtype=float)
# test_label = np.array([2,3,4],dtype=float)
# traindata,testdata,traindatalabel,testdatalabel = reshapeData()
# kernel_Dog_1 = shogun.GaussianKernel(traindata,traindata,float(0.5))
# kernel_Grad_1 = shogun.GaussianKernel(train_data1,train_data1,float(1))
# combin_feature = shogun.CombinedFeatures()
# combin_feature.append_feature_obj(traindata)
# combin_feature.append_feature_obj(train_data1)
# combin_kernel = shogun.CombinedKernel()
# combin_kernel.append_kernel(kernel_Dog_1)
# combin_kernel.append_kernel(kernel_Grad_1)
# combin_kernel.init(combin_feature,combin_feature)
#
# binary_svm_solver = shogun.SVRLight()
# mkl = shogun.MKLRegression(binary_svm_solver)
# mkl.set_kernel(combin_kernel)
# mkl.set_labels(traindatalabel)
# # mkl.set_C(1, 1)
# mkl.set_mkl_norm(1)
# mkl.train()
# beta = combin_kernel.get_subkernel_weights()
# alpha = mkl.get_alphas()
# combin_kernel.init(testdata, testdata)
# labels_predict = mkl.apply_regression()
# b = labels_predict.get_labels()




