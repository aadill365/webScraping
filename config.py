import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ARTICLE(
        id INTEGER NOT NULL PRIMARY KEY,
        url TEXT,
        headline TEXT,
        author TEXT,
        date TEXT
        );""")
        
        
    def insert(self,id,url,headline,author,date):
        
        try:
            data = self.cursor.execute("INSERT INTO ARTICLE VALUES(?,?,?,?,?)",(id,url, headline,author,date,))
            self.conn.commit()
        except:
            
            print('Duplicates found')
        
    def select(self):
        data = self.cursor.execute("SELECT * FROM ARTICLE")
        return data.fetchall()
    
    def close(self):
        self.conn.close()

