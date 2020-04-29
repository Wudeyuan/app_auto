# app_auto
 app自动化，本代码是在真机上进行测试，测试的学习强国app和快手极速版。注意在测试前**先登录**app，并保持在**主页面**，本代码没有进行模拟登录。

## 配置
1. 安装anoconda,安装uiautomator2和weditor两个python包
2. 安装Android Studio,也可以只安装Android SDK然后配置环境

## CMD连接
1. 输入`adb devices`查看是否连接上，连接上可获取手机名字
2. 连接手机后，输入`python -m uiautomator2 init`对手机进行初始化
3. 输入`python -m weditor`打开网页，输入（1）中获取的手机名进行连接，然后可逐步调试，**可视化界面**做得非常好。

## python程序（[auto.py](https://github.com/Wudeyuan/app_auto/blob/master/app_auto.py)）
#### 学习强国移动应用程序，刷文章和视频阅读（共24分）。代码包括一个函数和一个类。全程大约38分钟，可获得23-24分。
- `rand()`函数。在手机运行过程中，暂停（time.sleep）非常重要，`rand()`是为了让暂停时间长短稍显不同而设计（^-^其实就是让软件商更难监测，可能没啥用）。
- `auto_app()`类，包含4个函数
1. `read()`函数：文章阅读方式，首先循环遍历每个文章链接，然后滑动阅读，每次滑动暂停10s左右，每篇阅读110s左右。
2. `article()`函数：获取文章链接，在文章更新最快的“综合”里面寻找文章，首先滑屏跳过比较重要的文章（一般不怎么新），然后根据日期定位今天的文章，`read()`完成以后，下滑再定位今天和昨天的文章，再阅读。
3. `watch()`函数：看视频方式，先遍历视频链接，每个视频根据是否出现“重新播放”来确定是否放完，对于新闻联播，最多播放450s(time1=45)，对于其它较长的视频，最多播放360s(time1=36).
4. `video()`函数：获取视频链接，在电视台中的联播频道中获取视频，观看后滑屏再观看。
#### 快手短视频移动应用程序，每过10s左右上滑，比较简单。
