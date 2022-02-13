# CONNECTING DATABASE AND ADDING REQUIREMENTS
import mysql.connector as mcon
import time

con = mcon.connect(host="localhost", user="root", passwd="", database="GROCERY_MANAGEMENT_SYS")
cur = con.cursor()

msg1 = "GROCERY MANAGEMENT SYSTEM"
pmsg1 = msg1.center(120)
print(pmsg1)

# MAIN MENU
print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
print("1. PRODUCT DATA\n2. CUSTOMER DATA\n3. MANUFACTURER DATA\n4. QUIT")
choice = int(input('ENTER YOUR CHOICE (1/2/3/4):- '))

# PRODUCT DATA MENU
if choice == 1:
    print("1. PRODUCT DETAILS\n2. ADD PRODUCT'S DATA\n3. REMOVE PRODUCT'S DATA\n4. UPDATE PRODUCT'S DATA\n5. QUIT")
    prod_choice = int(input('ENTER YOUR CHOICE (1/2/3/4/5):- '))

# PRODUCT DETAILS
    if prod_choice == 1:
        cur.execute("SELECT * FROM PROD_DETAILS;")
        prod_data = cur.fetchall()

        if len(prod_data) > 0:
            for i in prod_data:
                print(i)
            else:
                print("STOCK IS EMPTY")

# ADDING PRODUCTS
        elif prod_choice == 2:
            choice = 'y' or "Y"
            while choice == 'y' or "Y":
                cur.execute('SELECT PROD_NAME FROM PROD_DETAILS')
                stock_avail = cur.fetchall()
                prod_name = input("ENTER PRODUCT'S NAME :- ")

# UPDATING PRODUCTS QUATITY IF PRODUCT ALREADY EXISTS
                if (prod_name,) in stock_avail:
                    print("THIS PRODUCT IS ALREADY AVAILABLE IN STOCK")
                    prod_quantity = int(input("ENTER QUANTITY OF THE PRODUCT :- "))
                    cur.execute("UPDATE PROD_DETAILS SET PROD_QUANTITY = PROD_QUANTITY+{} WHERE PROD_NAME='{}'".format(prod_quantity, prod_name))
                    con.commit()
                    print("PRODUCT UPDATED SUCCESSFULLY")
                    choice = input("\nDO YOU WANT TO UPDATE ANY OTHER PRODUCT (Y/N):- ")

# ADDING PRODUCT DATA IF PRODUCT DOESN'T EXISTS ALREADY
                else:
                    prod_sell_cost = int(input("ENTER PRODUCT'S SELLING COST :- "))
                    prod_quantity = int(input("ENTER QUANTITY OF THE PRODUCT :- "))

                    if prod_quantity > 0:
                        cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST,PROD_QUANTITY) VALUES('{}',{},{})".format(prod_name, prod_sell_cost, prod_quantity))
                        con.commit()
                        print("PRODUCT ADDED SUCCESSFULLY")
                        choice = input("\nDO YOU WANT TO UPDATE ANY OTHER PRODUCT (Y/N):- ")

                    else:
                        print("NOT ALLOWED")
                        break

# REMOVING PRODUCTS
    elif prod_choice == 3:
        cur.execute('SELECT PROD_ID FROM PROD_DETAILS;')
        prod_ids = cur.fetchall()
        choice = 'y' or "Y"
        while choice == 'y' or "Y":
            prod_id = int(input("ENTER ID OF THE PRODUCT YOU WANT TO REMOVE :- "))

            if (prod_id,) in prod_ids:
                cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
                con.commit()
                print("PRODUCT'S DATA REMOVED SUCCESSFULLY")
                choice = input('\nDO YOU WANT TO REMOVE ANY OTHER PRODUCT(Y/N):- ')

            elif (prod_id,) not in prod_ids:
                print("NO PRODUCT EXISTS WITH THIS PRODUCT ID")
                break

            else:
                print("INVALID INPUT")

# UPDATING PRODUCTS
    elif prod_choice == 4:
        print("WHAT YOU WANT TO UPDATE :- ")
        print("1. PRODUCT'S NAME\n2. PRODUCTS'S SELL COST")
        update_prod = int(input("ENTER YOUR CHOICE (1/2/3):- "))
        which_prod = int(input("ENTER PRODUCT'S ID :- "))

# UPDATING PRODUCT NAME
        if update_prod == 1:
            prod_name = input("ENTER PRODUCT'S NAME :- ")
            cur.execute("UPDATE PROD_DETAILS SET PROD_NAME = '{}' WHERE PROD_ID = {}".format(prod_name, which_prod))
            con.commit()
            print("PRODUCTS'S NAME UPDATED SUCCESSFULLY")

# UPDATING PRODUCTS SELLING COST
        elif update_prod == 2:
            prod_update_scost = input("ENTER PRODUCT'S NEW SELLING COST :- ")
            cur.execute("UPDATE PROD_DETAILS SET PROD_SELL_COST = '{}' WHERE PROD_ID = {}".format(prod_update_scost, which_prod))
            con.commit()
            print("PRODUCT'S SELLING UPDATED SUCCESSFULLY")

