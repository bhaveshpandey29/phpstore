import numpy as np
import pandas as pd
from databaseConnector import getDBConnection as connection

def generateCustomerCSV():
    db,cursor = connection()
    dataframe = pd.read_sql('select * from customer',db)
    dataframe.to_csv("customer.csv")
    
#generateCustomerCSV()