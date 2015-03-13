__author__ = 'haroldhannon'

from flask import Flask
import time
import wiringpi2


app = Flask(__name__)

wiringpi2.wiringPiSetup()
wiringpi2.pinMode(0,1)
wiringpi2.pinMode(1,1)

@app.route('/')
def hello_world():
    return 'Hey you found the thing'

@app.route('/clean')
def clean():
    # set roomba to clean mode
    wiringpi2.digitalWrite(0,1)
    time.sleep(5)
    wiringpi2.digitalWrite(0,0)
    return 'Cleaning'

@app.route('/dock')
def dock():
    # set roomba to dock mode
    wiringpi2.digitalWrite(1,1)
    time.sleep(5)
    wiringpi2.digitalWrite(1,0)
    return 'Docking'

if __name__ == '__main__':
    app.run(host='0.0.0.0')