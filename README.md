# beat fake

本资源暂时供团队打比赛[deep fake](https://www.kaggle.com/c/deepfake-detection-challenge)使用。

## 安装：
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
## 文件目录：
tools 放置训练代码  
demo 放置baseline代码  
data 放置样例视频文件和训练好的数据文件(目前只放了两个视频)  

#### 训练数据文件下载链接[shape_predictor_194_face_landmarks.dat](https://www.dropbox.com/sh/t5h024w0xkedq0j/AABS3GprqIvb_PwqeHOn2dxNa?dl=0)
#### git提交时一律不要提交视频文件和数据文件，只能提交代码
