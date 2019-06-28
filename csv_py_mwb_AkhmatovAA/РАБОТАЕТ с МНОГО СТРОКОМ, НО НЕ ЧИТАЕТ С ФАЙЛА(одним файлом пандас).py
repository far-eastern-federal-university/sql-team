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
#print(frame) 


def insert_library_data_book_has_author(library_data_book_has_author):
    query = "INSERT INTO library_data_book_has_author(id, ISBN, Name, page_num, pub_year) VALUES (%s, %s, %s, %s,%s)"
    
    try:
        conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')

        cursor = conn.cursor()
        cursor.executemany(query, library_data_book_has_author)
        
        #frame.to_sql(name='billing_simple', con=conn, if_exists = 'append', index=False) 
        #conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()
        
def main():        
    library_data_book_has_author = [(	1,4887084793486,"Lord Of Dread",252,1992	),
(	2,1781739866104,"Pilot Of Fortune",308,1963	),
(	3,2238467303760,"Fish Without Faith",283,1986	),
(	4,4109664522524,"Horses With Honor",407,1914	),
(	5,6990901198455,"Foes And Wives",642,1957	),
(	6,5215396882083,"Lords And Fish",581,1999	),
(	7,6989765696623,"Defeat Of The Gods",102,1997	),
(	8,4987890299437,"Fortune Of Perfection",654,1900)]
    insert_library_data_book_has_author(library_data_book_has_author)                
  
if __name__ == '__main__':
    main()