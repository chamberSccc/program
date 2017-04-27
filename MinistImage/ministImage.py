#coding=utf-8
import numpy as np
from os import listdir
import operator
import time
import struct
from PIL import Image
import matplotlib.pyplot as plt
from sklearn import svm
import traceback


train_data_path = "D:\\pythonProject\\MinistImage\\file\\train"
test_data_path  = "D:\\pythonProject\\MinistImage\\file\\test"
train_label_path = "D:\\pythonProject\\MinistImage\\file\\train_label\\label.txt"
test_label_path = "D:\\pythonProject\\MinistImage\\file\\test_label\\label.txt"

#参数：imgFile--图像名  如：0.png
def showImg(file):
    filename = 'train-images.idx3-ubyte'
    binfile = open(filename, 'rb')
    buf = binfile.read()
    binfile.close()
    index = 0
    magic, numImages, numRows, numColumns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')
    im = struct.unpack_from('>784B', buf, index)
    index += struct.calcsize('>784B')

    im = np.array(im)
    im = im.reshape(28, 28)

    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im, cmap='gray')
    plt.show()

# 将每个28px * 28px 的图像数据转换成 1*784 的 numpy 向量
# 参数：imgFile--图像名  如：0.png
# 返回：1*784 的 numpy 向量
def img2Vector(imgFilePath):
    img =Image.open(imgFilePath)
    img_arr = np.array(img)#灰度图像
    temp = np.round(img_arr/255.0)
    img_normlization = np.round(temp)  # 归一化 这样两部处理才能四舍五入
    img_arr2 = np.reshape(img_arr, (1, -1))  # 1 * 784 向量
    return img_arr2

# 读取一个类别的所有数据并转换成矩阵
# 返回：某一类别的所有数据----[样本数量*(图像宽x图像高)] 矩阵和标签向量
def read_and_convert(train_list,test_list):
    train_dataLabel,test_dataLabel = [],[]
    train_dataNum = len(train_list)
    test_dataNum = len(test_list)
    # train_dataMat = np.zeros((train_dataNum, 784))
    # test_dataMat  = np.zeros((test_dataNum, 784))

    train_dataMat = np.zeros((5000, 784))
    test_dataMat  = np.zeros((2000, 784))
    #图片矩阵
    #for i in range(train_dataNum):
    for i in range(5000):
        train_imgNameStr = train_list[i]
        imgName = get_img_name_str(train_imgNameStr)  # 得到 数字_实例编号.png
        classTag = train_tagarr[i]
        train_dataLabel.append(classTag)
        train_dataMat[i, :] = img2Vector(train_data_path+"\\"+train_imgNameStr)
    #标签数组
    #for i in range(test_dataNum):
    for i in range(2000):
        test_imgNameStr = test_list[i]
        imgName = get_img_name_str(test_imgNameStr)
        classTag = test_tagarr[i] # 得到 类标签(数字)
        test_dataLabel.append(classTag)
        test_dataMat[i, :] = img2Vector(test_data_path+"\\"+test_imgNameStr)
    return train_dataMat, train_dataLabel, test_dataMat, test_dataLabel

# 读取训练数据
def read_all_data():
    flist = get_file_list(train_data_path)
    tlist = get_file_list(test_data_path)
    train_dataMat, train_dataLabel,test_dataMat, test_dataLabel = read_and_convert(flist,tlist)
    print(train_dataMat.shape)
    print(len(train_dataLabel))
    return train_dataMat, train_dataLabel, test_dataMat, test_dataLabel

def get_img_name_str(imgName):
    return imgName.split(".")[0]
#得到文件列表
def get_file_list(dataPath):
    return listdir(dataPath)
def get_img_tagarr(label_path):
    labelfile = open(label_path, 'r')
    labelbuf = labelfile.read()
    labelfile.close()
    return  labelbuf.split(",")

def creat_svm(dataMat,dataLabel,decision='ovr'):
    # clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    # decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    # max_iter=-1, probability=False, random_state=None, shrinking=True,
    #  tol=0.001, verbose=False)
    try:
        clf = svm.SVC(decision_function_shape=decision)
        clf.fit(dataMat, dataLabel)
    except Exception, e:
        print e.message
        print traceback.format_exc()
    return clf

if __name__ == '__main__':
    global train_tagarr,test_tagarr
    train_tagarr = get_img_tagarr(train_label_path)
    test_tagarr = get_img_tagarr(test_label_path)
    train_dataMat, train_dataLabel, test_dataMat, test_dataLabel = read_all_data()
    #对测试集进行测试
    tst = time.clock()

    allErrRate  = 0.0
    allScore = 0
    tfile = get_file_list(test_data_path)
    print("测试矩阵大小为: {0}, 测试标签长度为: {1} ".format(test_dataMat.shape, len(test_dataLabel)))
    start = time.clock()
    clf = creat_svm(train_dataMat, train_dataLabel)
    preResult = clf.predict(test_dataMat)
    end = time.clock()
    #allErrcount = (x for x in preResult for t in test_dataLabel if x != t)
    print("预测耗时为: {0}".format(end-start))
    print("---------------------------------------------------------")
    score = clf.score(test_dataMat, test_dataLabel)
    #print("错误个数为: {}.".format(allErrcount))
    print("正确率为: {:.6f}.".format(score))
    print("错误率为 {:.6f}.".format((1 - score)))










