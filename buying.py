from databaseConnector import getDBConnection as connection
def buyProduct(customer_id,product_id,buying_quantity,buying_total_bill):
    db,cursor = connection()
    check_quantity = f"select product_quantity from product where product_id like '{product_id}'"
    cursor.execute(check_quantity)
    quantity = cursor.fetchall()
    #checking the quantity.
    if(int(quantity[0][0]) < 1):
        print("Sorry the product is sold out.")
    else:
        try:
            flag = 0
            db,cursor = connection()
            insert_sql = f"insert into buying(customer_id,product_id,buying_quantity,buying_total_bill) values('{customer_id}','{product_id}','{buying_quantity}','{buying_total_bill}')"        
            search_sql = f"select * from buying where product_id like '{product_id}'and customer_id like '{customer_id}'"
            update_sql = f"update product set product_quantity = product_quantity-'{buying_quantity}' where product_id like '{product_id}'"
            cursor.execute(search_sql)
            rs = cursor.fetchall()
            if(len(rs)>0):
                flag = 1
            else:
                cursor.execute(insert_sql)
                cursor.execute(search_sql)
                cursor.execute(update_sql)
                db.commit()
        except Exception as e:
            db.rollback()
            raise e
        else:
            if(flag == 0):
                print("bought successfully")
                return(True)
            else:
                print("Already purchased")
                return(False)
        finally:
            db.close()

#buyProduct(4,7,'2','400')

def getTotalBuyDetail(customer_id):
    try:
        flag = 0
        db,cursor = connection()
        sql = f"select * from buying where customer_id like'{customer_id}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        if(len(res)>0):
            flag = 1
    except Exception as e:
        print("Something went wrong!!")
        raise e
    else:
        if(flag == 1):
            print(list(res))
        else:
            print(f"No record found for customer id {customer_id}")
    finally:
        db.close()

#getTotalBuyDetail(3)

def getTotalBill(product_id,product_quantity):
    try:
        flag = 1
        db,cursor = connection()
        sql_price = f"select product_price from product where product_id like '{product_id}'"
        cursor.execute(sql_price)
        res = cursor.fetchall()
    except Exception as e:
        print("Something went wrong!!")
        raise e
    else:
        res = int(res[0][0])*(product_quantity)
        return res
    finally:
        db.close()
#print(getTotalBill(1,2))