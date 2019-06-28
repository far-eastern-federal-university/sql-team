# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:09:39 2019

@author: axmatov.ari
"""

import csv
import pandas as pd
import numpy as np
from mysql.connector import MySQLConnection, Error
            
frame = pd.read_csv('list_book.csv', sep=',')
#print(frame) 

def connect():
    """ Connect to MySQL database """
    try:
        print('Connecting to MySQL billing_simple...')
        conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')
        
        # Подготовка объекта cursor с помощью метода cursor()
        cursor =conn.cursor()
        # Удалите таблицу, если она уже существует с помощью метода execute()
        cursor.execute("DROP TABLE IF EXISTS list_book")
        # Создайте таблицу согласно требованию
        sql = """CREATE TABLE list_book (id INT, ISBN FLOAT, Name CHAR(40), page_num INT, pub_year INT )"""
       
        cursor.execute(sql)
                    
        # Подготовьте запрос SQL для вставки записи в базу данных.
        sql = """INSERT INTO list_book(id, ISBN, Name, page_num, pub_year) 
                 VALUES (000,6990901198455,"Foes Anderew Wresiveshg",642,1957)"""
                        
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
            print('YES connection.')
        else:
            print('NOT connection.')

    except Error as error:
        print(error)
        
    finally:
        conn.close()
        print('Connection closed.')
        

def insert_list_book(list_book):
    sql = """INSERT INTO list_book(id, ISBN, Name, page_num, pub_year) VALUES (%s, %s, %s, %s,%s)"""
    
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')

        cursor = conn.cursor()
        cursor.executemany(sql, list_book)
        conn.commit()
        #frame.to_sql(name='billing_simple', con=conn, if_exists = 'append', index=False) 
        
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print('Connection closed.')
        
def main():        
    list_book = [(	00,4887084793486,"Lord Of Dread",252,1992	),
                 (	2,1781739866104,"Pilot Of Fortune",308,1963	),
                 (	3,2238467303760,"Fish Without Faith",283,1986	),
                 (	4,4109664522524,"Horses With Honor",407,1914	),
                 (	5,6990901198455,"Foes And Wives",642,1957	),
                 (	6,5215396882083,"Lords And Fish",581,1999	),
                 (	7,6989765696623,"Defeat Of The Gods",102,1997	),
                 (	8,4987890299437,"Fortune Of Perfection",654,1900)]
    insert_list_book(list_book)                
         
if __name__ == '__main__':  
    connect()  
    main() 


    
