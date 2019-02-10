# Purpose: To jot down anything I find interesting in my readings


# Miscellaneous Facts
--------------------
* **Use name of variable to denote intent. (I'll fill this out more the more I learn)**

        e.g. DEBUG_DJANGO_FALSE
        
* **Maybe I should start checking for status codes in my unit tests for my API return**

* **Database Layer Validation**
    
    - Validation at the databse layer is the  ultimate guarantee of data integrity
    - It's also inflexible as you can't ever have inconsistent data
    - It's not designed for user-friendliness
    
* **DRY is your friend!**

    - Don't Repeat Yourself
    - Coding words to leave by!
    
    
# Web development Facts
-----------------------

* **When running a `POST` operation, return a redirect to a new page**

* **Keep your `views` thin**
> if you find youreself looking at complex views, and having to write a lot of tests for them, it's time to start thinking about moving that logic elsewhere. 

* **ALWAYS include validation on server side as well as front side**
> Should never trust the front end will provide ample validation. 

# Javascript/JQuery Facts
-------------------------

* **The TDD cycle with Javascript**

    1) Write a Functional Test and see it fail
    
    2) Figure out what kind of code you need next: Python or JavaScript?
    
    3) Write a unit test in either langauage and see it fail
    
    4) Write some code in either language and make the test pass
    
    5) Rinse and repeat
    

* **Utilize the `jQuery.ready()` method to ensure that your initialize boilerplate code is loaded once the DOM(Document Object Model) is available. You shouldn't rely on the `<script>` tags to load the JavaScript for you**

* **It's good practice to put yor script loads at the end of your body HTML, as it means the user doesn't have to wait for all your JavaSciprt to load before they can see something on the page. It also helps to make sure most of the DOM has laoded before any scripts run**

* **One of the main difficulties with JavaScript testing is execution order. (i.e. what happens when). Utilize the following strategries to assist:**

    1) console logging
    
            e.g. 
                console.log('qunit tests start');
                
    2) Define an `initialize` function
    > Rather than just relying on JavaScript to run `<script>` whenever, we can use a common pattern, which is to define an "initialize" function and call that when we want to in our tests(and later in real life)
    
            e.g.
            
                test.html
                -----------
                
                <body>
                  <div id="qunit"></div>
                  <div id="qunit-fixture">
                    <form>
                      <input name="text" />
                      <div class="has-error">Error text</div>
                    </form>
                  </div>
                  
                  
                  
                  <script src="../jquery-3.3.1.js"></script>
                  <script src="../list.js"></script>
                  <script src="qunit-2.9.1.js"></script>
                  
                  <script>
                  
                  console.log('qunit tests start');
                  
                  QUnit.test("errors should be hidden on keypress", function (assert) {
                    console.log('in test 1');
                    
                    initialize();
                    
                    $('input[name="text"]').trigger('keypress');
                    
                    assert.equal($('.has-error').is(':visible'), false);
                    
                  });
                  
            
                list.js
                ---------
                
                var initialize = function () {
                  console.log('initialize called');
                  
                  $('input[name="text"]').on('keypress', function() {
                    console.log('in keypress handler');
                    
                    $('.has-error').hide();
                  });
                };
                
    

* **`$` is the jQuery Swiss Army knife. It's used to find bits of the DOM. It's first argument is a CSS slector; In the example below, we're telling it to find all elements that have the class `has-error`. It reutrns an boject that represnts one or more DOM elements.**

> The `is` method tells us whether an element matches a particular CSS property. Below we use :visible to check whether the elemnt is displayed or hidden

 > The `.hide` method is used to hide the div. Behind the scenes, it dynamically sets a style="display: none" on the element

            eg. 
                
                  <form>
                    <input name="text" />
                    <div class="has-error">Error text</div>
                  </form>
                  
                  <script src="../jquery-3.3.1.js"></script>
                  <script src="qunit-2.9.1.js"></script>
                  
                  <script>
                  
                  QUnit.test("smoke test", function (assert) {
                    assert.equal($('.has-error').is(':visible'), true);
                    $('.has-error').hide();
                    assert.equal($('.has-error').is(':visible'), false);
                  });
                  
                  </script>
                  
