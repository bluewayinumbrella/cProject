#!/usr/bin/python
#-*- coding: utf-8 -*-

from AppStore import *


from common import *
# logError(blabla)
# filterList(list, filter)
# isNetworkAlive(addr, maxSec=5)


site = "http://android.myapp.com/myapp"
keyword = "/detail.htm?apkName"


obj = AppStore()
obj.searchInBing(site, keyword)
print("test completed")
