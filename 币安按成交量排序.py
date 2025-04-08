# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
import pyodbc

from PIL import Image, ImageDraw,ImageFont
import random

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
    #print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=125) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


if __name__ == "__main__":
    htmll=""

    aaa={"1m":60, "3m":180, "5m":300, "15m":900, "30m":1800, "1h":3600, "2h":7200,
         "4h":14400, "6h":21600, "8h":28800, "12h":43200, "1d":86400, "3d":259200, "1w":604800}


    bbb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT',
         'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT',
         'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', 'VETUSDT',
         'PAXUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'ONGUSDT',
         'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT',
         'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT',
         'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', 'ATOMUSDT',
         'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT',
         'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'NPXSUSDT', 'COCOSUSDT',
         'MTLUSDT', 'TOMOUSDT', 'PERLUSDT', 'DENTUSDT', 'MFTUSDT', 'KEYUSDT',
         'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT',
         'BUSDUSDT', 'BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT',
         'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT',
         'CTXCUSDT', 'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'EURUSDT',
         'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT', 'BTSUSDT', 'LSKUSDT',
         'BNTUSDT', 'LTOUSDT', 'AIONUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT',
         'WTCUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT',
         'GXSUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'REPUSDT',
         'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT',
         'VTHOUSDT', 'DGBUSDT', 'GBPUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT',
         'STORJUSDT', 'MANAUSDT', 'AUDUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT',
         'IRISUSDT', 'KMDUSDT', 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT',
         'SANDUSDT', 'OCEANUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT',
         'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT',
         'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT',
         'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT', 'OXTUSDT', 'SUNUSDT',
         'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT',
         'ALPHAUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT',
         'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT', 'STRAXUSDT',
         'UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'SUSDUSDT',
         'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'REEFUSDT', 'OGUSDT',
         'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT',
         'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT']

    #--去除稳定币
    bbb.remove("AUDUSDT")
    bbb.remove("BUSDUSDT")
    bbb.remove("EURUSDT")
    bbb.remove("GBPUSDT")
    bbb.remove("PAXGUSDT")
    bbb.remove("PAXUSDT")
    bbb.remove("SUSDUSDT")
    bbb.remove("TUSDUSDT")
    bbb.remove("USDCUSDT")
    #=============
    
    vols={}
    limit=11
    aa="1d"
    for bb in bbb:
        time_start=time.time()
        startTime=time_start-aaa[aa]*limit
        t = threading.Thread(target=get_htmll,args=("http://bi.kefabu.com:5000/bian/?symbol="+bb+"&interval="\
                                                    +aa+"&startTime="+str(int(startTime*1000))+"&endTime="+str(int(time_start*1000))+"&limit="+str(limit),))


        t.setDaemon(True)
        t.start()
        t.join(13)
        if t.is_alive ():
            stop_thread(t)
            print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            ddd=json.loads(htmll)
            ddd.pop()
            vol=0
            for dd in ddd:
                #id,openn,high,low,closee,amount,vol,count,a_amount,a_vol
                #0  1     2    3   4      5      7   8     9        10
                vol+=float(dd[7])

            vols[bb]=vol

    ttt=sorted(vols.items(), key=lambda x : x[1], reverse=True)
    print(ttt)

    mmm=[]
    for tt in ttt:
        mmm.append(tt[0])
    print(mmm)
