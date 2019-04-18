# Здесь был код
# one third of the  semester is over
#RELEASE THE KRAKEN!!
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:41:27 2019

@author: Dmitry
"""

import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='sakila',
                                       user='root',
                                       password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM actor")
            row = cursor.fetchone()
            while row is not None:
                print(row)
                row = cursor.fetchone()
#            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()