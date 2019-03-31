# Purpose: To list any commands that I deem cool.

# Shell Commands
-------------------------------

* **Run a shell command and assign to a variable/Run a shell command in a seperate terminal**

        $()
        
        e.g.
        
        export TAG=$(date +DEPLOYED-%F^CH%M)
        

* **Set and expand a variable in bash**

        TEST=$(date +DEPLOYED-%F)   
        echo $TEST  
        
* **Specify date format via bash**

        date +(format option)
        
        $date +F


* **readlink - Print value of a symbolic link or canonical file name**

        readlink <path_to_symlink>

        For example: 
            $ readlink -f default 
            /etc/nginx/sites-available/default

*  **export - Creates an environment variable for terminal**

        export <name_of_variable>

        For example:
            (virtualenv) shadowwalker@Havoc:/etc/nginx/sites-enabled$ export SITENAME=superlists-staging.jlw
            
            (virtualenv) shadowwalker@Havoc:/etc/nginx/sites-enabled$ printenv | grep SITENAME 
            SITENAME=superlists-staging.jlw

*  **Create an enviroment variable for a test run**

        KEY=Value to set environment variable

        For example:

            $ STAGING_SERVER=localhost:80 ./manage.py test functional_tests/ --failfast
            
* **Redirect/Copy standard input to each FILE, and also to standard output**

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
        
* **Edit a file without opening and create another file from output**

        cat ./deploy_tools/nginx.template.conf | sed "s/DOMAIN/jeremy_test_sed.org/g" | sudo tee superlists.ottg.eu
        
* **Search for a pattern and do a replace on result set**

        grep -IZlr "item_text" lists | xargs -0 sed -i -e "s/item_text/text/g"
        
        Grep
        
            -I - ignores binary files
            -Z - each result ends with a blank
            -l - lists the path to the fiels
            -r - searches recursively
        
        Xargs
        
            -0 - Each argument will be ending with a blank line
        
        Sed
        
            -i - Edits file in place with no back up being created
            -e - Pattern being used for replace

        
# Django Commands
-----------------

**How to reset the database**

        python manage.py flush 

* **How to build a URI(URL) in a view**
> You should use the `build_absolute_uri` function. 

		Views.py
			email = request.POST['email']
			url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
			
* **How to get the User model being used for Authentication**
>> _This presumes you have a AUTH_USER_MODEL within your `settings.py`_

		from django.contrib.auth import get_user_model
		
		User = get_user_model()


* **Collect all static files in Django**

        ./virtualenv/bin/python manage.py collectstatic

        For example: 
            shadowwalker@Havoc:~/public_html/superlists$ ./virtualenv/bin/python manage.py collectstatic
                Copying '/home/shadowwalker/public_html/superlists/lists/static/base.css'

     
* **How to run python one liners via terminal**
     
        $ echo DJANGO_SECRET_KEY=$(python3.6 -c "import random; print(''.join(random.SystemRandom().choices('abcefghijklmnopqrstuvwxyz123456789', k=50)))") >> .env
        
* **Test individual module unitTests**

        python manage.py test <package_path.module>
        
        e.g.

        python manage.py test functional_tests.test_list_item_validation
        python manage.py test lists.tests.test_views
        
* **Test indivdual tests within a module**
        
        python manage.py test <package_path.module.class_name.method_name0>
        
        e.g.
        
        python manage.py test functional_tests.test_list_item_validation.ItemValidationTest.test_cannot_add_duplicate_items        
        
* **How to run all functional and unittests**

        python manage.py test
        
* **How to render a django form as HTMl**

> To render a django form as HTML, invoke the `as_p()` method of the form

        from django import forms

        class ItemForm(forms.Form):
            item_text = forms.CharField()
            
        test_Form = ItemForm()
        
        test_form.as_p()
        
* **How to override a ModelForm `save()` method to save a foreign key
> The example below shows overriding a `ModelForm` `save()` method to allow the Form to save an Item to list upon the invocation of `save()`

        def save(self, for_list):
            self.instance.list = for_list
            
            return super().save()

# Systemd commands
-------------------------------

_**Commands to use in systemd to manage services**_
        
* **Loads new config**

        sudo systemctl daemon-reload
        
* **Enables a service in systemd to run on boot**

        sudo systemctl enable <name_of_service>
        
* **Starts a service**

        sudo systemctl service start <name_of_service>
        
* **Read information from systemd logs**

        sudo journalctl -u <name_of_service>
    
# Fabric Commands
-------------------------------

* **How to run multiple context managers**
> [http://docs.fabfile.org/en/1.14/api/core/context_managers.html#module-fabric.context_managers](Context managers)
            with settings(host_string=f'wu@{host}'):
                env_vars = _get_server_env_vars(host)
                
                with shell_env(**env_vars):
                    session_key = run(f'{manage_dot_py} create_session {email}')
                    
                    return session_key.strip()


* **How to set the user/host/port via environment variable**
> [http://docs.fabfile.org/en/1.14/usage/env.html#host-string](Host String)
        with settings(host_string=f'wu@{host}'):
            run(f'{manage_dot_py} flush --noinput')

* **How to set environment variables within a shell**
    
        env_vars = dict(env1=variable1, env2=variable2)

        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')

* **How to run a shell command on a server**

        run(f'<command_to_run')

          e.g.
            run(f'mkdir -p /test/')
            
* **Run commands against all files in a current working directory**

        cd(<directory>) 
            _<run_function_blah>
        
* **Check if a directory exists**
        
        exists(<directory>)
       
* **Run command on local machine**

        local("<command_to_run")
        
* **Check out latest code, blow away all local code**

        current_commit = local("git log -n 1 --format=%H", capture=True)
        run(f'git reset --hard {current_commit}')


* **Append line to a file if line doesn't exist**

        append('example.txt','DJANGO_DEBUG_FALSE=y')
        
        
* **How to silence yes/no interactive with run command**

        run('<command>, --noinput')
        
* **How to override environment variables**

        from fabric.context_managers import settings

            with settings(host_string=f'wu@{host}'):
                run(f'{manage_dot_py} flush --noinput')
    
    
# Git Commands
-------------------------------

* **Show git log - shows latest commits locally**
       
        git log
        
* **Show latest entry in git log as a hash**

        git log -n 1 --format=%H
        
* **Rename a file in git**
        
        git mv <source> <destination>
    
# Unit Tests
-------------------------------

* **Can use assertRaises with a context manager**

        with self.assertRaises(SomeException):
        do_something()


