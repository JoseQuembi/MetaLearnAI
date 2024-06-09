import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        search_space TEXT NOT NULL,
        objective_function TEXT NOT NULL,
        constraints TEXT
    );"""
    conn.execute(sql_create_projects_table)

def add_problem(conn, problem):
    sql = ''' INSERT INTO problems(search_space, objective_function, constraints)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, problem)
    conn.commit()
    return cur.lastrowid

def get_problems(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM problems")
    return cur.fetchall()
