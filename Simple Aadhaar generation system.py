import mysql.connector as sqltor
import random



#generating Aadhaar id
def Ad():
    id = random.randint(100000000000,999999999999)
    print("=============================================================")
    print("Your new generated Id is....",id)
    print("=============================================================")
    


#new enrollment
def New():
    try:
      mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
      cur=mycon.cursor()
      print("-----------------------------------------------------------------")
      Ad_id = (input("Please enter your new generated aadhaar_id:"))
      print("-----------------------------------------------------------------")
      Name = input("Enter Name:")
      print("-----------------------------------------------------------------")
      DOB = input("Enter Date of Birth:")
      print("-----------------------------------------------------------------")
      Gender = input("Enter Gender:")
      print("-----------------------------------------------------------------")
      Phone_no = int(input("Enter your phone number:"))
      print("-----------------------------------------------------------------")
      Address = input("Enter Address:")
      print("-----------------------------------------------------------------")
    
      query = "insert into data(Ad_id,Name,DOB,Gender,Phone_no,Address)values('{}','{}','{}','{}','{}','{}')".format(Ad_id,Name,DOB,Gender,Phone_no,Address) 
      cur.execute(query)
      mycon.commit()
      mycon.close()
      print("-----------------------------------------------------------------")
      print("Records has been successfully entered  !!!")
      print("For registration of biometric details please visit your nearest enrollment centre....")
      print("#################################################################")
    except:
        print("Error!!!")
        print("-----------------------------------------------------------------")
        
        
        
# check status
def checkall():
      mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
      cur=mycon.cursor()
      cur.execute("select * from data")
      record = cur.fetchall()
      for row in record:
        print(row)
        print("-----------------------------------------------------------------")
   
    
def checksingle():
    try:
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     ad = input("Enter your Aadhaar id:")
     st = "select * from data where Ad_id='%s'" % (ad)
     cur.execute(st)
     record = cur.fetchall()
     for row in record:
         print(row)
    except:
      print("ERROR!!!....This id doesnot exist")
      print("-----------------------------------------------------------------")
    
    

#edit option
def edit_name():
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     ad = input("Enter your Aadhaar id:")
     nm = input("Enter correct name:")
     st = "update data set Name='%s' where Ad_id='%s'"%(nm,ad)
     cur.execute(st)
     mycon.commit()
     print("Data updated Successfully")
     
     
def edit_dob():
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     ad = input("Enter your Aadhaar id:")
     nm = input("Enter correct dob:")
     st = "update data set Name='%s' where DOB='%s'"%(nm,ad)
     cur.execute(st)
     mycon.commit()
     print("Data updated Successfully")
     
def edit_gen():
    mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
    cur=mycon.cursor()
    ad = input("Enter your Aadhaar id:")
    nm = input("Enter correct Gender:")
    st = "update data set Gender='%s' where Ad_id='%s'"%(nm,ad)
    cur.execute(st)
    mycon.commit()
    print("Data updated Successfully")

def edit_ph():
    mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
    cur=mycon.cursor()
    ad = int(input("Enter your Aadhaar id:"))
    nm = int(input("Enter correct phone number:"))
    st = "update data set Phone_no='%s' where Ad_id='%s'"%(nm,ad)
    cur.execute(st)
    mycon.commit()
    print("Data updated Successfully")

def edit_address():
    mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
    cur=mycon.cursor()
    ad = input("Enter your Aadhaar id:")
    nm = input("Enter correct Address:")
    st = "update data set Address='%s' where Ad_id='%s'"%(nm,ad)
    cur.execute(st)
    mycon.commit()
    print("Data updated Successfully")


      
# update
def update():
     print("******************************************************************")
     print("Do you want to -")
     print("1. Edit Name")
     print("2. Edit Dob")
     print("3. Edit Gender")
     print("4. Edit Phone number")
     print("5. Edit Address")
     print("6. Return")
     print("\t\t\t-------------------------------------------------------------")
     choice=int(input("Enter your choice:"))
     if choice == 1:
         edit_name()
         print("-----------------------------------------------------------------")
     elif choice==2:
         edit_dob()
         print("-----------------------------------------------------------------")
     elif choice==3:
         edit_gen()
         print("-----------------------------------------------------------------")
     elif choice==4:
         edit_ph()
         print("-----------------------------------------------------------------")
     elif choice==5:
         edit_address()
         print("-----------------------------------------------------------------")
     elif choice==6:
         return
     else:
         print("Error: invalid choice Try again....")
         print("-----------------------------------------------------------------")
         
 
def newec():
     try:
         mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
         cur=mycon.cursor()
         City = input("Enter City:")
         Type = input("Enter Type(Permanent/temporary):") 
         Address =  input("Enter Address:")
      
         query = "insert into centres(City,Type,Address)values('{}','{}','{}')".format(City,Type,Address) 
         cur.execute(query)
         mycon.commit()
         print("Records has been successfully entered....")
         print("#################################################################")
     except:
         print("Error!!!")
         print("-----------------------------------------------------------------")
      
    
def searchec():
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     cur.execute("select * from centres")
     record = cur.fetchall()
     for row in record:
        print("------------------------------------------------------------------") 
        print(row)
        print("------------------------------------------------------------------")
    

