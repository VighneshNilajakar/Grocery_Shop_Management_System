# IMPORTING REQUIRED MODULES
from random import choice
import mysql.connector as mcon
import time

# CONNECTING DATABASE AND ADDING REQUIREMENTS
def CONNECT():
    global con
    con = mcon.connect(host="localhost", user="root", passwd="", database="GROCERY_MANAGEMENT_SYS", charset = "utf8")
    global cur
    cur = con.cursor()
    msg1 = "\nGROCERY MANAGEMENT SYSTEM\n"
    pmsg1 = msg1.center(120)
    print(pmsg1)

# MAIN MENU
def MAIN_MENU():
    print("\nMAIN MENU\n")
    print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
    print("1. PRODUCT DATA\n2. CUSTOMER DATA\n3. MANUFACTURER DATA\n4. QUIT\n")
    choice = int(input('ENTER YOUR CHOICE (1/2/3/4):- '))
    if choice == 1:
        PRODUCT_DATA_MENU()
    elif choice == 2:
        CUSTOMER_DATA_MENU()
    elif choice == 3:
        MANUFACTURER_DATA_MENU()
    elif choice == 4:
        QUIT()
    else:
        print("PLEASE CHOOSE AN APPROPRIATE OPTION\nGOING BACK TO MAIN MENU")
        MAIN_MENU()

# PRODUCT DATA MENU
def PRODUCT_DATA_MENU():
    print("\nPRODUCT DATA MENU\n")
    print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
    print("1. PRODUCT DETAILS\n2. ADD PRODUCT DATA\n3. REMOVE PRODUCT DATA\n4. UPDATE PRODUCT DATA\n5. MAIN MENU\n6. QUIT\n")
    prod_choice = int(input('ENTER YOUR CHOICE (1/2/3/4/5/6):- '))
    if prod_choice == 1:
        PRODUCT_DETAILS()
    elif prod_choice == 2:
        ADD_PRODUCT_DATA()
    elif prod_choice == 3:
        REMOVE_PRODUCT_DATA()
    elif prod_choice == 4:
        UPDATE_PRODUCT_DATA_MENU()
    elif prod_choice == 5:
        print("GOING BACK TO THE MAIN MENU")
        MAIN_MENU()
    elif prod_choice == 6:
        QUIT()
    else :
        print("PLEASE CHOOSE AN APPROPRAITE OPTION\nGOING BACK TO PRODUCT DATA MENU")
        PRODUCT_DATA_MENU()

# PRODUCT DETAILS
def PRODUCT_DETAILS():
    cur.execute("SELECT * FROM PROD_DETAILS;")
    prod_data = cur.fetchall()
    if len(prod_data) > 0:
        for i in prod_data:
            print(i)
        ch = print("DO YOU WANT TO GO BACK TO THE CUSTOMER DATA MENU (Y/N):-")
        ch.lower()
        if ch == 'y' :
            PRODUCT_DATA_MENU()
        else :
            print(" ")
    else:
        print("STOCK IS EMPTY\nGOING BACK TO THE PRODUCT DATA MENU")
        PRODUCT_DATA_MENU()

# ADD PRODUCT DATA
def ADD_PRODUCT_DATA():
    choice = 'y'
    while choice == 'y':
        cur.execute('SELECT PROD_NAME FROM PROD_DETAILS')
        stock_avail = cur.fetchall()
        prod_name = input("ENTER PRODUCT NAME :- ")
        if (prod_name,) in stock_avail:
            print("THIS PRODUCT IS ALREADY AVAILABLE IN STOCK")
            prod_quantity = int(input("UPDATE QUANTITY OF THE PRODUCT :- "))
            cur.execute("UPDATE PROD_DETAILS SET PROD_QUANTITY = PROD_QUANTITY+{} WHERE PROD_NAME='{}'".format(prod_quantity, prod_name))
            con.commit()
            print("PRODUCT UPDATED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO ADD ANY OTHER PRODUCT (Y/N):- ")
            choice.lower()
            break
        else:
            prod_sell_cost = int(input("ENTER PRODUCT SELLING COST :- "))
            prod_quantity = int(input("ENTER QUANTITY OF THE PRODUCT :- "))
            if prod_quantity > 0:
                cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST,PROD_QUANTITY) VALUES('{}',{},{})".format(prod_name, prod_sell_cost, prod_quantity))
                con.commit()
                print("PRODUCT ADDED SUCCESSFULLY")
                choice = input("\nDO YOU WANT TO ADD ANY OTHER PRODUCT (Y/N):- ")
                choice.lower()
                break
            else:
                print("PLEASE CHOOSE AN APPROPRIATE OPTION/nGOING BACK TO THE PRODUCT DATA MENU")
                PRODUCT_DATA_MENU()

