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

if __name__ == "__main__":
    with open(r'币安交易对_new.txt', 'r', encoding='utf-8-sig', newline='\r\n') as f:
        ddd=json.loads(f.read())

    aaa=[]

    for dd in ddd["symbols"]:
        if dd["symbol"][-4:]=="USDT" and dd["status"]=="TRADING" and dd["symbol"].find("DOWNUSDT")==-1 and dd["symbol"].find("UPUSDT")==-1:
            #print(dd["symbol"])
            aaa.append(dd["symbol"])

    print(aaa)
    print(len(aaa))
    print("--end--")

