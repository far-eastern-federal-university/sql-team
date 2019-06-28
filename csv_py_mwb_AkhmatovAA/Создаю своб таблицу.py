# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:09:39 2019

@author: axmatov.ari
"""
from mysql.connector import MySQLConnection, Error

import csv
import pandas as pd
import numpy as np

def library_data_book_has_author(): 
    def csv_reader(file_obj):
        """
        Read a csv file
        """
        reader = csv.reader(file_obj)
        for row in reader:
            print(" ".join(row))
 
    if __name__ == "__main__":
        with open("library_data_book_has_author.csv", "r") as f_obj:
            csv_reader(f_obj)
            
frame = pd.read_csv('library_data_book_has_author.csv', sep=',')
print(frame) 

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
        cursor.execute("DROP TABLE IF EXISTS library_data_book_has_author")
        # Создайте таблицу согласно требованию
        sql = """CREATE TABLE library_data_book_has_author 
                (id  INT,
                 ISBN  FLOAT,
                 Name CHAR(40),  
                 page_num INT,
                 pub_year INT )"""
       
        cursor.execute(sql)
                    
        # Подготовьте запрос SQL для вставки записи в базу данных.
        sql = """INSERT INTO library_data_book_has_author(id, ISBN, Name, page_num, pub_year) 
                 VALUES (109,6990901198455,"Foes Anderew Wresiveshg",642,1957)"""
                 
                 
        frame.to_sql(name='billing_simple', con=conn, if_exists = 'append', index=False)           
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



    