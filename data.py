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
                case 2:
                print("\t1. Change name")
                print("\t2. Change Date of Birth")
                print("\t3. Change Phone Number")
                print("\t4. Change Email Id")
                up = int(input("\tEnter Choice:"))
                up_id = int(input("Enter Id for updating details:"))

                match up:
                    case 1:
                        name_up=input("Changed name :")
                        sqlq=f"update set fullname = {name_up} where studentid = {up_id}"
                        cur.execute(sqlq)
                        conn.commit()
                    case 2:
                        dob_up=input("Changed Date Of Birth(DD-MON-YY): ")
                        sqlq=f"update set dob = {dob_up} where studentid = {up_id}"
                        cur.execute(sqlq)
                        conn.commit()
                    case 3:
                        phone_up=int(input("Changed Phone number : +91"))
                        sqlq=f"update set phoneno = {phone_up} where studentid = {up_id}"
                        cur.execute(sqlq)
                        conn.commit()
                    case 4:
                        email_up=input("Changed Email ID:")
                        sqlq=f"update set email = {email_up} where studentid = {up_id}"
                        cur.execute(sqlq)
                        conn.commit()
                    case _:
                        print("Pls Enter valid choice")
                        