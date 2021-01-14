#!/bin/python
#encoding=utf8
from tkinter import *
import snap7
from snap7.util import *
from functools import reduce
import time
import datetime




def readarea(areanam,DBnumber,start,Bnum,amount,bitnum):
    #判断是I QM DB还是C T
    if(areanam=="I"):
        area = snap7.snap7types.areas.PE
    elif(areanam=="Q"):
        area = snap7.snap7types.areas.PA
    elif(areanam=="M"):
        area = snap7.snap7types.areas.MK
    elif(areanam=="DB"):
        area = snap7.snap7types.areas.DB
    elif(areanam=="C"):
        area = snap7.snap7types.areas.CT
    elif(areanam=="T"):
        area = snap7.snap7types.areas.TM
    else:
        print("格式错误，请重新输入")
        return

    Bamount=Bnum*amount    #总计多少字节的缓存
    #判断一个数据包括多少字节，如果bit为07则输出位数据
    if(Bnum=="" )or (Bnum==1) :
        Bnum==1
        if (bitnum==''):
            size = '!'+'B'*amount
        elif(bitnum >=0 and bitnum <=7):
            size='!'+'B'
            Bamount=1
            amount=1
        else:
            print("数据大小或位数错误")
            return
    elif(Bnum==2):
        size = '!'+'H'*amount
    elif(Bnum==4):
        size ='!'+'I'*amount
    else:
        print("数据大小错误")
        return
    
    result = client.read_area(area, DBnumber, start, Bamount)
    word=[]
    word1 = struct.unpack(size, result)
    for i in range(amount):
        word.append(int(word1[i]))
        if bitnum!='':
            if(bitnum >= 0) and (bitnum <= 7):
                #1B拆开为8bit
                wl=['' for i in range(8)]
                word=bin(word[i])
                word=str(word)
                if(word=="0b0"):
                    return(0)
                for j in range(8):
                    if(word[9-j] is not None):
                        wl[j]=word[9-j]
                word=wl[bitnum]
    return(word)

    '''
    
    eg:snap7.snap7types.areas.PE = 0x81 =132
    areas = ADict({
    'PE': 0x81,  # Inputs 输入 I
    'PA': 0x82, # Outputs 输出 Q
    'MK': 0x83, # Merkers 临时点 M
    'DB': 0x84, # Timers DB块
    'CT': 0x1C, # Counters 计数器
    'TM': 0x1D, # Timers 计时器
    })

    
    #读取Q点
    start=200
    size=1
    result = client.ab_read(start,size)
    word1 = struct.unpack('!B', result)
    word1=int(word1[0])
    print(word1)
    '''
    

if __name__ == '__main__':


    plc = snap7.client.Client()
    # 设置PLC的连接地址
    ip = '10.200.150.2'  # PLC的ip地址
    rack = 0  # 机架号
    slot = 2  # 插槽号
    tcpport = 102  # TCP端口号

    # 建立连接
    client = snap7.client.Client()
    client.connect(ip, rack, slot, tcpport)
    print('ok')
   
    #DB
    area = "DB"
    DBnumber = 712
    start = 170
    start2 =140
    Bnum=1
    amount = 17
    amount2 =7
    bitnum=''

    delay=10
    while 1:
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print(datetime.datetime.now(),"循环间隔为：",str(delay),"s,起始地址",area+str(DBnumber)+"."+str(start),"长度为：",str(amount))
        
        word1 = readarea(area, DBnumber, start,Bnum, amount,bitnum)
        
        output=["" for i in range(len(word1))]
        for i in range(len(word1)):
            output[i] = chr(word1[i])
        print(output)

        print(datetime.datetime.now(),"循环间隔为：",str(delay),"s,起始地址",area+str(DBnumber)+"."+str(start2),"长度为：",str(amount2))
        
        word2 = readarea(area, DBnumber, start2,Bnum, amount2,bitnum)
        
        output=["" for i in range(len(word2))]
        for i in range(len(word2)):
            output[i] = chr(word2[i])
        print(output)

        print("")
        
        time.sleep(delay)




    '''
    #读取Q点 I 点
    area = "I"
    DBnumber = 0 #求I或者Q时无影响
    start = 0 #I或者Q的号(对8位数值使用）
    Bnum=1
    amount=10
    bitnum=''
    word1 = readarea(area, DBnumber, start,Bnum, amount,bitnum)    
    print(word1)
     '''

    # 断开连接
    client.disconnect()
    client.destroy()

