__author__ = 'haroldhannon'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey you found the thing'

@app.route('/clean')
def clean():
    # set roomba to clean mode
    return 'Cleaning'

@app.route('/dock')
def dock():
    # set roomba to dock mode
    return 'Docking'

if __name__ == '__main__':
    app.run(host='0.0.0.0')