* **The jquery `.trigger` method is mainly used for testing. It says "fire off a Javascript DOM event on the element(s)". Below we use the keypress event, which is fired off by the browser behind the scenes whenever a user types something into a particular input element**

            e.g.
            
                $('input[name="text"]').trigger('keypress');
              
* **How to find input elements with JQuery**
> Below we create a form which has an input field with a name called `text`. Using the `$()`, we're able to select the value held in this element. 

            e.g.
                
                    <form>
                      <input name="text" />
                      <div class="has-error">Error text</div>
                    </form>
                    
                    $('input[name="text"]')
# QUnit Facts
-------------

* **In order to have isolation between tests, you must wrap your fixtures within a `"qunit-fixture" div`**

            e.g
            
                  <div id="qunit-fixture">
                    <form>
                      <input name="text" />
                      <div class="has-error">Error text</div>
                    </form>
                  </div>
        

# TDD Facts
-----------

* **A benefit of having tests is they allow you to remember why you wrote code a certain way. You may forget why some code works the way it does, looking at your tests could help jog your memory. That's why it's import to name your test verbosely. Your tests express what your requriements are of a particular class or function**

* **A `fixture` in testing is a way to tidy up between tests. It's code that run each time before a test runs**

* **For POST requests, make sure you test both the valid case and the invalid case**

* **If test doesn't raise an exception, write a short comment as to why**

* **Sometimes you should write a test for your stupidity**

* **Write tests for exploration of tools**

* **Don't forget to write the *MINIMAL* amount of code required to get a test to pass** 
> The code will be refactored after the testing is working. 

* **Place your unit tests in a tests directory. Include an __init__.py.**
> This ensures that test runners can import the tests via a package. Your functional tests have no 
  such requirement. For functional tests, group them according to feature or user story. For unit tests, you probably want a seperate test file for each tested source
  code file. 
  
* **Have a place holder test for *EVERY* function and class**

* **Don't refactor from failing _unit_ tests!**
> Working state to working state! The latest functional test you're creating, i.e. the current user story, that _IS_ OK to have failing
when doing a unit test

* **Don't forget the "Refactor" in "Red, Green, Refactor".**
> The whole point of having test is to allow you to refactor your code! Use them and make your code (including tests)
  as clean as you can. You don't need to wait until all coding is done to refactor. After you get your failing test to past, refactor that bad boy!

* **Never commit unit test skips to repo**
> Along with that note, only commit code to the repo that is in a working state minus your latest functional test(user story)

* When using TDD, you're only committing code that is in a working state. The idea is to go from working state to working state. Also, after going Red(failing test), 
  Green(minimal code to pass test), you must refactor. Ok, MUSt _maybe_ a little of an exageration. Just remember to refactor!

* **Fuctional tests running against staging vs locally**
    - Update functional tests(integrated tests) to check for environment variable named
    STAGING. If set, all post requests should go to that URL. If not set, run against local
    developmenet server. 
    
* **Three Strikes and Refactor**
> Copy and paste code once but on the third time, it's time to refactor. If you wait until you have three use cases, each might be slightly different, providing a 
    better view fo what the common functionality is. If you refactor too early, you may find that the third use case doesnt quite fit your refactored code.
    
* **Development-Driven Tests**
> When you're exploring an Api, there is no need to stick to TDD. You can create unitTests if you like, but this isn't mandatory. Once you've completed exploration of the Api and need to integrate the Api, get back to the testing goat. BAAAAAAAH!

* **Each UnitTest should test *ONE THING ONLY*!**
> Breaking things into multiple tests is definetely worthwhile. It helps you isolate the exact problem you may have, when you later come and change your code and accidentally introduce a bug.

# Python Facts
--------------
* Can use assertRaises with a context manager. If only the exception argument is given, returns a context manager so that the code under test can be written inline rather 
* than as a function

        with self.assertRaises(SomeException):
        do_something()
    
