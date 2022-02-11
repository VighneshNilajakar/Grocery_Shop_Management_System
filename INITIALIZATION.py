import mysql.connector as mcon
print("INITIALIZING..........")
con = mcon.connect(host = "localhost", user = "root", passwd = "", charset = "utf8")
if con.is_connected() == True:
    print("CONNECTION SUCCESSFULL")
else:
    print("ERROR CONNECTING MYSQL")
cur = con.cursor()
cur.execute("DROP DATABASE IF EXISTS GROCERY_MANAGEMENT_SYS")
cur.execute("CREATE DATABASE IF NOT EXISTS GROCERY_MANAGEMENT_SYS;")
cur.execute("USE GROCERY_MANAGEMENT_SYS;")
print("CREATED REQUIRED DATABASES")
cur.execute("CREATE TABLE IF NOT EXISTS PROD_DETAILS (PROD_ID INT(3) AUTO_INCREMENT PRIMARY KEY, PROD_NAME VARCHAR(200) NOT NULL UNIQUE, PROD_SELL_COST INT(10) NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS PROD_BUY_COST (PROD_BUY_COST INT(20) NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS CUST_DETAILS (CUST_ID INT(3) AUTO_INCREMENT PRIMARY KEY, CUST_NAME VARCHAR(30) NOT NULL, CUST_ADRS VARCHAR (200), CUST_MNO INT(10) NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS MAN_DETAILS (MAN_ID INT(3) AUTO_INCREMENT PRIMARY KEY, MAN_NAME VARCHAR(200) NOT NULL);")
print("CREATED REQUIRED TABLES")
print("REQUIREMENTS INITIALIZED")
print("STARTING SOFTWARE---\n\n\n")
msg1 = "GROCERY MANAGEMENT SYSTEM"
pmsg1 = msg1.center(120)
print(pmsg1)
print("-------CHOOSE FROM THE FOLLOWING-------")
print("<1>PRODUCT DETAILs\n<2>CUSTOMER DETAILS")


try:
    choice=int(input('Enter Your choice: '))
    if choice==1:
        print("<1>PRODUCT DETAILS\n<2>ADD PRODUCT\n<3>REMOVE PRODUCT")
        try:
            prod_choice=int(input('Enter your choice: '))
            if prod_choice==1:
                cur.execute("SELECT * FROM PROD_DETAILS;")
                prod_data=cur.fetchall()
                for i in prod_data:
                    print(i)
            elif prod_choice==2:
                prod_name=input('Enter product name: ')
                prod_sell_cost=int(input('Enter product selling price: '))
                cur.execute("INSERT INTO PROD_DETAILS(PROD_NAME,PROD_SELL_COST) VALUES('{}',{})".format(prod_name,prod_sell_cost))
                con.commit()
                print('Product added successfully')
            elif prod_choice==3:
                prod_id=int(input('Enter the product id you want to remove: '))
                cur.execute("DELETE FROM PROD_DETAILS WHERE PROD_ID = {}".format(prod_id))
                con.commit()
                print('product removed successfully')
            else:
                print()
        except:
            print('Invalid input')

    elif choice==2:
        print("<1>CUSTORMER DETAILS\n<2>ADD CUSTOMER\n<3>REMOVE CUSTOMER\n<4>UPDATE CUSTOMER")
        try:
            cust_choice=int(input('Enter your choice: '))
            if cust_choice==1:
                cur.execute("SELECT * FROM CUST_DETAILS;")
                cust_details=cur.fetchll()
                for j in cust_details:
                    print(j)
            elif cust_choice==2:
                cust_name=input('Enter customer name: ')
                cust_adrs=input('Enter customer address: ')
                cust_mno=int(input('Enter customer mobile number: '))
                cur.execute("INSERT INTO CUST_DETAILS(CUST_NAME,CUST_ADRS,CUST_MNO) VALUES('{}','{}',{})".format(cust_name,cust_adrs,cust_mno))
                con.commit()
                print('customer added successfully')
  
            elif cust_choice==3:
                cust_id=int(input('Enter customer id: '))
                cur.execute('DELETE FROM CUST_DETAILS WHERE CUST_ID={}'.format(cust_id))
                con.cummit()
                print('Customer removed successfully')

            elif cust_choice==4:
                print('WHAT YOU WANT TO UPDATE: ')
                print('<1>CUSTOMER NAME\n<2>CUSTOMER ADDRESS\n<3>CUSTOMER_MOBILE NUMBER')
                update_cust=int(input('Enter your choice: '))
                which_cust=int(input('Enter customer id whose data you want to update: '))
                if update_cust==1:
                    cust_name=int(input('Enter the customer name to update: '))
                    cur.execute("UPDATE CUST_DETAILS SET CUST_NAME = '{}' WHERE CUST_ID={}".format(cust_name,which_cust))
                    con.commit()
                    print('Customer update successfully')

                elif update_cust==2:
                    cust_update_adrs=input('Enter the new address of the address: ')
                    cur.execute('UPDATE CUST_DETAILS SET ')
                    con.commit()
                    print("customer address updated successfully")


                elif update_cust==3:
                    cust_update_mno=int(input('Enter the new address of the address: '))
                    cur.execute('UPDATE CUST_DETAILS SET ')
                    con.commit()
                    print("customer mobile number updated successfully")
            
            else:
                print('Invalid input')
        except:
            print('Invalid input')
except:
    print('Invalid input')
