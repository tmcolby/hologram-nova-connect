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
import usb.core as usb

#ublox vendor and product codes
ubloxIdVendor=0x1546
ubloxIdProduct=0x1102

def modem_usb_find():
    return usb.find(idVendor=ubloxIdVendor, idProduct=ubloxIdProduct)

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
    #print('Checking for existing PPP sessions')
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except:
            raise HologramError('Failed to check for existing PPP sessions')
            return False

        if 'pppd' in pinfo['name']:
            #print('Found existing PPP session on pid: {}'.format(pinfo['pid']))
            return pinfo['pid']
            # print 'Killing pid %s now' % pinfo['pid']
            # psutil.Process(pinfo['pid']).terminate()
    #print('No PPP session running. Not Connected')
    return False

def modem_sim():
    cloud = CustomCloud(None, network='cellular')
    print('ICCID: {}'.format(str(cloud.network.iccid)))

def modem_operator():
    cloud = CustomCloud(None, network='cellular')
    print('Operator: {}'.format(str(cloud.network.operator)))
    return cloud.network.operator

def modem_type():
    cloud = CustomCloud(None, network='cellular')
    print('Type: {}'.format(str(cloud.network.description)))

def main():
    while True:
        hologramModemAttached = hologram.modem_usb_find()
        hologramPppRunning = hologram.modem_connection_status()
        if hologramModemAttached and not hologramPppRunning:
            print("Hologram modem attached to USB, but PPP is not running..")
            print("Cheecking if the modem is attached to an operator...")
            hologramModemOperator = hologram.modem_operator()
            if hologramModemOperator is not None:
                print("Modem attached to {}".format(hologramModemOperator))
                print("Attempting to connect a data session...")
                hologram.modem_connect()
        elif not hologramModemAttached and hologramPppRunning:
            print("Hologram modem not attached to USB, and PPP is running..")
            print("Killing PPP...")
            hologram.modem_disconnect()
        elif not hologramModemAttached and not hologramPppRunning:
            print("Hologram modem is not attached to USB.. :(")
        else:
            print("Hologram modem is attached to USB, and PPP is running.. Yay!")

        #if hologram.modem_usb_find():
        #    if not hologram.modem_connection_status():
        #        hologram.modem_connect();
        print("Sleeping now...")
        time.sleep(10)


if __name__ == "__main__":
    main()
