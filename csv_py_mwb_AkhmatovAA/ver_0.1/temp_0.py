# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:09:39 2019

@author: axmatov.ari
Создаю свою таблицу
"""
from mysql.connector import MySQLConnection, Error

import csv
import pandas as pd
import numpy as np

            
frame = pd.read_csv('list_book.csv', sep=',')
#print(frame) 

def connect():
    """ Connect to MySQL database """
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')
        
        # Подготовка объекта cursor с помощью метода cursor()
        cursor =conn.cursor()
        # Удалите таблицу, если она уже существует с помощью метода execute()
        cursor.execute("DROP TABLE IF EXISTS list_book")
        # Создайте таблицу согласно требованию
        sql = """CREATE TABLE list_book(
                 id  INT,
                 ISBN  FLOAT,
                 Name CHAR(40),  
                 page_num INT,
                 pub_year INT )"""
       
        cursor.execute(sql)
                    
        # Подготовьте запрос SQL для вставки записи в базу данных.
        sql = """INSERT INTO library_data_book_has_author(id, ISBN, Name, page_num, pub_year) 
                 VALUES (109,6990901198455,"Foes Anderew Wresiveshg",642,1957)"""
                 
                 
        #frame.to_sql(name='billing_simple', con=conn, if_exists = 'append', index=False)           
        try:
             # Выполните команду SQL
             cursor.execute(sql)
             # Зафиксировать изменения в базе данных
             conn.commit()
        except:
                 # Откат в случае ошибки
                 conn.rollback()
        
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)
        
    finally:
        conn.close()
        print('Connection closed.')
    
if __name__ == '__main__':
    connect()



    
