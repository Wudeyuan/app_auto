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
    # 看文章
    # 文章阅读方式
    def read(self,list,times): # 阅读driver链接列表，阅读时间10*(time+1)秒
        for i in list:
            i.click()
            time.sleep(rand(10))
            for j in range(0,times):
                x1 = rand(800)
                d.swipe(x1,rand(1000),x1,rand(700)) # swipe移动,向下滑
                time.sleep(rand(10))
            d.click(rand(0.073), rand(0.073)) # 阅读后返回
            time.sleep(rand(2))      
    def article(self):
        time.sleep(rand(2))
        d.xpath("//*[@text='综合']").click()
        time.sleep(rand(2))
        x1 = rand(800)
        [d.swipe(x1,rand(1000),x1,rand(400)) for x in range(3)] # 下滑，接近半屏
        time.sleep(rand(1))
        articlelist1=d.xpath("//*[@text='%s']" % self.date_now).all() # 跟selenium有所不同
        print("阅读文章：",len(articlelist1))
        self.read(articlelist1,10) # 阅读
        time.sleep(rand(2))
        d.swipe(x1,rand(1000),x1,rand(400))
        articlelist0=d.xpath("//*[@text='%s']" % self.date_now).all()
        articlelist=d.xpath("//*[@text='%s']" % self.date_yesterday).all()
        print("阅读文章：",len(articlelist0)+len(articlelist[-3:-1]))
        self.read(set(articlelist0),12) # 阅读
        self.read(set(articlelist[-3:]),12)
        time.sleep(rand(2))       
    # 看视频 (联播频道5)
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
            d.click(rand(0.073), rand(0.073)) # 返回
            time.sleep(rand(2))
    def video(self):
        time.sleep(rand(2))
        d.xpath("//*[@text='电视台']").click()
        time.sleep(rand(2))
        d.xpath("//*[@text='联播频道']").click()
        time.sleep(rand(2))
        videolist0=d.xpath("//*[@text='%s']" % self.date_yesterday).all()
        print("观看视频：",len(videolist0))
        self.watch(videolist0,45)
        time.sleep(rand(2))
        x1=rand(800)
        [d.swipe(x1,rand(1000),x1,rand(460)) for x in range(2)] # 能够获取更多的driver，说明app是不滑动不加载
        time.sleep(rand(1))
        videolist=d.xpath("//*[@text='%s']" % self.date_yesterday).all() # 跟selenium有所不同
        print("观看视频：",len(videolist[-3:]))
        self.watch(set(videolist[-3:]),36)
          
if __name__ == "__main__":
    d=u2.connect('872QEDU8****') # 根据手机而定
    read=auto_app()
    beign = datetime.datetime.today()
    if False:
        d.app_start('com.kuaishou.nebula') # 快手极速版，无限循环
        while(True):
            time.sleep(rand(15))        
            d.swipe(rand(800),rand(1000),rand(800),rand(200))
    if True:
        d.app_start('cn.xuexi.android') # 学习强国
        read.article()
        read.video()
    print(datetime.datetime.today()-beign)