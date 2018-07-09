#!/bin/bash
sudo mkdir /opt/hologram
sudo cp hologram.py /opt/hologram

sudo cp hologram.service /lib/systemd/system/
sudo cp hologram.timer /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/hologram.service
sudo chmod 644 /lib/systemd/system/hologram.timer

sudo systemctl daemon-reload
sudo systemctl enable hologram.service
sudo systemctl enable hologram.timer
sudo systemctl start hologram.timer
