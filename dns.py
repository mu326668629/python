#coding=utf-8
"""
�Զ��޸�dns
ע��������غ���˵��:
OpenKey()
EnumKey()�о��Ӽ� ���൱���ļ���/
EnumValue() �о�ֵ(ֵ����һ��һ�Ե�) ������ֵ������
QueryInfoKey() ����(0,1,2) 0:�Ӽ����� 1:ֵ�ĸ��� 2:�޸�ʱ��
QueryValue()   û����
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


