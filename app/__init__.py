# -*- coding: utf-8 -*-

"""Top-level package for flask_platform."""

__author__ = """Eimear Galligan"""
__email__ = 'eimear.galligan@ucdconnect.ie'
__version__ = '0.1.0'

from flask import Flask
app = Flask(__name__)
from app import views
