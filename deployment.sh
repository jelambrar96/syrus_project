#!bin/sh
cd /var/www/syrus_project
git pull origin master
sudo service apache2 restart
