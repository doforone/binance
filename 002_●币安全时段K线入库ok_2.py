# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
#import pyodbc

from PIL import Image, ImageDraw,ImageFont
import random
import os

import datetime
from datetime import timedelta
#from datetime import datetime, timezone

#============================时间到强制结束线程
import threading
import inspect
import ctypes

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

#=============================

def get_htmll(urll,dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=125) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


f0=lambda x: 0.0 if x=="" else float(x)


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


def a_b(a,b):
    # 计算a-b,保留最长的小数位
    a=str(a);b=str(b)
    
    if a.find(".")==-1:
        a_max=0
    else:
        a_max=len(str(a).split('.')[-1])

    if b.find(".")==-1:
        b_max=0
    else:
        b_max=len(str(b).split('.')[-1])

    maxx=max(a_max, b_max)

    return round(float(a)-float(b),maxx)


##            #id,openn,high,low,closee,amount,vol,count,a_amount,a_vol
##            #0  1     2    3   4      5      7   8     9        10


if __name__ == "__main__":
    htmll=""

    aa={"1m":60, "3m":180, "5m":300, "15m":900, "30m":1800, "1h":3600, "2h":7200, \
        "4h":14400, "6h":21600, "8h":28800, "12h":43200, "1d":86400, "3d":259200, "1w":604800}

    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', \
        'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', \
        'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', \
        'VETUSDT', 'BCHUSDT', 'LINKUSDT', \
        'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', \
        'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', \
        'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', \
        'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT']

    bb+=['UNIUSDT', 'DOGEUSDT', 'MDXUSDT', 'DOTUSDT', 'FILUSDT']

    bb+=['AAVEUSDT', 'COMPUSDT']
    
    a="1d"
    #a="1h"
    #a="30m"
    #a="15m"
    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', \
        'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', \
        'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT', \
        'PAXUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', \
        'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', \
        'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT', \
        'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT', \
        'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT', \
        'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'NPXSUSDT', 'COCOSUSDT', \
        'MTLUSDT', 'TOMOUSDT', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT', \
        'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT', \
        'BUSDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', \
        'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', \
        'CTXCUSDT', 'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'EURUSDT', \
        'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT', \
        'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT', \
        'WTCUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', \
        'GXSUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'REPUSDT', \
        'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', \
        'VTHOUSDT', 'DGBUSDT', 'GBPUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT', \
        'STORJUSDT', 'MANAUSDT', 'AUDUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT', \
        'IRISUSDT', 'KMDUSDT', 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT', \
        'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', \
        'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT', \
        'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', \
        'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT', 'OXTUSDT', 'SUNUSDT', \
        'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT', \
        'ALPHAUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT', \
        'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT', 'STRAXUSDT', \
        'UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'SUSDUSDT', \
        'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'REEFUSDT', 'OGUSDT', \
        'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT', \
        'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT']

