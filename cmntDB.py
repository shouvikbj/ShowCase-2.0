import sqlite3

con = sqlite3.connect('cmnt.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
        CREATE TABLE IF NOT EXISTS cmnt(
            name VARCHAR2(200),
            cmnt VARCHAR2(100000000000000000000)
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS cmntBackUp AS SELECT * FROM cmnt WHERE 1=1;
    """)

def sendCmnt(name,cmnt):
    db.execute("INSERT INTO cmnt VALUES(?,?)",(name,cmnt))
    db.execute("INSERT INTO cmntBackUp VALUES(?,?)",(name,cmnt))
    con.commit()

def getCmnt():
    db.execute("SELECT * FROM cmnt")
    cmnt = db.fetchall()
    return cmnt
#sendCmnt('Shouvik Bajpayee','Comment body to test commenting fecility..')
#sendCmnt('Shouvik Bajpayee','Comment body to test commenting fecility..')
#sendCmnt('Shouvik Bajpayee','Comment body to test commenting fecility..')
#createTable()