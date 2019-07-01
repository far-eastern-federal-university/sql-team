# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:13:48 2019

@author: axmatov.ari
"""

# Create dataframe
from mysql.connector import MySQLConnection, Error
import pandas as pd
from sqlalchemy import create_engine

# input csv:
author = pd.read_csv('author.csv', sep=';')
data_book = pd.read_csv('data_book.csv', sep=';')
data_copy= pd.read_csv('data_copy.csv', sep=';')
data_category= pd.read_csv('data_category.csv', sep=';')
data_issuance = pd.read_csv('data_issuance.csv', sep=';')
data_category_has_book = pd.read_csv('data_category_has_book.csv', sep=';')
book_has_author = pd.read_csv('book_has_author.csv', sep=';')
data_reader = pd.read_csv('data_reader.csv', sep=';')
#print(FRAME)

# var:

database_user = 'root'
database_password = 'root'
database_host     = 'localhost'
database_name     = 'library_data'

# var:

#table_author = "author"
#table_data_book = "data_book"
#table_data_copy = "data_copy"
#table_data_category = 'data_category"
#table_data_issuance = "data_issuance"
#table_data_category_has_book = "data_category_has_book" 
#table_book_has_author = "book_has_author"
#table_data_reader = "data_reader"


def connect():
    """ Connect to MySQL database """
    try:
        
        conn = MySQLConnection(host = database_host,
                                      # database=database_name,
                                       user = database_user,
                                       password = database_password)
        
        if conn.is_connected() and conn.database == None:
            
            if  database_name != conn.database:
                #if database_name = :
                conn.cursor().execute("DROP DATABASE IF EXISTS " + database_name )
                #else
                conn.cursor().execute("CREATE DATABASE " + database_name )
            conn.database = database_name
            print('База данных '+ database_name +' созданна, Ура!')
            
    except Error as e:
        print(e)
    finally:
        conn.commit()
        conn.close()

# begin:
if __name__ == '__main__':
    connect()        
    
#Чтобы соединиться с СУБД, мы используем функцию create_engine():
conn = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(database_user, 
                                                      database_password, 
                                                      database_host, 
                                                      database_name))
#Удалите таблицу, если она уже существует с помощью метода execute()  
#result = conn.execute('DROP TABLE IF EXISTS' + имя)
#append: Insert new values to the existing table.
author.to_sql( name='author', con=conn, if_exists='append')
data_book.to_sql( name='data_book', con=conn, if_exists='append')
data_copy.to_sql( name='data_copy', con=conn, if_exists='append')
data_category.to_sql( name='data_category', con=conn, if_exists='append')
data_issuance.to_sql( name='data_issuance', con=conn, if_exists='append')
data_category_has_book.to_sql( name='data_category_has_book', con=conn, if_exists='append')
book_has_author.to_sql( name='book_has_author', con=conn, if_exists='append')
data_reader.to_sql( name='data_reader', con=conn, if_exists='append')

# end.

