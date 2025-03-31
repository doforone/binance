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


if __name__ == "__main__":
    rrr=[]
    rrr2=[]
    rrr3=[]
    
    if os.path.exists(f'001.txt'):
        with open(f'001.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
            uuu=json.loads(f.read())

        for uu in uuu["symbols"]:
            if uu["status"]=="TRADING" and "LIMIT" in uu["orderTypes"] and "MARKET" in uu["orderTypes"]:
                rrr.append(uu["symbol"])
                if uu["symbol"][-4:]=="USDT":
                    rrr2.append(uu["symbol"])

                if uu["symbol"][-3:]=="BTC":
                    rrr3.append(uu["symbol"])
    else:
        print("文件不存在")

    print(rrr)
    print(f"全部交易对共: {len(rrr)}交易对")
    print(rrr2)
    print(f"以USDT计价的交易对共: {len(rrr2)}")
    print(rrr3)
    print(f"以BTC计价的交易对共: {len(rrr3)}")


    print("-- End --")
