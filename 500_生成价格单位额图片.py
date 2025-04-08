# 白点数据，运行环境Python3.8
# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import time
import datetime
import json
import base64
import hashlib
import random
import os
import io
import zipfile
import zlib

import urllib.request
import gzip

from PIL import Image, ImageDraw,ImageFont


ddd=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT',
     'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT',
     'CELRUSDT', 'DASHUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MATICUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT',
     'WINUSDT', 'COSUSDT', 'MTLUSDT', 'DENTUSDT', 'KEYUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT',
     'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'EURUSDT', 'OGNUSDT', 'DREPUSDT', 'WRXUSDT',
     'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT',
     'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'YFIUSDT', 'BALUSDT',
     'BLZUSDT', 'IRISUSDT', 'KMDUSDT', 'JSTUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT',
     'SUSHIUSDT', 'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'FLMUSDT', 'ORNUSDT',
     'UTKUSDT', 'XVSUSDT', 'ALPHAUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT', 'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'STRAXUSDT', 'UNFIUSDT',
     'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'REEFUSDT', 'OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'TRUUSDT',
     'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT', 'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT', 'ALICEUSDT',
     'LINAUSDT', 'PERPUSDT', 'SUPERUSDT', 'CFXUSDT', 'TKOUSDT', 'PUNDIXUSDT', 'TLMUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT', 'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT',
     'ARUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT', 'XVGUSDT', 'ATAUSDT', 'GTCUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'BONDUSDT', 'MLNUSDT', 'DEXEUSDT', 'C98USDT',
     'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'MINAUSDT', 'RAYUSDT', 'FARMUSDT', 'ALPACAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'GHSTUSDT', 'WAXPUSDT', 'GNOUSDT',
     'XECUSDT', 'ELFUSDT', 'DYDXUSDT', 'IDEXUSDT', 'VIDTUSDT', 'USDPUSDT', 'GALAUSDT', 'ILVUSDT', 'YGGUSDT', 'SYSUSDT', 'DFUSDT', 'FIDAUSDT', 'FRONTUSDT', 'CVPUSDT', 'AGLDUSDT',
     'RADUSDT', 'BETAUSDT', 'RAREUSDT', 'LAZIOUSDT', 'CHESSUSDT', 'ADXUSDT', 'AUCTIONUSDT', 'DARUSDT', 'BNXUSDT', 'MOVRUSDT', 'CITYUSDT', 'ENSUSDT', 'KP3RUSDT', 'QIUSDT',
     'PORTOUSDT', 'POWRUSDT', 'VGXUSDT', 'JASMYUSDT', 'AMPUSDT', 'PLAUSDT', 'PYRUSDT', 'RNDRUSDT', 'ALCXUSDT', 'SANTOSUSDT', 'BICOUSDT', 'FLUXUSDT', 'FXSUSDT', 'VOXELUSDT',
     'HIGHUSDT', 'CVXUSDT', 'PEOPLEUSDT', 'OOKIUSDT', 'SPELLUSDT', 'JOEUSDT', 'ACHUSDT', 'IMXUSDT', 'GLMRUSDT', 'LOKAUSDT', 'SCRTUSDT', 'API3USDT', 'BTTCUSDT', 'ACAUSDT',
     'XNOUSDT', 'WOOUSDT', 'ALPINEUSDT', 'TUSDT', 'ASTRUSDT', 'GMTUSDT', 'KDAUSDT', 'APEUSDT', 'BSWUSDT', 'BIFIUSDT', 'MULTIUSDT', 'STEEMUSDT', 'MOBUSDT', 'NEXOUSDT', 'REIUSDT',
     'GALUSDT', 'LDOUSDT', 'EPXUSDT', 'OPUSDT', 'LEVERUSDT', 'STGUSDT', 'LUNCUSDT', 'GMXUSDT', 'POLYXUSDT', 'APTUSDT', 'OSMOUSDT', 'HFTUSDT', 'PHBUSDT', 'HOOKUSDT', 'MAGICUSDT',
     'HIFIUSDT', 'RPLUSDT', 'PROSUSDT', 'AGIXUSDT', 'GNSUSDT', 'SYNUSDT', 'VIBUSDT', 'SSVUSDT', 'LQTYUSDT', 'AMBUSDT', 'USTCUSDT', 'GASUSDT', 'GLMUSDT', 'PROMUSDT', 'QKCUSDT',
     'UFTUSDT', 'IDUSDT', 'ARBUSDT', 'LOOMUSDT', 'OAXUSDT', 'RDNTUSDT', 'WBTCUSDT', 'EDUUSDT', 'SUIUSDT', 'AERGOUSDT', 'PEPEUSDT', 'FLOKIUSDT', 'ASTUSDT', 'SNTUSDT', 'COMBOUSDT',
     'MAVUSDT', 'PENDLEUSDT', 'ARKMUSDT', 'WBETHUSDT', 'WLDUSDT', 'FDUSDUSDT', 'SEIUSDT', 'CYBERUSDT', 'ARKUSDT', 'CREAMUSDT', 'GFTUSDT', 'IQUSDT', 'NTRNUSDT', 'TIAUSDT',
     'MEMEUSDT', 'ORDIUSDT', 'BEAMXUSDT', 'PIVXUSDT', 'VICUSDT', 'BLURUSDT', 'VANRYUSDT', 'AEURUSDT', 'JTOUSDT', '1000SATSUSDT', 'BONKUSDT', 'ACEUSDT', 'NFPUSDT', 'AIUSDT',
     'XAIUSDT', 'MANTAUSDT', 'ALTUSDT']

