# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote

import time
import json
import pyodbc

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
    #aa={"4h":14400}

    bb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', \
        'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'IOTAUSDT', \
        'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'NULSUSDT', \
        'VETUSDT', 'BCHABCUSDT', 'LINKUSDT', \
        'WAVESUSDT', 'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', \
        'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', \
        'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT', \
        'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT']
    
##    bb+=['ETHBTC', 'BNBBTC', 'NEOBTC', 'LTCBTC', 'QTUMBTC', 'ADABTC', \
##         'XRPBTC', 'EOSBTC', 'IOTABTC', 'XLMBTC', 'ONTBTC', 'TRXBTC', \
##         'ETCBTC', 'ICXBTC', 'NULSBTC', 'VETBTC', 'BCHABCBTC', \
##         'LINKBTC', 'WAVESBTC', 'BTTBTC', 'ONGBTC', 'HOTBTC', \
##         'ZILBTC', 'ZRXBTC', 'FETBTC', 'BATBTC', 'XMRBTC', 'ZECBTC', 'IOSTBTC', 'CELRBTC', \
##         'DASHBTC', 'NANOBTC', 'OMGBTC', 'THETABTC', 'ENJBTC', 'MITHBTC', 'MATICBTC', \
##         'ATOMBTC', 'TFUELBTC', 'ONEBTC', 'FTMBTC']
        #btc对为usdt和btc共同交易对

    #bb=["BTCUSDT"]
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=kline;UID=aaa_all;PWD=chaoxian102')
    cursor = cnxn.cursor()

    while True:
        for a,a_v in aa.items():
            for b in bb:
            #for b in ["BTCUSDT"]:
                time_start=time.time()
                
                strsql="select top 1 id from bian where symbol='"+b+"' and interval='"+a+"' order by id desc"
                cursor.execute(strsql)
                row=cursor.fetchone()
                if row:
                    startTime=row.id
                else:
                    startTime=0

                if startTime<=time_start-2*a_v:
                    numm=0
                    limit=int((time_start-startTime)/a_v)+1
                    if limit>500:
                        limit=1000
                    elif limit>100:
                        limit=500
                    elif limit>50:
                        limit=100
                    elif limit>20:
                        limit=50
                    elif limit>10:
                        limit=20
                    elif limit>5:
                        limit=10
                    elif limit>0:
                        limit=5
                    
##                    t = threading.Thread(target=get_htmll,args=("https://api.binance.com/api/v3/klines?symbol="+b+"&interval="\
##                                                                +a+"&startTime="+str(int(startTime*1000))+"&endTime="+str(int(time_start*1000))+"&limit="+str(limit),))
                    t = threading.Thread(target=get_htmll,args=("http://198.176.54.17:5000/bian/?symbol="+b+"&interval="\
                                                                +a+"&startTime="+str(int(startTime*1000))+"&endTime="+str(int(time_start*1000))+"&limit="+str(limit),))

                    t.setDaemon(True)
                    t.start()
                    t.join(130)
                    if t.isAlive ():
                        stop_thread(t)
                        print("查询K线失败！......"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    else:
                        try:
                            dd=json.loads(htmll)
                            lenn=len(dd)
                            for d in dd[:lenn-1]:
                                strsql="select id from bian where symbol='"+b+"' and interval='"+a+"' and id="+str(int(d[0]/1000))
                                cursor.execute(strsql)
                                row=cursor.fetchone()
                                if row is None:
                                    strsql="insert into bian(symbol,interval,id,openn,high,low,closee,amount,vol,count,a_amount,a_vol) values \
                                    ('"+b+"','"+a+"',"+str(int(d[0]/1000))+",'"+str(d[1])+"','"+str(d[2])+"','"+str(d[3])+"',\
                                    '"+str(d[4])+"','"+str(d[5])+"','"+str(d[7])+"',"+str(d[8])+",'"+str(d[9])+"','"+str(d[10])+"')"
                                    cursor.execute(strsql)
                                    cursor.commit()
                                else:
                                    numm+=1
                                    #break
                        except Exception as e:
                            print(e)
                            pass

                    time.sleep(3.01)
                    time_end=time.time()
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime)))
                    print(a+" "+b+" "+str(numm)+'    time cost:',time_end-time_start,'s=='+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end)))

    print("--end--")

