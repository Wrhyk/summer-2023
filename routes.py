import sqlite3, random
from flask import Flask, flash, render_template, request, redirect, url_for, g
from setup import add_fish, add_user, select_user
app = Flask(__name__)

app.secret_key = "VERY_SECRET"

DATABASE = './database.db'


#need to rework entire app file to be able to cooperate with jinja and async