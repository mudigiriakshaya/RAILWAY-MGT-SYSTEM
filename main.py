# importing Required modules
from traindetails import details
from traincapacity import capacity
from routes import routes
from bookin import book
import numpy as np

print("-----------Welcome to Railway Management System----------")
print('-------- For Inserting the Data Enter - 1--')
print('-------- For Reading the Data Enter - 2--')
print('-------- For Updating the Data Enter - 3--')
print('-------- For Deleting the Data Enter - 4--')

opr = int(input("Please Enter your operation: "))
if opr==1:
    print('--- For inserting the data in traindetails press 1---')
    print('--- For inserting the data in traincapacity press 2---')
    print('--- For inserting the data in routes press 3---')
    print('--- For Booking a ticket press 4 ---')
    inopr = int(input("Please Select an operation: "))
    if inopr==1:
        obj = details()
        tno = int(input("Please enter train no:"))
        src = input("Please Enter Source station:")
        dst = input("Please enter Destination station:")
        tname = input("Please enter train name:")
        obj.insertdetails(tno,src,dst,tname)
    if inopr==2:
        obj = capacity()
        obj1 = details()
        obj1.trainofetch()
        trn = int(input("Please Enter train number: "))
        ac1 = int(input("Please Enter Capacity of AC 1: "))
        ac2 = int(input("Please Enter Capacity of AC 2: "))
        ac3 = int(input("Please Enter Capacity of AC 3: "))
        sl = int(input("Please Enter Capacity of Sleeper class: "))
        gen = int(input("Please Enter Capacity of General Class: "))
        obj.capacityinsert(trn,ac1,ac2,ac3,sl,gen)
    if inopr==3:
        obj = routes()
        obj1 = details()
        obj1.trainofetchroutes()
        trn = int(input("Please Enter train number: "))
        st1 = input("Please Enter Stop 1: ")
        st2 = input("Please Enter Stop 2: ")
        st3 = input("Please Enter Stop 3: ")
        st4 = input("Please Enter Stop 4: ")
        obj.routesinsert(trn,st1,st2,st3,st4)
    if inopr==4:
        source=input("Please Enter Your Source From:")
        dest=input("Please Enter Your Destination:")
        obj=book()
        obj.trainfetch(source,dest)
        train_no=int(input("Please3 Enter Train No: "))
        cls=input("Please Enter Your Coach: ")
        #passenger info 
        pid=int(input("Please Enter Your ID: "))
        pname=input("Please Enter Your Name: ")
        Age=input("Please Enter Your Age: ")
        Mobile_no=input("Please Enter Your Mobile_no: ")
        Gender=input("Please Enter Your Gender: ")
        
        obj.add_psngr(pid,pname,Age,Mobile_no,Gender)
        #making Transaction
        t_id=int(input("Please Enter Your T_id: "))
        amount=int(input("Please Enter Your Amount: "))
        mode=input("Please Enter Your Payment Method: ")
        obj.add_transaction(t_id,pid,amount,mode)
        #booking ticket 
        bid=np.random.randint(0,500000,1)[0]
        st_no=np.random.randint(0,60,1)[0]
        obj.bookticket(bid,pid,cls,t_id,st_no,source,dest,train_no)

if opr==2:
    pass
if opr==3:
    pass
if opr==4:
    pass








































# from traindetails import details  
# obj=details()


# tno=int(input("Please Enter Train No: "))
# src=input("Please Enter Your Source Station: ")
# dst=input("Please Enter Your Destination Station: ")
# tname=input("Please Enter Train Name: ")
# # obj.insertdetails()

# obj.insertdetails(tno,src,dst,tname)
