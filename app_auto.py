# 需要多订阅使得每天有6篇以上的当日文章，文章选取是在订阅模块
# 订阅不会更新很早，建议在下午或者晚上刷
# d.click()里面位置虽然是百分比，但是不同的手机位置可能还是有区别的，需要自己调试“返回”等在哪
# “.......................”表示该行需要根据具体手机做调整
# swipe的x，y轴的值可能需要修改（手机屏幕小于5寸），也可能不需要修改（屏幕较大）
import time
import datetime
import random
import uiautomator2 as u2

# 让时间有个范围
def rand(x):
    return x*random.randint(90,110)/100  
    
class auto_app():
    # 今天，昨天
    def __init__(self):
        today = datetime.datetime.today().date()
        self.date_now = str(today)
        self.date_yesterday = str(today-datetime.timedelta(days=1))
        self.x1=800 # swipe的x轴值
    # 点击返回
    def back(self):
        d.click(0.073, 0.073) # 阅读后返回.......................
        time.sleep(rand(2))         
    # 看文章（订阅）
    # 文章阅读方式
    def read(self,list,times): # 阅读driver链接列表，阅读时间10*(time+1)秒
        for i in list:
            i.click()
            time.sleep(rand(10))
            for j in range(0,times):
                d.swipe(rand(self.x1),rand(1000),rand(self.x1),rand(700)) # swipe移动,向下滑
                time.sleep(rand(10))
            self.back()    
    # 收藏转发评论
    def mix(self,mix_article):
        for i in mix_article:
            # 由于模式固定，就直接简单的点点点
            i.click()
            time.sleep(rand(3))
            d.click(0.773, 0.924) # 底下收藏符号.......................
            time.sleep(rand(1))
            d.click(0.913, 0.924) # 分享.......................
            d(textContains="分享到学习").click(timeout=4)
            time.sleep(rand(1))
            d(text="学习交流群").click(timeout=4)
            time.sleep(rand(1))
            d(text="发送").click(timeout=4)
            time.sleep(rand(2))
            d.click(0.316, 0.93) # 评论.......................
            time.sleep(rand(1.5))
            d.send_keys("努力学习，")
            d.send_keys("爱国强国，振兴祖国")
            d(text="发布").click(timeout=4)
            time.sleep(rand(2))
            self.back()    
    # 获取链接
    def article(self):
        time.sleep(rand(3))
        d.click(0.934, 0.137) # 右上角的那几杠.......................
        time.sleep(1)
        d.xpath("//*[@text='订阅']").click()
        time.sleep(rand(1))
        d.xpath("//*[@text='订阅']").click()
        time.sleep(rand(2))
        articlelist1=d.xpath("//*[@text='%s']" % self.date_now).all() # 跟selenium有所不同
        print("阅读文章：",len(articlelist1))
        mix_article=articlelist1[0:2]
        self.mix(mix_article=mix_article)
        self.read(articlelist1,11) # 阅读
        time.sleep(rand(2))
        [d.swipe(rand(self.x1),rand(1000),rand(self.x1),rand(400)) for x in range(3)]
        articlelist0=d.xpath("//*[@text='%s']" % self.date_now).all()
        print("阅读文章：",len(articlelist0[-(6-len(articlelist1)):]))
        self.read(set(articlelist0[-(6-len(articlelist1)):]),11)
        time.sleep(rand(2))       
    # 看视频 (联播频道)
    # 视频观看方式
    def watch(self,list,times1): # time*10秒       
        for i in list:          
            i.click()
            time.sleep(rand(10))
            k=0
            while (not d.xpath("//*[@text='重新播放']").exists): # 不出现“重新播放”，持续观看
                k=k+1
                time.sleep(rand(10))
                if k>times1: # 大于time*10s，停止观看
                    break
            self.back()
    # 获取链接        
    def video(self):
        time.sleep(rand(2))
        d.xpath("//*[@text='电视台']").click()
        time.sleep(rand(2))
        d.xpath("//*[@text='联播频道']").click()
        time.sleep(rand(5))
        videolist0=d.xpath("//*[@text='%s']" % self.date_yesterday).all()
        print("观看视频：",len(videolist0))
        self.watch(videolist0,45)
        time.sleep(rand(2))
        [d.swipe(rand(self.x1),rand(1000),rand(self.x1),rand(460)) for x in range(2)] # 能够获取更多的driver
        time.sleep(rand(1))
        videolist=d.xpath("//*[@text='%s']" % self.date_yesterday).all() # 跟selenium有所不同
        print("观看视频：",len(videolist[-(6-len(videolist0)):]))
        self.watch(set(videolist[-(6-len(videolist0)):]),36)
          
if __name__ == "__main__":
    A=True; B=False
    # d=u2.connect('192.168.31***:89**') # wifi连接
    # 端口可以连接usb时在cmd中设置 adb tcpip 5566 
    # wifi连接不上时，可以先连接usb启动
    d=u2.connect('872QEDU82***') # 手机名字.......................
    read=auto_app()
    beign = datetime.datetime.today()
    if B:
        d.app_start('com.kuaishou.nebula') # 快手极速版
        while(True):
            time.sleep(rand(5))        
            d.swipe(rand(800),rand(600),rand(800),rand(200))
    if A:
        d.app_start('cn.xuexi.android') # 学习强国
        time.sleep(rand(2))
        d.click(0.934, 0.137) # 右上角的那几杠.......................
        time.sleep(2)
        d.xpath("//*[@text='北京']").click() # 本地频道，不同地区会所有不同.......................
        time.sleep(rand(1))
        d(text="北京学习平台").click(timeout=3) # 本地频道，不同地区会所有不同.......................
        time.sleep(rand(2))
        read.back()       
        read.article()
        read.video()
    print(datetime.datetime.today()-beign)
