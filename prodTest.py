from databaseConnector import getDBConnection as connection
def registerProduct(product_name,product_price,product_quantity):
    try:
        flag=0
        db,cursor= connection()
        insert_sql = f"insert into product(product_name,product_price,product_quantity) values ('{product_name}','{product_price}','{product_quantity}')"
        search_sql = f"select * from product where product_name like '{product_name}' and product_price like {product_price}"
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
            print("produt already exist")
    finally:
        db.close()

#registerProduct('PHP','200','6')

def getProductDetail(product_name):
    try:
        flag = 0
        db,cursor = connection()
        sql = f"select * from product where product_name like '{product_name}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        if len(res)>0:
            flag =1         
    except Exception as e:
        print("Something went wrong")
        raise e        
    else:
        print(list(res))
    finally:
        db.close()

#getProductDetail('python')

def getAllProduct():
    db,cursor = connection()
    try:
        sql = f"select * from product"
        cursor.execute(sql)
        resu = cursor.fetchall()
                
    except Exception as e:
        print("Something went wrong")
        raise e        
    else:
        print(list(resu))
    finally:
        db.close()

getAllProduct()