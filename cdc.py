# -*- coding: utf-8 -*-
#imports
import json
import re
import sys
import time
from wsgiref import headers
from xml.etree.ElementInclude import include
import feedparser
import requests

#檢查更新
while True:
    #設定debug print所列印之內容
    prefix = str('[INFO] [' + str(time.ctime()) + '] ') 

    #偵測1
    d = feedparser.parse('https://www.cdc.gov.tw/RSS/RssXml/Hh094B49-DRwe2RR4eFfrQ?type=1')
    rsstitle = d['entries'][0]['title']
    print(prefix + '偵測到現在的標題為: ' + rsstitle)
    #loading動畫
    animation = ["4%[□□□□□□□□□□□□□□□□□□□□□□□□□]","8%[■□□□□□□□□□□□□□□□□□□□□□□□□]","12%[■■□□□□□□□□□□□□□□□□□□□□□□□]","16%[■■■□□□□□□□□□□□□□□□□□□□□□□]","20%[■■■■□□□□□□□□□□□□□□□□□□□□□]","24%[■■■■■□□□□□□□□□□□□□□□□□□□□]","28%[■■■■■■□□□□□□□□□□□□□□□□□□□]","32%[■■■■■■■□□□□□□□□□□□□□□□□□□]","36%[■■■■■■■■□□□□□□□□□□□□□□□□□]","40%[■■■■■■■■■□□□□□□□□□□□□□□□□]","44%[■■■■■■■■■■□□□□□□□□□□□□□□□]","48%[■■■■■■■■■■■□□□□□□□□□□□□□□]","52%[■■■■■■■■■■■■□□□□□□□□□□□□□]","56%[■■■■■■■■■■■■■□□□□□□□□□□□□]","60%[■■■■■■■■■■■■■■□□□□□□□□□□□]","64%[■■■■■■■■■■■■■■■■□□□□□□□□□]","68%[■■■■■■■■■■■■■■■■□□□□□□□□□]","72%[■■■■■■■■■■■■■■■■■□□□□□□□□]","76%[■■■■■■■■■■■■■■■■■■□□□□□□□]","80%[■■■■■■■■■■■■■■■■■■■□□□□□□]","84%[■■■■■■■■■■■■■■■■■■■■□□□□□]","88%[■■■■■■■■■■■■■■■■■■■■■□□□□]","92%[■■■■■■■■■■■■■■■■■■■■■■□□□]","96%[■■■■■■■■■■■■■■■■■■■■■■■□□]","100%[■■■■■■■■■■■■■■■■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + 'Loading...' + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
    #偵測2
    d = feedparser.parse('https://www.cdc.gov.tw/RSS/RssXml/Hh094B49-DRwe2RR4eFfrQ?type=1')
    rsstitle2 = d['entries'][0]['title']
    print(prefix + '\n偵測到現在的標題為: ' + rsstitle2)

    #如果1=2
    if rsstitle == rsstitle2:
        print(prefix + '結果相同，無須動作')
    #有新的新聞稿
    else:
        title = rsstitle2
        link = d['entries'][0]['link']
        #檢查是否為新增數
        print(prefix + '結果不同，檢查結果是否為病例:(title: ' + title + ' link: ' + link + ')')
        if '新增' in title and 'COVID-19' in title and '分別' in title:
            print(prefix + '為新增病例，將傳送webhook')

        #擷取數量
            titlenum = title
            #從後面刪過來
            text_check = True
            while text_check == True:
                titlenum = titlenum[:-1]
                if '例' in titlenum:
                    text_check = True
                else:
                    text_check = False
            #刪除特定字元
            print(titlenum)
            titlenum = re.sub("新增","",titlenum)
            #先換成abc
            titlenum = re.sub("0","a",titlenum)
            titlenum = re.sub("1","b",titlenum)
            titlenum = re.sub("2","c",titlenum)
            titlenum = re.sub("3","d",titlenum)
            titlenum = re.sub("4","e",titlenum)
            titlenum = re.sub("5","f",titlenum)
            titlenum = re.sub("6","g",titlenum)
            titlenum = re.sub("7","h",titlenum)
            titlenum = re.sub("8","i",titlenum)
            titlenum = re.sub("9","j",titlenum)
            #再換成discord emoji
            titlenum = re.sub("a","<:0_:936466292188278795>",titlenum)
            titlenum = re.sub("b","<:1_:936466306583130133>",titlenum)
            titlenum = re.sub("c","<:2_:936466316884332564>",titlenum)
            titlenum = re.sub("d","<:3_:936466325801406464>",titlenum)
            titlenum = re.sub("e","<:4_:936466334873714749>",titlenum)
            titlenum = re.sub("f","<:5_:936466346152181760>",titlenum)
            titlenum = re.sub("g","<:6_:936466355610333216>",titlenum)
            titlenum = re.sub("h","<:7_:936466365546655755>",titlenum)
            titlenum = re.sub("i","<:8_:936466375743008768>",titlenum)
            titlenum = re.sub("j","<:9_:936466387801608222>",titlenum)
            print(titlenum)

        #擷取其他細節
            detail = title
            #從前面刪過來
            text_check = True
            while text_check == True:
                detail = re.sub(r'.', '', detail, count = 1)
                if '，' in detail:
                    text_check = True
                else:
                    text_check = False

            #傳送webhook
            webhookurl = '自己丟你的webhook url'
            data1 = {'content':'<@&936278338127941632>以下是今日新增的總病例數:'}
            data2 = {'content': titlenum + '<:lee:936474188464664656>'}
            data3 = {'content':'其中，**__' + detail + '__**\n[點我了解更多](<' + link + '>)'}
            r = requests.post(webhookurl, data=json.dumps(data1), headers={'Content-Type': 'application/json'})
            time.sleep(0.5)
            r = requests.post(webhookurl, data=json.dumps(data2), headers={'Content-Type': 'application/json'})
            time.sleep(0.5)
            r = requests.post(webhookurl, data=json.dumps(data3), headers={'Content-Type': 'application/json'})


        #webhook 
        #message 新增64例COVID-19確定病例，分別為21例本土及43例境外移入
        #role <@&936278338127941632>
        #nums:
        # <:0_:936466292188278795>
        # <:1_:936466306583130133>
        # <:2_:936466316884332564>
        # <:3_:936466325801406464>
        # <:4_:936466334873714749>
        # <:5_:936466346152181760>
        # <:6_:936466355610333216>
        # <:7_:936466365546655755>
        # <:8_:936466375743008768>
        # <:9_:936466387801608222>

        else:
            print(prefix + '不是病例，回傳重新偵測')