import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_word(conn, Words):
    """
    Create a new project into the projects table
    :param conn:
    :param Words:
    :return: project id
    """
    sql = ''' INSERT INTO Words(word,category,pegi,commentCount,commentScore,appSizeMB,downloads,ranking)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, Words)
    conn.commit()
    return cur.lastrowid

def create_color(conn, Color):
    """
    Create a new project into the projects table
    :param conn:
    :param Color:
    :return: project id
    """
    sql = ''' INSERT INTO Colors(category,pegi,commentCount,commentScore,appSizeMB,downloads,ranking,FirstRGB,FirstHEX,FirstHSL,SecondRGB,SecondHEX,SecondHSL)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, Color)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"C:\Users\Gokturk\Desktop\MyDatabase.db"

    sql_create_words_table = """ CREATE TABLE IF NOT EXISTS Words (
                                        id integer PRIMARY KEY,
                                        word text,
                                        category text,
                                        pegi int,
                                        commentCount integer,
                                        commentScore real,
                                        appSizeMB real,
                                        downloads integer,
                                        ranking integer
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_words_table)
    else:
        print("Error! cannot create the database connection.")


def push_new_word_to_db(word,category,pegi,commentCount,commentScore,appSize,downloads,ranking):
    database = r"C:\Users\Gokturk\Desktop\MyDatabase.db"
    conn = create_connection(database)
    with conn:
        newdata = (word,category,pegi,commentCount,commentScore,appSize,downloads,ranking)
        create_word(conn,newdata)


def push_new_color_to_db(category,pegi,commentCount,commentScore,appSize,downloads,ranking,rgb,hex,hsl,srgb,shex,shsl):
    database = r"C:\Users\Gokturk\Desktop\MyDatabase.db"
    conn = create_connection(database)
    with conn:
        newdata = (category,pegi,commentCount,commentScore,appSize,downloads,ranking,rgb,hex,hsl,srgb,shex,shsl)
        create_color(conn,newdata)
#push_new_word_to_db('heloo','categ',3,4,15,8,2,123,4)