* The context manager will store the caught exception object in its exception attribute. This can be useful if the intention is to perform additional checks on the exception raised:

        with self.assertRaises(SomeException) as cm:
        do_something()

        the_exception - cm.exception
        self.assertEqual(the_exception.error_code, 3)
    
* WSGI (Web Server Gateway Interface)
    - Standard way of running python web applications
    - Exposes a callable which returns an `application` 
    - The WSGI marrys the `application` to web server
        
        
# Django Facts
--------------

* **Django Quirk: When creating a model, if no primary key is specified, Django will _implicity_ create one. In order words, if you don't specify a primary key for a model, Django will create one for you named `id`.**

* **User object**
> Django utilizes a `User` object for representing users who are logging into your application. These `User` objects is what the Django system wraps itself around to perform user authentication. When you're starting a new project, it's recommended to create your own custom `User` model. This will allow you to set which information you would like stored from the user by overriding the defaults. You need to update your projects `settings.py` and provide a `AUTH_USER_MODEL` variable in order to have this custom `User` model enabled within Django

                e.g.
                    INSTALLED_APPS = [
                    #'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'lists',
                    'accounts',
                ]

                AUTH_USER_MODEL = 'accounts.User'

>> Also, in order to create a new `User` object, you *_MUST_* create a model within your application `models.py`. The name of this `User` object needs to match the `AUTH_USER_MODEL` in the project `settings.py`. Also, keep in mind that once you create a new `User` in `<app>.models.py`, you will need to perform a `makemigrations` to have those changes applied to the database. 

>> Your custom `User` model has some required class level attributes:

    1) `REQUIRED_FIELDS` (list) - A list of the field names that will be prompted for when creating a user via the createsuperuser management command. The user will be prompted to supply a value for each of these fields. It must include any field for which blank is False or undefined and may include additional fields you want prompted for when a user is created interactively.
    
    2) `USERNAME_FIELD` (str) - A string describing the name of the field on the user model that is used as the unique identifier. This will usually be a username of some kind, but it can also be an email address, or any other unique identifier. The field must be unique (i.e., have unique=True set in its definition), unless you use a custom authentication backend that can support non-unique usernames.
    
    3) `is_anonymous` (boolean) - Read-only attribute which is always False. This is a way of differentiating User and AnonymousUser objects. Generally, you should prefer using is_authenticated to this attribute.
    
    4) `is_authenticated` (boolean) - Read-only attribute which is always True (as opposed to AnonymousUser.is_authenticated which is always False). This is a way to tell if the user has been authenticated. This does not imply any permissions and doesn’t check if the user is active or has a valid session. Even though normally you will check this attribute on request.user to find out whether it has been populated by the AuthenticationMiddleware (representing the currently logged-in user), you should know this attribute is True for any User instance.
    
>> The easiest way to construct a compliant custom user model is to inherit from `AbstractBaseUser`. AbstractBaseUser provides the core implementation of a user model, including hashed passwords and tokenized password resets. You must then provide some key implementation details

                

>> The `User` object can be used to set permissions and authorization for a given user interacting with your system. 

>> On top of `User` objects, you have a `UserManager` object. This object performs administration for `User` objects such as creating a new `User object` user credentials or for creating `superusers`. When you create your own customer `User` object, please be sure to create a corresponding `UserManager`. 

>> If you reference `User` directly (for example, by referring to it in a foreign key), your code will not work in projects where the `AUTH_USER_MODEL` setting has been changed to a different user mode

* **Authentication**
> Authenicate() vs login()
>> The `authenticate` method takes a username an password, unless they've been overriden by a custom user model to provide different crendental types, is queries each _authentication backend_ to see if the credentials are valid. If they are, a new User object, whether it be a custom user or the default User object, is returned. 

>>> The `login` method simply takes the `User` object returned via the `authenticate` method and stores it in the Django session. 

>>> These two methods work together in order to provide authentication and authorization within the Django Framework

