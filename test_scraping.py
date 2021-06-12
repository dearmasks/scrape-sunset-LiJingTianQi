# -*- coding: utf-8 -*-
# import requests
# import datetime

def get_LiJingTianQi_info_url():
    '''
    url: 是用Charles软件抓包得到的莉景天气小程序首页的链接，所有信息在该url抓取
    '''
    # return url
    pass


def scrape_info(url):
    '''
    info_dict: 是爬取url后，返回的字典，包含了天气、晚霞的信息(概率、质量、时间等)
    '''
    # return info_dict
    pass


def notification(info_dict):
    pass
    

def caidai():
    '''
    如果这一天是农历十五，并且这个代码保持在运行的话，不管是否有晚霞的通知，
    python里（和邮件里）都会收到该彩蛋，可以根据彩蛋的提示来回复，
    既可以在python里输入回复的文字，或者回复该邮件(邮件功能暂未支持)，
    有惊喜2333
    '''
    while True:
        answer = input('今晚有月光嘛？  请文字输入回答：')
        if '有' in answer and '没' not in answer:
            print('今晚月色真美~')
            break
        elif '没有' in answer:
            print('街灯亮起来也像月亮~在一条微博的p4，你发现了嘛？~')
            break
        elif '今晚月色真美' in answer or '月は綺麗ですね' in answer or 'が' in answer:
            print('我顺手打开另一罐啤酒，说微醺的酒意和涨落的潮汐才是 夏天')
            print('搞不好树丛里有只调皮的黑猫2333')
            break
        else:
            print('至少需要回答“有”，或者“没有”！再输入一次吧')


if __name__ == '__main__':
    caidai()


