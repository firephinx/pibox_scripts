# pibox_scripts

## Installation
1. Copy the scripts to /etc/systemd/system
```
cd systemd_services
sudo cp *.service /etc/systemd/system/
```
2. Change permissions of all the services to 644. Then enable them to start on boot.
```
sudo chmod 644 /etc/systemd/system/*.service
sudo systemctl enable 
```