> How to login a user
>> To log a user in, from a view, use `login()`. It takes an HttpRequest object and a User object. `login()` saves the user’s ID in the session, using Django’s session framework. Use `authenticate()` to verify a set of credentials. It takes credentials as keyword arguments, username and password for the default case, checks them against each authentication backend, and returns a User object if the credentials are valid for a backend. If the credentials aren’t valid for any backend or if a backend raises PermissionDenied, it returns None. For example:

            e.g.
                from django.contrib.auth import authenticate, login

                def my_view(request):
                    username = request.POST['username']
                    password = request.POST['password']
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        # Redirect to a success page.
                        ...
                    else:
                        # Return an 'invalid login' error message.
                        ...
                        
* **How to test Django is sending an email**
> Django is VERY magical. I would _SWEAR_ it's supposed to be in Ascender....When sending emails from Django, you can use the `mail` object to retrieve access to emails that Django is attempting to send. This `mail` object has an `outbox` attribute. This attribute gives access to any emails the Django server tries to send. 

            e.g
                from django.core import mail
                
                email = mail.outbox[0]

* **How to send emails within Django**
> You will need to update your projects settings.py to include the host information. Within the module that will be sendng the email, you use the `send_mail fuction` from the core django mail package

            e.g. 
                Settings.py
                
                    EMAIL_HOST = 'smtp.gmail.com'
                    EMAIL_HOST_USER = 'walkej19@gmail.com'
                    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
                    EMAIL_PORT = 587
                    EMAIL_USE_TLS = True
                    
                Views.py
                
                    url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
                    
                    send_mail(
                        'Your login link for Superlists',
                        f'Use this link to log in:\n\n{url}',
                        'noreply@superlists',
                        [email]
                    )

* **Django project vs Django App**
> A Django project contains a collection of Django Apps. The Django Apps are web applications. The Django project allows setting of global settings and managing said web applications. Or in Django's words:
    
>>_What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects._
>>>>>>> Stashed changes

* **You can use the Django test case to test for which template was used in a view**

* **You can check the context passed to a view to ensure a correct object was passed**

