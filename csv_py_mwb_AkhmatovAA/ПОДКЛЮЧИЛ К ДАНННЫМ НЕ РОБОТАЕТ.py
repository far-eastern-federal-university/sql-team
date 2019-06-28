# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 03:58:09 2019

@author: axmatov.ari
"""
from mysql.connector import MySQLConnection, Error

import csv

def CSV(): 
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
        
        def insert_library_data_book_has_author(library_data_book_has_author):
            sql = """CREATE TABLE library_data_book_has_author 
                (id  INT,
                 ISBN  FLOAT,
                 Name CHAR(20),  
                 page_num INT,
                 pub_year INT )"""
                
            #cursor.execute(sql)
                    
            # Подготовьте запрос SQL для вставки записи в базу данных.
            sql = """INSERT INTO library_data_book_has_author
                 (id, ISBN, Name, page_num, pub_year)
                 VALUES (%s,%s, %s, %S, %s)"""

            try:
                conn = MySQLConnection(host='localhost',
                                       database='billing_simple',
                                       user='root',
                                       password='root')

                cursor = conn.cursor()
                cursor.executemany(sql, library_data_book_has_author)

                conn.commit()
            except Error as e:
                print('Error:', e)

            finally:
                cursor.close()
                conn.close()

        def main():
            library_data_book_has_author = [(CSV())]
            insert_library_data_book_has_author(library_data_book_has_author)
        if __name__ == '__main__':
            main()
        
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
    