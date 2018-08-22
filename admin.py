from databaseConnector import getDBConnection as connection
def registerAdmin(name,username,password,contact_no,access_token):
    try:
        flag = 0
        db,cursor = connection()
        insert_sql = f"insert into admin(name,username,password,contact_no,access_token) values('{name}','{username}','{password}','{contact_no}','{access_token}')"
        
        search_sql = f"select * from admin where username like '{username}' and password like '{password}' and contact_no like '{contact_no}'"

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
            print("user already exist")
    finally:
        db.close()

#registerAdmin('a','a','a','a','a','a')

def checkAdminLogin(username,password):
    try:
        flag =0
        db,cursor = connection()
        sql = f"select * from admin where username like '{username}' and password like '{password}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res)>0:
            flag =1 
        
    except Exception as e:
        print("Something went wrong")
        raise e        
    else:
        if(flag):
            print(f"Welcome admin '{username}'")
            return(True)
        else:
            return(False)    
    finally:
        db.close()

#checkAdminLogin('a','a')
    