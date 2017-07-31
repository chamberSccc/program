# -*- coding: utf-8 -*-
import numpy as np
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import modshogun as shogun


def getCombinKernel(kernelWidth, TrainDataList):
    """
    Get combined kernel function instance
    Parameter
    ---------
    kernelWidth: list_like kernel width param list for each kernel
    TrainDataList: feature data list
                   data format:[feature1,feature2,feature3......]
    """
    sgTrainDataList = []
    for x in TrainDataList:
        dimen = x.shape
        if len(dimen) == 1:
            temp = x.reshape((-1, x.size))
        else:
            temp = x
        sgTrainDataList.append(shogun.RealFeatures(temp))
    kernel_X_Y = shogun.GaussianKernel(sgTrainDataList[0], sgTrainDataList[0], kernelWidth[0])
    kernel_Gau_R1 = shogun.GaussianKernel(sgTrainDataList[1], sgTrainDataList[1], kernelWidth[1])
    kernel_Gau_R2 = shogun.GaussianKernel(sgTrainDataList[2], sgTrainDataList[2], kernelWidth[2])
    kernel_Gau_R4 = shogun.GaussianKernel(sgTrainDataList[3], sgTrainDataList[3], kernelWidth[3])
    kernel_Grad_R1 = shogun.GaussianKernel(sgTrainDataList[4], sgTrainDataList[4], kernelWidth[4])
    kernel_Grad_R2 = shogun.GaussianKernel(sgTrainDataList[5], sgTrainDataList[5], kernelWidth[5])
    kernel_Grad_R4 = shogun.GaussianKernel(sgTrainDataList[6], sgTrainDataList[6], kernelWidth[6])
    kernel_Dir_R1_X = shogun.GaussianKernel(sgTrainDataList[7], sgTrainDataList[7], kernelWidth[7])
    kernel_Dir_R2_X = shogun.GaussianKernel(sgTrainDataList[8], sgTrainDataList[8], kernelWidth[8])
    kernel_Dir_R4_X = shogun.GaussianKernel(sgTrainDataList[9], sgTrainDataList[9], kernelWidth[9])
    kernel_Dir_R1_Y = shogun.GaussianKernel(sgTrainDataList[10], sgTrainDataList[10], kernelWidth[10])
    kernel_Dir_R2_Y = shogun.GaussianKernel(sgTrainDataList[11], sgTrainDataList[11], kernelWidth[11])
    kernel_Dir_R4_Y = shogun.GaussianKernel(sgTrainDataList[12], sgTrainDataList[12], kernelWidth[12])
    kernel_Dog_R2_R1 = shogun.GaussianKernel(sgTrainDataList[13], sgTrainDataList[13], kernelWidth[13])
    kernel_Dog_R4_R2 = shogun.GaussianKernel(sgTrainDataList[14], sgTrainDataList[14], kernelWidth[14])
    kernel_Dog_R8_R6 = shogun.GaussianKernel(sgTrainDataList[15], sgTrainDataList[15], kernelWidth[15])

    kernel_train_list = [kernel_X_Y,kernel_Gau_R1,kernel_Gau_R2,kernel_Gau_R4,kernel_Grad_R1,kernel_Grad_R2,kernel_Grad_R4,
                         kernel_Dir_R1_X,kernel_Dir_R2_X,kernel_Dir_R4_X,kernel_Dir_R1_Y,kernel_Dir_R2_Y,kernel_Dir_R4_Y,
                         kernel_Dog_R2_R1,kernel_Dog_R4_R2,kernel_Dog_R8_R6]

    combined_kernel = shogun.CombinedKernel()
    for kernel in kernel_train_list:
        combined_kernel.append_kernel(kernel)
    return combined_kernel

#get shogun's combined feature
def getShogunFeature(trainDataList):
    combin_feature = shogun.CombinedFeatures()
    for x in trainDataList:
        dimen = x.shape
        if len(dimen) == 1:
            temp = x.reshape((-1, x.size))
        else:
            temp = x
        combin_feature.append_feature_obj(shogun.RealFeatures(temp))
    return combin_feature

#get mkl instance
def getMkl(kernel,label):
    svm_solver = shogun.SVRLight()
    mkl = shogun.MKLRegression(svm_solver)
    mkl.set_kernel(kernel)
    mkl.set_labels(shogun.RegressionLabels(label))
    mkl.set_mkl_norm(1)
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




