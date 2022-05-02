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
        int values are defined as IntegerFields and should be given a default
        bool valued are BooleanFields and can only be true or false
        images can be stored in ImageFields
        many types of files can be stored in FileFields
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