# REMOVE PRODUCT DATA
def REMOVE_PRODUCT_DATA():
    cur.execute('SELECT PROD_ID FROM PROD_DETAILS;')
    prod_ids = cur.fetchall()
    choice = 'y'
    while choice == 'y':
        prod_id = int(input("ENTER ID OF THE PRODUCT YOU WANT TO REMOVE :- "))
        if (prod_id,) in prod_ids:
            cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
            con.commit()
            print("PRODUCT DATA REMOVED SUCCESSFULLY")
            choice = input('\nDO YOU WANT TO REMOVE ANY OTHER PRODUCT(Y/N):- ')
            choice.lower()
            break
        elif (prod_id,) not in prod_ids:
            print("NO PRODUCT EXISTS WITH THIS PRODUCT ID\nGOING BACK TO THE PRODUCT DATA MENU")
            PRODUCT_DATA_MENU()
        else:
            print("PLEASE CHOOSE AN APPROPRIATE OPTION\nGOING BACK TO THE PRODUCT DATA MENU")
            PRODUCT_DATA_MENU()

# UPDATE PRODUCT DATA MENU
def UPDATE_PRODUCT_DATA_MENU():
    print("\nUPDATE PRODUCT DATA MENU\n")
    print("WHAT YOU WANT TO UPDATE :- ")
    print("1. PRODUCT NAME\n2. PRODUCT SELLING COST\n3. PRODUCT DATA MENU\n4. QUIT")
    update_prod = int(input("ENTER YOUR CHOICE (1/2/3/4):- "))
    global which_prod
    which_prod = int(input("ENTER PRODUCT ID :- "))
    if update_prod == 1:
        UPDATE_PRODUCT_NAME()
    elif update_prod == 2:
        UPDATE_PRODUCT_SELLING_COST()
    elif update_prod == 3:
        print("GOING BACK TO THE PRODUCT DATA MENU")
        PRODUCT_DATA_MENU()
    elif update_prod == 4:
        QUIT()
    else :
        print("PLEASE CHOOSE AN APPROPRAITE OPTION\nGOING BACK TO UPDATE PRODUCT DATA MENU")
        UPDATE_PRODUCT_DATA_MENU()

# UPDATE PRODUCT NAME
def UPDATE_PRODUCT_NAME():
    prod_name = input("ENTER PRODUCT NAME :- ")
    cur.execute("UPDATE PROD_DETAILS SET PROD_NAME = '{}' WHERE PROD_ID = {}".format(prod_name, which_prod))
    con.commit()
    print("PRODUCT NAME UPDATED SUCCESSFULLY")                
    print("GOING BACK TO THE UPDATE PRODUCT DATA MENU")
    UPDATE_PRODUCT_DATA_MENU()

# UPDATE PRODUCT SELLING COST
def UPDATE_PRODUCT_SELLING_COST():
    prod_update_scost = input("ENTER PRODUCT NEW SELLING COST :- ")
    cur.execute("UPDATE PROD_DETAILS SET PROD_SELL_COST = '{}' WHERE PROD_ID = {}".format(prod_update_scost, which_prod))
    con.commit()
    print("PRODUCT SELLING COST UPDATED SUCCESSFULLY")
    print("GOING BACK TO THE UPDATE PRODUCT DATA MENU....")
    UPDATE_PRODUCT_DATA_MENU()

