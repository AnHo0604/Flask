# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:55:00 2021

@author: anho
"""
###############################################################################
from flask import Flask

# simple Flask web app :
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello there!'

###############################################################################
# chay :
def main():
    app.run()
if __name__=='__main__':
    main()