# QUIT PROGRAM
    elif prod_choice == 5:
        print("EXITING PROGRAM...")
        time.sleep(2)
        quit()

    else:
        print('INVALID INPUT')

# CUSTOMER DATA MENU
elif choice == 2:
    print("1. CUSTORMER DETAILS\n2. ADD CUSTOMER'S DATA\n3. REMOVE CUSTOMER'S DATA\n4. UPDATE CUSTOMER'S DATA\n5. QUIT")
    cust_choice = int(input("ENTER YOUR CHOICE (1/2/3/4/5):- "))

# CUSTOMER DETAILS
    if cust_choice == 1:
        cur.execute("SELECT * FROM CUST_DETAILS;")
        cust_details = cur.fetchll()
        print()

        if len(cust_details) > 0:
            for j in cust_details:
                print(j)

        else:
            print("NO CUSTOMER'S DATA")

# ADDING CUSTOMERS
    elif cust_choice == 2:
        choice = "y" or "Y"
        while choice == "y" or "Y":
            cust_name = input("ENTER CUSTOMER'S NAME :- ")
            cust_mno = int(input("ENTER CUSTOMER'S MOBILE NUMBER :-"))
            cust_adrs = input("ENTER CUSTOMER'S ADDRESS :- ")
            cur.execute("INSERT INTO CUST_DETAILS(CUST_NAME,CUST_MNO,CUST_ADRS) VALUES('{}','{}',{})".format(cust_name, cust_mno, cust_adrs))
            con.commit()
            print("CUSTOMER'S DATA ADDED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO ADD MORE CUSTOMER'S DATA(Y/N):- ")

# REMOVING CUSTOMERS
    elif cust_choice == 3:
        choice = 'y'
        while choice == 'y':
            cur.execute("SELECT * FROM CUST_DETAILS;")
            data = cur.fetchall()

            if len(data) > 0:
                cust_id = int(input("ENTER CUSTOMER'S ID :- "))
                cur.execute('DELETE FROM CUST_DETAILS WHERE CUST_ID={}'.format(cust_id))
                con.cummit()
                print("CUSTOMER'S DATA REMOVED SUCCESSFULLY")
                choice = input("\nDO YOU WANT TO REMOVE ANY OTHER CUSTOMER'S DATA(Y/N) :- ")
            else:
                print(f"NO CUSTOMER'S DATA FOUND WITH THIS CUSTOMER'S ID")
                choice = input("\nDO YOU WANT TO REMOVE ANY OTHER CUSTOMER'S DATA(Y/N): -")

# UPDATING CUSTOMERS MENU
    elif cust_choice == 4:
        print("WHAT YOU WANT TO UPDATE :- ")
        print("1. CUSTOMER'S NAME\n2. CUSTOMER'S ADDRESS\n3. CUSTOMER'S MOBILE NUMBER\n4. QUIT")
        update_cust = int(input("ENTER YOUR CHOICE (1/2/3/4):- "))
        which_cust = int(input("ENTER CUSTOMER'S ID :- "))

# UPDATING CUSTOMER NAME
        if update_cust == 1:
            cust_name = int(input("ENTER CUSTOMER'S NAME :- "))
            cur.execute("UPDATE CUST_DETAILS SET CUST_NAME = '{}' WHERE CUST_ID={}".format(
            cust_name, which_cust))
            con.commit()
            print("CUSTOMER'S NAME UPDATED SUCCESSFULLY")

# UPDATING CUSTOMER ADDRESS
        elif update_cust == 2:
            cust_update_adrs = input("ENTER CUSTOMER'S NEW ADDRESS :- ")
            cur.execute('UPDATE CUST_DETAILS SET ')
            con.commit()
            print("CUSTOMER'S ADDRESS UPDATED SUCCESSFULLY")

# UPDATING CUSTOMER MOBILE NUMBER
        elif update_cust == 3:
            cust_update_mno = int(
            input("ENTER CUSTOMER'S NEW MOBILE NUMBER :- "))
            cur.execute('UPDATE CUST_DETAILS SET ')
            con.commit()
            print("CUSTOMER'S MOBILE NUMBER UPDATED SUCCESSFULLY")

# QUIT PROGRAM (CUSTOMER UPDATE)
        elif update_cust == 4:
            print("EXITING PROGRAM...")
            time.sleep(2)
            quit()

        else:
            print('INVALID INPUT')

# QUIT PROGRAM
    elif cust_choice == 5:
        print("EXITING PROGRAM...")
        time.sleep(2)
        quit()
    
    else:
        print("INVALID INPUT")

# MANUFACTORER DATA MENU
elif choice == 3:
    print("1. MANUFACTURER DETAILS\n2. ADD MANUFACTURER'S DATA\n3. REMOVE MANUFACTURER'S DATA\n4. UPDATE MANUFACTURER'S DATA\n5. QUIT")
    man_choice = int(input('ENTER YOUR CHOICE (1/2/3/4/5):- '))

