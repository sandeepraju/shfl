# Local project imports
from core import app
from core.models import User
import helpers as util

# Standard python imports
import json

# Third party imports
from flask import render_template

# Application index
@app.route("/")
def index():
    return render_template("index.html")


# Application error handlers
@app.errorhandler(404)
def not_found(error=None):
    return render_template("404.html"), 404
