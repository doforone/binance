# -*- coding: UTF-8 -*-

from urllib import request, parse
from urllib.parse import quote
import urllib.parse

import time
import datetime
import json
import base64
import hashlib
import random
import os
import io
import zipfile
import zlib

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


f0=lambda x: 0.0 if x=="" else float(x)


def get_htmll(urll,dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    print(urll)
    if 1:
        global htmll
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            req = request.Request(urll, headers=headers)
            with request.urlopen(req, timeout=6000) as resp:
                htmll=resp.read().decode("utf-8")
        except Exception as e:
            htmll=""


def get_htmll2(urll, p, dataa=None):     #请求页面，这个函数要用线程，长时间不响应就杀死线程，参数5秒有时不起作用
    #headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36'}
    
    #data={"areaSn":"","entType":"02","entName":"","pageIndex":p}
    #data={"jjrSel":"","p":p}
    data=dataa
    data=urllib.parse.urlencode(data,encoding='utf-8')
    data=bytes(data,'utf-8')
    
    try:
        #req = request.Request(urll, headers=headers)
        req = request.Request(urll, headers=headers, data=data, method="POST")
        with request.urlopen(req, timeout=6000) as resp:  # ===================
            #htmll=resp.read().decode("GBK","ignore")
            htmll=resp.read().decode("utf-8","replace")
            #with open('aaa.txt', 'a', encoding='utf-8', newline='\r\n') as f:
                #f.write(htmll)
            return htmll
    except Exception as e:
        print(e)
        htmll=""
        with open(f'err.txt', 'a', encoding='utf-8', newline='\r\n') as f:
            f.write(str(p)+"\r\n")
        return htmll


if __name__ == "__main__":

##    iof=io.BytesIO()
##    with zipfile.ZipFile("00000a.rar", 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as myzip:
##        # 逐个将文件添加到压缩包中
##        for f in ["BTCUSDT_15m.txt"]:
##            myzip.write(f"{f}")
##
##    # 压缩完成
##    print('压缩完成！')
##    
##
##    data = iof.getvalue()
##    print(len(data))
##    #md5_hash = hashlib.md5(data).hexdigest()
##    data = base64.b64encode(data)  # 将二进制数据编码为Base64字符串
##    print(data)
##    print(len(data))


    with open('000_new_data_1d.txt', 'rb') as f:
        ddd=f.read()
    ddd=zlib.compress(ddd, level=6)
    ddd = base64.b64encode(ddd)

    data={"key":"fa8a78877cddffa7d1899de36823ed9b", "path":"010","cycle":"1d","k_data":ddd}
    #rrr=get_htmll2("http://127.0.0.1:5121/extend_K_line.py", 1, dataa=data)
    rrr=get_htmll2("https://www.abtrue.com:5121/extend_K_line.py", 1, dataa=data)
    #rrr=get_htmll2("http://www.abtrue.com:5121/extend_K_line.py", 1, dataa=data)
    print(rrr)

    print("--end--")

