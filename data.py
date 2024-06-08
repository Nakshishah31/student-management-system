import cx_Oracle
import time
constr = 'system/2172987539319@localhost:1521/XE_XPT'
conn = None
try:
    conn = cx_Oracle.connect(constr)
    cur = conn.cursor()
    while True:
        
        print("-------------------------------------------------------")
        print("----------Welcome To Student Database System-----------")
        print("-------------------------------------------------------")
        print("\t1.Add a New Student")
        print("\t2.Update a detail of Existing")
        print("\t3.Delete An Existing Studnet")
        print("\t4.Display Student")
        print("\t5.Exit")
        ch = int(input("\tEnter Choice:"))
        match ch:
            case 1:

                id = int(input("Enter Student ID:"))
                name = input("Enter Full Name:")
                dob = input("Enter Date Of Birth(DD-MON-YY):")
                gen = input("Enter Gender:")
                phone = int(input("Enter Phone Number:+91 "))
                email = input("Enter Email ID:")
                sqlq = 'INSERT into student values(:1,:2,:3,:4,:5,:6)'
                cur.execute(sqlq, (id, name, dob, gen, phone, email))
                conn.commit()

                print("1 Row inserted Successfully..")
                time.sleep(3)