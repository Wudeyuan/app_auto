# app_auto
 - [x] app自动化，本代码是在真机上进行测试，测试的学习强国app和快手极速版。注意在测试前先登录app，并保证从桌面进入app时能在主页面，因为本代码没有进行模拟登录。
 - [x] 除答题和订阅部分，其余分值均可获得。由于供自己使用，只适配了本机的屏幕大小，其它手机可能需要调整`click()`里面的位置
 - [x] "\*"号表示仅作了解。

## 配置
1. 安装anoconda,安装<kbd>uiautomator2</kbd>和<kbd>weditor</kbd>两个python包
2. 安装Android Studio,也可以只安装SDK Platform Tools然后配置系统环境。<kbd>cmd</kbd>中输入adb不出错即可

## CMD初始化
1. usb连接手机（开发模式）后，输入<kbd>adb devices</kbd>查看是否连接上，连接上可获取手机名字
2. 连接手机后，输入<kbd>python -m uiautomator2 init</kbd>对手机进行初始化
3. 输入<kbd>python -m weditor</kbd>打开网页，输入（1）中获取的手机名进行连接，然后可逐步调试，可视化界面做得非常好。

## Python程序（[auto.py](https://github.com/Wudeyuan/app_auto/blob/master/app_auto.py)）
#### 学习强国移动应用程序，文章和视频阅读（共24分）以及最后5分。代码包括一个函数和一个类。代码运行全程大约33分钟，可获得29-30分（余下答题和订阅部分）。
- `rand()`函数。在手机运行过程中，暂停（`time.sleep()`）非常重要，`rand()`是为了让暂停时间长短稍显不同而设计（^-^其实就是让软件商更难监测，可能没啥用）。
- `auto_app()`类，包含5个函数
1. `read()`函数：文章阅读方式，首先循环遍历每个文章链接，然后滑动阅读，每次滑动暂停10s左右，每篇阅读110s左右。
2. `article()`函数：获取文章链接，在文章格式比较固定以及更新很快的“订阅”里面寻找6篇今天的文章，阅读完当前页面的文章后，下滑再定位今天的文章，再阅读。
3. `watch()`函数：看视频方式，先遍历视频链接，每个视频根据是否出现“重新播放”来确定是否放完，对于新闻联播，最多播放450s(time1=45)，对于其它较长的视频，最多播放360s(time1=36).
4. `video()`函数：获取视频链接，在电视台中的“联播频道”中获取6个昨天的视频，观看后滑屏再观看。
5. `mix()`函数：收藏转发评论前两篇文章。
6. `back()`函数：返回。
#### 快手短视频移动应用程序，每过10s左右上滑，比较简单。
  
  
## 配置\*（仅做了解）
网上也有不少用appium来调试，这里做简单的介绍。
#### 案例：用夜神模拟器打开学习强国（已登录）
- 配置
1. 安装jdk，配置环境变量
2. 安装anoconda，安装<kbd>Appium-Python-Client</kbd>包
3. 安装Android Studio，配置环境变量（<kbd>ANDROID_HOME</kbd>和<kbd>Path</kbd>（...Sdk\platform-tools））
4. 安装Appium
5. 安装夜神模拟器，并用Android Studio里的<kbd>adb.exe</kbd>替换夜神的<kbd>nox_adb.exe</kbd>并更名（避免版本不兼容），安装学习强国
6. 网上说还要安装node.js，没有安装也能跑，就没安装了
- 连接
1. 夜神运行app后，cmd输入<kbd>adb devices</kbd>连接获取手机名字
2. 打开需要测试的app，cmd输入<kbd>adb shell dumpsys activity activities | grep mFocusedActivity</kbd>，获取当前Activity
3. 打开appium软件，填写主机地址，端口不变，点击放大镜，配置后可以对app进行调试。配置如下：
```
{
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62025",
  "appPackage": "cn.xuexi.android",
  "appActivity": "com.alibaba.android.rimet.biz.home.activity.HomeActivity",
  "automationName": "UiAutomator1",
  "noReset": "true",
  "newCommandTimeout":"600"
}
```
4. <kbd>noReset</kbd>表示不要重置，登录后调试app时可以不用再登陆。<kbd>automationName</kbd>，网上教程很多没有这一项，但是不加这一项程序会报错，没有找到合适的解决办法，因此加上了（这一项会改变将默认的uiautomator2），<kbd>newCommandTimeout</kbd>表示无动作重置时间。下面代码可以启动学习强国
```
# 需要保持appium服务在运行
from appium import webdriver
caps = {} # (3)中的内容
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
# 接下来进行xpath定位，driver.tap点击和driver.swipe滑动
```
