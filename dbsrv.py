
import sqlite3

# for sqlite
def save_users(name, age):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connect.commit()
    connect.close()

class DBService:
    def __init__(self):
        self.dbdata = {}
    def add_user(self, aduser, adname):
        if aduser in self.dbdata:
           raise ValueError("This user already exist in a DB")
        self.dbdata[aduser] = adname
    def get_user(self, gtuser):
        return self.dbdata.get(gtuser, None)
    def update_user(self):
        pass
    def delete_user(self, dluser):
        if dluser in self.dbdata:
            del self.dbdata[dluser]

