# -*- coding: utf-8 -*-
from DataProcess import *
from CalcOperator import MyGaussianBlur

r=1 #模版半径，自己自由调整
LapOpeator = np.array([[0,1,0],[1,-4,1],[0,1,0]])#laplace 算子
sobelX = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])#方向导数暂用sobel算子
sobelY = np.array([[1,2,1],[0,0,0],[-1,-2,1]])
#解析地震数据,测井数据
wellLogList = getWellData(wellLogDataDir)
seisDataList, waveMat, seisCoord  = seisData2Mat(seisDataDir)

#构造17种特征数据    返回特征矩阵列表
#1：DOG R2和R1  R4和R2  R8和R6
#2：Grad R1 R2 R4
#3：Dir Y1 Y2 Y4 X1 X2 X4
#4 Smooth R1 R2 R4
def generateFeatureMat():
    GBlur_R1 = MyGaussianBlur(radius=r, sigma=1.0)  # 声明高斯模糊类
    GBlur_R2 = MyGaussianBlur(radius=r, sigma=2.0)
    GBlur_R4 = MyGaussianBlur(radius=r, sigma=4.0)
    GBlur_R6 = MyGaussianBlur(radius=r, sigma=6.0)
    GBlur_R8 = MyGaussianBlur(radius=r, sigma=8.0)
    R1_Template = GBlur_R1.GaussKernelMat()  # 得到滤波模版
    R2_Template = GBlur_R2.GaussKernelMat()
    R4_Template = GBlur_R4.GaussKernelMat()
    R6_Template = GBlur_R6.GaussKernelMat()
    R8_Template = GBlur_R8.GaussKernelMat()

    Gaus_R1 = GBlur_R1.Convolute(waveMat, R1_Template)  # 15种特征,高斯模糊
    Gaus_R2 = GBlur_R2.Convolute(waveMat, R2_Template)
    Gaus_R4 = GBlur_R4.Convolute(waveMat, R4_Template)
    Gaus_R6 = GBlur_R6.Convolute(waveMat, R6_Template)
    Gaus_R8 = GBlur_R8.Convolute(waveMat, R8_Template)
    Grad_R1 = GBlur_R1.Convolute(Gaus_R1, LapOpeator)  # 梯度
    Grad_R2 = GBlur_R2.Convolute(Gaus_R2, LapOpeator)
    Grad_R4 = GBlur_R4.Convolute(Gaus_R4, LapOpeator)
    Dir_X_R1 = GBlur_R1.Convolute(Gaus_R1, sobelX)  # 方向倒数
    Dir_X_R2 = GBlur_R2.Convolute(Gaus_R2, sobelX)
    Dir_X_R4 = GBlur_R4.Convolute(Gaus_R4, sobelX)
    Dir_Y_R1 = GBlur_R1.Convolute(Gaus_R1, sobelY)
    Dir_Y_R2 = GBlur_R2.Convolute(Gaus_R2, sobelY)
    Dir_Y_R4 = GBlur_R4.Convolute(Gaus_R4, sobelY)
    Dog_R2_R1 = GBlur_R1.diffOfGauus(Gaus_R1, Gaus_R2)  # 高斯差分
    Dog_R4_R2 = GBlur_R1.diffOfGauus(Gaus_R2, Gaus_R4)
    Dog_R8_R6 = GBlur_R1.diffOfGauus(Gaus_R6, Gaus_R8)
    featureList = [Gaus_R1, Gaus_R2, Gaus_R4,Grad_R1, Grad_R2, Grad_R4,
                   Dir_X_R1, Dir_X_R2, Dir_X_R4, Dir_Y_R1, Dir_Y_R2, Dir_Y_R4,
                   Dog_R2_R1, Dog_R4_R2, Dog_R8_R6]
    return featureList

# 将测井数据与地震数据转换为训练数据格式，方便加入15种特征
def combinDataAndFeature(seisDataList, wellLogList, featureMatList):
    train_seis_data = getSeisTrainData(seisDataList, featureMatList)
    seisTrainData = delZeroFromSeisTrain(train_seis_data)
    wellTrainData = getWellTrainData(train_seis_data, wellLogList)
    wellTrainData = np.delete(wellTrainData, 0, axis=1)
    wellTrainData = np.array(wellTrainData.tolist(), dtype=float)
    return wellTrainData,seisTrainData

#返回测井训练数据列表,地震测试数据列表 按照15种特征顺序
def detailFeature(wellTrain,seistrain):
    Well_X_Y_Data_temp = np.array(wellTrain[:, 0:2])  # 测井(训练用)的16种特征
    Well_X_Y_Data = np.transpose(Well_X_Y_Data_temp)
    Well_Gaus_R1_Feature = np.array(wellTrain[:, 6])
    Well_Gaus_R2_Feature = np.array(wellTrain[:, 7])
    Well_Gaus_R4_Feature = np.array(wellTrain[:, 8])
    Well_Grad_R1_Feature = np.array(wellTrain[:, 9])
    Well_Grad_R2_Feature = np.array(wellTrain[:, 10])
    Well_Grad_R4_Feature = np.array(wellTrain[:, 11])
    Well_Dir_X_R1_Feature = np.array(wellTrain[:, 12])
    Well_Dir_X_R2_Feature = np.array(wellTrain[:, 13])
    Well_Dir_X_R4_Feature = np.array(wellTrain[:, 14])
    Well_Dir_Y_R1_Feature = np.array(wellTrain[:, 15])
    Well_Dir_Y_R2_Feature = np.array(wellTrain[:, 16])
    Well_Dir_Y_R4_Feature = np.array(wellTrain[:, 17])
    Well_Dog_R2_R1_Feature = np.array(wellTrain[:, 18])
    Well_Dog_R4_R2_Feature = np.array(wellTrain[:, 19])
    Well_Dog_R8_R6_Feature = np.array(wellTrain[:, 20])
    wellFeatureList = [Well_X_Y_Data, Well_Gaus_R1_Feature, Well_Gaus_R2_Feature, Well_Gaus_R4_Feature,
                       Well_Grad_R1_Feature, Well_Grad_R2_Feature, Well_Grad_R4_Feature,
                       Well_Dir_X_R1_Feature, Well_Dir_X_R2_Feature, Well_Dir_X_R4_Feature,
                       Well_Dir_Y_R1_Feature, Well_Dir_Y_R2_Feature, Well_Dir_Y_R4_Feature,
                       Well_Dog_R2_R1_Feature, Well_Dog_R4_R2_Feature, Well_Dog_R8_R6_Feature]

    Seis_X_Y_Data_temp = np.array(seistrain[:, 0:2])  # 地震数据(测试用)的16种特征
    Seis_X_Y_Data = np.transpose(Seis_X_Y_Data_temp)
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
    seisFeatureList = [Seis_X_Y_Data, Seis_Gaus_R1_Feature, Seis_Gaus_R2_Feature, Seis_Gaus_R4_Feature,
                       Seis_Grad_R1_Feature, Seis_Grad_R2_Feature, Seis_Grad_R4_Feature,
                       Seis_Dir_X_R1_Feature, Seis_Dir_X_R2_Feature, Seis_Dir_X_R4_Feature,
                       Seis_Dir_Y_R1_Feature, Seis_Dir_Y_R2_Feature, Seis_Dir_Y_R4_Feature,
                       Seis_Dog_R2_R1_Feature, Seis_Dog_R4_R2_Feature, Seis_Dog_R8_R6_Feature]
    return wellFeatureList,seisFeatureList
