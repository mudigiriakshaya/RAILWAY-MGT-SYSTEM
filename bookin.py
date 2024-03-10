import mysql.connector
class book:
   def __init__(self):
         self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='Amysql@123',
            database='railway1'
            )
   def trainfetch(self,src,dest):
        cur = self.conn.cursor()
        cur.execute('''SELECT ROUTES.TRAIN_NO,STOP1,STOP2,STOP3,STOP4,SOURCE,DESTINATION FROM ROUTES 
                    INNER JOIN 
                    TRAIN_DETAILS ON
                    ROUTES.TRAIN_NO=TRAIN_DETAILS.TRAIN_NO WHERE 
                    SOURCE='{src}' OR STOP1='{src}'OR STOP2='{src}' OR STOP3='{src}' OR STOP4='{src}';''')
        dt=cur.fetchall()
        try:
           tr=[]
           for i in dt:
                for j in i[i.index(src)+1]:
                    if j==dest:
                        tr.append(i)
        except:
            pass
        print(tr)
# jt=book()
# jt.trainfetch('bgl','khm')
   def add_psngr(self,PID,Pname,age,mbl_no,Gender):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO PASSENGERS VALUES({PID},'{Pname}',{age},{mbl_no},'{Gender}')")
        self.conn.commit()
        print("Passenger Details Added Succesfully....") 
   def add_transaction(self,tid,PID,amount,mode):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},{PID},{amount},'{mode}')")
        self.conn.commit()
        print("Transaction Succesful....")
   def bookticket(self,b_id,PID,cls,tid,seat_no,source,dest,trainno):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO  BOOK_TICKETS VALUES({b_id},{PID},'{cls}',{seat_no},{tid},'{source}','{dest}',{trainno})")
        self.conn.commit()
        print("Data has been Booked sucessfully")
        print(PID,seat_no,b_id,cls,source,dest,tid,sep="\n")
    