##    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'CHZUSDT', 'ADAUSDT', 'DOTUSDT', 
##        'ENJUSDT', 'XRPUSDT', 'CHRUSDT', 'LTCUSDT', 'MATICUSDT', 'XEMUSDT', 
##        'UNIUSDT', 'SXPUSDT', 'DOGEUSDT', 'LINKUSDT', 'THETAUSDT', 'VETUSDT', 
##        'LUNAUSDT', 'MANAUSDT', 'AVAXUSDT']
##    bb+=['FILUSDT', 'DOGEUSDT']
##
##    bb=['BTCUSDT', 'ETHUSDT', 'MATICUSDT']
##    bb=['LTCUSDT', 'XRPUSDT', 'EOSUSDT']
    #bb=['TCTUSDT','MDTUSDT','RIFUSDT']

    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT',
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
    
    MN=5
    rrr=[]
    nnn={}
    lenn=len(bb)
    for i,b in enumerate(bb):
        print(lenn-i,b)
        nnn[b]=[]
        limit=1000
        if os.access("data\\"+b+"_"+a+".txt", os.F_OK):
            with open('data\\'+b+'_'+a+'.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
                ddd=json.loads(f.read())
        else:
            ddd=[]
            
        if ddd==[]:
            start_id=0
        else:
            start_id=ddd[-1][0]+aa[a]*1000
            
        havee=1
        while havee==1:
##            t = threading.Thread(target=get_htmll,args=("http://bi.kefabu.com:5000/bian/?symbol="+b+"&interval="\
##                                                        +a+"&startTime="+str(start_id)+"&limit="+str(limit),))

            t = threading.Thread(target=get_htmll,args=("https://api.binance.com/api/v3/klines?symbol="+b+"&interval="\
                                                        +a+"&startTime="+str(start_id)+"&limit="+str(limit),))


            t.setDaemon(True)
            t.start()
            t.join(33)
            if t.is_alive ():
                stop_thread(t)
                print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            else:
                try:
                    ttt=json.loads(htmll)
                    
                    if len(ttt)<limit:
                        havee=0
                    else:
                        havee=1
                        start_id=ttt[-1][0]

                    for tt in ttt[:-1]:
                        ddd.append(tt)
##                        nnn[b].append([tt_d(int(tt[0]/1000)),None,f0(tt[1]),f0(tt[3]),f0(tt[2]),
##                                       f0(tt[4]),f0(tt[5]),f0(tt[7]),None])
                        
                        nnn[b].append([tt_d(int(tt[0]/1000)),f0(tt[1]),f0(tt[3]),f0(tt[2]),f0(tt[4]),
                                       a_b(f0(tt[4]),f0(tt[1])),
                                       round(a_b(f0(tt[4]),f0(tt[1]))*100/f0(tt[1]),2),
                                       f0(tt[5]),f0(tt[7]),0])
                    
                except Exception as e:
                    print(e)
                    pass
                
        #jjj=json.dumps(ddd, indent=4)+"\r\n"
        jjj=json.dumps(ddd, indent=0)+"\r\n"
        with open('data\\'+b+'_'+a+'.txt', 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(jjj)


    with open(f'000_new_data_{a}.txt', 'w', encoding='utf-8', newline='\r\n') as f:
        #f.write(json.dumps(ddd2, indent=4, ensure_ascii=False)+"\r\n")
        f.write(json.dumps(nnn, ensure_ascii=False))
        #f.write(json.dumps(ddd2, indent=0, ensure_ascii=False)+"\r\n")


##        #---------------------
##        mmm=[]
##        for dd in ddd:
##            #id,openn,high,low,closee,amount,vol,count,a_amount,a_vol
##            #0  1     2    3   4      5      7   8     9        10
##            mmm.append(float(dd[4])-float(dd[1]))
##            
##        mmm_len=len(mmm)
##        i=MN
##        p=float(ddd[0][1])  #初始化price=第一次的open
##        sub_p=abs(float(ddd[0][4])-float(ddd[0][1]))
##        print(sub_p)
##        win=0
##        fai=0
##        AB=3
##        while i<mmm_len:
##            if p>0:
##                if (mmm[i]>max(mn:=mmm[i-MN:i]) and mmm[i]>-min(mn)) or float(ddd[i][4])>p+sub_p*AB:
##                #if (mmm[i]>max(mn:=mmm[i-MN:i]) and mmm[i]>-min(mn)):
##                    if float(ddd[i][4])>p*1.003:
##                        win+=1
##                        #win+=(float(ddd[i][4])-p)*0.998
##                        p=0
##                        sub_p=0
##                        #print(f'+++{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ddd[i][0]/1000))}')
##                    else:
##                        fai+=1
##                        #fai+=(float(ddd[i][4])-p)*1.002
##                        p=0
##                        sub_p=0
##                        #print(f'---{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ddd[i][0]/1000))}')
##            else:
##                if mmm[i]<-max(mn:=mmm[i-MN:i]) and mmm[i]<min(mn) and mmm[i-1]<0:
##                #if mmm[i]<-max(mn:=mmm[i-MN:i]) and mmm[i]<min(mn):
##                    p=float(ddd[i][4])
##                    sub_p=float(ddd[i][1])-float(ddd[i][4])
##
##            i+=1
##
##        print(f'{b}  {a}  MN:{MN}  AB:{AB}  win:{win}  fai:{fai}  = {win/(fai+0.001)}')  #防止fai为0
##        #print(f'{b}  {a}  {MN}  win:{win}  fai:{fai}  = {win+fai}')
##        rrr.append([win/fai,b,a,MN,win,fai])
##        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
##        #===============================
    rrr.sort()
    print(rrr)
    print("--end--")




time.sleep(6)
import os

# 启动第一个程序
# 这里假设第一个程序是 test1.py
os.system("python 003_●币安K线上传同步.py")