# CUSTOMER DATA MENU
def CUSTOMER_DATA_MENU():
    print("\nCUSTOMER DATA MENU\n")
    print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
    print("1. CUSTORMER DETAILS\n2. ADD CUSTOMER DATA\n3. REMOVE CUSTOMER DATA\n4. UPDATE CUSTOMER DATA\n5. MAIN MENU\n6. QUIT\n")
    cust_choice = int(input("ENTER YOUR CHOICE (1/2/3/4/5/6):- "))
    if cust_choice == 1:
        CUSTOMER_DETAILS()
    elif cust_choice == 2:
        ADD_CUSTOMER_DATA()
    elif cust_choice == 3:
        REMOVE_CUSTOMER_DATA()
    elif cust_choice == 4:
        UPDATE_CUSTOMER_DATA_MENU()
    elif cust_choice == 5:
        MAIN_MENU()
    elif cust_choice == 6:
        QUIT()
    else :
        print("PLEASE CHOOSE AN APPROPRIATE OPTION\nGOING BACK TO CUSTOMER DATA MENU")
        CUSTOMER_DATA_MENU()

# CUSTOMER DETAILS
def CUSTOMER_DETAILS():
    while choice == "y":
        cur.execute("SELECT * FROM CUST_DETAILS;")
        cust_details = cur.fetchll()
        print()
        if len(cust_details) > 0:
            for j in cust_details:
                print(j)
                choice = print("DO YOU WANT TO GO BACK TO THE CUSTOMER DATA MENU (Y/N):-")
                choice.lower()
                break
        else:
            print("NO CUSTOMER DATA\nGOING BACK TO THE CUSTOMER DATA MENU....")
            CUSTOMER_DATA_MENU()

# ADD CUSTOMER DATA
def ADD_CUSTOMER_DATA():
        cust_name = input("ENTER CUSTOMER NAME :- ")
        cust_mno = int(input("ENTER CUSTOMER MOBILE NUMBER :-"))
        cust_adrs = input("ENTER CUSTOMER ADDRESS :- ")
        choice = "y"
        while choice == "y":
            cur.execute("INSERT INTO CUST_DETAILS(CUST_NAME,CUST_MNO,CUST_ADRS) VALUES('{}','{}',{})".format(cust_name, cust_mno, cust_adrs))
            con.commit()
            print("CUSTOMER DATA ADDED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO ADD MORE CUSTOMER DATA(Y/N):- ")
            choice.lower()
            break
        if choice == 'y':
            ADD_CUSTOMER_DATA()
        else:
            print("GOING BACK TO THE CUSTOMER DATA MENU")
            CUSTOMER_DATA_MENU()

# REMOVE CUSTOMER DATA
def REMOVE_CUSTOMER_DATA():
    choice = 'y'
    while choice == 'y':
        cur.execute("SELECT * FROM CUST_DETAILS;")
        data = cur.fetchall()
        if len(data) > 0:
            cust_id = int(input("ENTER CUSTOMER ID :- "))
            cur.execute('DELETE FROM CUST_DETAILS WHERE CUST_ID={}'.format(cust_id))
            con.cummit()
            print("CUSTOMER DATA REMOVED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO REMOVE ANY OTHER CUSTOMER DATA(Y/N) :- ")
            choice.lower()
            break
        else:    
            print("GOING BACK TO THE CUSTOMER DATA MENU")
            CUSTOMER_DATA_MENU()

# UPDATE CUSTOMER DATA MENU
def UPDATE_CUSTOMER_DATA_MENU():
    print("\nUPDATE CUSTOMER DATA MENU\n")
    print("WHAT YOU WANT TO UPDATE :- ")
    print("1. CUSTOMER NAME\n2. CUSTOMER ADDRESS\n3. CUSTOMER MOBILE NUMBER\n4. CUSTOMER DATA MENU\n5. QUIT")
    update_cust = int(input("ENTER YOUR CHOICE (1/2/3/4/5):- "))
    global which_cust
    which_cust = int(input("ENTER CUSTOMER ID :- "))
    if update_cust == 1:
        UPDATE_CUSTOMER_NAME()
    elif update_cust == 2:
        UPDATE_CUSTOMER_ADDRESS()
    elif update_cust == 3:
        UPDATE_CUSTOMER_MOBILE_NUMBER()
    elif update_cust == 4:
        CUSTOMER_DATA_MENU()
    elif update_cust == 5:
        QUIT()
    else:
        print("PLEASE CHOOSE AN APPROPRIATE OPTION\nGOING BACK TO UPDATE CUSTOMER DATA MENU")
        UPDATE_CUSTOMER_DATA_MENU()

