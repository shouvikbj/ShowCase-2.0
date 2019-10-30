import sqlite3

con = sqlite3.connect('msg.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
        CREATE TABLE IF NOT EXISTS msg(
            name VARCHAR2(100),
            email VARCHAR2(300),
            msg VARCHAR2(100000000000000000000)
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS msgBackUp AS SELECT * FROM msg WHERE 1=1;
    """)

def enterMsg(name,email,msg):
    db.execute("INSERT INTO msg VALUES(?,?,?)",(name,email,msg))
    db.execute("INSERT INTO msgBackUp VALUES(?,?,?)",(name,email,msg))
    con.commit()

def getMsgs():
    db.execute("SELECT * FROM msg")
    msgs = db.fetchall()
    return msgs





#createTable()