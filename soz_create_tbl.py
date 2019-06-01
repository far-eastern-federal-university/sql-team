# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:09:45 2019

@author: sozonova.aal
"""

import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='school',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            mycursor = conn.cursor()
            #            mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
            mycursor.execute("SHOW TABLES")
            
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            if "customers" in existing_tbls:
                mycursor.execute("Select Count(name) From customers")
                ch = mycursor.fetchall()
            #
            if ch[0][0] == 0:
                """Блок с идеей
                """
                lst = [["john", "svetlanskaya 5"],["yen", "svetlanskaya 6"]]
                for el in lst:
                    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
                    val = (el[0], el[1])
                    mycursor.execute(sql, val)
                mycursor.execute("SELECT * FROM customers")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM customers")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)

#            mycursor.execute("CREATE TABLE puples (name VARCHAR(255), address VARCHAR(255))")
 
    except Error as e:
        print(e)
 
    finally:
        conn.commit()
        conn.close()
 
 
if __name__ == '__main__':
    
    
    connect()