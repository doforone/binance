##def gen():
##    for i in range(1,10):
##        yield i
##
##g = gen()
##for i in g:
##    print(i)



def gen():
    while True:
        i = 0
        x = yield i
        if x == 0:
            break
        i = i*x
g = gen()
print(g.send(None))
print(g.send(1))
#print(g.send(2))
#print(g.send(0))

print("--------------")

def f_str(f,d):
    #f为浮点数如：123，123.0000001，12e-4等格式，
    #d为小数点后位数，返回为字符串
    
    f=str(f).lower()  #1e-8 or 1E-8
    d=abs(int(d))  #本函数只操作小数点后位数

    if (s:=f.find("e-"))>-1:
        f=f"{float(f):0.{-int(f[s+1:])}f}"
    elif (s:=f.find("e"))>-1:
        f=f"{float(f):0.0f}"

    if (s:=f.find("."))>-1 and (l:=len(f))-s-1>d:
        f=f[:s+1+d]

    if f.find(".")>-1:
        for i in range(len(f)-1,-1,-1):
            if f[i]!="0":
                f=f[:i+1]
                break
    
    if f[-1]==".":
        f=f[:-1]
        
    return f


print(f_str("12.388888923", 3))
        
##aaa="abc123"
##for aa,bb in enumerate(aaa[::-1]):
##    print(aa)
##    print(bb)

def stop_t(t):
    timee_1=time.time()
    alivee=1
    while alivee==1:
        time.sleep(1)
        t_21=time.time()-timee_1
        alivee=0
        for symbol in ddd["symbols"].keys():
            if ddd["symbols"][symbol]['oth']!=0:
                if ddd["symbols"][symbol]['oth'].is_alive():
                    alivee=1
                    if t_21>10:
                        stop_thread(ddd["symbols"][symbol]['oth'])
                        ddd["symbols"][symbol]['oth']=0
                        print("强制结束线程：K_line  "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        alivee=0
                else:
                    ddd["symbols"][symbol]['oth']=0







                                        
