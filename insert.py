# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:47:13 2019

@author: User
"""


import mysql.connector
from mysql.connector import Error
import Generator_Mostovaya_Bookstore as GMB
 
 
def connect():
    """ Connect to MySQL database """
    try:
        
        
        conn = mysql.connector.connect(host='localhost',
                                      # database='OldBooks',
                                       user='root',
                                       password='root')
        
        if conn.is_connected() and conn.database == None:
            if  'OldBooks' not in conn.cursor():
                conn.cursor().execute("CREATE DATABASE OldBooks")
        conn.database = 'OldBooks'
            
        if conn.is_connected():
            print(conn.database)
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            if 'Publishers' in existing_tbls:
                print('Done')
            else:    
                mycursor.execute("CREATE TABLE Publishers ( PublisherID INT NOT NULL, PublisherName VARCHAR(25), Year_Of_Establishing INT, PRIMARY KEY (PublisherID))")
            
            if 'Authors' not in existing_tbls:
                mycursor.execute("CREATE TABLE Authors ( AuthorID INT NOT NULL, AuthorName VARCHAR(25), AuthorSurname VARCHAR(25), PRIMARY KEY (AuthorID))")
            
            if 'Clients' not in existing_tbls:
                mycursor.execute("CREATE TABLE `Clients` ( ClientID INT NOT NULL, ClientName VARCHAR(25), ClientSurname VARCHAR(25), PhoneNumber VARCHAR(25), PRIMARY KEY (ClientID))")
          
            if 'Orders' not in existing_tbls:
                mycursor.execute("CREATE TABLE Orders ( OrderID INT NOT NULL, ClientID_FK INT NOT NULL, Price FLOAT(10,2) PRIMARY KEY (OrderID), CONSTRAINT ClientID_FK FOREIGN KEY (ClientID_FK) REFERENCES Clients (ClientID) ON DELETE CASCADE) ENGINE=INNODB;")

            if 'Books' not in existing_tbls:
                mycursor.execute("CREATE TABLE Books (BookID INT NOT NULL, BookTitle VARCHAR(30), BookGenre VARCHAR(25), AuthorID INT NOT NULL, PublisherID INT NOT NULL, Price FLOAT(10,2), PRIMARY KEY (BookID), FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID), FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)) ENGINE=INNODB;")
           
            
            if 'OrderedBooks' not in existing_tbls:
                mycursor.execute("CREATE TABLE OrderedBooks ( OrderedBooksID INT NOT NULL, OrderID INT NOT NULL, BookID INT NOT NULL,  PRIMARY KEY (OrderedBooksID), FOREIGN KEY (BookID) REFERENCES Books(BookID), FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)) ENGINE=INNODB;")
           
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            
#            if "OldBooks" not in mycursor:
#                mycursor.execute("CREATE DATABASE OldBooks")
                 
            
       
#            tables = mycursor.fetchall()
#            existing_tbls = [x[0] for x in tables]
#            if "Publishers" in existing_tbls:
#                mycursor.execute("Select Count(name) From Publishers")
#                ch = mycursor.fetchall()
#            #
#            if ch[0][0] == 0:
#                """Блок с идеей
#                """
#                lst = [["john", "svetlanskaya 5"],["yen", "svetlanskaya 6"]]
#                for el in lst:
#                    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#                    val = (el[0], el[1])
#                    mycursor.execute(sql, val)
#                mycursor.execute("SELECT * FROM customers")
#                myresult = mycursor.fetchall()
#                
#                for x in myresult:
#                    print(x)
#            else:
#                mycursor.execute("SELECT * FROM customers")
#                myresult = mycursor.fetchall()
                
#                for x in myresult:
#                    print(x)

#            mycursor.execute("CREATE TABLE puples (name VARCHAR(255), address VARCHAR(255))")
 
    except Error as e:
        print(e)
 
    finally:
        conn.commit()
        conn.close()
 
 
if __name__ == '__main__':
    
    
    connect()