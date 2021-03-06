Shfl
====

__Shfl__ is a minimal [Flask](http://flask.pocoo.org/) boilerplate structured to build large web applications in a modular way.


## Built Using

1. [Flask](http://flask.pocoo.org/) micro framework.
2. [MySQL](http://www.mysql.com/) database using [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/).
2. HTML5 & CSS3 via [Initializr](http://www.initializr.com/).
3. [jQuery](http://jquery.com) javascript library.
4. [Backbone.js](http://backbonejs.org/) javascript library.


## Installation

This installation guide assumes that the application is being installed on the latest version of [Ubuntu](http://www.ubuntu.com/ubuntu).


### Prerequisites

1. Install essential Python packages using, `sudo apt-get install python-setuptools python-dev build-essential`
2. Install MySQL Server and client library using, `sudo apt-get install mysql-server libmysqlclient-dev`
4. Install [virtualenv](https://pypi.python.org/pypi/virtualenv) using `sudo pip install -U virtualenv`
5. In the project root, run `virtualenv venv`
6. Activate the virtual environment using `source venv/bin/activate`
7. Once the virtual environment is active, run `pip install -r src/requirements.txt`
8. To deactivate the virtual environment (after you are done with the development), type `deactivate` and hit ENTER.
9. To re enable the virtual environment `cd src/scripts` and `source dev.sh` or just run `source venv/bin/activate`.


### Configuration

All the project configurations are present in the file `settings.py.sample` located at `src/core/`. Copy it to `settings.py` and add any configurations or modifications you need to `settings.py`.  

Some Ideal configurations for development are listed below.


```python

DEVELOPMENT = True
DEBUG = True
```


### Setting up the Database

1. Create a database with any name you wish.
2. Then change directory to `src/core` using `cd src/core`
3. Update the schema from alembic version files using the command, `alembic upgrade head`
4. When you edit the schema and want to sync it to the database, go to `src/core` and run the command `alembic revision --autogenerate -m "<revision_message_here>"`. Here the revision message is a simple short line telling what was changed just like a git commit message. Then run, `alembic upgrade head`


### Running the Application (For Development)

1. Go to `src/` and run the application using, `python run.py`
2. Point your browser to the url that gets displayed.


## Development Workflow

1. Copy the `settings.py.sample` using the command, `cp settings.py.sample setting.py`
2. Make appropriate settings in `settings.py`
3. Go to `src/scripts` and run `source dev.sh`.
4. Run the migrations as mentioned in the previous section.
5. Go to `src/` and run the application using, `python run.py` and point your browser to the url that gets displayed.


## Contributing

I love contributors! Fork the repository and start sending pull requests...  

As [Ken Keyes](http://en.wikipedia.org/wiki/Ken_Keyes,_Jr.) said,

>“Everyone and everything around you is your teacher.”

If you feel there is something in __shfl__ that can be done better, let me know or better, do it and send me a pull request! I believe, "code is worth a thousand words!"


## Bug Reporting

If you find any bugs, feel free to report it by raising an [issue here](https://github.com/sandeepraju/shfl/issues).


## Author

Hi! I'm [Sandeep Raju P](https://github.com/sandeepraju). I tweet as [@sandeeprajup](https://twitter.com/sandeeprajup). To know more about me, check out [my website](http://sandeepraju.in).  
To contact me directly, shoot me a mail at [me@sandeepraju.in](mailto:me@sandeepraju.in).


## License

This project is licensed under the [MIT License](https://github.com/sandeepraju/shfl/blob/master/LICENSE.txt).


## Getting Started

1. Flask Tutorial - http://flask.pocoo.org/docs/quickstart/
2. Flask Mega Tutorial - http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
