import sqlite3
from peewee import *

def test():
    con = sqlite3.connect("sensor.db")

