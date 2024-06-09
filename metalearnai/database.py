import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_problem(conn, name, search_space, objective_function, constraints):
    """Add a new problem to the problems table"""
    sql = ''' INSERT INTO problems(name, search_space, objective_function, constraints)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (name, search_space, objective_function, constraints))
    conn.commit()

def add_algorithm(conn, strategy, criteria):
    """Add a new algorithm to the algorithms table"""
    sql = ''' INSERT INTO algorithms(strategy, criteria)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (strategy, criteria))
    conn.commit()

def main():
    database = "metalearnai.db"

    sql_create_problems_table = """ CREATE TABLE IF NOT EXISTS problems (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        search_space text,
                                        objective_function text,
                                        constraints text
                                    ); """

    sql_create_algorithms_table = """ CREATE TABLE IF NOT EXISTS algorithms (
                                        id integer PRIMARY KEY,
                                        strategy text NOT NULL,
                                        criteria text
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_problems_table)
        create_table(conn, sql_create_algorithms_table)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
