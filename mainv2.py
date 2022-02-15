# CONNECTING DATABASE AND ADDING REQUIREMENTS
from random import choice
from turtle import update


def CONNECT():
    import mysql.connector as mcon
    import time

    con = mcon.connect(host="localhost", user="root", passwd="#Vinu@5142.", database="GROCERY_MANAGEMENT_SYS", charset = "utf8")
    cur = con.cursor()

    msg1 = "GROCERY MANAGEMENT SYSTEM\n\n"
    pmsg1 = msg1.center(120)
    print(pmsg1)

# MAIN MENU
def MAIN_MENU():
    print("MAIN MENU")
    print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
    print("1. PRODUCT DATA\n2. CUSTOMER DATA\n3. MANUFACTURER DATA\n4. QUIT")
    choice = int(input('ENTER YOUR CHOICE (1/2/3/4):- '))
    if choice == 1:
        PRODUCT_DATA_MENU()


# PRODUCT DATA MENU
def PRODUCT_DATA_MENU():
    print("PRODUCT DATA MENU")
    print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
    print("1. PRODUCT DETAILS\n2. ADD PRODUCT DATA\n3. REMOVE PRODUCT DATA\n4. UPDATE PRODUCT DATA\n5. MAIN MENU\n6. QUIT")
    prod_choice = int(input('ENTER YOUR CHOICE (1/2/3/4/5):- '))
    if prod_choice == 1:
        PRODUCT_DETAILS()
    elif prod_choice == 2:
        ADD_PRODUCT_DATA()
    elif prod_choice == 3:
        REMOVE_PRODUCT_DATA()
    elif prod_choice == 4:
        UPDATE_PRODUCT_DATA_MENU()
    elif prod_choice == 5:
        print("GOING BACK TO THE MAIN MENU....")
        MAIN_MENU()
    elif prod_choice == 6:
        QUIT()
    else :
        print("PLEASE CHOOSE AN APPROPRAITE OPTION\nGOING BACK TO PRODUCT DATA MENU....")
        PRODUCT_DATA_MENU


# PRODUCT DETAILS
def PRODUCT_DETAILS():
    cur.execute("SELECT * FROM PROD_DETAILS;")
    prod_data = cur.fetchall()
    if len(prod_data) > 0:
        for i in prod_data:
            print(i)
        print("GOING BACK TO THE PRODUCT DATA MENU....")
        PRODUCT_DATA_MENU()
    else:
        print("STOCK IS EMPTY")
        print("GOING BACK TO THE PRODUCT DATA MENU....")
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
            prod_quantity = int(input("ENTER QUANTITY OF THE PRODUCT :- "))
            cur.execute("UPDATE PROD_DETAILS SET PROD_QUANTITY = PROD_QUANTITY+{} WHERE PROD_NAME='{}'".format(prod_quantity, prod_name))
            con.commit()
            print("PRODUCT UPDATED SUCCESSFULLY")
            choice = input("\nDO YOU WANT TO UPDATE ANY OTHER PRODUCT (Y/N):- ")
            choice.lower()
        else:
            prod_sell_cost = int(input("ENTER PRODUCT SELLING COST :- "))
            prod_quantity = int(input("ENTER QUANTITY OF THE PRODUCT :- "))
            if prod_quantity > 0:
                cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST,PROD_QUANTITY) VALUES('{}',{},{})".format(prod_name, prod_sell_cost, prod_quantity))
                con.commit()
                print("PRODUCT ADDED SUCCESSFULLY")
                choice = input("\nDO YOU WANT TO UPDATE ANY OTHER PRODUCT (Y/N):- ")
                choice.lower()
            else:
                print("NOT ALLOWED")
                print("GOING BACK TO THE PRODUCT DATA MENU....")
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
        elif (prod_id,) not in prod_ids:
            print("NO PRODUCT EXISTS WITH THIS PRODUCT ID")
            print("GOING BACK TO PRODUCT DATA MENU....")
            PRODUCT_DATA_MENU
        else:
            print("INVALID INPUT")
            print("GOING BACK TO THE PRODUCT DATA MENU....")
            PRODUCT_DATA_MENU()


# UPDATE PRODUCT DATA MENU
def UPDATE_PRODUCT_DATA_MENU():
    print("UPDATE PRODUCT DATA MENU")
    print("WHAT YOU WANT TO UPDATE :- ")
    print("1. PRODUCT NAME\n2. PRODUCT SELLING COST\n3. PRODUCT DATA MENU\n4. QUIT")
    update_prod = int(input("ENTER YOUR CHOICE (1/2/3):- "))
    which_prod = int(input("ENTER PRODUCT'S ID :- "))
    if update_prod == 1:
        UPDATE_PRODUCT_NAME
    elif update_prod == 2:
        UPDATE_PRODUCT_SELLING_COST
    elif update_prod == 3:
        print("GOING BACK TO THE PRODUCT DATA MENU....")
        PRODUCT_DATA_MENU()
    elif update_prod == 4:
        QUIT()
    else :
        print("PLEASE CHOOSE AN APPROPRAITE OPTION\nGOING BACK TO UPDATE PRODUCT DATA MENU....")
        UPDATE_PRODUCT_DATA_MENU


# UPDATE PRODUCT NAME
def UPDATE_PRODUCT_NAME():
    prod_name = input("ENTER PRODUCT NAME :- ")
    cur.execute("UPDATE PROD_DETAILS SET PROD_NAME = '{}' WHERE PROD_ID = {}".format(prod_name, which_prod))
    con.commit()
    print("PRODUCT NAME UPDATED SUCCESSFULLY")                
    print("GOING BACK TO THE UPDATE PRODUCT DATA MENU....")
    UPDATE_PRODUCT_DATA_MENU()


# UPDATE PRODUCT SELLING COST
def UPDATE_PRODUCT_SELLING_COST():
    prod_update_scost = input("ENTER PRODUCT NEW SELLING COST :- ")
    cur.execute("UPDATE PROD_DETAILS SET PROD_SELL_COST = '{}' WHERE PROD_ID = {}".format(prod_update_scost, which_prod))
    con.commit()
    print("PRODUCT SELLING COST UPDATED SUCCESSFULLY")
    print("GOING BACK TO THE UPDATE PRODUCT DATA MENU....")
    UPDATE_PRODUCT_DATA_MENU()






CONNECT()
MAIN_MENU()