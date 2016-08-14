'''
Test To check If class is working for Linc_Latency_get.py


'''

from link_latency_get import *

src = 'houston'
dst = 'dallas'
node = dst
intf = 'ge-0/1/3'
emp1 = RedisStatus(src,dst,node,intf)  
emp1.ErrorList()
emp1.AvergaeLatency()
#currentLatency()



