import pymysql as sql
def getDBConnection(ip="localhost",uname="root",password="04200420",dbname="mds"):
    try:
        db = sql.connect(ip,uname,password,dbname)
        cursor = db.cursor()
    except Exception as e:
        raise e
    else:
        #print("Connection Successful!")
        return(db,cursor)

#print(getDBConnection())