ddd={x:[x.replace("USDT","")] for x in ddd}

ddd=list(ddd.items())
random.shuffle(ddd)
ddd=dict(ddd)

f0=lambda x: 0.0 if x=="" or x==None else float(x)  # 把字符串转为浮点数


def tt_d(x):  # 时间戳转日期
    timestamp = x  # 假设这是一个时间戳
    # 使用 fromtimestamp() 方法将时间戳转换为日期时间对象
    #date_time = datetime.datetime.fromtimestamp(timestamp)
    date_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
    #date_time = datetime.datetime.fromtimestamp(timestamp, tz=pytz.timezone('Asia/Shanghai'))
    # 然后可以使用 strftime() 方法将日期时间格式化为特定的日期字符串
    #formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
    formatted_date = date_time.strftime('%Y-%m-%d')
    return formatted_date  # 输出格式化后的日期字符串


##[
##  [
##    1499040000000,      // k线开盘时间  0
##    "0.01634790",       // 开盘价  1
##    "0.80000000",       // 最高价  2
##    "0.01575800",       // 最低价  3
##    "0.01577100",       // 收盘价(当前K线未结束的即为最新价)  4
##    "148976.11427815",  // 成交量  5
##    1499644799999,      // k线收盘时间  6
##    "2434.19055334",    // 成交额  7
##    308,                // 成交笔数  8
##    "1756.87402397",    // 主动买入成交量  9
##    "28.46694368",      // 主动买入成交额  10
##    "17928899.62484339" // 请忽略该参数
##  ]
##]


