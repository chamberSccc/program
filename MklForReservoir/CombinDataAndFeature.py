# -*- coding: utf-8 -*-
from DataProcess import *
from CalcOperator import MyGaussianBlur

r=1 #模版半径，自己自由调整
LapOpeator = np.array([[0,1,0],[1,-4,1],[0,1,0]])#laplace 算子
sobelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])#方向导数暂用sobel算子
sobelY = np.array([[1,2,1],[0,0,0],[-1,-2,1]])

#构造17种特征数据    返回特征矩阵列表
#1：DOG R2和R1  R4和R2  R8和R6
#2：Grad R1 R2 R4
#3：Dir Y1 Y2 Y4 X1 X2 X4
#4 Smooth R1 R2 R4
def generateFeatureMat(attribute):
    GBlur_R1 = MyGaussianBlur(radius=1, sigma=1.0)  # 声明高斯模糊类
    GBlur_R2 = MyGaussianBlur(radius=2, sigma=1.0)
    GBlur_R4 = MyGaussianBlur(radius=3, sigma=1.0)
    GBlur_R6 = MyGaussianBlur(radius=4, sigma=1.0)
    GBlur_R8 = MyGaussianBlur(radius=5, sigma=1.0)
    R1_Template = GBlur_R1.GaussKernelMat()  # 得到滤波模版
    R2_Template = GBlur_R2.GaussKernelMat()
    R4_Template = GBlur_R4.GaussKernelMat()
    R6_Template = GBlur_R6.GaussKernelMat()

    Gaus_R1 = GBlur_R1.Convolute(attribute, R1_Template)  # 15种特征,高斯模糊
    Gaus_R2 = GBlur_R2.Convolute(attribute, R2_Template)
    Gaus_R4 = GBlur_R4.Convolute(attribute, R4_Template)
    Gaus_R6 = GBlur_R6.Convolute(attribute, R6_Template)
    Grad_R1 = GBlur_R1.Convolute(Gaus_R1, LapOpeator)  # Gradient Norm
    Grad_R2 = GBlur_R2.Convolute(Gaus_R2, LapOpeator)
    Grad_R4 = GBlur_R4.Convolute(Gaus_R4, LapOpeator)
    Dir_X_R1 = GBlur_R1.Convolute(Gaus_R1, sobelX)  # Directional derivative
    Dir_X_R2 = GBlur_R2.Convolute(Gaus_R2, sobelX)
    Dir_X_R4 = GBlur_R4.Convolute(Gaus_R4, sobelX)
    Dir_Y_R1 = GBlur_R1.Convolute(Gaus_R1, sobelY)
    Dir_Y_R2 = GBlur_R2.Convolute(Gaus_R2, sobelY)
    Dir_Y_R4 = GBlur_R4.Convolute(Gaus_R4, sobelY)
    Dog_R2_R1 = GBlur_R1.diffOfGauus(Gaus_R1, Gaus_R2)  # DOG
    Dog_R4_R2 = GBlur_R1.diffOfGauus(Gaus_R2, Gaus_R4)
    Dog_R6_R4 = GBlur_R1.diffOfGauus(Gaus_R4, Gaus_R6)
    # index1 = np.where(Dog_R2_R1 < -100)
    # index2 = np.where(Dog_R4_R2 < -20)
    # index3 = np.where(Dog_R8_R6 < -1.5)
    # Dog_R2_R1[index1] = 0
    # Dog_R4_R2[index2] = 0
    # Dog_R8_R6[index3] = 0
    featureList = [Gaus_R1, Gaus_R2, Gaus_R4,Grad_R1, Grad_R2, Grad_R4,
                   Dir_X_R1, Dir_X_R2, Dir_X_R4, Dir_Y_R1, Dir_Y_R2, Dir_Y_R4,
                   Dog_R2_R1, Dog_R4_R2, Dog_R6_R4]
    return featureList

# 将测井数据与地震数据转换为训练数据格式，方便加入15种特征
def combinDataAndFeature(seisDataList, wellLogList, featureMatList,porosityList):
    seisTrainData = getSeisTrainData(seisDataList, featureMatList)
    #数据中如果波阻抗的数据为0,则删除改行数据
    # seisTrainData,index = delZeroData(seisTrainData, 4)
    npPorosityList = np.array(porosityList)
    npPorosityList = npPorosityList[:,3]
    return seisTrainData,npPorosityList

