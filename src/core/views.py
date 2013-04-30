# Local project imports
from core import app
from core.models import User
import helpers as util

# Standard python imports
import json
import os

# Third party imports
from flask import render_template, send_from_directory


# Application index
@app.route("/")
def index():
    return render_template("index.html")


# Application error handlers
@app.errorhandler(404)
def not_found(error=None):
    return render_template("404.html"), 404


# Etc routes (favicon, robots.txt, humans.txt, etc.)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt', mimetype='text/plain')


@app.route('/humans.txt')
def humans():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'humans.txt', mimetype='text/plain')
