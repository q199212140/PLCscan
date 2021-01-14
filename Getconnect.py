import snap7

class PLC:
    def __init__(self, plcadr):
        # 设置PLC的连接地址
        if(plcadr[0] == ""):
            print("请输入一个PLC的IP")
        else:
            self.ip = plcadr[0]
            #ip = '10.200.83.2'  # PLC的ip地址
        if(plcadr[1] == ""):
            self.rack = 0
        else:
            self.rack = plcadr[1]
        if(plcadr[2] == ""):
            self.slot = 2  # 插槽号
        else:
            self.slot = plcadr[2]
        if(plcadr[3] == ""):
            self.tcpport = 102  # TCP端口号
        else:
            self.tcpport = plcadr[3]

        self.client = ""

    def Connect(self):
        # 建立连接
        client = snap7.client.Client
        client = client.connect(self.ip, self.rack, self.slot, self.tcpport)
        self.client = client

        print('ok')
        return(client)


#
# def readarea(client, areanam, DBnumber, start, Bnum, amount, bitnum):
#     # 判断是I QM DB还是C T
#     if (areanam == "I"):
#         area = snap7.snap7types.areas.PE
#     elif (areanam == "Q"):
#         area = snap7.snap7types.areas.PA
#     elif (areanam == "M"):
#         area = snap7.snap7types.areas.MK
#     elif (areanam == "DB"):
#         area = snap7.snap7types.areas.DB
#     elif (areanam == "C"):
#         area = snap7.snap7types.areas.CT
#     elif (areanam == "T"):
#         area = snap7.snap7types.areas.TM
#     else:
#         print("格式错误，请重新输入")
#         return
#
#     Bamount = Bnum * amount  # 总计多少字节的缓存
#     # 判断一个数据包括多少字节，如果bit为07则输出位数据
#     if (Bnum == "") or (Bnum == 1):
#         Bnum == 1
#         if (bitnum == ''):
#             size = '!' + 'B' * amount
#         elif (bitnum >= 0 and bitnum <= 7):
#             size = '!' + 'B'
#             Bamount = 1
#             amount = 1
#         else:
#             print("数据大小或位数错误")
#             return
#     elif (Bnum == 2):
#         size = '!' + 'H' * amount
#     elif (Bnum == 4):
#         size = '!' + 'I' * amount
#     else:
#         print("数据大小错误")
#         return
#
#     result = client.read_area(area, DBnumber, start, Bamount)
#     word = []
#     word1 = struct.unpack(size, result)
#     for i in range(amount):
#         word.append(int(word1[i]))
#         if bitnum != '':
#             if (bitnum >= 0) and (bitnum <= 7):
#                 # 1B拆开为8bit
#                 wl = ['' for i in range(8)]
#                 word = bin(word[i])
#                 word = str(word)
#                 if (word == "0b0"):
#                     return (0)
#                 for j in range(8):
#                     if (word[9 - j] is not None):
#                         wl[j] = word[9 - j]
#                 word = wl[bitnum]
#     return (word)
