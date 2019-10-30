import sqlite3

con = sqlite3.connect('posts.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
        CREATE TABLE IF NOT EXISTS posts(
            cat VARCHAR2(150),
            short VARCHAR2(5000),
            long VARCHAR2(100000000),
            specs VARCHAR2(100000000),
            imgfile VARCHAR2(150),
            vdofile VARCHAR2(150)
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS postsBackUp AS SELECT * FROM posts  WHERE 1=1;
    """)


def createPost(cat,short,long,specs,imgfile,vdofile):
    db.execute("INSERT INTO posts VALUES(?,?,?,?,?,?)",(cat,short,long,specs,imgfile,vdofile))
    db.execute("INSERT INTO postsBackUp VALUES(?,?,?,?,?,?)",(cat,short,long,specs,imgfile,vdofile))
    con.commit()

def getPosts():
    db.execute("SELECT * FROM posts")
    posts = db.fetchall()
    return posts


#createTable()
