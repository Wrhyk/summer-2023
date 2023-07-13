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
                    `nickname` VARCHAR(45) NOT NULL PRIMARY KEY,
                    `first_name` VARCHAR(45) NOT NULL,
                    `last_name` VARCHAR(45) NOT NULL,
                    `password` CHAR(60) NOT NULL,
                    `fish_id` INT,
                    FOREIGN KEY ("fish_id") REFERENCES `fish` (`fish_id`)
                    );"""


sql_create_fish = """CREATE TABLE IF NOT EXISTS `fish` (
                `fish_id` INT NOT NULL PRIMARY KEY,
                `fish_type` VARCHAR(60) NOT NULL,
                `size` VARCHAR(20) NOT NULL,
                `x_location` DECIMAL(30) NOT NULL,
                `y_location` DECIMAL(30) NOT NULL,
                `nickname` varchar(45) NOT NULL,
                FOREIGN KEY ("nickname") REFERENCES `users` (`nickname`)
                );"""


def create_table(conn, sql_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)



def add_user(conn, nickname, first_name, last_name, password):
    sql = ''' INSERT INTO users(nickname, first_name, last_name, password)
              VALUES(*,*,*,*,*,*) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, (nickname, first_name, last_name, password))
        conn.commit()
    except Error as e:
        print(e)


def add_fish(conn, fish_id, fish_type, size, x_location, y_location, nickname):
    sql = ''' INSERT INTO fish(fish_id, fish_type, size, x_location, y_location, user_id)
            VALUES(*,*,*,*,*)'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (fish_id, fish_type, size, x_location, y_location, nickname))
        conn.commit()
    except Error as e:
        print(e)


def select_user(conn, nickname):
        cur = conn.cursor()
        sql = 'SELECT * FROM users u WHERE u.nickname = ('nickname')'
        cur.execute(sql)
        return cur





def setup():
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_users)
        create_table(conn, sql_create_fish)
        conn.close()


if __name__ == '__main__':
    setup()

# Need to rework entire setup file to work with sql schema and others#