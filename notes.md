#general django knowledge
    `python -m manage shell` is an interpretive shell that can interact with the django project
    `python -m manage createsuperuser` creates an admin user over the project
#Starting Project Structure
    asgi file is for asynchronous deployment
    wsgi file is for synchronous deployment
    settings.py manages the project settings
        define base_dir from pathlib
        secret key is part of security, should never be public
        debug shows debug info, should be set to false in production
        allowed hosts shows whitelisted hosts to run the django server
        installed apps shows the apps installed in your project
        root url is the path to the urls.py file
        tenplates shows config objects for templates
            'DIRS' shows paths for other template directories within apps
        DATABASES is used for configuring databases 
        the engine is the specific database, ex: postgres, mysql, etc
        name is the name of the database
        auth password validators checks for password security
        language code shows the language you are using
        time zone is the web server timezone
        static url is the dit for staticfiles
            css, js, images
    manage.py is where we interact with the server as developers through the CLI
    db.sqlite3 is the database file
#Apps and Structure
    containerized module of code
        ex Users, Billing, Leads apps
    syntax for creating an app is `python -m manage startapp <app name>`
    project structure
        migrations folder shows database changes
        admin.py file control the django admin
        apps.py is not developer useful
        models.py is where we declare our models
        tests.py is for writing tests
        views.py returns and handles web requests
    to register the app in the django project you need to include it in the settings.py/installed_apps list
#Django models
    a model defines the sql schema
    field types:
        string values are defines as CharFields and must be given a max_length argument
            Charfields can be given options parameters, which dont restrict the input possibilities but are used for forms
        int values are defined as IntegerFields and should be given a default
        bool valued are BooleanFields and can only be true or false
        images can be stored in ImageFields
        many types of files can be stored in FileFields
        foreign keys:
            used to connect database info between tables
            must be put on the reciever of the data
                leads have one agent but agents have many leads
        OneToOneFields act the same as foreign keys but can only be mapped in a one to one relationship
    fields can be given arguments like default, null, and blank to control their properties
    to initialize this model run python -m manage `makemigrations`
        after doing this we will see a new file in the migrations folder of our app
        this will create a new class `Migration`
            inside here the modt important value is `operations`
                this shows the operations acted on the project
                migrations.CreateModel makes a model
                name is the name of our model
                fields is all the parameters we passed into our model
                django autocreates an `id` parameter which is our primary key for querying
                database is not changed yet
    to finalize migrations run `python -m manage migrate`
        now our model is applied to our database
    django provides custom templates for certain models
        for example the user model
            `from django.contrib.auth import get_user_model`
            django recommends using custom user models
        custom user models through inhereted models
            `from django.contrib.auth.models import AbstractUser`
            is a way to allow adding on to user models later on as project requirements expand
            if you dont want to change anything initally just pass in the class
#Querysets and managers
    Model Managers
        to access the model manager use `<model>.objects`
        we can now use this manager to do things
            create
                `<model>.objects.create(<params>)`
                create is used to actually populate the sql table
    Querysets
        used to fetch data from the sql database
            `<model>.objects.all()` is used to fetch all objects
            `<model>.objects.filter(<attrs>)` is used to fetch objects with certain attributes
                there are some switches like `__gt` to do things like fetch things greater than
                `__lt` is less than
            `<model>.objects.get(<attrs>)` gets a single object based on its attributes
        the datatype returned by querys is called a queryset
            can loop through it
            can interact with it in templates
    