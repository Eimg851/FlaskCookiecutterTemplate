# -*- coding: utf-8 -*-

"""Main module."""
from flask import render_template
from app import app

from systeminfo.main import get_platform 

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'COMP30670'
    returnDict['title'] = 'Home'
    returnDict['platform'] = get_platform()
    return render_template("index.html", **returnDict)