for kk in ddd.keys():
    print(kk)
    # 0日期  1开盘  2最低  3最高  4收盘  5成交量  6成交额  7换手率
    with open(f'data/{kk}_1d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu0=json.loads(f.read())
        mn=len(uuu0)//1280+1
        uuu0=uuu0[-1280*mn:]
        uuu0=[[tt_d(int(uu[0]/1000)),f0(uu[1]),f0(uu[3]),f0(uu[2]),f0(uu[4]),f0(uu[5]),
               f0(uu[7]),0] for uu in uuu0]
    with open(f'data/{kk}_1d.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu1=json.loads(f.read())[-1280*mn:]
        uuu1=[[tt_d(int(uu[0]/1000)),f0(uu[1]),f0(uu[3]),f0(uu[2]),f0(uu[4]),f0(uu[5]),
               f0(uu[7]),0] for uu in uuu1]

    if (lenn:=len(uuu0))==len(uuu1) and lenn>0 and uuu0[0][0]==uuu1[0][0]:
        uuu0=uuu0[::-1]  # 不复权
        uuu0=[uuu0[i:i+mn] for i in range(0,lenn,mn)]
        ppp0=[[x[0][0],round(sum([y[4] for y in x])/len(x),3)] for x in uuu0]  # 价格
##        vvv0=[[x[0][0],sum([y[5] for y in x])] for x in uuu0]  # 成交量volume
##        aaa0=[[x[0][0],sum([y[6] for y in x])] for x in uuu0]  # 成交额amount
##        ttt0=[[x[0][0],sum([y[7] for y in x])] for x in uuu0]  # 换手率turnoverrate
##        hhll0=[[x[0][0],(max([y[3] for y in x])-min([y[2] for y in x]))*2-
##                abs(x[0][4]-x[-1][1])] for x in uuu0]
##        hl_x=[[x[0], 0.0 if x[1]==0 else y[1]/x[1]] for x in hhll0 for y in aaa0]

        uuu1=uuu1[::-1]  # 前复权
        uuu1=[uuu1[i:i+mn] for i in range(0,lenn,mn)]
        ppp1=[[x[0][0],round(sum([y[4] for y in x])/len(x),3)] for x in uuu1]  # 价格
##        vvv1=[[x[0][0],sum([y[5] for y in x])] for x in uuu1]  # 成交量volume
        aaa1=[[x[0][0],round(sum([y[6] if y[6]>0 else 0 for y in x]),3)] for x in uuu1]  # 成交额amount
##        ttt1=[[x[0][0],sum([y[7] for y in x])] for x in uuu1]  # 换手率turnoverrate
        
        hhll1=[[x[0][0],round((max([y[3] for y in x])-min([y[2] for y in x]))*2-
                abs(x[0][4]-x[-1][1]),3)] for x in uuu1]
        
        hhll1=[[x[0],x[1] if x[1]>0 else 0] for x in hhll1]

        hl_x=[[v[0], 0 if v[1]==0 else round(aaa1[i][1]/v[1],3)] for i,v in enumerate(hhll1)]

        #hl_x: 钱比钱应该更好一些


        #--------------------------------开始制图
        img = Image.open("000_1280.png")
        #img = img.convert('RGBA')
        draw =ImageDraw.Draw(img)
        #draw =ImageDraw.Draw(img, mode="RGBA")

        draw.line((0, 308-30,1280,308-30), "#cccccc")
        draw.line((0, 308-60,1280,308-60), "#cccccc")
        draw.line((0, 308-90,1280,308-90), "#cccccc")
        draw.line((0, 308-120,1280,308-120), "#cccccc")
        draw.line((0, 308-150,1280,308-150), "#cccccc")
        draw.line((0, 308-180,1280,308-180), "#cccccc")
        draw.line((0, 308-210,1280,308-210), "#cccccc")
        draw.line((0, 308-240,1280,308-240), "#cccccc")
        draw.line((0, 308-270,1280,308-270), "#cccccc")
        #draw.line((0, 308-300,1280,308-300), "#cccccc")
        #------------------------

        
        #---------不复权
        year=ppp0[-1][0][:4]  #取年份
        maxx=max([x[1] for x in ppp0]+[x[1] for x in ppp1])
        minn=min([x[1] if x[1]>0 else 0 for x in ppp0]+[x[1] if x[1]>0 else 0 for x in ppp1])
        maxx_minn=maxx-minn
        h_l_0=f"H/L: {round(maxx/minn,3) if minn>0 else '-'}"
        i=0
        for pp in ppp0[::-1]:
            if pp[1]==None or pp[1]==0 or maxx_minn==0:
                #draw.line((i, 308, i, 308), '#ffffff')
                pass
            else:
                #draw.line((i, 308, i, 308-int(((pp-minn)/maxx_minn)*300)), 'black')
                draw.line((i, 308, i, 308-int(((pp[1]-minn)/maxx_minn)*300)), '#000000')
            
            if year!=pp[0][:4]:
                if pp[1]==None or pp[1]==0 or maxx_minn==0:
                    #draw.line((i, 308, i, 308), '#ffffff')
                    pass
                else:
                    draw.line((i, 308-int(((pp[1]-minn)/maxx_minn)*300),i,30), "#ff0000")  # 原为: i,0
                year=pp[0][:4]
            i+=1

        #----------前复权 
        i=0
        for pp in ppp1[::-1]:
            if pp[1]==None or pp[1]==0 or maxx_minn==0:
                #draw.line((i, 308, i, 308), '#ffffff')
                pass
            else:
                draw.line((i, 308, i, 308-int(((pp[1]-minn)/maxx_minn)*300)), fill = (255, 204, 0, 255))
                #draw.line((i, 308, i, 308-int(((pp-minn)/maxx_minn)*300)), "#0000ff")
                #print("-------")

            i+=1
        #=========================
        #------------------------

        year=hl_x[-1][0][:4]  #取年份
        maxx=max([x[1] for x in hl_x])
        minn=min([x[1] if x[1]>0 else 0 for x in hl_x])
        maxx_minn=maxx-minn
        h_l_1=f"H/L: {round(maxx/minn,3) if minn>0 else '-'}"
        i=0
        for vv in hl_x[::-1]:
            #draw.line((i, 629, i, 629-int(((dd-minn)/maxx_minn)*300)), 'black')
            #draw.line((i, 329, i, 329+int(((dd-minn)/maxx_minn)*300)), 'black')
            if vv[1]==None or vv[1]==0 or maxx_minn==0:
                #draw.line((i, 312, i, 312), '#ffffff')
                pass
            else:
                draw.line((i, 312, i, 312+int(((vv[1]-minn)/maxx_minn)*300)), '#0033ff')

            if year!=vv[0][:4]:
                if vv[1]==None or vv[1]==0 or maxx_minn==0:
                    #draw.line((i, 312,i,619), "#ffffff")
                    pass
                else:
                    draw.line((i, 312+int(((vv[1]-minn)/maxx_minn)*300),i,619-30), "#ff0000")  # 原为: 619
                year=vv[0][:4]
            i+=1
        #=========================

        #----------------写入文字
        setFont = ImageFont.truetype('fonts/msyh.ttf', 16)
        fillColor = "#000066"
        width, height = img.size
        #ttt1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ddd[0][0]/1000))

        #txtt=f"{kk}_5d {ddd[kk][0]}（{' '.join(ddd[kk][1:2]).replace('@','')}）（{uuu0[-1][-1][0]}__{uuu0[0][0][0]}）{h_l_0}（AB量化  www.abtrue.com）"
        txtt=f"{kk}_{mn}d {ddd[kk][0]}（加密币）（{uuu0[-1][-1][0]}__{uuu0[0][0][0]}）{h_l_0}（AB量化  www.abtrue.com）"
        text_size = setFont.getsize(txtt)
        text_size2 = setFont.getsize(h_l_1)

        draw.text(((width-text_size[0])/2, 0), txtt, font=setFont, fill=fillColor)
        draw.text(((width-text_size2[0])/2, height-20), h_l_1, font=setFont, fill=fillColor)
        
        #Image1.show()
        
        
        img.save(f"img_价格单位额/{kk}.png", "png")



print("--end--")
