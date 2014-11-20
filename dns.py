#coding=utf-8
"""
自动修改dns
注册表操作相关函数说明:
OpenKey()
EnumKey()列举子键 键相当于文件夹/
EnumValue() 列举值(值都是一对一对的) 后面是值的类型
QueryInfoKey() 返回(0,1,2) 0:子键个数 1:值的个数 2:修改时间
QueryValue()   没明白
QueryValueEx()
"""
import _winreg
def listKEY_VALUE():
    print '--------------KEYS:'
    for i in range(numOfKey):
        subKey =  _winreg.EnumKey(hkey,i)
        h = _winreg.OpenKey(hkey,subKey)
        a,b,c  =_winreg.QueryInfoKey(h)
        print "--"+subKey+"Key:%d,Value:%d"%(a,b)
        for j in range(b):
            v = _winreg.EnumValue(h,j)
            print "--"*i+"%s=%s"%(v[0],type(v[1]))
        
    print "--------------VALUES:"
    for i in range(numOfValue):
        print _winreg.EnumValue(hkey,i)
def QueryValue(subkey):
    print _winreg.QueryValue(hkey,subkey)
def QueryValueEx(valueName): 
    print _winreg.QueryValue(hkey,valueName)  #valueName
key = r"SYSTEM\ControlSet001\services\Tcpip\Parameters\Interfaces" #\Parameters
hkey= _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,key)
numOfKey,numOfValue,lastTime  =_winreg.QueryInfoKey(hkey)
print "NumOfKey:%d,NumOfValue:%d, lastTime:%d"%(numOfKey,numOfValue,lastTime)
listKEY_VALUE()#DhcpDomain
#QueryValueEx("ICSDomain")


