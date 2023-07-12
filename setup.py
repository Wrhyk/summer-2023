import sqlite3
from sqlite3 import Error

database = r"./datafish.db"

def create_connection(datafish):
    conn = None
    try:
        conn = sqlite3.connect(datafish)
        return conn
    except Error as e:
        print(e)

    return conn


sql_create_users = """CREATE TABLE IF NOT EXISTS `users` (
                    `user_id` INT NOT NULL PRIMARY KEY,
                    `first_name` VARCHAR(45) NOT NULL,
                    `last_name` VARCHAR(45) NOT NULL,
                    `nickname` VARCHAR(45) NOT NULL,
                    `password` CHAR(60) NOT NULL,
                    );"""

sql_create_fish_types = """CREATE TABLE IF NOT EXISTS `fish_types` (
                        `fish_name` VARCHAR(60) NOT NULL PRIMARY KEY 
                        );"""



sql_create_fish = """CREATE TABLE IF NOT EXISTS `fish` (
                `fish_id` INT NOT NULL PRIMARY KEY,
                `fish_type` VARCHAR(60) NOT NULL,
                `size` VARCHAR(20) NOT NULL,
                `x_location` DECIMAL(30) NOT NULL,
                `y_location` DECIMAL(30) NOT NULL,
                `user_id` int NOT NULL,
                FOREIGN KEY (`fish_type`) REFERENCES `fish_types` (`fish_name`),
                FOREIGN KEY ("user_id) REFERENCES `users` (`user_id`)
                );"""


def create_table(conn, sql_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)



def add_user(conn, user_id, first_name, last_name, nickname, password):
    sql = ''' INSERT INTO users(user_id, first_name, last_name, nickname, password)
              VALUES(*,*,*,*,*,*) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (user_id, first_name, last_name, nickname, password))
        conn.commit()
    except Error as e:
        print(e)


def add_fishtype(conn, fish_name):

    sql = ''' INSERT INTO fish_types(fish_name)
              VALUES(*) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, fish_name)
        conn.commit()
    except Error as e:
        print(e)

def add_fish(conn, fish_id, fish_type, size, x_location, y_location, user_id):
    sql = ''' INSERT INTO fish(fish_id, fish_type, size, x_location, y_location, user_id)
            VALUES(*,*,*,*,*)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (fish_id, fish_type, size, x_location, y_location, user_id))
        conn.commit()
    except Error as e:
        print(e)

def setup():
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_users)
        create_table(conn, sql_create_fish_types)
        create_table(conn, sql_create_fish)
        conn.close()


if __name__ == '__main__':
    setup()
