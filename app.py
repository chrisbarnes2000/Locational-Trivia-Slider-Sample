from flask import Flask, render_template, request
import os
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

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
