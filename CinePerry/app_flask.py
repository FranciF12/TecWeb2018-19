#
# MOVIE TICKET PROJECT
#
# WEB TECHNOLOGIES
#
# Professor: Raffaele Montella
#
# Student: Francesco Perrotta
# Mat:0124000796
#
# 
# Server Flask Python
#


import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from db.dbConnection import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey!'
