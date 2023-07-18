# Imports needed for initalisation of the app #
import os
import sqlite3 
from sqlite3 import Error
from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import check_password_hash 
import secrets
from flask_talisman import Talisman

SECRET_KEY = "secret"

# class for config #
class Config(object):
    SK = secrets.token_hex()
    DB = 'datafish.db'


    
# Creating an app #
app = Flask(__name__)
Bootstrap(app)

# Activating reCaptcha #
app.config.from_object(Config)
app.secret_key = app.config["SK"]
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'





# Initalize database for the first time #
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Get an instance of the database #
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db


# Add a user to the fish website #
def add_user(nickname, first_name, last_name, password):
    conn = get_db()
    cur = conn.cursor()
    sql = ''' INSERT INTO users(nickname, first_name, last_name, password)
              VALUES( ?, ?, ?, ?, ?, ?) '''
    try:
        
        cur.execute(sql, (nickname, first_name, last_name, password))
        conn.commit()
    except Error as e:
        print(e)
    else: 
        print("User created with nickname {}.".format(nickname))
        return cur.lastrowid
    finally:
        conn.close()

# Query for adding fish to db #
def add_fish(fish_id, fish_type, weight, length, x_location, y_location, nickname):
    conn = get_db()
    cur = conn.cursor()
    sql = ('INSERT INTO fish(fish_id, fish_type, f_weight, f_length, x_location, y_location, nickname) VALUES (?, ?, ?, ?, ?, ?, ?)')
    try:
        cur.execute(sql, (fish_id, fish_type, weight, length, x_location, y_location, nickname))
        conn.commit()
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return -1
    else:
        print("Fish {} created with id {} and added to user {}.".format(fish_type, fish_id, nickname))
        return cur.lastrowid
    finally:
        cur.close()


# Query for selecting user from inputed nickname #
def select_user(nickname):
        conn = get_db()
        cur = conn.cursor()
        try:
            sql = ('SELECT nickname, first_name, last_name, fish_id FROM users u WHERE u.nickname = ?')
            cur.execute(sql, nickname)
            for row in cur:
                (nickname, first_name, last_name) = row
                return{
                    "nickname": nickname,
                    "first_name": first_name,
                    "last_name": last_name
                }
            user = (nickname, first_name, last_name)
            return user
        except sqlite3.Error as e:
            print("Error: {}".format(e))
            return -1
        finally:
            cur.close()


# Query for selecting all fish types in database
def select_fish_types():
    conn = get_db()
    cur = conn.cursor()
    try:
        sql = ('SELECT * FROM fish_types')
        cur.execute(sql)
        array = []
        for row in cur:
            array.append(row)
            return array
    except sqlite3.Error as e:
        print("Error: {}".format(e))
        return -1
    finally:
        cur.close()

# Automatically called when application is closed, and closes db connection #
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if not os.path.exists(app.config['DB']):
    init_db()


# Need to rework entire setup file to work with sql schema and others #

#from flask_login import LoginManager