# MANUFACTURER DETAILS
    if man_choice == 1:
        cur.execute("SELECT * FROM MAN_DETAILS;")
        man_data = cur.fetchall()

        if len(man_data) > 0:
            for i in man_data:
                print(i)
            else:
                print("NO MANUFACTURERS")

# ADDING MANUFACTURER
        elif man_choice == 2:
            choice = 'y' or "Y"
            while choice == 'y' or "Y":
                cur.execute('SELECT MAN_NAME FROM MAN_DETAILS')
                man_avail = cur.fetchall()
                man_name = input("ENTER MANUFACTURER'S NAME :- ")

# UPDATING PRODUCT ID IF MANUFACTURER ALREADY EXISTS
                if (man_name,) in man_avail:
                    print("THIS PRODUCT IS ALREADY AVAILABLE IN STOCK")
                    prod_id = int(input("ENTER PRODUCT ID OF THE PROCDUCT BY MANUFACTURER :- "))
                    cur.execute("UPDATE MAN_DETAILS SET PROD_ID = PROD_ID+{} WHERE MAN_NAME='{}'".format(prod_id, man_name))
                    con.commit()
                    print("PRODUCT ID UPDATED SUCCESSFULLY")
                    choice = input("\nDO YOU WANT TO UPDATE ANY OTHER MANUFACTURER'S DATA (Y/N):- ")

# ADDING MANUFACTURER'S DATA IF MANUFACTURER DOESN'T EXISTS ALREADY
                else:
                    man_name = input("ENTER MANUFACTURER'S NAME :- ")
                    prod_id = int(input("ENTER PRODUCT ID OF THE PRODUCT BY MANUFACTURER :- "))

                    if prod_id > 0:
                        cur.execute("INSERT INTO MAN_DETAILS(MAN_NAME,PROD_ID) VALUES('{}',{})".format(man_name, prod_id))
                        con.commit()
                        print("MANUFACTURER ADDED SUCCESSFULLY")
                        choice = input("\nDO YOU WANT TO UPDATE ANY OTHER MANUFACTURER'S DATA (Y/N):- ")

                    else:
                        print("NOT ALLOWED")
                        break

# REMOVING MANUFACTURER
    elif man_choice == 3:
        cur.execute('SELECT MAN_ID FROM MAN_DETAILS;')
        man_ids = cur.fetchall()
        choice = 'y' or "Y"
        while choice == 'y' or "Y":
            man_id = int(input("ENTER ID OF THE MANUFACTURER YOU WANT TO REMOVE :- "))

            if (man_id,) in man_ids:
                cur.execute("DELETE FROM MAN_DETAILS WHERE MAN_ID = {}".format(man_id))
                con.commit()
                print("MANUFACTURER'S DATA REMOVED SUCCESSFULLY")
                choice = input("\nDO YOU WANT TO REMOVE ANY OTHER MANUFACTURER'S DATA (Y/N):- ")

            elif (man_id,) not in man_ids:
                print("NO MANUFACTURER EXISTS WITH THIS MANUFACTURER'S ID")
                break

            else:
                print("INVALID INPUT")

# UPDATING MANUFACTURER
    elif man_choice == 4:
        print("WHAT YOU WANT TO UPDATE :- ")
        print("1. MANUFACTURER'S NAME\n2. PRODUCT'S BUY COST\n3. QUIT")
        update_man = int(input("ENTER YOUR CHOICE (1/2/3):- "))
        which_man = int(input("ENTER MANUFACTURER'S ID :- "))

# UPDATING MANUFACTURER NAME
        if update_man == 1:
            man_name = input("ENTER MANUFACTURER'S NAME :- ")
            cur.execute("UPDATE MAN_DETAILS SET MAN_NAME = '{}' WHERE MAN_ID = {}".format(man_name, which_man))
            con.commit()
            print("MANUFACTURER'S NAME UPDATED SUCCESSFULLY")

# UPDATING MANUFACTURERS BUYING COST
        elif update_man == 2:
            which_prod = int(input("ENTER PRODUCT ID :- "))
            prod_update_bcost = int(input("ENTER PRODUCT'S NEW BUYING COST :- "))
            cur.execute("UPDATE MAN_DETAILS SET PROD_BUY_COST = {} WHERE PROD_ID = {}".format(prod_update_bcost, which_prod))
            con.commit()
            print("PRODUCT'S BUYING COST UPDATED SUCCESSFULLY")

# QUIT PROGRAM
        elif man_choice == 5:
            print("EXITING PROGRAM...")
            time.sleep(2)
            quit()

        else:
            print('INVALID INPUT')

# QUIT PROGRAM
elif choice == 4:
    print("EXITING PROGRAM...")
    time.sleep(2)
    quit()

else:
    print('INVALID INPUT')