# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:13:48 2019

@author: axmatov.ari
"""

# Create dataframe
from mysql.connector import MySQLConnection, Error
import pandas as pd
#import sqlalchemy 
from sqlalchemy import create_engine

frame = pd.read_csv('list_Books.csv', sep=';')

#print(FRAME)

# var:
database_user = 'root'
database_password = 'root'
database_host     = 'localhost'
database_name     = 'books'

def connect():
    """ Connect to MySQL database """
    try:
        
        conn = MySQLConnection(host = database_host,
                                      # database=database_name,
                                       user = database_user,
                                       password = database_password)
        
        if conn.is_connected() and conn.database == None:
            
            if  database_name != conn.database:
                conn.cursor().execute("DROP DATABASE " + database_name )
                conn.cursor().execute("CREATE DATABASE " + database_name )
            conn.database = database_name
            print('База данных '+ database_name +' созданна')
            
    except Error as e:
        print(e)
    finally:
        conn.commit()
        conn.close()

if __name__ == '__main__':
    connect()        
    
#Чтобы соединиться с СУБД, мы используем функцию create_engine():
conn = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(database_user, 
                                                      database_password, 
                                                      database_host, 
                                                      database_name))
# Удалите таблицу, если она уже существует с помощью метода execute()  
#result = conn.execute('DROP TABLE IF EXISTS list')
frame.to_sql( name='list', con=conn, if_exists='replace')
print("Connected")



