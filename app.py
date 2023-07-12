import sqlite3, random
from flask import Flask, flash, render_template, request, redirect, url_for, g

app = Flask(__name__)

app.secret_key = "lmao"

DATABASE = './database.db'