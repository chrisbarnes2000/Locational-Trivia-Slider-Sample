from flask import Flask, render_template, request,
import os

app = Flask(__name__)

# INDEX
@app.route('/')
@app.route('/index')
def items_index():
    """Show the Home page."""
    return render_template('index.html')  # , items=items.find()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
