'''
Created on 04-Sep-2019
@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
import os

COLOR= os.getenv('color')

from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/healthz/readiness/')   # URL '/' to be handled by main() route handler
def readiness():
    """Say hello"""
    return 'Hello, readiness test'

@app.route('/healthz/liveness/')   # url '/' to be handled by main() route handler
def liveness():
    """say hello"""
    return 'hello, liveness test'

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    msg = 'Hello the color is ' + COLOR
    return msg

@app.route('/delay/<seconds>')   # URL '/' to be handled by main() route handler
def delay(seconds):
    import time
    """Say hello"""
    msg = 'Time response v1.0 (seconds) is  ' + str(seconds) + '\n'
    time.sleep(int(seconds))
    return msg

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
