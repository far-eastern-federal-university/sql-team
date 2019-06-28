# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 04:25:31 2019

@author: axmatov.ari
"""
import csv 
import numpy as np
import pandas as pd
from mysql.connector import MySQLConnection, Error

frame = pd.read_csv('library_data_book_has_author.csv', sep=',')
print(frame) 


def insert_library_data_book_has_author(library_data_book_has_author):
    query = "INSERT INTO library_data_book_has_author(id, ISBN, Name, page_num, pub_year) VALUES (%s, %s, %s, %s,%s)"
    
    try:
        conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')

        cursor = conn.cursor()
        cursor.executemany(query, library_data_book_has_author)
        
        frame.to_sql(name='billing_simple', con=conn, if_exists = 'append', index=False) 
        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()
        
def main():        
    library_data_book_has_author = []
    insert_library_data_book_has_author(library_data_book_has_author)                
  
if __name__ == '__main__':
    main()