#!/usr/bin/env bash
# Configure a web server
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "Nginx Configuration" > /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-avaliable/default
service nginx restart
