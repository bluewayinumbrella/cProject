#-*- coding: utf-8 -*-
import sys

def logError(msg):
    sys.stderr.write(msg+"\n")

def filterList(strList, conditionWord):
    # Make list in which all element contains conditionWord

    filteredList = []
    for string in strList:
        if string.find(conditionWord) != -1:
            filteredList.append(string)
        else:
            pass

    return filteredList

def isNetworkAlive(addr, maxSec=5):
    # try connect with timeout argument
    # catch exception timeout event
    try:
        requests.get(url=addr, timeout=maxSec)
        return True
    except:
        logError('Network state is abnormal!' + \
        'Check market server("{0}") and local network state.'.format(addr))
        return False

