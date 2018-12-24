Purpose: To jot down anything I find interesting in my readings

# Nginx vs Apache
    - NEED TO DO MORE RESEARCH TO FULLY UNDERSTAND DIFFERENCES (Do I care???)
    - Nginx is considered the new hotness
    - Apache is considered old and bloated
    - Main differences I see is the execution model
        - How each deals with processing requests
        - Apache
            - 1) Creates a new process for each connection with no threading
            - 2) Creates a new process for each connection along with threading 
            - 3) Does an event model I don't understand yet
            - Due to creating processes per request, more expensive memory wise
            - Keeps a pool of workers ready for connections
        - Nginx
            - 1) Doesn't create a worker per connection
            - 2) Worker should be created per CPU
            
            
# Spoof a domain
    - Just add an entry to the /etc/hosts file
    $ sudo cat /etc/hosts
        127.0.0.1	localhost
        127.0.1.1	Havoc
        127.0.0.1   superlists-staging.jlw
        
# WSGI (Web Server Gateway Interface)
    - Standard way of running python web applications
    - Exposes a callable which returns an `application` 
    - The WSGI marrys the `application` to web server

# Fuctional tests running against staging vs locally
    - Update functional tests(integrated tests) to check for environment variable named
    STAGING. If set, all post requests should go to that URL. If not set, run against local
    developmenet server. 
    
    
# How to run functional tests in Django
    - Need a directory named `functional_tests`
        - Needs to contain `tests.py`
    - python manage.py test functional_tests
    - passing --failfast will force test to stop at first failure
        - python manage.py test functional_tests --failfast
        
# How to setup Nginx to reverse proxy to Gunicorn via unix socket
    - Create site file in sites-available
        -e.g. /etc/nginx/sites-available/superlists-staging.jlw
    - Add unix socket path to reverse proxy in location block in site file 
        -e.g. location / {
        proxy_pass http://unix:/tmp/superlists-staging.jlw.socket;
    }
    - Bind Gunicorn to same unix socket path
        - e.g. ./virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging.jlw.socket superlists.wsgi:application
        
# How to ensure that production config requires key values
    - Check for the existance of a flag. If flag present, then grab items from application environment
    using dictionary access
        - All entries that should be required, will throw key errors if not present
    - If flag doesn't exist in os.environ
        - Use development config
    e.g. if 'DJANGO_DEBUG_FALSE' in os.environ:
            DEBUG = False
            SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
            ALLOWED_HOSTS = [os.environ['SITENAME']]
         else:
            DEBUG = True
            SECRET_KEY = 'insecure-key-for-dev'
            ALLOWED_HOSTS = []
            
            
# When doing a reverse proxy from Nginx, the client headers are stripped out. In order to retrieve the 
client request hostname, you must tell Nginx to pass the hostname along. You use a predefined variable 
within Nginx to pass the host, named $host. See variables here: http://nginx.org/en/docs/http/ngx_http_core_module.html#variables

    e.g. location / {
        proxy_pass http://unix:/tmp/superlists-staging.jlw.socket;
        proxy_set_header Host $host;
    }

# Use name of variable to denote intent. (I'll fill this out more the more I learn)

e.g. DEBUG_DJANGO_FALSE

# Systemd is daemon Ubuntu uses to manage services. These services are started on default if they are placed in the correct directory.
# Each directory appears to mean a certain runlevel. Files must be named <name>.service. You then enable the service to have Systemd 
# start said service. Service files must be placed in /etc/systemd/system

    e.g.[Unit]
        Description=Gunicorn server for superlists-staging.jlw

        [Service]
        Restart=on-failure
        User=shadowwalker
        WorkingDirectory=/home/shadowwalker/public_html/superlists
        EnvironmentFile=/home/shadowwalker/public_html/superlists/.env
        ExecStart=/home/shadowwalker/public_html/superlists/virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging.jlw.socket superlists.wsgi:application

        [Install]
        WantedBy=multi-user.target

# Systemd has a journal(log) that can be accessed for each service. It appears that the journal logs anything written to systemd. 

    e.g. sudo journalctl -u gunicorn-superlists-staging.jlw
    
# When needed to write down deployment instuctions, create a .md file and add it to the repo. Creating a directory named `deploy_tools` and adding to repo can
# be used to stored the .md file. 

    e.g. Provisioning a new site
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
                
# The deployment should be idempotent. Meaning when the deployment is run multiple times, it has the same effect. 
# The deployment should also be repeatable. That way I can automate the things I do over and over again. It ensures that once we go to production, the deployment 
# will have the same effect. 


# Fabric vs Homegrown deployment using os library
# Main advantage I currently see is running commands over SSH. I'm pretty sure that Fabric relies on Invoke(a shell command runner). Huh, I bet it's named invoke
# as it invokes shell commans? Anyways, the main difference appears to be running the commands via SSH. Invoke appears to rely on subprocess which is in the 
# python native language. 


# Use git mv over mv when renaming a file in a git repo. git mv is a short hand for the following:

    mv <source> <destination>
    git add <destintation>
    git rm <source>
    
# When using TDD, you're only committing code that is in a working state. The idea is to go from working state to working state

# When using Selenium, if the page needs to refresh, you must put an explicit wait to ensure whatever item you're waiting for has loaded. Whenever you submit a form with
# Keys.ENTER or click something thatis going to cause a page to load, you probably wnat an explicit wati fro your next assertion
