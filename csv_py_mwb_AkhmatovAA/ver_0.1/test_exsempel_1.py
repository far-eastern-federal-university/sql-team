    # -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 02:33:12 2019

@author: axmatov.ari
"""

# Create dataframe
from mysql.connector import MySQLConnection, Error
import csv
import pandas as pd
import numpy as np

#я изменил 

data = pd.read_csv('list_book.csv', sep=',')
print(data) 

conn = MySQLConnection(host='localhost',
                           database='billing_simple',
                           user='root',
                           password='root')

"""cursor =conn.cursor()   # Подготовка объекта cursor с помощью метода cursor()
cursor.execute("DROP TABLE IF EXISTS list_book")# Удалите таблицу, если она уже существует 
                                                                   #с помощью метода execute()
# Создайте таблицу согласно требованию
sql = "CREATE TABLE list_book(
                 id  INT,
                 ISBN  FLOAT,
                 Name CHAR(40),  
                 page_num INT,
                 pub_year INT )"

cursor.execute(sql)

#conn.cursor().execute("CREATE DATABASE IF NOT EXISTS {0} ".format(billing_simple))
"""
data.to_sql(name='billing_simple', con=conn, if_exists = 'replace', index=False) 
#как работает 
