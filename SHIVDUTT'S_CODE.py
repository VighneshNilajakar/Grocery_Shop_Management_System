#<GROCERY SHOP MANAGEMENT SYSTEM>
#<ESTABLISHING CONNECTION WITH MYSQL>
import mysql.connector as mcon
con = mcon.connect(host = "localhost", user = "root", passwd = "password", charset = "utf8",auth_plugin='mysql_native_password')
if con.is_connected() == True:
    print("CONNECTION SUCCESSFULL")
else:
    print("ERROR CONNECTING MYSQL")
cur = con.cursor() #MAKING CURSOR OBJECT
print("INITIALIZING...")

#<CREATING DATABASE>
'''cur.execute("CREATE DATABASE IF NOT EXISTS GROCERY_MANAGEMENT_SYS;")''' #--> COMMENT IT AFTER THE FIRST RUN OF THE PROGRAM
cur.execute("USE GROCERY_MANAGEMENT_SYS;")
print("CREATED REQUIRED DATABASES")

#<CREATING REQUIRED TABLES>
'''cur.execute("CREATE TABLE IF NOT EXISTS PROD_DETAILS (PROD_ID INT(3) AUTO_INCREMENT PRIMARY KEY, PROD_NAME VARCHAR(200) NOT NULL UNIQUE, PROD_SELL_COST INT(10) NOT NULL,PROD_QUANTITY INT NOT NULL;")
cur.execute("ALTER TABLE PROD_DETAILS AUTO_INCREMENT=100") #setting prod_id to start from 100 not from 1

cur.execute("CREATE TABLE IF NOT EXISTS PROD_BUY_COST (PROD_BUY_COST INT(20) NOT NULL);")

cur.execute("CREATE TABLE IF NOT EXISTS CUST_DETAILS (CUST_ID INT(3) AUTO_INCREMENT PRIMARY KEY, CUST_NAME VARCHAR(30) NOT NULL, CUST_ADRS VARCHAR (200), CUST_MNO INT NOT NULL);")
cur.execute("ALTER TABLE CUST_DETAILS AUTO_INCREMENT=100;") #setting prod_id to start from 100 not from 1
print("CREATED REQUIRED TABLES")''' #--> COMMENT IT AFTER THE FIRST RUN OF THE PROGRAM


#<MY CONTRIBUTION>
print("\n-------CHOOSE FROM THE FOLLOWING-------")
print("\n<1>PRODUCT DETAILs\n<2>CUSTOMER DETAILS")

#<SELECTING WHICH FIELD TO EXPLORE>

try:
    choice=int(input('Enter Your choice: '))
    #SELECTING PRODUCT FIELD
    if choice==1: 
        print("\nWHAT ACTION YOU WANT TO PERFORM\n<1>PRODUCT DETAILS\n<2>ADD PRODUCT\n<3>REMOVE PRODUCT\n")
        try:
            prod_choice=int(input('Enter your choice: '))
            print()
            if prod_choice==1: #PRODUCT DETAILS
                cur.execute("SELECT * FROM PROD_DETAILS;")
                prod_data=cur.fetchall()
                if len(prod_data)>0:
                    for i in prod_data:
                        print(i)
                else:
                    print('Stock is empty')

            elif prod_choice==2: #ADDING NEW PRODUCT
                choice='y'
                while choice=='y':
                    cur.execute('SELECT PROD_NAME FROM PROD_DETAILS')
                    already_in_stock=cur.fetchall() 
                    prod_name=input('Enter product name: ')
                    if (prod_name,) in already_in_stock:
                        print('This product is already in the stock')
                        prod_quantity=int(input('Enter quantity of product: '))
                        cur.execute("UPDATE PROD_DETAILS SET PROD_QUANTITY = PROD_QUANTITY+{} WHERE PROD_NAME='{}'".format(prod_quantity,prod_name))
                        con.commit()
                        print('Product updated successfully')
                        choice=input('\nDo you want to enter one more product(y or n):')
                    else:
                        prod_sell_cost=int(input('Enter product selling price: '))
                        prod_quantity=int(input('Enter quantity of product: '))
                        if prod_quantity>0:
                            cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST,PROD_QUANTITY) VALUES('{}',{},{})".format(prod_name,prod_sell_cost,prod_quantity))
                            con.commit()
                            print('Product added successfully')
                            choice=input('\nDo you want to enter one more product(y or n):') 
                        else:
                            print('Not allowed')
                            break

                     

            elif prod_choice==3: #REMOVING PRODUCT
                cur.execute('SELECT PROD_ID FROM PROD_DETAILS;')
                prod_ids=cur.fetchall()
                choice='y'
                while choice=='y':
                    prod_id=int(input('Enter the product id you want to remove: '))
                    if (prod_id,) in prod_ids:
                        cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
                        con.commit()
                        print('product removed successfully')
                        choice=input('\nDo you want to remove one more product(y or n):')
                    elif (prod_id,) not in prod_ids: #IF PRODUCT NOT IN THE STOCK
                        print(f'No product with that product id {prod_id}')
                        break
            else:
                print('Invalid input')
        except:
            print('Try again something went wrong')

