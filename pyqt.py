# from PyQt5 import QtWidgets
# #从PyQt 库导入QtWidget 通用窗口类
# class firstwindows(QtWidgets.QWidget):
# #自己建一个mywindows类，以class 开头， mywindows是自己的类名，
# #（QtWidgets.QWidget ）是继承QtWidgets.QWidget 类方法，
# # 定义类或函数不要忘记':' 符号，判断语句也必须以':' 结尾！
#     def __init__(self):
#         #def 是定义函数（类方法）了，同样第二个__init__ 是函数名
#         # (self) 是pyqt 类方法必须要有的，代表自己，相当于java ，c++中的this
#         #其实__init__ 是析构函数，也就是类被创建后就会预先加载的项目
#         super(firstwindows, self).__init__()
#         #这里我们要重载一下mywindows同时也包含了QtWidgets.QWidget 的预加载项
#
# def mainwindows():
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     #pyqt 窗口必须在QApplication 方法中使用，
#     #要不然会报错 QWidget: Must construct a QApplication before a QWidget
#     new = firstwindows()
#     # 生成过一个实例（对象） , windows 是实例（对象）的名字，可以随便起！
#     # mywindows（）是我们上面自定义的类
#     new.show()
#     #有了实例，就得让他显示这里的show() 是QWidget的方法，用来显示窗口的！
#     sys.exit(app.exec_())
#     #启动事件循环
#
#
# if __name__ == "__main__":
#     mainwindows()


import OpenOPC  #导入模块
opc = OpenOPC.client()
opc.servers()   #列出本机中所有opc server清单
opc.connect(u'Takebishi.Melsec.1') #从opc server清单中选择需要连接的服务
opc.read('PLC1.A01.BldCntL')  #读取指定设备Device，组Group，标签Tag的数据