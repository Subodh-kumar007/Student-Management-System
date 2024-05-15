import sqlite3
def stm_database():
    con=sqlite3.connect(database="stm.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY,name text,email text,gender text,contact text,dob text,address text)")
    con.commit()

    con.close()

stm_database()





