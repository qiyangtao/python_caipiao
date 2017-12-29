# -*- coding: utf-8 -*-
import urllib2
import re
import json
import time
import gc


def chongqing():
    url = 'http://www.cqcp.net/game/ssc/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    request = urllib2.Request(url=url, headers=header_link)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('([0-9])-([0-9])-([0-9])-([0-9])-([0-9])')
    num = pattern.search(content)
    list_cq = num.group().split('-')
    total = 0
    for i in list_cq:
        total = total + int(i)
    if total > 34 or total < 11:
        string = ('重庆总和：') + str(total) + ':' + str(list_cq)
        return string


def tianjin():
    url = 'https://shishicai.cjcp.com.cn/tianjin/kaijiang/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    request = urllib2.Request(url=url, headers=header_link)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<div class="kjjg_hm_bg">.*?([0-9]).*<\/div>')
    num = pattern.search(content)
    nums = num.group()
    list_tj = []
    total = 0
    for i in nums:
        if i.isdigit():
            total = total + int(i)
            list_tj.append(i)
    if total > 34 or total < 11:
        string = ('天津总和：') + str(total) + ':' + str(list_tj)
        return string

def xinjiang():s
    url = 'https://shishicai.cjcp.com.cn/xinjiang/kaijiang/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    request = urllib2.Request(url=url, headers=header_link)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<div class="kjjg_hm_bg">.*?([0-9]).*<\/div>')
    num = pattern.search(content)
    nums = num.group()
    list_xj = []
    total = 0
    for i in nums:
        if i.isdigit():
            total = total + int(i)
            list_xj.append(i)
    if total > 34 or total < 11:
        string = ('新疆总和：') + str(total) + ':' + str(list_xj)
        return string


def beijing():
    url = 'http://smwap.playgamings.com/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    request = urllib2.Request(url=url, headers=header_link)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<p class="last-time last_open_5">([0-9]).*<\/p>')
    num = pattern.search(content)
    nums = num.group()
    b = []
    for i in nums:
        if i.isdigit():
            b.append(i)
    return (b[1:])

def sender(parm):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=59f0284c9b9c481799b71c35985081262fde23c91a4791609db5cdb0242da1f2'
    hearder = {
        'Content-Type':'application/json',
        'Charset':'utf-8'
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": parm
        },
        "at": {
            'atMobiles':[18502872291]
            # "isAtAll": True
        }
    }
    send_data = json.dumps(data)
    request = urllib2.Request(url, data=send_data, headers=hearder)
    urllib2.urlopen(request)

if __name__ == '__main__':
    while 1:
        cq = str(chongqing())
        tj = str(tianjin())
        xj = str(xinjiang())
        if cq != 'None' or tj != 'None' or xj != 'None':
            data = cq + '\n' + tj + '\n' + xj
            sender(data)
        gc.collect()
        time.sleep(200)
