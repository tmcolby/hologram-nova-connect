#/usr/bin/env python
from __future__ import (absolute_import,
                        division,
                        print_function,
                        unicode_literals)
from builtins import *

from Hologram.CustomCloud import CustomCloud
from Exceptions.HologramError import HologramError
#from hologram_util import handle_timeout
#from hologram_util import VAction

import json
import psutil
import subprocess
import time

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
            return True
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
