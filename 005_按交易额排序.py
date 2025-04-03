# -*- coding: UTF-8 -*-
# 运行环境：Python 3.8（为兼容 Windows 7 及 Windows 2008 系统）
# 作者邮箱：chaoxian102@gmail.com
# 微信：chaoxian102（超弦102）
# 支付宝：abtrue@hotmail.com
# Paypal：https://paypal.me/abtruecom
# 感谢打赏


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


# ---------------- 对自己不完全可控的线程, 必要时可强制结束
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

#  ================


def get_htmll(urll):  # 请求页面
    headers = {
        'user-agent': (
            'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 '
            '(compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        )
    }

    try:
        req = request.Request(urll, headers=headers)
        with request.urlopen(req, timeout=130) as resp:  # 如果超过130秒的请求时间, 就放弃 
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'Err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(urll+"\r\n")
        return htmll


f0=lambda x: 0.0 if x=="" else float(x)  # 空值转为浮点数0.0


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
    # 计算a-b, 保留最长的小数位
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


##  币安K线数据结构
##  id,openn,high,low,closee,amount,vol,count,a_amount,a_vol
##  0  1     2    3   4      5      7   8     9        10

##[
##  [
##    1499040000000,      // 开盘时间
##    "0.01634790",       // 开盘价
##    "0.80000000",       // 最高价
##    "0.01575800",       // 最低价
##    "0.01577100",       // 收盘价(当前K线未结束的即为最新价)
##    "148976.11427815",  // 成交量
##    1499644799999,      // 收盘时间
##    "2434.19055334",    // 成交额
##    308,                // 成交笔数
##    "1756.87402397",    // 主动买入成交量
##    "28.46694368",      // 主动买入成交额
##    "17928899.62484339" // 请忽略该参数
##  ]
##]


if __name__ == "__main__":
    #aaa={"1m":60, "3m":180, "5m":300, "15m":900, "30m":1800, "1h":3600, "2h":7200, "4h":14400, "6h":21600, "8h":28800, "12h":43200, "1d":86400, "3d":259200, "1w":604800}
    bbb=['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT',
         'ICXUSDT', 'NULSUSDT', 'VETUSDT', 'USDCUSDT', 'LINKUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT',
         'THETAUSDT', 'ENJUSDT', 'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'DOGEUSDT', 'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'MTLUSDT', 'DENTUSDT',
         'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT', 'BANDUSDT', 'XTZUSDT', 'RVNUSDT', 'HBARUSDT', 'NKNUSDT', 'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT',
         'BCHUSDT', 'TROYUSDT', 'VITEUSDT', 'FTTUSDT', 'EURUSDT', 'OGNUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT', 'MBLUSDT', 'COTIUSDT', 'STPTUSDT', 'DATAUSDT', 'SOLUSDT', 'CTSIUSDT',
         'HIVEUSDT', 'CHRUSDT', 'ARDRUSDT', 'MDTUSDT', 'STMXUSDT', 'KNCUSDT', 'LRCUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'SXPUSDT', 'MKRUSDT',
         'DCRUSDT', 'STORJUSDT', 'MANAUSDT', 'YFIUSDT', 'BALUSDT', 'KMDUSDT', 'JSTUSDT', 'CRVUSDT', 'SANDUSDT', 'NMRUSDT', 'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'TRBUSDT',
         'SUSHIUSDT', 'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'FLMUSDT', 'UTKUSDT',
         'XVSUSDT', 'ALPHAUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AUDIOUSDT', 'CTKUSDT', 'AXSUSDT', 'HARDUSDT', 'STRAXUSDT', 'ROSEUSDT', 'AVAUSDT', 'SKLUSDT',
         'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'TRUUSDT', 'CKBUSDT', 'TWTUSDT', 'FIROUSDT', 'LITUSDT', 'SFPUSDT',
         'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT', 'ALICEUSDT', 'LINAUSDT', 'PERPUSDT', 'SUPERUSDT', 'CFXUSDT', 'TKOUSDT',
         'PUNDIXUSDT', 'TLMUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT', 'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'MASKUSDT', 'LPTUSDT', 'XVGUSDT', 'ATAUSDT',
         'GTCUSDT', 'ERNUSDT', 'PHAUSDT', 'MLNUSDT', 'DEXEUSDT', 'C98USDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'MINAUSDT', 'RAYUSDT', 'FARMUSDT', 'ALPACAUSDT', 'QUICKUSDT',
         'MBOXUSDT', 'REQUSDT', 'GHSTUSDT', 'WAXPUSDT', 'GNOUSDT', 'XECUSDT', 'ELFUSDT', 'DYDXUSDT', 'IDEXUSDT', 'VIDTUSDT', 'USDPUSDT', 'GALAUSDT', 'ILVUSDT', 'YGGUSDT', 'SYSUSDT',
         'DFUSDT', 'FIDAUSDT', 'AGLDUSDT', 'RADUSDT', 'BETAUSDT', 'RAREUSDT', 'LAZIOUSDT', 'CHESSUSDT', 'ADXUSDT', 'AUCTIONUSDT', 'BNXUSDT', 'MOVRUSDT', 'CITYUSDT', 'ENSUSDT',
         'QIUSDT', 'PORTOUSDT', 'POWRUSDT', 'JASMYUSDT', 'AMPUSDT', 'PYRUSDT', 'ALCXUSDT', 'SANTOSUSDT', 'BICOUSDT', 'FLUXUSDT', 'FXSUSDT', 'VOXELUSDT', 'HIGHUSDT', 'CVXUSDT',
         'PEOPLEUSDT', 'SPELLUSDT', 'JOEUSDT', 'ACHUSDT', 'IMXUSDT', 'GLMRUSDT', 'LOKAUSDT', 'SCRTUSDT', 'API3USDT', 'BTTCUSDT', 'ACAUSDT', 'XNOUSDT', 'WOOUSDT', 'ALPINEUSDT',
         'TUSDT', 'ASTRUSDT', 'GMTUSDT', 'KDAUSDT', 'APEUSDT', 'BSWUSDT', 'BIFIUSDT', 'STEEMUSDT', 'NEXOUSDT', 'REIUSDT', 'LDOUSDT', 'OPUSDT', 'LEVERUSDT', 'STGUSDT', 'LUNCUSDT',
         'GMXUSDT', 'POLYXUSDT', 'APTUSDT', 'OSMOUSDT', 'HFTUSDT', 'PHBUSDT', 'HOOKUSDT', 'MAGICUSDT', 'HIFIUSDT', 'RPLUSDT', 'PROSUSDT', 'GNSUSDT', 'SYNUSDT', 'VIBUSDT', 'SSVUSDT',
         'LQTYUSDT', 'AMBUSDT', 'USTCUSDT', 'GASUSDT', 'GLMUSDT', 'PROMUSDT', 'QKCUSDT', 'UFTUSDT', 'IDUSDT', 'ARBUSDT', 'RDNTUSDT', 'WBTCUSDT', 'EDUUSDT', 'SUIUSDT', 'AERGOUSDT',
         'PEPEUSDT', 'FLOKIUSDT', 'ASTUSDT', 'SNTUSDT', 'COMBOUSDT', 'MAVUSDT', 'PENDLEUSDT', 'ARKMUSDT', 'WBETHUSDT', 'WLDUSDT', 'FDUSDUSDT', 'SEIUSDT', 'CYBERUSDT', 'ARKUSDT',
         'CREAMUSDT', 'IQUSDT', 'NTRNUSDT', 'TIAUSDT', 'MEMEUSDT', 'ORDIUSDT', 'BEAMXUSDT', 'PIVXUSDT', 'VICUSDT', 'BLURUSDT', 'VANRYUSDT', 'AEURUSDT', 'JTOUSDT', '1000SATSUSDT',
         'BONKUSDT', 'ACEUSDT', 'NFPUSDT', 'AIUSDT', 'XAIUSDT', 'MANTAUSDT', 'ALTUSDT', 'JUPUSDT', 'PYTHUSDT', 'RONINUSDT', 'DYMUSDT', 'PIXELUSDT', 'STRKUSDT', 'PORTALUSDT',
         'PDAUSDT', 'AXLUSDT', 'WIFUSDT', 'METISUSDT', 'AEVOUSDT', 'BOMEUSDT', 'ETHFIUSDT', 'ENAUSDT', 'WUSDT', 'TNSRUSDT', 'SAGAUSDT', 'TAOUSDT', 'OMNIUSDT', 'REZUSDT', 'BBUSDT',
         'NOTUSDT', 'IOUSDT', 'ZKUSDT', 'LISTAUSDT', 'ZROUSDT', 'GUSDT', 'BANANAUSDT', 'RENDERUSDT', 'TONUSDT', 'DOGSUSDT', 'EURIUSDT', 'SLFUSDT', 'POLUSDT', 'NEIROUSDT',
         'TURBOUSDT', '1MBABYDOGEUSDT', 'CATIUSDT', 'HMSTRUSDT', 'EIGENUSDT', 'SCRUSDT', 'BNSOLUSDT', 'LUMIAUSDT', 'KAIAUSDT', 'COWUSDT', 'CETUSUSDT', 'PNUTUSDT', 'ACTUSDT',
         'USUALUSDT', 'THEUSDT', 'ACXUSDT', 'ORCAUSDT', 'MOVEUSDT', 'MEUSDT', 'VELODROMEUSDT', 'VANAUSDT', '1000CATUSDT', 'PENGUUSDT', 'BIOUSDT', 'DUSDT']

    rrr=[]  # 存储交易对名称和交易额
    rrr2=[]  # 只存储交易对名称

    # 统计最近7日的交易额, 并以BTC的日期进行对齐验证
    with open(f"data/BTCUSDT_1d.txt", 'r', encoding='utf-8-sig', newline='\r\n') as f:
        uuu=json.loads(f.read())
    start_id=uuu[-7][0]
    end_id=uuu[-1][0]
        
    for bb in bbb:
        if os.path.exists(f"data/{bb}_1d.txt"):
            with open(f"data/{bb}_1d.txt", 'r', encoding='utf-8-sig', newline='\r\n') as f:
                uuu=json.loads(f.read())
        else:
            uuu=[]

        if len(uuu)>=7:  # 保证交易天数大于7天, 因为可能会有一些刚上架的新币
            if uuu[-7][0]==start_id and uuu[-1][0]==end_id:  # 与BTC的日期进行对齐校验
                usdts=sum([x[7] for x in uuu[-7:]])  # 统计近7日的交易总额
                rrr.append([bb,usdts])

    rrr=sorted(rrr, key=lambda x: x[1], reverse=True)  # 按交易额从大到小进行排序
    rrr2=[x[0] for x in rrr]
    print(rrr2)  # 按交易额排序后的交易对名称列表一次性全部输出

    for rr in rrr:  # 循环输出交易对名称和交易额
        print(rr)
       
    print("--End--")