# UPDATE CUSTOMER NAME
def UPDATE_CUSTOMER_NAME():
    cust_name = int(input("ENTER CUSTOMER NAME :- "))
    cur.execute("UPDATE CUST_DETAILS SET CUST_NAME = '{}' WHERE CUST_ID={}".format(cust_name, which_cust))
    con.commit()
    print("CUSTOMER NAME UPDATED SUCCESSFULLY\nGOING BACK TO UPDATE CUSTOMER DATA MENU")
    UPDATE_CUSTOMER_DATA_MENU()

# UPDATE CUSTOMER ADDRESS
def UPDATE_CUSTOMER_ADDRESS():
    cust_update_adrs = input("ENTER CUSTOMER NEW ADDRESS :- ")
    cur.execute("UPDATE CUST_DETAILS SET CUST_ADRS='{}' WHERE CUST_ID={}".format(cust_update_adrs,which_cust))
    con.commit()
    print("CUSTOMER ADDRESS UPDATED SUCCESSFULLY\nGOING BACK TO UPDATE CUSTOMER DATA MENU")
    UPDATE_CUSTOMER_DATA_MENU()

# UPDATE CUSTOMER MOBILE NUMBER
def UPDATE_CUSTOMER_MOBILE_NUMBER():
    cust_update_mno = int(input("ENTER CUSTOMER NEW MOBILE NUMBER :- "))
    cur.execute('UPDATE CUST_DETAILS SET CUST_MNO={} WHERE CUST_ID={}'.format(cust_update_mno,which_cust))
    con.commit()
    print("CUSTOMER MOBILE NUMBER UPDATED SUCCESSFULLY\nGOING BACK TO UPDATE CUSTOMER DATA MENU")
    UPDATE_CUSTOMER_DATA_MENU()

# MANUFACTORER DATA MENU
def MANUFACTURER_DATA_MENU():
    print("\nMANUFACTURER DATA MENU\n")
    print("1. MANUFACTURER DETAILS\n2. ADD MANUFACTURER DATA\n3. REMOVE MANUFACTURER DATA\n4. UPDATE MANUFACTURER DATA\n5. MAIN MENU\n6. QUIT")
    man_choice = int(input('ENTER YOUR CHOICE (1/2/3/4/5/6):- '))
    if man_choice == 1 :
        MANUFACTURER_DETAILS()
    elif man_choice == 2 :
        ADD_MANUFACTURER_DATA()
    elif man_choice == 3 :
        REMOVE_MANUFACTURER_DATA()
    elif man_choice == 4 :
        UPDATE_MANUFACTURER_DATA_MENU()
    elif man_choice == 5:
        MAIN_MENU()
    elif man_choice == 6:
        QUIT()
    else:
        print("PLEASE CHOOSE AN APPRORIATE OPTION\nGOING BACK TO MANUFACTURER DATA MENU")
        MANUFACTURER_DATA_MENU()

# MANUFACTURER DETAILS
def MANUFACTURER_DETAILS():
    choice = "y"
    while choice == "y":
        cur.execute("SELECT * FROM MAN_DETAILS;")
        man_data = cur.fetchall()
        if len(man_data) > 0:
            for i in man_data:
                print(i)
            choice = print("DO YOU WANT TO GO BACK TO THE MANUFACTURER DATA MENU (Y/N):-")
            choice.lower()
            break
        else:
            print("NO MANUFACTURE DATA\nGOING BACK TO THE MANUFACTURER DATA MENU")
            MANUFACTURER_DATA_MENU()

