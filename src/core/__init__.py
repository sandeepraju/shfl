from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail

# Configuring Flask Application
app = Flask(__name__)
app.config.from_object("core.settings")

# Web Assets Configuration
webAssets = Environment(app)
webAssets.register("js_lib", Bundle("js/underscore.js",
                        "js/jquery.js", "js/backbone.js",
                        filters="jsmin",
                        output="assets/min.libs.js"))
webAssets.register("js_main", Bundle("js/main.js", filters="jsmin",
                        output="assets/min.main.js"))

# Configuring database
db = SQLAlchemy(app)

# Configuring flask debug toolbar
toolbar = DebugToolbarExtension(app)

# Configuring flask mail
mail = Mail(app)

__import__("core.models")
__import__("core.views")

