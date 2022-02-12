import mysql.connector as mcon
con = mcon.connect(host = "localhost", user = "root", passwd = "#Vinu@5142.", database = "GROCERY_MANAGEMENT_SYS")
cur = con.cursor()
msg1 = "GROCERY MANAGEMENT SYSTEM"
pmsg1 = msg1.center(120)
print(pmsg1)
print("CHOOSE FROM THE FOLLOWING OPTIONS :-")
print("1. PRODUCT DETAILS\n2. CUSTOMER DETAILS\n3. MANUFACTURER DETAILS\n4. QUIT")
try:
    choice=int(input('ENTER YOUR CHOICE (1/2/3/4):- '))
    if choice==1:
        print("1. PRODUCT DETAILS\n2. ADD PRODUCT'S DATA\n3. REMOVE PRODUCT'S DATA\n4. UPDATE PRODUCT'S DATA")
        try:
            prod_choice=int(input('ENTER YOUR CHOICE (1/2/3/4):- '))
            if prod_choice==1:
                cur.execute("SELECT * FROM PROD_DETAILS;")
                prod_data=cur.fetchall()
                for i in prod_data:
                    print(i)
            elif prod_choice==2:
                prod_name=input("ENTER PRODUCT'S NAME :- ")
                prod_sell_cost=int(input("ENTER PRODUCT'S SELLING COST :- "))
                cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST) VALUES('{}',{})".format(prod_name,prod_sell_cost))
                con.commit()
                print("PRODUCT'S DATA ADDED SUCCESSFULLY")
            elif prod_choice==3:
                prod_id=int(input("ENTER ID OF THE PRODUCT YOU WANT TO REMOVE :- "))
                cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
                con.commit()
                print("PRODUCT'S DATA REMOVED SUCCESSFULLY")
            #elif prod_choice==4: Product Modification
             #   prod_id=int(input("ENTER ID OF THE PRODUCT YOU WANT TO REMOVE :- "))
              #  cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
               # con.commit()
                #print("PRODUCT REMOVED SUCCESSFULLY")
            else:
                print()
        except:
            print("INVALID INPUT")

    elif choice==2:
        print("1. CUSTORMER DETAILS\n2. ADD CUSTOMER'S DATA\n3. REMOVE CUSTOMER'S DATA\n4. UPDATE CUSTOMER'S DATA")
        try:
            cust_choice=int(input("ENTER YOUR CHOICE (1/2):- "))
            if cust_choice==1:
                cur.execute("SELECT * FROM CUST_DETAILS;")
                cust_details=cur.fetchll()
                for j in cust_details:
                    print(j)
            elif cust_choice==2:
                cust_name=input("ENTER CUSTOMER'S NAME :- ")
                cust_mno=int(input("ENTER CUSTOMER'S MOBILE NUMBER :-"))
                cust_adrs=input("ENTER CUSTOMER'S ADDRESS :- ")
                cur.execute("INSERT INTO CUST_DETAILS(CUST_NAME,CUST_MNO,CUST_ADRS) VALUES('{}','{}',{})".format(cust_name,cust_mno,cust_adrs))
                con.commit()
                print("CUSTOMER'S DATA ADDED SUCCESSFULLY")
  
            elif cust_choice==3:
                cust_id=int(input("ENTER CUSTOMER'S ID :- "))
                cur.execute('DELETE FROM CUST_DETAILS WHERE CUST_ID={}'.format(cust_id))
                con.cummit()
                print("CUSTOMER'S DATA REMOVED SUCCESSFULLY")

            elif cust_choice==4:
                print("WHAT YOU WANT TO UPDATE :- ")
                print("1. CUSTOMER'S NAME\n2. CUSTOMER'S ADDRESS\n3. CUSTOMER'S MOBILE NUMBER")
                update_cust=int(input("ENTER YOUR CHOICE (1/2/3):- "))
                which_cust=int(input("ENTER CUSTOMER'S ID :- "))
                if update_cust==1:
                    cust_name=int(input("ENTER CUSTOMER'S NAME :- "))
                    cur.execute("UPDATE CUST_DETAILS SET CUST_NAME = '{}' WHERE CUST_ID={}".format(cust_name,which_cust))
                    con.commit()
                    print("CUSTOMER'S NAME UPDATED SUCCESSFULLY")

                elif update_cust==2:
                    cust_update_adrs=input("ENTER CUSTOMER'S NEW ADDRESS :- ")
                    cur.execute('UPDATE CUST_DETAILS SET ')
                    con.commit()
                    print("CUSTOMER'S ADDRESS UPDATED SUCCESSFULLY")


                elif update_cust==3:
                    cust_update_mno=int(input("ENTER CUSTOMER'S NEW MOBILE NUMBER :- "))
                    cur.execute('UPDATE CUST_DETAILS SET ')
                    con.commit()
                    print("CUSTOMER'S MOBILE NUMBER UPDATED SUCCESSFULLY")
            
            else:
                print('INVALID INPUT')
        except:
            print('INVALID INPUT')
except:
    print('INVALID INPUT')