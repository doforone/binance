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
    htmll=""
    #aaa={"1m":60, "3m":180, "5m":300, "15m":900, "30m":1800, "1h":3600, "2h":7200, "4h":14400, "6h":21600, "8h":28800, "12h":43200, "1d":86400, "3d":259200, "1w":604800}
    #aaa={"15m":900, "30m":1800, "1h":3600, "1d":86400}
    aaa={"1d":86400}
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
    bbb2=['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'GASBTC', 'LRCBTC', 'QTUMBTC', 'ZRXBTC', 'KNCBTC', 'IOTABTC', 'LINKBTC', 'MTLBTC', 'EOSBTC', 'SNTBTC', 'ETCBTC', 'ZECBTC',
          'DASHBTC', 'REQBTC', 'VIBBTC', 'TRXBTC', 'POWRBTC', 'XRPBTC', 'ENJBTC', 'STORJBTC', 'KMDBTC', 'NULSBTC', 'BATBTC', 'LSKBTC', 'MANABTC', 'ADXBTC', 'ADABTC', 'XLMBTC',
          'ICXBTC', 'ELFBTC', 'RLCBTC', 'PIVXBTC', 'STEEMBTC', 'ZILBTC', 'ONTBTC', 'WANBTC', 'SYSBTC', 'ZENBTC', 'THETABTC', 'IOTXBTC', 'DATABTC', 'ARDRBTC', 'VETBTC', 'RVNBTC',
          'ONGBTC', 'FETBTC', 'CELRBTC', 'ATOMBTC', 'PHBBTC', 'TFUELBTC', 'ONEBTC', 'ALGOBTC', 'DOGEBTC', 'DUSKBTC', 'ANKRBTC', 'CHZBTC', 'BANDBTC', 'XTZBTC', 'HBARBTC', 'NKNBTC',
          'STXBTC', 'KAVABTC', 'ARPABTC', 'CTXCBTC', 'BCHBTC', 'VITEBTC', 'OGNBTC', 'LTOBTC', 'COTIBTC', 'STPTBTC', 'SOLBTC', 'CTSIBTC', 'HIVEBTC', 'CHRBTC', 'MDTBTC', 'COMPBTC',
          'SXPBTC', 'SNXBTC', 'MKRBTC', 'RUNEBTC', 'FIOBTC', 'AVABTC', 'YFIBTC', 'JSTBTC', 'CRVBTC', 'SANDBTC', 'NMRBTC', 'DOTBTC', 'IDEXBTC', 'PAXGBTC', 'TRBBTC', 'WBTCBTC',
          'SUSHIBTC', 'KSMBTC', 'EGLDBTC', 'DIABTC', 'UMABTC', 'BELBTC', 'UNIBTC', 'OXTBTC', 'AVAXBTC', 'FLMBTC', 'SCRTBTC', 'XVSBTC', 'ALPHABTC', 'VIDTBTC', 'AAVEBTC', 'NEARBTC',
          'FILBTC', 'INJBTC', 'AUDIOBTC', 'CTKBTC', 'AXSBTC', 'STRAXBTC', 'ROSEBTC', 'SKLBTC', 'GLMBTC', 'GRTBTC', '1INCHBTC', 'OGBTC', 'CELOBTC', 'RIFBTC', 'TRUBTC', 'TWTBTC',
          'LITBTC', 'SFPBTC', 'DODOBTC', 'CAKEBTC', 'AUCTIONBTC', 'PHABTC', 'BADGERBTC', 'FISBTC', 'OMBTC', 'PONDBTC', 'ALICEBTC', 'PERPBTC', 'SUPERBTC', 'CFXBTC', 'TKOBTC',
          'TLMBTC', 'FORTHBTC', 'ICPBTC', 'ARBTC', 'LPTBTC', 'ATABTC', 'GTCBTC', 'BAKEBTC', 'MLNBTC', 'CLVBTC', 'QNTBTC', 'FLOWBTC', 'MINABTC', 'MBOXBTC', 'WAXPBTC', 'DYDXBTC',
          'GALABTC', 'ILVBTC', 'YGGBTC', 'FIDABTC', 'AGLDBTC', 'RAREBTC', 'SSVBTC', 'BNXBTC', 'MOVRBTC', 'ENSBTC', 'QIBTC', 'PYRBTC', 'SANTOSBTC', 'BICOBTC', 'FLUXBTC', 'HIGHBTC',
          'PEOPLEBTC', 'JOEBTC', 'ACHBTC', 'IMXBTC', 'GLMRBTC', 'LOKABTC', 'API3BTC', 'ACABTC', 'XNOBTC', 'WOOBTC', 'GMTBTC', 'KDABTC', 'APEBTC', 'ASTRBTC', 'NEXOBTC', 'LDOBTC',
          'OPBTC', 'STGBTC', 'POLYXBTC', 'APTBTC', 'HFTBTC', 'MAGICBTC', 'LQTYBTC', 'IDBTC', 'ARBBTC', 'EDUBTC', 'SUIBTC', 'MAVBTC', 'PENDLEBTC', 'ARKMBTC', 'WLDBTC', 'SEIBTC',
          'CYBERBTC', 'TIABTC', 'ORDIBTC', 'VICBTC', 'BLURBTC', 'VANRYBTC', 'NFPBTC', 'AIBTC', 'XAIBTC', 'MANTABTC', 'ALTBTC', 'PYTHBTC', 'RONINBTC', 'PIXELBTC', 'STRKBTC',
          'PORTALBTC', 'AXLBTC', 'WIFBTC', 'AEVOBTC', 'ETHFIBTC', 'ENABTC', 'WBTC', 'TNSRBTC', 'SAGABTC', 'TAOBTC', 'OMNIBTC', 'REZBTC', 'BBBTC', 'IOBTC', 'ZKBTC', 'ZROBTC',
          'BANANABTC', 'RENDERBTC', 'TONBTC', 'SLFBTC', 'POLBTC', 'EIGENBTC', 'SCRBTC', 'PNUTBTC', 'THEBTC', 'MOVEBTC', 'MEBTC', 'USUALBTC']
    bbb.extend(bbb2)
    ccc=[[bb,aa] for bb in bbb for aa in aaa.keys()]  # aaa与bbb两个列表嵌套循环生成ccc列表, 为后面的请求数据做准备
    
    if not os.path.exists(f"DATA/"):  # DATA文件夹不存在就创建, 一般只用于第一次
        os.mkdir(f"DATA/")

    limit=1000  # 币安一次请求的最大条数
    again=0  # 控制循环
    while ccc!=[]:
        time.sleep(.1)
        print(ccc[-1])
        if again==0:
            if os.path.exists(f"data/{ccc[-1][0]}_{ccc[-1][1]}.txt"):
                with open(f"data/{ccc[-1][0]}_{ccc[-1][1]}.txt", 'r', encoding='utf-8-sig', newline='\r\n') as f:
                    uuu=json.loads(f.read())
            else:
                uuu=[]
            
            if uuu==[]:
                start_id=0
            else:
                #start_id=uuu[-1][0]+aaa[ccc[-1][1]]*1000  #  下一个的K线起始时间, 因为币安的时间戳是精确到毫秒的
                start_id=uuu[-1][0]*1000+aaa[ccc[-1][1]]*1000  #  这是精简后的数据, 最后保存的时间戳要*1000, 下一个的K线起始时间, 因为币安的时间戳是精确到毫秒的

        urll=f"https://api4.binance.com/api/v3/klines?symbol={ccc[-1][0]}&interval={ccc[-1][1]}&startTime={str(start_id)}&limit={limit}"
        print(urll)

        try:
            htmll=get_htmll(urll=urll)
            vvv=json.loads(htmll)
            
            if len(vvv)<limit:
                #uuu.extend(vvv[:-1])
                #  以下语句, 对列表格式进行了精简, 利于节省存储空间
                uuu.extend([[int(x[0]/1000), f0(x[1]), f0(x[2]), f0(x[3]), f0(x[4]), f0(x[5]), x[6], f0(x[7]), x[8], f0(x[9]), f0(x[10])] for x in vvv[:-1]])
                with open(f"data/{ccc[-1][0]}_{ccc[-1][1]}.txt", 'w', encoding='utf-8', newline='\r\n') as f:
                    f.write(json.dumps(uuu, indent=0, ensure_ascii=False)+"\r\n")
                ccc.pop()  # 删除最后一个。
                again=0  # 下一次循环时读取文件
            else:
                #uuu.extend(vvv[:-1])
                #  以下语句, 对列表格式进行了精简, 利于节省存储空间
                uuu.extend([[int(x[0]/1000), f0(x[1]), f0(x[2]), f0(x[3]), f0(x[4]), f0(x[5]), x[6], f0(x[7]), x[8], f0(x[9]), f0(x[10])] for x in vvv[:-1]])
                start_id=vvv[-1][0]+aaa[ccc[-1][1]]*1000  # 此项不需要修改, 因为vvv是原始数据, 而非精简后的数据
                again=1  # 因为还需要继续请求数据, 本次并没有写入, 所以下次也不能重新打开文件进行读取
                
        except Exception as e:
            print(e)
            pass

    print("--End--")
