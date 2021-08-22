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
3. Copy the rc.local file to the /etc directory.
```
sudo cp rc.local /etc/
sudo chmod +x /etc/rc.local
```
