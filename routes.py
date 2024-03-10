import mysql.connector 
import mysql.connector
class routes:
    def __init__(self):
         self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Amysql@123',
            database='railway1'
            ) 
    def routesinsert(self,trn,st1,st2,st3,st4):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO routes VALUES({trn},'{st1}','{st2}','{st3}','{st4}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")