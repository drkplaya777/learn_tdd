Provisioning a new site
=======================


## Required Packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo ad-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git pythn36 python3.6-venv
    
## Nginx Virutal Host ocnfig

* see enginz.temlate.conf
* repalce DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* See gunicorn-systemd.template.service
* repalce DOMAIN with, e.g., staging.my-domain.com

## Folder Structure

Assume we have a user account at /home/username

/home/usernmae
|__ sites
    |__ DOMAIN1
        |__ .env
        |__ db.sqlite3
        |__ manage.py etc
        |__ static
        |__ virtualenv
    |__ DOMAIN2
        |__ .env
        |__ db.sqlite3
        |__ etc
