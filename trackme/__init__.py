from flask import Flask
from pymongo import Connection

app=Flask(__name__)

connection = Connection('localhost', 27017)
db = connection.trackme

from . import views
