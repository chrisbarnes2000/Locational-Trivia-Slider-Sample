# -*- coding: utf-8 -*-

import os

REPO_NAME = "flask-ghpages-example"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# INDEX
@app.route('/')
@app.route('/index')
def index():
    """Show the Home page."""
    return render_template('index.html')

# ABOUT
@app.route('/about')
def about():
    """Show the About page."""
    return render_template('about.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
