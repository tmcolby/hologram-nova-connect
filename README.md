# hologram-nova-connect
Do you have a Nova modem from Hologram.io?  Do you have a RaspberryPi?  Do you want to be able to simply plug in your USB Nova modem and have it automatically establish a data session with the Hologram network?  Great.. follow along.

python script w/hologram sdk methods, systemd service file, systemd timer file, and dead simple install script are included in this git repo.

## What it does..
A systemd timer fires off every 15 seconds or so..

..it checks to see if the Nova modem is enumerated on the USB bus.  If it is, it waits for the modem to establish a connection with an operator (TMobile, Versizon, AT&T, etc).  Once
it connects with a carrier, it will start a data session and bring up a PPP interface and add appropriate routes.

..if the Nova modem is removed from USB, the service will detect this and clean up and kill any lingering PPP interface and routes.

## Install
Clone this git repo and run the `install.sh` script.

#### Notes
This currently is set to look for the Nova 2G/3G modem.  If you are using the LTE Cat-M1 modem, modify the idProduct string in the hologram.py file.

The install script is not comprehensive.  It assumes you have https://github.com/hologram-io/hologram-python installed already.

You may need to install some python depencies.  You can do a `sudo pip install -r requirements.pip`.
