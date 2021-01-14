## 利用python-snap7 连接西门子s7系列plc，进行数据读写操作

很久没起了，有时间再跑起来。有几个注意事项。


1.拷贝dll插件
拷贝dll和lib
解压snap7-full-1.4.2，找到release\windows\win32下的的snap7.dll和snap7.lib，
分别拷贝到Python的安装目录和系统windows下的SysWOW64下。
压缩包内容和参考文档见附件


2.snap7.dll好像只能是用在32位的python。否则会报错
OSError: [WinError 193] %1 不是有效的 Win32 应用程序。
可以用单独的32环境来启动

3安装snap7 
pip install python-snap7

4.可以用s7-300的plc仿真器和step7进行联调，具体记不清了

具体硬件设置方式，博图版参考
https://blog.csdn.net/lcb411/article/details/101936678

代码是19年初写过可用的。后面从维修转java了，代码没维护丢给其他有用的同事了。有机会我要个新版的过来完善一下。待尝试java版的连接程序
