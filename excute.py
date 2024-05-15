import sqlite3
from sqlite3 import Error
def show():
    try:
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        cur.execute("select * from student")
        #cur.execute("SELECT name FROM sqlite_master WHERE type='table'") #all tables name in database
        rows=cur.fetchall()
        for row in rows:
            print(row)
        con.close()
    except Error as ex:
        print(ex)

show()
