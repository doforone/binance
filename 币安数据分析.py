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

    a="1d"
    b="EOSUSDT"
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
            
            idd_lll=[]
            amount_v=[]
            count_v=[]
            a_amount_v=[]
            a_amount_amount=[]
            amount_lll=[]
            price_v=[]
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

                high_low=high-low
                #lll.append({"idd":idd/1000,"amount_v":amount/high_low,"count_v":count/high_low,"a_amount_v":a_amount/high_low,"a_amount_amount":a_amount/amount})
                idd_lll.append(idd/1000)
                amount_v.append(amount/high_low)
                count_v.append(count/high_low)
                a_amount_v.append(a_amount/high_low)
                a_amount_amount.append(a_amount/amount)
                amount_lll.append(amount)
                price_v.append(vol/amount)


            Image1 = Image.open("000.jpg")
            draw =ImageDraw.Draw(Image1)
            #------------------------
            maxx=max(amount_v)
            minn=min(amount_v)
            maxx_minn=maxx-minn
            i=0
            for dd in amount_v:
                draw.line((i, 629, i, 629-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            #------------------------
            maxx=max(count_v)
            minn=min(count_v)
            maxx_minn=maxx-minn
            i=0
            for dd in count_v:
                draw.line((i, 524, i, 524-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            #------------------------
            maxx=max(a_amount_v)
            minn=min(a_amount_v)
            maxx_minn=maxx-minn
            i=0
            for dd in a_amount_v:
                draw.line((i, 419, i, 419-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            #------------------------
            maxx=max(a_amount_amount)
            minn=min(a_amount_amount)
            maxx_minn=maxx-minn
            i=0
            for dd in a_amount_amount:
                draw.line((i, 314, i, 314-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            #------------------------
            maxx=max(amount_lll)
            minn=min(amount_lll)
            maxx_minn=maxx-minn
            i=0
            for dd in amount_lll:
                draw.line((i, 209, i, 209-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            #------------------------
            maxx=max(price_v)
            minn=min(price_v)
            maxx_minn=maxx-minn
            i=0
            for dd in price_v:
                draw.line((i, 104, i, 104-int(((dd-minn)/maxx_minn)*100)), 'black')
                i+=1
            #=========================
            Image1.show()
            Image1.save(f"{b}_{a}.png", "png")
        except Exception as e:
            print(e)
            pass

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print("--end--")

