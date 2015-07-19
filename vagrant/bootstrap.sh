#!/usr/bin/env bash

apt-get update

########### install server dependencies
apt-get -y install python3-dev
apt-get -y install python3-pip
apt-get -y install libpq-dev
apt-get -y install postgresql-9.3

########## install project dependencies
cd /vagrant ; pip3 install -r requirements/local.txt

########## setup postgres
sudo -u postgres bash -c "psql -c \"CREATE USER vagrant WITH PASSWORD 'vagrant';\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE osa;\""
sudo -u postgres bash -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE osa to vagrant;\""

########## migrate the db
sudo -H -u vagrant bash -c 'cd /vagrant/osa; python3 manage.py migrate'

########## print info
echo "Your machine is ready, just run:"
echo "vagrant ssh"
echo "And inside the machine run the server:"
echo "cd /vagrant/osa; python3 manage.py runserver 0.0.0.0:8000"
echo ""

