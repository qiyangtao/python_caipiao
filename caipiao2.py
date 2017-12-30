# -*- coding: utf-8 -*-
import urllib2
import requests
import re
import json
import time
import gc

def bingo(pre,now,city,list):
    if pre > 34:
        if now < 23:
            string = ('中！')+ city + ('总和：') + str(now) + ':' + str(list)
            pre = 23
            return [string, pre]
        else:
            string = ('没中！')+ city + ('总和：') + str(now) + ':' + str(list)
            return [string,pre]
    elif pre < 11:
        if now > 22:
            string = ('中！')+ city + ('总和：') + str(now) + ':' + str(list)
            pre = 23
            return [string, pre]
        else:
            string = ('没中！')+ city + ('总和：') + str(now) + ':' + str(list)
            return [string, pre]

def chongqing(cqtol):
    city = '重庆'
    url = 'http://www.cqcp.net/game/ssc/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    try:
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
            string = city + ('总和：') + str(total) + ':' + str(list_cq)
            return [string,total]
        elif cqtol > 34 or cqtol < 11:
            result = bingo(cqtol,total,city,list_cq)
            return result
        else:
            return [None,total]
    except urllib2.HTTPError:
        return ('cq网络请求错误')


def tianjin(tjtol):
    city = '天津'
    url = 'https://shishicai.cjcp.com.cn/tianjin/kaijiang/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    try:
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
            string = city + ('总和：') + str(total) + ':' + str(list_tj)
            return [string,total]
        elif tjtol > 34 or tjtol < 11:
            result = bingo(tjtol,total,city,list_tj)
            return result
        else:
            return [None,total]
    except urllib2.HTTPError:
        return ('tj网络请求错误')

def xinjiang(xjtol):
    city = '新疆'
    url = 'https://shishicai.cjcp.com.cn/xinjiang/kaijiang/'
    header_link = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' +
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
    try:
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
            string = city + ('总和：') + str(total) + ':' + str(list_xj)
            return [string,total]
        elif xjtol > 34 or xjtol < 11:
            result = bingo(xjtol,total,city,list_xj)
            return result
        else:
            return [None,total]
    except urllib2.HTTPError:
        return ('xj网络请求错误')


def beijing(bjtol):
    # url1 = 'http://apicg011.ddplayers.com/api/public/LotteryTrend'
    # params1 = {
    #     'GID':15,
    #     'Count':1
    # }
    city = '北京'
    url2 = 'http://apicg011.ddplayers.com/api/public/getResultPrev'
    params2 = {
       'gid':15,
       'period':999999
    }
    try:
        request = requests.get(url2, params2)
        r_js2 = request.json()
        list_bj = (r_js2['data']['pr'][0]['r'])
        total = 0
        for i in range(0,5):
            total = total + int(list_bj[i])
        if total > 34 or total < 11:
            string = city + ('总和：') + str(total) + ':' + str(list_bj)
            return [string,total]
        elif bjtol > 34 or bjtol < 11:
            result = bingo(bjtol,total,city,list_bj)
            return result
        else:
            return [None,total]
    except requests.HTTPError:
        return ('bj网络请求错误')
    except KeyError:
        pass

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
    cqtol = 23
    tjtol = 23
    xjtol = 23
    bjtol = 23
    print ('program is starting...')
    while 1:
        bj = (beijing(bjtol))
        bjtol = bj[1]
        bjtext = str(bj[0])
        cq = (chongqing(cqtol))
        cqtext = str(cq[0])
        cqtol = cq[1]
        tj = (tianjin(tjtol))
        tjtext = str(tj[0])
        tjtol = tj[1]
        xj = (xinjiang(xjtol))
        xjtext = str(xj[0])
        xjtol = xj[1]
        if cqtext != 'None' or tjtext != 'None' or xjtext != 'None' or bjtext != 'None':
            data = cqtext + '\n' + tjtext + '\n' + xjtext  + '\n' + bjtext
            sender(data)
        gc.collect()
        time.sleep(200)
