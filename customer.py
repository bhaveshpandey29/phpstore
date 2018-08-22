from databaseConnector import getDBConnection as connection
def registerCustomer(name,contact_no,address,c_type,customer_email):
    try:
        flag = 0
        db,cursor = connection()
        insert_sql = f"insert into customer(customer_name,customer_contact,customer_address,customer_type,customer_email) values('{name}','{contact_no}','{address}','{c_type}','{customer_email}')"

        search_sql = f"select * from customer where customer_name like '{name}' and customer_contact like '{contact_no}'"

        cursor.execute(search_sql)
        rs = cursor.fetchall()
        if(len(rs)>0):
            flag = 1
        else:
            cursor.execute(insert_sql)
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    else:
        if(flag == 0):
            print("inserted successfully")
        else:
            print("customer already exist")
    finally:
        db.close()

#registerCustomer('Max','9029006525','test address','individual','abc@xyz.com')

def checkLogin(username,contact_no):
    try:
        flag =0
        db,cursor = connection()
        sql = f"select * from customer where customer_name like '{username}' and customer_contact like '{contact_no}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res)>0:
            flag =1        
    except Exception as e:
        print("Something went wrong")
        raise e        
    else:
        if(flag):
            print(f"Welcome! {username}")
            return(True)
        else:
            print("No records available")
            #return(False)    
    finally:
        db.close()

#checkLogin('bunn','9930')

def getCustomer(username):
    try:
        flag = 0
        db,cursor = connection()
        sql = f"select * from customer where customer_name like '{username}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        if(len(result)>0):
            flag = 1
    except Exception as e:
        print("Something went wrong!!")
        raise e
    else:
        if(flag == 0):
            print(f"No records found")
        else:
            print(list(result))
            #print(result[0][1]) this can be used to print values in the tuple
            #print(type(result))
    finally:
        db.close()

#getCustomer('bunn')

def getCustomerId(customer_contact):
    try:
        flag = 0
        db,cursor = connection()
        sql = f"select customer_id from customer where customer_contact like '{customer_contact}'"
        cursor.execute(sql)
        resul = cursor.fetchall()
        if(len(resul)>0):
            flag = 1
    except Exception as e:
        print("Something went wrong!!")
        raise e
    else:
        if(flag == 0):
            print(f"No records found")
        else:
            #return resul
            return(resul[0][0])
    finally:
        db.close()

#print(getCustomerId('9930'))