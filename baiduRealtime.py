from urllib.request import urlopen,Request
from fake_useragent import UserAgent
import re

class baiduRealtimeScraper:
    def __init__(self):
        self.url = 'https://top.baidu.com/board?tab=realtime'
        self.headers = {'User-Agent': UserAgent().random}

    def grasp(self):
        req = Request(url = self.url, headers = self.headers)
        self.html = urlopen(req).read().decode()

    def parse(self):
        pattern1 = re.compile('"desc":"(.*?)","hotChange":"same","hotScore":"\d+"',re.S)
        pattern2 = re.compile('"query":"(.*?)","rawUrl"',re.S)
        self.messageList = pattern1.findall(self.html)
        self.titleList = pattern2.findall(self.html)

    def display(self):
        div = '-----------------------------------------------------------'
        for i in range(len(self.titleList)-1):
            message = self.messageList[i]
            print(i+1, end = ': '+self.titleList[i]+'\n')
            if(len(message) != 0):
                print('\t|--'+message)
            else:
                print()
            print(div)

    def work(self):
        self.grasp()
        self.parse()
        self.display()

if __name__ == '__main__':
    spider = spider_baiduRealtime()
    spider.work()


