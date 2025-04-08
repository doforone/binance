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
        'VETUSDT', 'BCHUSDT', 'LINKUSDT', \
        'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', \
        'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', \
        'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', \
        'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT']

    bb+=['UNIUSDT', 'DOGEUSDT', 'MDXUSDT', 'DOTUSDT', 'FILUSDT']

    bb+=['AAVEUSDT', 'COMPUSDT']
    
    a="1h"
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

    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'CHZUSDT', 'ADAUSDT', 'DOTUSDT', 
        'ENJUSDT', 'XRPUSDT', 'CHRUSDT', 'LTCUSDT', 'MATICUSDT', 'XEMUSDT', 
        'UNIUSDT', 'SXPUSDT', 'DOGEUSDT', 'LINKUSDT', 'THETAUSDT', 'VETUSDT', 
        'LUNAUSDT', 'MANAUSDT', 'AVAXUSDT']
    for b in bb:
        limit=1000
        time_start=time.time()
        startTime=time_start-aa[a]*limit
        t = threading.Thread(target=get_htmll,args=("http://bi.kefabu.com:5000/bian/?symbol="+b+"&interval="\
                                                    +a+"&startTime="+str(int(startTime*1000))+"&endTime="+str(int(time_start*1000))+"&limit="+str(limit),))


        t.setDaemon(True)
        t.start()
        t.join(13)
        if t.is_alive ():
            stop_thread(t)
            print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        else:
            try:
                ddd=json.loads(htmll)
                #print(ddd)
                lenn=len(ddd)
                
                idd_lll=[]
                amount_v=[]
                count_v=[]
                a_amount_v=[]
                a_amount_amount=[]
                amount_lll=[]
                price_v=[]
                for d in ddd[:lenn-1]:
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

                    #high_low=high-low
                    high_low=(high-low)*2-abs(closee-openn)
                    if high_low!=0 and amount!=0:
                        #lll.append({"idd":idd/1000,"amount_v":amount/high_low,"count_v":count/high_low,"a_amount_v":a_amount/high_low,"a_amount_amount":a_amount/amount})
                        #idd_lll.append(idd/1000)
                        
                        #amount_v.append(amount/high_low)
                        amount_v.append(count)
                        
                        #count_v.append(count/high_low)
                        #a_amount_v.append(a_amount/high_low)
                        #a_amount_amount.append(a_amount/amount)
                        #amount_lll.append(amount)
                        price_v.append(vol/amount)


                image = Image.open("111.png")
                draw =ImageDraw.Draw(image)
                #------------------------
                maxx=max(amount_v)
                minn=min(amount_v)
                amount_v[amount_v.index(maxx)]=minn  #-----------
                maxx=max(amount_v)
                
                #h_l_1=f"H:{maxx}, L:{minn}"
                h_l_1=f"H/L: {round(maxx/minn,3)}"
                maxx_minn=maxx-minn
                i=0
                lenn=len(amount_v)
                for dd in amount_v:
                    #draw.line((i, 629, i, 629-int(((dd-minn)/maxx_minn)*300)), 'black')
                    #draw.line((i, 329, i, 329+int(((dd-minn)/maxx_minn)*300)), 'black')
                    draw.line((i, 312, i, 312+int(((dd-minn)/maxx_minn)*300)), 'black')
                    i+=1
                    if i==lenn-20:
                        draw.line((i, 312+int(((dd-minn)/maxx_minn)*300),i,619), "#cccccc")
                #=========================
                #------------------------
                maxx=max(price_v)
                minn=min(price_v)
                price_v[price_v.index(maxx)]=minn  #------------
                maxx=max(price_v)
                
                #h_l_2=f"H:{maxx}, L:{minn}"
                h_l_2=f"H/L: {round(maxx/minn,3)}"
                maxx_minn=maxx-minn
                i=0
                lenn=len(price_v)
                for dd in price_v:
                    draw.line((i, 308, i, 308-int(((dd-minn)/maxx_minn)*300)), 'black')
                    i+=1
                    if i==lenn-20:
                        draw.line((i, 308-int(((dd-minn)/maxx_minn)*300),i,0), "#cccccc")
                #=========================
                setFont = ImageFont.truetype('fonts/msyh.ttf', 16)
                fillColor = "#000000"
                width, height = image.size
                #ttt1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ddd[0][0]/1000))
                ttt1=time.strftime("%Y-%m-%d", time.localtime(ddd[0][0]/1000))
                ttt2=time.strftime("%Y-%m-%d", time.localtime(ddd[lenn-2][0]/1000))
                text_size = setFont.getsize(f"{b}_{a} ({ttt1}, {ttt2}) ({h_l_2})")
                text_size2 = setFont.getsize(f"({h_l_1})")
                #print(text_size)
                draw.text(((width-text_size[0])/2, 0), f"{b}_{a} ({ttt1}, {ttt2}) ({h_l_2})", font=setFont, fill=fillColor)
                draw.text(((width-text_size2[0])/2, height-20), f"({h_l_1})", font=setFont, fill=fillColor)
                
                #Image1.show()
                print("币安已选")
                image.save(f"img_2成交次数/{b}_{a}_1.png", "png")
            except Exception as e:
                print(e)
                pass

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print("--end--")

