Shfl
====

__Shfl__ is a minimal [Flask](http://flask.pocoo.org/) boilerplate structured to build large web applications in a modular way.


## Technologies Used

1. [Flask](http://flask.pocoo.org/) micro framework.
2. HTML5 & CSS3 via [Initializr](http://www.initializr.com/).
3. [jQuery](http://jquery.com).
4. [Backbone.js](http://backbonejs.org/).


## Installation

This installation guide assumes that the application is being installed on the latest version of [Ubuntu](http://www.ubuntu.com/ubuntu).


### Prerequisites

1. Install Python development packages using, `sudo apt-get install python-dev`
2. Install [Python pip](https://pypi.python.org/pypi/pip) using `sudo apt-get install python-pip`
3. Install Python MySQLDB package using, `sudo apt-get install python-mysqldb` 
4. Install [virtualenv](https://pypi.python.org/pypi/virtualenv) using `sudo pip install virtualenv`
5. In the project root, run `virtualenv venv`
6. Activate the virtual environment using `. venv/bin/activate`
7. Once the virtual environment is active, run `pip install -r src/requirements.txt`
8. To deactivate the virtual environment, type `deactivate` and hit ENTER.


### Configuration

All the project configurations are done in the file `settings.py` located at `src/core/settings.py.sample`. Rename it to `settings.py` before adding any configurations or modifying them.  

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


## Development Workflow

1. Rename the `settings.py.sample` using the command, `mv settings.py.sample setting.py`
2. Make appropriate settings in `settings.py`
3. Go to `src/scripts` and run `source dev.sh`.
4. Run the migrations as mentioned in the previous section.
5. Go to `src/` and run the application using, `python run.py` and point your browser to the url that gets displayed.


## Contributing

I love contributors! Fork the repository and start sending pull requests...  


## Bug Reporting

If you find any bugs, feel free to report it by raising an [issue here](https://github.com/sandeepraju/shfl/issues).


## Author

[Sandeep Raju P](https://github.com/sandeepraju)  
[@sandeeprajup](https://twitter.com/sandeeprajup)  
[me@sandeepraju.in](mailto:me@sandeepraju.in)  
[sandeepraju.in](http://sandeepraju.in)  


## License

This project is licensed under the [MIT License](https://github.com/sandeepraju/shfl/blob/master/LICENSE.txt).


## Getting Started

1. Flask Tutorial - http://flask.pocoo.org/docs/quickstart/
2. Flask Mega Tutorial - http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
