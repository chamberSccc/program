# -*- coding: utf-8 -*-
import numpy as np
import os
SHOGUN_DATA_DIR=os.getenv('SHOGUN_DATA_DIR', '../../../data')
import modshogun as shogun

kernelWidthList = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,
                   1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,]
#获取核函数的组合实例
def getCombinKernel(kernelWidth):
    kernel_Gau_R1 = shogun.GaussianKernel(kernelWidth[0])
    kernel_Gau_R2 = shogun.GaussianKernel(kernelWidth[1])
    kernel_Gau_R4 = shogun.GaussianKernel(kernelWidth[2])
    kernel_Gau_R6 = shogun.GaussianKernel(kernelWidth[3])
    kernel_Gau_R8 = shogun.GaussianKernel(kernelWidth[4])
    kernel_Grad_R1 = shogun.GaussianKernel(kernelWidth[5])
    kernel_Grad_R2 = shogun.GaussianKernel(kernelWidth[6])
    kernel_Grad_R4 = shogun.GaussianKernel(kernelWidth[7])
    kernel_Dir_R1_X = shogun.GaussianKernel(kernelWidth[8])
    kernel_Dir_R2_X = shogun.GaussianKernel(kernelWidth[9])
    kernel_Dir_R4_X = shogun.GaussianKernel(kernelWidth[10])
    kernel_Dir_R1_Y = shogun.GaussianKernel(kernelWidth[11])
    kernel_Dir_R2_Y = shogun.GaussianKernel(kernelWidth[12])
    kernel_Dir_R4_Y = shogun.GaussianKernel(kernelWidth[13])
    kernel_Dog_R2_R1 = shogun.GaussianKernel(kernelWidth[14])
    kernel_Dog_R4_R2 = shogun.GaussianKernel(kernelWidth[15])
    kernel_Dog_R8_R6 = shogun.GaussianKernel(kernelWidth[16])
    kernel_X_Y = shogun.GaussianKernel(kernelWidth[17])

    combined_kernel = shogun.CombinedKernel()
    combined_kernel.append_kernel(kernel_Gau_R1)
    combined_kernel.append_kernel(kernel_Gau_R2)
    combined_kernel.append_kernel(kernel_Gau_R4)
    combined_kernel.append_kernel(kernel_Gau_R6)
    combined_kernel.append_kernel(kernel_Gau_R8)
    combined_kernel.append_kernel(kernel_Grad_R1)
    combined_kernel.append_kernel(kernel_Grad_R2)
    combined_kernel.append_kernel(kernel_Grad_R4)
    combined_kernel.append_kernel(kernel_Dir_R1_X)
    combined_kernel.append_kernel(kernel_Dir_R2_X)
    combined_kernel.append_kernel(kernel_Dir_R4_X)
    combined_kernel.append_kernel(kernel_Dir_R1_Y)
    combined_kernel.append_kernel(kernel_Dir_R2_Y)
    combined_kernel.append_kernel(kernel_Dir_R4_Y)
    combined_kernel.append_kernel(kernel_Dog_R2_R1)
    combined_kernel.append_kernel(kernel_Dog_R4_R2)
    combined_kernel.append_kernel(kernel_Dog_R8_R6)
    combined_kernel.append_kernel(kernel_X_Y)

    return combined_kernel

def reshapeData():
    features_train = shogun.RealFeatures(train_data)
    features_test  = shogun.RealFeatures(test_data)
    features_train_label = shogun.RegressionLabels(train_label)
    features_test_label = shogun.RegressionLabels(test_label)
    return features_train,features_test,features_train_label,features_test_label

def trainData():
    return
train_data = np.array([[1,2,3],[1.1,2.1,3.1]],dtype=float)
train_data1 = shogun.RealFeatures(np.array([[1.2,2.2,3.2],[1.3,2.3,3.3],[1.4,2.4,3.4]],dtype=float))
train_label = np.array([1,2,3],dtype=float)
test_data = np.array([[2,3,4],[2.1,3.1,4.1]],dtype=float)
test_label = np.array([2,3,4],dtype=float)
traindata,testdata,traindatalabel,testdatalabel = reshapeData()
kernel_Dog_1 = shogun.GaussianKernel(traindata,traindata,float(0.5))
kernel_Grad_1 = shogun.GaussianKernel(train_data1,train_data1,float(1))
combin_feature = shogun.CombinedFeatures()
combin_feature.append_feature_obj(traindata)
combin_feature.append_feature_obj(train_data1)


combin_kernel = shogun.CombinedKernel()
combin_kernel.append_kernel(kernel_Dog_1)
combin_kernel.append_kernel(kernel_Grad_1)
combin_kernel.init(combin_feature,combin_feature)

binary_svm_solver = shogun.SVRLight()
mkl = shogun.MKLRegression(binary_svm_solver)
mkl.set_kernel(combin_kernel)
mkl.set_labels(traindatalabel)
# mkl.set_C(1, 1)
mkl.set_mkl_norm(1)
mkl.train()
beta = combin_kernel.get_subkernel_weights()
alpha = mkl.get_alphas()
combin_kernel.init(testdata, testdata)
labels_predict = mkl.apply_regression()
b = labels_predict.get_labels()




