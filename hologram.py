#/usr/bin/env python
from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)
from builtins import *

from Hologram.CustomCloud import CustomCloud
from Exceptions.HologramError import HologramError

import json
import psutil
import subprocess
import time

import hologram

def modem_connect():
    """
    establish ppp connection to hologram network
    """
    try:
        cloud = CustomCloud(None, network='cellular')
        cloud.network.disable_at_sockets_mode()
        cloud.network.connect()
    except Exception as e:
        print(e)
        hologram.modem_disconnect()
        

def modem_disconnect():
    pppPid = hologram.modem_connection_status()
    if pppPid:
       print('Killing pid {} now'.format(pppPid))
       psutil.Process(pppPid).terminate()

def modem_connection_status():
    print('Checking for existing PPP sessions')
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except:
            raise HologramError('Failed to check for existing PPP sessions')
            return False

        if 'pppd' in pinfo['name']:
            print('Found existing PPP session on pid: {}'.format(pinfo['pid']))
            return pinfo['pid']
            # print 'Killing pid %s now' % pinfo['pid']
            # psutil.Process(pinfo['pid']).terminate()
    print('No PPP session running. Not Connected')
    return False

def modem_sim():
    cloud = CustomCloud(None, network='cellular')
    print('ICCID: {}'.format(str(cloud.network.iccid)))

def modem_operator():
    cloud = CustomCloud(None, network='cellular')
    print('Operator: {}'.format(str(cloud.network.operator)))

def modem_type():
    cloud = CustomCloud(None, network='cellular')
    print('Type: {}'.format(str(cloud.network.description)))

def main():
    while True:
        if not hologram.modem_connection_status():
            hologram.modem_connect();
        time.sleep(10)


if __name__ == "__main__":
    main()
