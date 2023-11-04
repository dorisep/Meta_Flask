# Meta_Flask
Second Go at Flask App 


## APP SUMMARY
Inside your flask_app directory, you’ll have an app.db database file and a config.py configuration file for your Flask application. The main Flask application will be in the app directory, which will have an __init__.py special file to make it a package for imports to work properly, and it will contain a function for creating the Flask application instance.

The app directory will contain an extensions.py file for managing the Flask extensions you’ll use in your application (in this tutorial, Flask-SQLAlchemy is the example of using a Flask extension). You will also have the following directories:

main: the main blueprint for main routes, such as the home page.
posts: the posts blueprint for managing blog posts.
questions: the questions blueprint for managing questions and answers.
models: the directory that will contain Flask-SQLAlchemy models.
templates: the templates directory that will contain files for the main blueprint and a directory for each blueprint.

### IMPORTANT NOTES
***env*** source flask_demo/bin/activate

[more_on_sessions](https://flask.palletsprojects.com/en/2.2.x/api/#sessions)

[creating_secret_keys](https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-3-handling-form-requests)



[more_on_templates](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)

[source](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy)
SECRET_KEY: A long random string used by Flask as a secret key, or a key used to secure the sessions that remember information from one request to another. The user can access the information stored in the session but cannot modify it unless they have the secret key, so you must never allow anyone to access your secret key. See the Flask documentation on sessions for more information. Other Flask extensions often use this secret key to secure data. See Step 3 of How To Use Web Forms in a Flask Application for more information on how to create a secure secret key. When developing your Flask applications, you should set the secret key with an environment variable called SECRET_KEY. To get its value in this config.py file and save it in a class variable called SECRET_KEY, you access the environment variable’s value via the os.environ object using its get() method. (Though you do not need to set a secret key to follow this tutorial, you can review the note at the end of this list for instructions on how to set a secret key.)