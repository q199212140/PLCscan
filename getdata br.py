#!/bin/python
#encoding=utf8
from tkinter import *
import snap7
from snap7.util import *
from functools import reduce
import time
import datetime
import time
from ReadData import readarea
#from Getconnect import connectPLC
from Getconnect import PLC
#from Getconnect import readarea

if __name__ == '__main__':
    plc1 = ["" for i in range(4)]
    plc1[0] = '10.200.82.2'
    #client = PLC(plc1)
    DURR1 = PLC.Connect(plc1)
    print((DURR1))
    #client1 = DURR1.Connect()
    # recordnum = 0
    # fname=str(datetime.datetime.now())[:13]+"-"+str(datetime.datetime.now())[14:16]
    # f = open(fname + '.xls', 'w')
    # f.write("系统时间"+'\t'+ "当前命令B"+'\t'+"当前状态Z"+'\t'+"前一B"+'\t'+"前一Z"+'\t'+"持续时间"+'\n' )

    # #DB
    # area = "DB"
    # DBnumber = 1112
    # DBnumber2 = 1114
    #
    # start = 12
    # Bnum=2
    # amount = 1
    # bitnum=''
    #
    # start2 = 98
    # Bnum2=1
    # amount2=17
    #
    # delay = 0.01
    # word1 = ""
    # word2 = ""
    # temprequest = ""
    # tempstate = ""
    # reqtime = 0
    # statetime = 0
    # cyclenum = 0
    #
    # Voutput = ["" for i in range(17)]
    # lastVIN = ["x" for i in range(17)]
    # VINtotal = ""
    # time_start = time.time()
    # time1_start = time.time()
    #
    # for i in range(1):
    # # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #     #print(datetime.datetime.now(),"循环间隔为：",str(delay),"s,起始地址",area+str(DBnumber)+"."+str(start),"长度为：",str(amount))
    #
    #     word1 = readarea(client1,area, DBnumber, start,Bnum, amount,bitnum)
    #     word2 = readarea(client1,area, DBnumber2, start,Bnum, amount,bitnum)
    #     VIN = readarea(client1,area, DBnumber, start2,Bnum2, amount2,bitnum)
    #
    #
    #
    #     if((VIN[0]!=0)and(lastVIN!=VIN)):
    #
    #         for i in range(17):
    #             Voutput[i] = chr(VIN[i])
    #             VINtotal = VINtotal +str(Voutput[i])
    #
    #         print("当前车号：" + VINtotal)
    #         f.write(VINtotal+'\n')
    #         VINtotal = ""
    #         lastVIN = VIN
    #         cyclenum = cyclenum+1
    #
    #     if((temprequest != str(word1[0])) or (tempstate != str(word2[0]) )):
    #         if(tempstate != str(word2[0])):
    #             # time_end=time.time()
    #             # time_start=time.time()
    #             time1_end = time.time()
    #             zcosttime = (time1_end - time1_start)
    #             print("前一Z" + tempstate, "状态持续时间:", "%.3f" % (time1_end - time1_start), "s")
    #             time1_start = time.time()
    #
    #         print(datetime.datetime.now(), ",当前B" + str(word1[0]), ",Z" + str(word2[0]))
    #         f.write(str(datetime.datetime.now())+'\t'+ str(word1[0])+'\t'+str(word2[0])+'\t'+"--"+'\t'+tempstate+'\t'+str("%.3f" % (zcosttime))+'\t'+'\n' )
    #
    #         temprequest = str(word1[0])
    #         tempstate = str(word2[0])
    #
    #
    #     #time.sleep(delay)
    #     if(cyclenum ==3):
    #         cyclenum=0
    #
    #         f.close()
    #         recordnum = recordnum +1
    #         fname = str(datetime.datetime.now())[:13]+"-"+str(datetime.datetime.now())[14:16]
    #         f=open(fname+'.xls','w')
    #         f.write("系统时间"+'\t'+ "当前命令B"+'\t'+"当前状态Z"+'\t'+"前一B"+'\t'+"前一Z"+'\t'+"持续时间"+'\n' )
    #
    # # 断开连接
    # client.disconnect()
    # client.destroy()
    #