#返回测井训练数据列表,地震测试数据列表 按照15种特征顺序
def detailFeature(seistrain):
    # Well_X_Y_Data_temp = np.array(wellTrain[:, 0:2])  # 测井(训练用)的16种特征
    # Well_X_Y_Data = np.transpose(Well_X_Y_Data_temp)
    # Well_Gaus_R1_Feature = np.array(wellTrain[:, 6])
    # Well_Gaus_R2_Feature = np.array(wellTrain[:, 7])
    # Well_Gaus_R4_Feature = np.array(wellTrain[:, 8])
    # Well_Grad_R1_Feature = np.array(wellTrain[:, 9])
    # Well_Grad_R2_Feature = np.array(wellTrain[:, 10])
    # Well_Grad_R4_Feature = np.array(wellTrain[:, 11])
    # Well_Dir_X_R1_Feature = np.array(wellTrain[:, 12])
    # Well_Dir_X_R2_Feature = np.array(wellTrain[:, 13])
    # Well_Dir_X_R4_Feature = np.array(wellTrain[:, 14])
    # Well_Dir_Y_R1_Feature = np.array(wellTrain[:, 15])
    # Well_Dir_Y_R2_Feature = np.array(wellTrain[:, 16])
    # Well_Dir_Y_R4_Feature = np.array(wellTrain[:, 17])
    # Well_Dog_R2_R1_Feature = np.array(wellTrain[:, 18])
    # Well_Dog_R4_R2_Feature = np.array(wellTrain[:, 19])
    # Well_Dog_R8_R6_Feature = np.array(wellTrain[:, 20])
    # wellFeatureList = [Well_X_Y_Data, Well_Gaus_R1_Feature, Well_Gaus_R2_Feature, Well_Gaus_R4_Feature,
    #                    Well_Grad_R1_Feature, Well_Grad_R2_Feature, Well_Grad_R4_Feature,
    #                    Well_Dir_X_R1_Feature, Well_Dir_X_R2_Feature, Well_Dir_X_R4_Feature,
    #                    Well_Dir_Y_R1_Feature, Well_Dir_Y_R2_Feature, Well_Dir_Y_R4_Feature,
    #                    Well_Dog_R2_R1_Feature, Well_Dog_R4_R2_Feature, Well_Dog_R8_R6_Feature]

    Seis_X_Data_temp = np.array(seistrain[:, 0])  # 地震数据(测试用)的16种特征
    # Seis_X_Y_Data = np.transpose(Seis_X_Y_Data_temp)
    Seis_Y_Data_temp = np.array(seistrain[:, 1])  # 地震数据(测试用)的16种特征
    Seis_Gaus_R1_Feature = np.array(seistrain[:, 4])
    Seis_Gaus_R2_Feature = np.array(seistrain[:, 5])
    Seis_Gaus_R4_Feature = np.array(seistrain[:, 6])
    Seis_Grad_R1_Feature = np.array(seistrain[:, 7])
    Seis_Grad_R2_Feature = np.array(seistrain[:, 8])
    Seis_Grad_R4_Feature = np.array(seistrain[:, 9])
    Seis_Dir_X_R1_Feature = np.array(seistrain[:, 10])
    Seis_Dir_X_R2_Feature = np.array(seistrain[:, 11])
    Seis_Dir_X_R4_Feature = np.array(seistrain[:, 12])
    Seis_Dir_Y_R1_Feature = np.array(seistrain[:, 13])
    Seis_Dir_Y_R2_Feature = np.array(seistrain[:, 14])
    Seis_Dir_Y_R4_Feature = np.array(seistrain[:, 16])
    Seis_Dog_R2_R1_Feature = np.array(seistrain[:, 16])
    Seis_Dog_R4_R2_Feature = np.array(seistrain[:, 17])
    Seis_Dog_R8_R6_Feature = np.array(seistrain[:, 18])
    seisFeatureList = [Seis_X_Data_temp,Seis_Y_Data_temp,
                       Seis_Grad_R1_Feature,
                       Seis_Grad_R2_Feature,
                       Seis_Grad_R4_Feature,
                       Seis_Dir_X_R1_Feature,
                       Seis_Dir_X_R2_Feature,
                       Seis_Dir_X_R4_Feature,
                       Seis_Dir_Y_R1_Feature,
                       Seis_Dir_Y_R2_Feature,
                       Seis_Dir_Y_R4_Feature,
                       Seis_Dog_R2_R1_Feature,
                       Seis_Dog_R4_R2_Feature,
                       Seis_Dog_R8_R6_Feature
    ]
    return seisFeatureList
