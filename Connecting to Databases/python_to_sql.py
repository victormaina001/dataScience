import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    connection=mysql.connector.connect(host='localhost',
                                         database='sales',
                                         user='root',
                                         password='roctiv',
                                         use_pure=True
    )
    if connection.is_connected():
        ''' db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record) '''
        customers_pd =pd.read_sql( "select * from transactions",connection)
    # get all records
        customers_pd.to_csv(r'E:\JOB\PROJECTS\generated csvs\transactions.csv',index=None)


except Error as e:
    print("Error while connecting to MySQL", e)

        

                                       
                                       
                                       
                                    
                                       
                                       
                                       
                                       
                                   