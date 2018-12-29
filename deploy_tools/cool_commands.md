# Purpose: To list any commands that I deem cool.

# Shell Commands
================

    ## Run a shell command and assign to a variable/Run a shell command in a seperate terminal

        $()
        
        e.g.
        
        export TAG=$(date +DEPLOYED-%F^CH%M)
        

    ## Set and expand a variable in bash

        TEST=$(date +DEPLOYED-%F)   
        echo $TEST  
        
    ## Specify date format via bash

        date +(format option)
        
        $date +F


    ## readlink - Print value of a symbolic link or canonical file name

        readlink <path_to_symlink>

        For example: 
            $ readlink -f default 
            /etc/nginx/sites-available/default

    ##  export - Creates an environment variable for terminal

        export <name_of_variable>

        For example:
            (virtualenv) shadowwalker@Havoc:/etc/nginx/sites-enabled$ export SITENAME=superlists-staging.jlw
            
            (virtualenv) shadowwalker@Havoc:/etc/nginx/sites-enabled$ printenv | grep SITENAME 
            SITENAME=superlists-staging.jlw

    ##  Create an enviroment variable for a test run

        KEY=Value to set environment variable

        For example:

            $ STAGING_SERVER=localhost:80 ./manage.py test functional_tests/ --failfast
            
    ## Redirect/Copy standard input to each FILE, and also to standard output

        $ cat ./deploy_tools/nginx.template.conf | tee test_test_command.txt
        server {

            listen 80;
            server_name DOMAIN;
            
            location /static {
                alias /home/shadowwalker/public_html/DOMAIN/static;
            }
            
            location / {
                proxy_pass http://unx:/tmp/DOMAIN.socket
                proxy_set_header Host $host
            }

        }
        
        $ cat test_test_command.txt 
        server {

            listen 80;
            server_name DOMAIN;
            
            location /static {
                alias /home/shadowwalker/public_html/DOMAIN/static;
            }
            
            location / {
                proxy_pass http://unx:/tmp/DOMAIN.socket
                proxy_set_header Host $host
            }

        }
        
    ## Edit a file without opening and create another file from output

        cat ./deploy_tools/nginx.template.conf | sed "s/DOMAIN/jeremy_test_sed.org/g" | sudo tee superlists.ottg.eu

        
# Danjgo Commands
-----------------


* Collect all static files in Django

        ./virtualenv/bin/python manage.py collectstatic

        For example: 
            shadowwalker@Havoc:~/public_html/superlists$ ./virtualenv/bin/python manage.py collectstatic
                Copying '/home/shadowwalker/public_html/superlists/lists/static/base.css'

     
* How to run python one liners via terminal 
     
        $ echo DJANGO_SECRET_KEY=$(python3.6 -c "import random; print(''.join(random.SystemRandom().choices('abcefghijklmnopqrstuvwxyz123456789', k=50)))") >> .env
        
* Test individual module unitTests

        python manage.py test <package_path.module>
        
        e.g.

        python manage.py test functional_tests.test_list_item_validation
        python manage.py test lists.tests.test_views
        
* How to run all functional and unittests

        python manage.py test

# SystemD commands
================

    ## Commands to use in systemd to manage services
        
    ## Loads new config
        sudo systemctl daemon-reload
        
    ## Enables a service in systemd to run on boot
        sudo systemctl enable <name_of_service>
        
    ## Starts a service
        sudo systemctl service start <name_of_service>
        
    ## Read information from systemd logs

        sudo journalctl -u <name_of_service>
    
# Fabric Commands
=================

    ## How to run a shell command on a server

        run(f'<command_to_run')

          e.g.
            run(f'mkdir -p /test/')
            
    ## Run commands against all files in a current working directory

        cd(<directory>) 
            _<run_function_blah>
        
    ## Check if a directory exists
        
        exists(<directory>)
       
    ## Run command on local machine

        local("<command_to_run")
        
    ## Check out latest code, blow away all local code 

        current_commit = local("git log -n 1 --format=%H", capture=True)
        run(f'git reset --hard {current_commit}')


    ## Append line to a file if line doesn't exist

        append('example.txt','DJANGO_DEBUG_FALSE=y')
        
        
    ## How to silence yes/no interactive with run command

        run('<command>, --noinput')
    
    
# Git Commands
==============

    ## Show git log - shows latest commits locally
       
        git log
        
    ## Show latest entry in git log as a hash

        git log -n 1 --format=%H
        
    ## Rename a file in git
        
        git mv <source> <destination>
    
# Unit Tests
============

    ## Can use assertRaises with a context manager

        with self.assertRaises(SomeException):
        do_something()