#<CUSTOMER BLOCK>

    elif choice==2:
        print('\nWHAT ACTION YOU WANT TO PERFORM')
        print("<1>CUSTORMER DETAILS\n<2>ADD CUSTOMER\n<3>REMOVE CUSTOMER\n<4>UPDATE CUSTOMER\n")
        try:
            cust_choice=int(input('Enter your choice: '))
            if cust_choice==1: #CUSTOMER DETAILS
                cur.execute("SELECT * FROM CUST_DETAILS;")
                cust_details=cur.fetchall()
                print()
                if len(cust_details)>0:
                    for j in cust_details:
                        print(j)
                else:
                    print('No customers')

            elif cust_choice==2: #ADDING NEW CUSTOMER
                choice='y'
                while choice=='y':
                    cust_name=input('\nEnter customer name: ')
                    cust_adrs=input('Enter customer address: ')
                    cust_mno=int(input('Enter customer mobile number: '))
                    cur.execute("INSERT INTO CUST_DETAILS(CUST_NAME,CUST_ADRS,CUST_MNO) VALUES('{}','{}',{})".format(cust_name,cust_adrs,cust_mno))
                    con.commit()
                    print('customer added successfully')
                    choice=input('\nDo you want to add one more customer(y or n): ')
                    
  
            elif cust_choice==3: #REMOVING CUSTOMER
                    choice='y'
                    while choice=='y':
                        cur.execute("SELECT * FROM CUST_DETAILS;")
                        data=cur.fetchall()
                        if len(data)>0:
                            cust_id=int(input('Enter customer id which you want to remove: '))
                            cur.execute("SELECT CUST_ID FROM CUST_DETAILS;")
                            cust_id_already_in=cur.fetchall()
                            if (cust_id,) in cust_id_already_in:
                                cur.execute('DELETE FROM CUST_DETAILS WHERE CUST_ID={}'.format(cust_id))
                                con.commit()
                                print('Customer removed successfully')
                                choice=input('\nDo you want to remove one more customer: ')
                            else:
                                print(f'No customer with {cust_id} customer id')
                                choice=input('\nDo you want to remove one more customer: ')
                        else:
                            print('No customers')
                            break

            elif cust_choice==4: #UPDATIGN CUSTOMER
                print('\nWHAT YOU WANT TO UPDATE: ')
                print('<1>CUSTOMER NAME\n<2>CUSTOMER ADDRESS\n<3>CUSTOMER_MOBILE NUMBER')
                update_cust=int(input('\nEnter your choice: '))
                which_cust=int(input('\nEnter customer id whose data you want to update: '))
                try:
                    cur.execute("SELECT CUST_ID FROM CUST_DETAILS;")
                    cust_id_already_in=cur.fetchall()
                    if update_cust==1:  #UPDATING CUSTOMER NAME
                        if (which_cust,) in cust_id_already_in:
                            cust_new_name=input('Enter the new name of the customer: ')
                            cur.execute("UPDATE CUST_DETAILS SET CUST_NAME = '{}' WHERE CUST_ID={}".format(cust_new_name,which_cust))
                            con.commit()
                            print('Customer name update successfully')
                        else:
                            print('No match found')
    
                    elif update_cust==2: #UPDATING CUSTOMER ADDRESS
                        if (which_cust,) in cust_id_already_in:
                            cust_new_adrs=input('Enter the new address of the address: ')
                            cur.execute("UPDATE CUST_DETAILS SET CUST_ADRS='{}' WHERE CUST_ID={}".format(cust_new_adrs,which_cust))
                            con.commit()
                            print("customer address updated successfully")
                        else:
                            print('No match found')
    
    
                    elif update_cust==3: #UPDATING CUSTOMER MOBILE NUMBER
                        if (which_cust,) in cust_id_already_in:
                            cust_new_mno=int(input('Enter the new mobile number of the customer: '))
                            cur.execute("UPDATE CUST_DETAILS SET CUST_MNO={} WHERE CUST_ID={}".format(cust_new_mno,which_cust))
                            con.commit()
                            print("customer mobile number updated successfully")
                        else:
                            print('No match found')
                    else:
                        print('Invalid input')
                except:
                    print('Try agian something went wrong')
            else:
                print('Invalid input')
        except:
            print('Try again something went wrong')
    else:
        print('Invalid Input')
except:
    print('Try again something went wrong')  

