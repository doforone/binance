# -*- coding: UTF-8 -*-

import random

if __name__ == "__main__":

    summ=1000000
    aaa=[]

    for i in range(10000):
        x=random.random()
        y=int(summ*x)
        summ-=y
        aaa.append(y)
        
    print(aaa)
