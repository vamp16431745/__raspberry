<<<<<<< HEAD
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql_projects = """
    CREATE TABLE IF NOT EXISTS led(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		date TEXT NOT NULL,
		state INTEGER NOT NULL		
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_projects)
        print("Table created successfully")  
    except Error as e:
        print(e)

def insert_data(state):
    conn = create_connection('iot.db')
    create_table(conn)

    sql_insert = """
    INSERT INTO led(date, state) VALUES(datetime('now','localtime'), ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql_insert, (state,))
    conn.commit()
    conn.close()
=======
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql_projects = """
    CREATE TABLE IF NOT EXISTS led(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		date TEXT NOT NULL,
		state INTEGER NOT NULL		
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_projects)
        print("Table created successfully")  
    except Error as e:
        print(e)

def insert_data(state):
    conn = create_connection('iot.db')
    create_table(conn)

    sql_insert = """
    INSERT INTO led(date, state) VALUES(datetime('now','localtime'), ?);
    """
    cursor = conn.cursor()
    cursor.execute(sql_insert, (state,))
    conn.commit()
    conn.close()
>>>>>>> 67c4d4eac47f8e7b2dd2ec395f8177750c552a9c