def deleec():
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     ad = input("Enter the address:")
     st = "delete from centres where Address='%s'" % (ad)
     cur.execute(st)
     mycon.commit()
     print("Record deleted successfully.....")
     print("==========================================================")
     
    
         
#editec
def edit():
    while True:
        print("1. New Centre")
        print("2. See all centres")
        print("3. Delete Centre")
        print("4. Exit")
        choice = int(input("Enter Choice between 1 to 4-----------> :" ))
        if choice == 1:
           print("-----------------------------------------------------------------")
           newec()
        elif choice == 2:
           print("-----------------------------------------------------------------")
           searchec()
        elif choice == 3:
           print("-----------------------------------------------------------------")
           deleec()
        else:
           break
           
       
           
        
         
#editing centres
def editec():
  while True:
      print("-----------------------------------------------------------------")
      print("\t\t\t Enrollment Centre Management Menu \n")
      Passwd = input("Enter login password:")
      if  Passwd == "password":
          print("---------->")
          edit()
      else:
          print("ERROR!!! You entered wrong password")
          print("----------------------------------")
          print("1. Try Again")
          print("2. Exit")
          choice = int(input("Enter Choice between 1 and 2-----------> :" ))   
          if choice == 1:
              editec()
          else:
              break
          
             
# search ec
def nearestec():
    mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
    cur=mycon.cursor()
    city = input("Enter your City:")
    query = "select * from centres where City='%s'" % (city)
    cur.execute(query)
    record = cur.fetchall()
    for row in record:
        print("------------------------------------------------------------------")
        print(row)
        print("------------------------------------------------------------------")
        

def citywiseec():
    mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
    cur=mycon.cursor()
    cur.execute("select * from centres")
    record = cur.fetchall()
    for row in record:
        print("------------------------------------------------------------------")
        print(row)
        print("------------------------------------------------------------------")
        

#delete 
def dele():
     mycon=sqltor.connect(host ="localhost",user ="root",passwd ="admin",database ="Aadhaar",use_pure = True)
     cur=mycon.cursor()
     ad = input("Enter your Aadhaar id:")
     st = "delete from data where Ad_id='%s'" % (ad)
     cur.execute(st)
     mycon.commit()
     print("Record deleted successfully.....")
     print("==========================================================")
     
     
#Operator Menu
def opmenu():
    while True:
       print("1. New Enrollment")
       print("2. Update")
       print("3. Check Status")
       print("4. Enrolment Centres")
       print("5. Delete data")
       print("6. Go to Home Page")
       print("======================================================================") 
       choice = int(input("Enter Choice between 1 to 6-----------> :" ))
       if choice==1:
          print("===================================================================")
          Ad()
          New()
       elif choice==2:
         print("====================================================================")
         update()
       elif choice==3:
         print("====================================================================")
         print("1. Check single record")
         print("2. Check all records")
         choice = int(input("Enter Choice between 1 & 2-----------> :" ))
         if choice==1:
             checksingle()
             print("----------------------------------------------------------------")
         else:
             checkall()
             print("----------------------------------------------------------------")
       elif choice==4:
         print("====================================================================")
         print("1. Search by City")
         print("2. Show all Centres")
         print("3. Edit Enrollment Centres")
         choice = int(input("Enter Choice between 1 and 3-----------> :" ))
         if choice == 1:
             nearestec()
         elif choice == 2:
             citywiseec()
         else:
             editec()
       elif choice==5:
         print("==========================================================")
         dele()
       else:
         print("==========================================================")
         break
         
         
         
         


#Operator login
def Loginfunc():
    while True:
       Username=input("Enter Username:")
       passw=input("Enter password:")
       if Username=="" or passw=="":
         print("Error","All fields are required")
       elif Username=="Admin" and passw=="1234" :
         print("======================================================================")
         print("\t\t Welcome to the Operator Menu \n")
         opmenu()
       else:
          print("Error","Invalid Username/Password")
          print("----------------------------------")
          print("1. Try Again")
          print("2. Exit")
          choice = int(input("Enter Choice between 1 and 2-----------> :" ))
          if choice == 1:
              print("----------------------------------------------------------------")
          else:
              break
        
       

#User Menu 
def usermenu():
    while True:
       print("1. New Enrolment") 
       print("2. Update")
       print("3. Check Status")
       print("4. Nearest Enrolment Centre")
       print("5. Exit User Menu")
       print("========================================================================================") 
       choice = int(input("Enter Choice between 1 to 5-----------> :" ))
       if choice==1:
         print("===============================================================================")
         Ad()
         New()
         print("#################################################################")
       elif choice==2:
         print("===============================================================================")
         update()
         print("#################################################################")
       elif choice==3:
         print("===============================================================================")
         checksingle()
         print("#################################################################")
       elif choice==4:
         print("===============================================================================")
         nearestec()
         print("#################################################################")
       else:
           break


#___main___

while True:
    print("============================================================================================")
    print("\t\t\t Welcome to Aadhaar Management System \n")
    print("============================================================================================")
    print("Are you :")
    print("1. Operator")
    print("2. User")
    print("3. Exit the program")
    choice = int(input("Enter your choice ( 1 or 2 ) :" ))
    if choice==1:
        print("========================================================================================")
        print("\t\t Log in \n")
        Loginfunc()
    elif choice==2:
        print("========================================================================================")
        usermenu()
    else:
        break
    
    
    
    
    
    
    

        

       