# ADD MANUFACTURER DATA
def ADD_MANUFACTURER_DATA():
    choice = 'y'
    while choice == 'y':
        cur.execute('SELECT MAN_NAME FROM MAN_DETAILS')
        man_avail = cur.fetchall()
        man_name = input("ENTER MANUFACTURER NAME :- ")
        if (man_name,) in man_avail:
            print("THIS MANUFACTURER ALREADY EXISTS IN LIST")
            prod_id = int(input("ENTER PRODUCT ID OF THE PROCDUCT BY MANUFACTURER :- "))
            cur.execute("UPDATE MAN_DETAILS SET PROD_ID = PROD_ID+{} WHERE MAN_NAME='{}'".format(prod_id, man_name))
            con.commit()
            print("PRODUCT ID UPDATED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO UPDATE ANY OTHER MANUFACTURER DATA (Y/N):- ")
            choice.lower()
            break
        else:
            man_name = input("ENTER MANUFACTURER NAME :- ")
            prod_id = int(input("ENTER PRODUCT ID OF THE PRODUCT BY MANUFACTURER :- "))
            if prod_id > 0:
                cur.execute("INSERT INTO MAN_DETAILS(MAN_NAME,PROD_ID) VALUES('{}',{})".format(man_name, prod_id))
                con.commit()
                print("MANUFACTURER ADDED SUCCESSFULLY")
                choice = input("\nDO YOU WANT TO UPDATE ANY OTHER MANUFACTURER DATA (Y/N):- ")
                choice.lower()
                break
            else:
                print("PLEASE CHOOSE AN APPRORIATE OPTION\nGOING BACK TO MANUFACTURER DATA MENU")
                MANUFACTURER_DATA_MENU()

# REMOVE MANUFACTURER DATA
def REMOVE_MANUFACTURER_DATA():
    cur.execute('SELECT MAN_ID FROM MAN_DETAILS;')
    man_ids = cur.fetchall()
    choice = 'y'
    while choice == 'y' :
        man_id = int(input("ENTER ID OF THE MANUFACTURER YOU WANT TO REMOVE :- "))
        if (man_id,) in man_ids:
            cur.execute("DELETE FROM MAN_DETAILS WHERE MAN_ID = {}".format(man_id))
            con.commit()
            print("MANUFACTURER DATA REMOVED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO REMOVE ANY OTHER MANUFACTURER DATA (Y/N):- ")
            choice.lower()
            break
        else :
            print("NO MANUFACTURER EXISTS WITH THIS MANUFACTURER ID\nGOING BACK TO MANUFACTURER DATA MENU")
            MANUFACTURER_DATA_MENU()

# UPDATE MANUFACTURER DATA MENU
def UPDATE_MANUFACTURER_DATA_MENU():
    print("\nUPDATE MANUFACTURER DATA MENU\n")
    print("WHAT YOU WANT TO UPDATE :- ")
    print("1. MANUFACTURER NAME\n2. PRODUCT BUY COST\n3. MANUFACTURER DATA MENU\n4. QUIT")
    update_man = int(input("ENTER YOUR CHOICE (1/2/3/4):- "))
    global which_man
    which_man = int(input("ENTER MANUFACTURER ID :- "))
    if update_man == 1:
        UPDATE_MANUFACTURER_NAME()
    elif update_man == 2:
        UPDATE_PRODUCT_BUY_COST()
    elif update_man == 3:
        MANUFACTURER_DATA_MENU()
    else :
        print("PLEASE CHOOSE AN APPROPRIATE OPTION\nGOING BACK TO UPDATE MANUFACTURER DATA MENU")
        UPDATE_MANUFACTURER_DATA_MENU()

# UPDATE MANUFACTURER NAME
def UPDATE_MANUFACTURER_NAME():
    man_name = input("ENTER MANUFACTURER NAME :- ")
    cur.execute("UPDATE MAN_DETAILS SET MAN_NAME = '{}' WHERE MAN_ID = {}".format(man_name, which_man))
    con.commit()
    print("MANUFACTURER NAME UPDATED SUCCESSFULLY\nGOING BACK TO UPDATE MANUFACTURER DATA MENU")
    UPDATE_MANUFACTURER_DATA_MENU()

# UPDATE PRODUCT BUY COST
def UPDATE_PRODUCT_BUY_COST():
    which_prod = int(input("ENTER PRODUCT ID :- "))
    prod_update_bcost = int(input("ENTER NEW BUYING COST OF PRODUCT :- "))
    cur.execute("UPDATE MAN_DETAILS SET PROD_BUY_COST = {} WHERE PROD_ID = {}".format(prod_update_bcost, which_prod))
    con.commit()
    print("PRODUCT BUYING COST UPDATED SUCCESSFULLY\nGOING BACK TO UPDATE MANUFACTURER DATA MENU")
    UPDATE_MANUFACTURER_DATA_MENU()

# QUIT PROGRAM
def QUIT():
    print("EXITING PROGRAM")
    time.sleep(2)
    quit()

# EXECUTION
CONNECT()
MAIN_MENU()