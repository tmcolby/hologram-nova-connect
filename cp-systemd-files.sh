#!/bin/bash
sudo cp hologram.service /lib/systemd/system/
#sudo cp hologram.path /lib/systemd/system/
sudo cp hologram.timer /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/hologram.service
#sudo chmod 664 /lib/systemd/system/hologram.path
sudo chmod 644 /lib/systemd/system/hologram.timer
sudo systemctl daemon-reload

