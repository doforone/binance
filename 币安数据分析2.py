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


if __name__ == "__main__":
    htmll=""

    aa={"1m":60, "3m":180, "5m":300, "15m":900, "30m":1800, "1h":3600, "2h":7200, \
        "4h":14400, "6h":21600, "8h":28800, "12h":43200, "1d":86400, "3d":259200, "1w":604800}

    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', \
        'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', \
        'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', \
        'VETUSDT', 'BCHABCUSDT', 'LINKUSDT', \
        'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', \
        'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', \
        'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', \
        'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT']

    a="1h"
    b="BTCUSDT"
    limit=1000
    time_start=time.time()
    startTime=time_start-aa[a]*limit
    t = threading.Thread(target=get_htmll,args=("http://198.176.54.46:5000/bian/?symbol="+b+"&interval="\
                                                +a+"&startTime="+str(int(startTime*1000))+"&endTime="+str(int(time_start*1000))+"&limit="+str(limit),))


    t.setDaemon(True)
    t.start()
    t.join(13)
    if t.is_alive ():
        stop_thread(t)
        print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        try:
            dd=json.loads(htmll)
            #print(dd)
            lenn=len(dd)
            
            usdt=0
            btc=1
            numm=0
            for d in dd[:lenn-1]:
                #id,openn,high,low,closee,amount,vol,count,a_amount,a_vol
                #0  1     2    3   4      5      7   8     9        10
                idd=d[0]
                openn=float(d[1])
                high=float(d[2])
                low=float(d[3])
                closee=float(d[4])
                amount=float(d[5])
                vol=float(d[7])
                count=d[8]
                a_amount=float(d[9])
                a_vol=float(d[10])

                if btc>0:
                    if high>=openn*1.022:
                        usdt=btc*openn*(1.022-0.001)  #默认千分之一的手续费
                        btc=0
                        print(usdt)
                        numm+=1
                        print(f"{str(numm).ljust(20)}{str(btc).ljust(20)}{str(usdt).ljust(20)}")
                else:
                    btc=usdt/(openn*1.001)  #默认千分之一的手续费
                    usdt=0
                    if high>=openn*1.022:
                        usdt=btc*openn*(1.022-0.001)  #默认千分之一的手续费
                        btc=0
                        numm+=1
                        print(f"{str(numm).ljust(20)}{str(btc).ljust(20)}{str(usdt).ljust(20)}")

                #print(numm)
                #print(btc)
                #print(usdt)

        except Exception as e:
            print(e)
            pass

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print("--end--")

