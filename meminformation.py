#! /usr/bin/env python
from collections import OrderedDict
import time
def meminfo(key=None):
    '''return the info of /proc/meminfo
    as a dictionary
    '''
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    if key is not  None and key in meminfo:
        return int(meminfo[key][:-3])
    return meminfo

if __name__ == '__main__':
    mem = meminfo()
    print("Free memory:{0}".format(meminfo('MemFree')))




