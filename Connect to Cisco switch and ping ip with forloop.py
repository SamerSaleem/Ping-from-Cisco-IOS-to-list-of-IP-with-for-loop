from pickle import PicklingError
from netmiko import ConnectHandler


SW={'username':'samer','password':'cisco','device_type':'cisco_ios','host':'10.211.10.36'}

SWconnect=ConnectHandler(**SW)
SWS=['10.211.1.150', '10.211.1.30']
for i in SWS:
    print(SWconnect)
    result=SWconnect.send_command('ping ' + i)
    print(result)
SWconnect.disconnect()
    