* **Items to test in a Django view**

    1) Use the Django test client
    
    2) Check the template used
    
    3) Check that any objects are the right ones or querysets have the correct items by checking the request context via the test client
    
    4) Check that any forms are of the correct class
    
    5)  Think about testing template logic: any for or if might deserve a minimal test
    
    6) For `POST` requests, make sure you test both the valid and invalid case
    
    7) Optionally, sanity-check that form is rendered and it's errors displayed
    
            e.g
    
                self.assertIsInstance(response.context['form'], ExistingListItemForm)
                self.assertContains(response, escape(EMPTY_ITEM_ERROR)
    

* **Test Client**

    > Can be imported directly or can be access via django `TestCase` subclass
        
            from django.test import Client
            c = Client()
            
            OR
            
            from django.test import TestCase
            
            class HomePageTest(TestCase):
        
            def test_home_page_returns_correct_html(self):
                response = self.client.get('/')
            
    - Simulate GET and POST requests on a URL and observe the response – everything from low-level HTTP (result headers and status codes) to page content.
    - See the chain of redirects (if any) and check the URL and status code at each step.
    - Test that a given request is rendered by a given Django template, with a template context that contains certain values.


* **How to run functional tests in Django**

    - Need a directory named `functional_tests`
    
        - Needs to contain `tests.py`
        
    - python manage.py test functional_tests
    
    - passing --failfast will force test to stop at first failure
    
        - python manage.py test functional_tests --failfast
        
* **Djano models have access to default field options. These can each be overridden. One of them is blank-False. This means that the model won't allow blanks to be saved in the database.**

* **Reverse Resolution of URLs (How to not hardcode URLs in views/templates)**

> You can use the urls.py in your templates via the {% url %} syntax and in python use the reverse function. That will pull the endpoint from the ```<project>/urls.py```

* **Reverse Resolution of URLS to models <a name="reverse_resolution_models"></a>**

>Django has this weird, spooky action. Some would call it magic. In other words, it's _EXTREMELY_ implicit. Regardless, Django allows you to return a URL from your model. It sounds weird as it IS
weird. It allows you to take the endpoint in the urlpatterns in  ```<project>/urls.py``` and append your model automatically. You must create a ```get_absolute_url``` method on your model. In this
method, you use the reverse function, passing in the name of the view that matches what is in your ```urls.py```. Doing this will allow your model to have access to the endpoint of the view. 

        e.g.
            ```lists/urls.py```
            urlpatterns = [url(r'^lists/(\d+)/$', views.view_list, name='view_list')]
            
            ```lists/models.py```
            class List(models.Model):
        
                def get_absolute_url(self):
                    return reverse('view_list', args=[self.id])
                
            That allows the following to occur on models:
            
            test_list = List.objects.create()
            test_list.get_absolute_url() 
            
            lists/12        (assuming the id generated via create is 12)

* **Django quirk: the model save() method will not run validation against data being saved to the database.**

    Validation means calling the `full_clean()` method on a djanjo model object.
    The `full_clean()` method validates the fields on the model, validates the model as a whole(whatever that means and valiates uniqueness constraints. If you want to run these, since `save()` does not,
    then you must call `full_clean()` explicity. 
    
    *Note*: 
    Some data integrity errors *are* picked up on `save()`. It depends on whether the integrity constraint is enforced by the database or via the model. If via the model, this means the database has the constraint present due to a migration occurring. 
  
* **Django quirk: A LOT of configuration for Django objects such as `ModelForm` objects occur with a nested class named `Meta` including Django models**
        
        e.g. 
        
        class ItemForm(forms.models.ModelForm):
        
            class Meta:
                model = Item
                fields = ('text',)
                widgets = {
                    'text': forms.fields.TextInput(attrs={
                        'placeholder': 'Enter a to-do item',
                        'class': 'form-control input-lg'
                    })
                }
                
                error_messages = {
                    'text': {'required': "You can't have an empty list item"}
                }


* **To create and save an object in a single step, use the Django model create() method**
    
    e.g.
        List.objects.create()
        
* **Djano Pattern**
    - Use the same view to process POST requests as to render the form they came from
    
     - e.g. _Current situation is that we have one view and URL for displaying a list and one view and URL for processing additions to that list. Combine those into one_
     
        
* **Returning redirect to model**
> Please see the section [Reverse Resolution Models](#reverse_resolution_models) on how to configure a model to have a URL. Once you've created a model, you will need to add a method named `get_absolute_url`.
That will allow you in your view to pass the models to the `redirect` function. That will then return 'automagically' the URl to the model.

        e.g.
            list_ = List.objects.create()
              
            return redirect(list_)      
            
* **ModelForms**
> These bad boys are used to create a form(Django/HTML form) from a model. In other words, Django provides a special class which can autogenerate a form for a model. This modelForm subclass can 
provide form level and model level validation. Just like normal form validation, model form validation is triggered implicitly when calling `is_valid()` or accessing the `errors` attribute and explicitly when calling `full_clean()`, although you will typically not use the latter method in practice.

    > The primary task of a Form object is to validate data. With a bound Form instance, call the `is_valid()` method to run validation and return a boolean designating whether the data was valid. It also has a side effect of populating the `errors` attribute
    
    > **Django quirk: _update_errors() allows overriding the corresponding model validation error Override any validation error messages defined at the model level with those defined at the form level.**
    
    > **Django quirk: The `ValidationError` has a `message_dict` attribute that you can override to pass custom errors back to the form**
    
                class ExistingListItemForm(ItemForm):
            
                    def __init__(self, for_list, *args, **kwargs):
                        super().__init__(*args, **kwargs)
                        self.instance.list = for_list
                        
                    def validate_unique(self):
                        try:
                            self.instance.validate_unique()
                        except ValidationError as e:
                            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
                            self._update_errors(e)
    > **Django Quirk: When using a ModelForm, you specify the fields to include in the form. If the Model itself contains a unique constraint and one of those fields _ISN'T_ one of the fields within the ModelForm, the unique constraint will *NOT* be enforced at the form level but the model level. In order to overcome this, you must call the model the for ModelForm is referencing, `validate_unique` method directly. You can access the model the ModelForm is referencing via the instance attribute. You then can call `validate_unique` on the model directly. You then need to ensure to override the `vaidate_unique` method on the ModelForm to have this behavior invoked**
    
                e.g. 
                    class ExistingListItemForm(forms.models.ModelForm):
                    
                        class Meta:
                            model = Item
                            fields = ('text',)
                            widgets = {
                                'text': forms.fields.TextInput(attrs={
                                    'placeholder': 'Enter a to-do item',
                                    'class': 'form-control input-lg'
                                })
                            }
                            
                            error_messages = {
                                'text': {'required': EMPTY_ITEM_ERROR}
                            }
        
                        def __init__(self, for_list, *args, **kwargs):
                            super().__init__(*args, **kwargs)
                            self.instance.list = for_list
                            
                        def validate_unique(self):
                            try:
                                self.instance.validate_unique()
                            except ValidationError as e:
                                e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
                                self._update_errors(e)
                    
    > Model validation (Model.full_clean()) is triggered from within the form validation step, right after the form’s clean() method is called.
    
    > The `.instance` attribute on a `Modelform` represents the databse object that is being modified or created. 
            
                Showing them being used:
                  
                form = ItemForm()
                form.instance == Item
        
                Sample Form
                
                    class ItemForm(forms.models.ModelForm):

                        class Meta:
                            model = Item
                            fields = ('text',)
                            widgets = {
                                'text': forms.fields.TextInput(attrs={
                                    'placeholder': 'Enter a to-do item',
                                    'class': 'form-control input-lg'
                                })
                            }
                            
                            error_messages = {
                                'text': {'required': EMPTY_ITEM_ERROR}
                            }
                        
                        def save(self, for_list):
                            self.instance.list = for_list
                            
                            return super().save()
                        
                        
                Sample Model
                
                    class Item(models.Model):
                        text = models.TextField(default='')
                        list = models.ForeignKey(List, default=None)
            
    - **The ModelForm `save()` method creates and saves a database object from the data bound to the form.**
        - Note that if the form hasn’t been validated, calling save() will do so by checking form.errors. A ValueError will be raised if the data in the form doesn’t validate – i.e., if form.errors evaluates to True.

    - **Model vs Form level validation**
    
    > When validating a form, the errors are stored under the `errors` attribute. This attribute is a dictionary of error messages. In this dictionary, the keys are the field names from the form, and the values are lists of Unicode strings representing the error messages. The error messages are stored in lists because a field can have multiple error messages.

                -  Form level validation runs the following steps via the `clean()` method
                
                    1. to_python()
                        - method on a Field is the first step in every validation. It coerces the value to a correct datatype and raises ValidationError if that is not possible.
                        
                    2. vaidate methond called on a field
                        - handles field-specific validation that is not suitable for a validator. It takes a value that has been coerced to a correct datatype and raises ValidationError on any error.
                        
                    3. run_validators()
                        -  runs all of the field’s validators and aggregates all the errors into a single ValidationError. You shouldn’t need to override this method.
                
                - Model level validation runs the following steps via the `is_valid()` method on a modelForm
                    
                    1. clean_fields() 
                        - This method will validate all fields on your model. The optional exclude argument lets you provide a list of field names to exclude from validation. It will raise a ValidationError if any fields fail validation.
                    
                    2. clean()
                        - This method should be used to provide custom model validation, and to modify attributes on your model if desired. 
                    
                    3. validate_unique()
                        - This method is similar to clean_fields(), but validates all uniqueness constraints on your model instead of individual field values.
    
* **How to render a ModelForm via a Django Template**

    1. Create your modelForm
    2. Pass an instance of the form to the render function as the context
    3. Update your template to render the form in the template
    
            eg. 
                Form:
                class ItemForm(forms.models.ModelForm):
                    class Meta:
                        model = Item
                        fields = ('text',)
                        widgets = {
                            'text': forms.fields.TextInput(attrs={
                                'placeholder': 'Enter a to-do item',
                                'class': 'form-control input-lg'
                            })
                        }
                        
                        error_messages = {
                            'text': {'required': EMPTY_ITEM_ERROR}
                        }
                        
                View:
                def home_page(request):
                    return render(request, 'home.html', {'form': ItemForm() })
                    
                 
                Template:
                <form method="POST" action="{% block form_action %}{% endblock %}">
                    {{ form.text }}
                </form>
                
                This will render the HTML equivalent of the text field in the ModelForm in the template with the appropriate input box with corresponding placeholder and class
                
* **How to render a ModelForm errors via a Django Template**
> Each modelForm carries the `errors` attributes. This attribute is populated via the `full_clean()` method on the model attribute or via the `is_valid()` method on the ModelForm object. The `errors`
ModelForm attribute is a dictionary with the keys being the fields contained within the ModelForm object. Each of the values is a list of the errors associated with the corresponding field in the model. The
ModelForm fields can be accessed directly along with their corresponding `errors` dictionary. i.e. `ItemForm().text.errors`

    1. Create your modelForm
    2. Pass an instance of the form to the render function as the context
    3. Update your template to render the form in the template
    
            eg. 
                Form:
                class ItemForm(forms.models.ModelForm):
                    class Meta:
                        model = Item
                        fields = ('text',)
                        widgets = {
                            'text': forms.fields.TextInput(attrs={
                                'placeholder': 'Enter a to-do item',
                                'class': 'form-control input-lg'
                            })
                        }
                        
                        error_messages = {
                            'text': {'required': EMPTY_ITEM_ERROR}
                        }
                        
                View:
                def home_page(request):
                    return render(request, 'home.html', {'form': ItemForm() })
                    
                 
                Template:
                <form method="POST" action="{% block form_action %}{% endblock %}">
                    {{ form.text }}
                    {% if form.errors %}
                        <div class="form-group has-error">
                            <span class="help-block">{{ form.text.errors }}</span>
                        </div>
                    {% endif %}
                </form>
                
                This will render the HTML equivalent of the text field in the ModelForm in the template with the appropriate input box with corresponding placeholder and class

* **How Django derives table names** 
    
    To save you time, Django automatically derives the name of the database table from the name of your model class and the app that contains it. A model’s database table name is constructed by joining the model’s “app label” – the name you used in manage.py startapp – to the model’s class name, with an underscore between them.

    For example, if you have an app bookstore (as created by manage.py startapp bookstore), a model defined as class Book will have a database table named bookstore_book.

    To override the database table name, use the db_table parameter in class Meta.
    
* **Access related Django model objects**
> What is a `related` Django model? It's how Django represents foreign key relationships within the ORM. So if you have a `List` table and an `Item` table and the `Item` table contains a foreign key for the 
`List` table, these tables would be considered `related` Django models. Django provides the ability to quickly gather all related tables to a table whose foreign key is in use on other tables. You have to go
through the main table in order to access the linked tables.  i.e `main_table.(name_of_linked_table_lower_case)_set`

        e.g. 
            
            class List(models.Model):
    
                def get_absolute_url(self):
                    return reverse('view_list', args=[self.id])
                

            class Item(models.Model):
                text = models.TextField(default='')
                list = models.ForeignKey(List, default=None)
                
            list_ = List.objects.create()
            item = Item()
            item.list = list_
                
            item.save()
            
            How to access the List related Items
            
            list_.item_set.all()
            
            

# System Adminstration Facts
----------------------------
* How to setup Nginx to reverse proxy to Gunicorn via unix socket
    - Create site file in sites-available
        -e.g. /etc/nginx/sites-available/superlists-staging.jlw
    - Add unix socket path to reverse proxy in location block in site file 
        -e.g. 
            location / {
            proxy_pass http://unix:/tmp/superlists-staging.jlw.socket;
        }
    - Bind Gunicorn to same unix socket path
        - e.g. ./virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging.jlw.socket superlists.wsgi:application
        

            
* When doing a reverse proxy from Nginx, the client headers are stripped out. In order to retrieve the 
  client request hostname, you must tell Nginx to pass the hostname along. You use a predefined variable 
  within Nginx to pass the host, named $host. See variables here: http://nginx.org/en/docs/http/ngx_http_core_module.html*variables

    e.g. 
        location / {
            proxy_pass http://unix:/tmp/superlists-staging.jlw.socket;
            proxy_set_header Host $host;
        }
    
* Systemd is daemon Ubuntu uses to manage services. These services are started on default if they are placed in the correct directory.
* Each directory appears to mean a certain runlevel. Files must be named <name>.service. You then enable the service to have Systemd 
  start said service.
* Service files must be placed in /etc/systemd/system

    e.g.[Unit]
        Description-Gunicorn server for superlists-staging.jlw

        [Service]
        Restart-on-failure
        User-shadowwalker
        WorkingDirectory-/home/shadowwalker/public_html/superlists
        EnvironmentFile-/home/shadowwalker/public_html/superlists/.env
        ExecStart-/home/shadowwalker/public_html/superlists/virtualenv/bin/gunicorn --bind unix:/tmp/superlists-staging.jlw.socket superlists.wsgi:application

        [Install]
        WantedBy-multi-user.target

* Systemd has a journal(log) that can be accessed for each service. It appears that the journal logs anything written to systemd. 

    e.g. sudo journalctl -u gunicorn-superlists-staging.jlw
    
* Nginx vs Apache
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
        
        
* Spoof a domain
    - Just add an entry to the /etc/hosts file
    $ sudo cat /etc/hosts
        127.0.0.1	localhost
        127.0.1.1	Havoc
        127.0.0.1   superlists-staging.jlw


# Deployment Facts
------------------
* The deployment should be idempotent. Meaning when the deployment is run multiple times, it has the same effect. 

* The deployment should also be repeatable. That way I can automate the things I do over and over again. It ensures that once we go to production, the deployment 
  will have the same effect. 


* Fabric vs Homegrown deployment using os library
    - Main advantage I currently see is running commands over SSH. I'm pretty sure that Fabric relies on Invoke(a shell command runner). Huh, I bet it's named invoke
      as it invokes shell commans? Anyways, the main difference appears to be running the commands via SSH. Invoke appears to rely on subprocess which is in the 
      python native language. 

* When needing to write down deployment instuctions, create a .md file and add it to the repo. Creating a directory named `deploy_tools` and adding to repo can
  be used to stored the .md file. 

    e.g. Provisioning a new site
        -----------------------


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
                
* How to ensure that production config requires key values
    - Check for the existance of a flag. If flag present, then grab items from application environment
    using dictionary access
        - All entries that should be required, will throw key errors if not present
    - If flag doesn't exist in os.environ
        - Use development config
    e.g. if 'DJANGO_DEBUG_FALSE' in os.environ:
            DEBUG - False
            SECRET_KEY - os.environ['DJANGO_SECRET_KEY']
            ALLOWED_HOSTS - [os.environ['SITENAME']]
         else:
            DEBUG - True
            SECRET_KEY - 'insecure-key-for-dev'
            ALLOWED_HOSTS - []
            
                

    
# Git Facts
-----------
* Use git mv over mv when renaming a file in a git repo. git mv is a short hand for the following:

    mv <source> <destination>
    git add <destintation>
    git rm <source>
    

# Selenium Facts
----------------

* **`is_displayed` teslls you wethere an elemnt is visible or not. You can't just rely on checking whether the element is present in the DOM, because you can hide elements in the**

* **Create your own wait_for helper function. This is used for Selenium tests that require a refresh or a loadig of a feature.**
> When using Selenium, if the page needs to refresh, you must put an explicit wait to ensure whatever item you're waiting for has loaded. Whenever you submit a form with
Keys.ENTER or click something thatis going to cause a page to load, you probably wnat an explicit wati fro your next assertion

            e.g.     
            
                def wait_for(self, fn):
                    start_time - time.time()
                    
                    while True:
                        try:
                            return fn()
                        except (AssertionError, WebDriverException) as e:
                            if time.time() - start_time > MAX_WAIT:
                                raise e
                            time.sleep(0.5) 

* **Selenium can locate items via the following methods**

    1. find_element_by_id
    2. find_element_by_name
    3. find_element_by_xpath
    4. find_element_by_link_text
    5. find_element_by_partial_link_text
    6. find_element_by_tag_name
    7. find_element_by_class_name
    8. find_element_by_css_selector


