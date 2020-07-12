# beat fake

## 简介
本资源为[Deepfake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge)比赛代码。目前比赛已结束，现将代码公开。  

该代码是我们的方案一思路：利用dlib开源库定位人脸的关键点，利用这些关键点构造特征，最终放入XGBoost分类器预测视频的真假。

特征介绍(部分)：  
• 面部的色度:找到一个凸包，在已有边界的基础上再往上拓展 0.5 个已有的极差。先算每一张脸的均值，再算视频中均值的标准差  
• 面部色度差异性:max(每张脸的色度的标准差)  
• 眼皮的色度与脸部的色度差的标准差:找到一个矩形包住眼球，再将上边界往上 1/4 个眼
球的上下差，算出去眼球区域的像素-脸部的像素均值，再求标准差  
• 眼球中心到眉毛中心:找到眼睛中心点(外接矩形中心点)，往上做竖直的线条，取穿过眉毛区域时两个交点的中点，算这个距离的标准差   
• 鼻梁和眉毛夹角标准差  
• 嘴唇颜色变化  
• ...

## 环境
直接在根目录下，
```{bash}
pip install -r requirements.txt
```
或者查看requirements.txt中所需的包，自行安装自己所需。如果速度太慢，可使用清华镜像，使用方法：
```{bash}
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxx # xxx是你所需要安装的包
```
如果安装dlib报错，请先
```{bash}
pip install cmake
```

## 使用
demo文件夹包含有特征工程脚本(feature_service.ipynb)+xgboost分类器(classifier_xgboost.ipynb)

## 训练
如果需要重新训练关键点参数，请参考tools/train_shape_predictor.py，脚本中训练流程已注明。

## 数据
脸部关键点定位文件下载链接 [shape_predictor_194_face_landmarks.dat](https://www.dropbox.com/sh/t5h024w0xkedq0j/AABS3GprqIvb_PwqeHOn2dxNa?dl=0)  
官网链接：https://www.kaggle.com/c/deepfake-detection-challenge/data


#### 

