# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:47:13 2019

@author: User
"""


import mysql.connector
from mysql.connector import Error
import Generator_Mostovaya_Bookstore as GMB
import pandas as pd
 
 
def connect():
    """ Connect to MySQL database """
    try:
        
        
        conn = mysql.connector.connect(host='localhost',
                                      # database='OldBooks',
                                       user='root',
                                       password='root')
        
        if conn.is_connected() and conn.database == None:
            if  'OldBooks' != conn.database:
                conn.cursor().execute("CREATE DATABASE OldBooks")
            conn.database = 'OldBooks'
            
        if conn.is_connected():
            print(conn.database)
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
           # print(existing_tbls)
            if 'Publishers' in existing_tbls:
                print('Done')
            else:    
                mycursor.execute("CREATE TABLE Publishers ( PublisherID INT NOT NULL, PublisherName VARCHAR(25)," + 
                                                           "Year_Of_Establishing INT, PRIMARY KEY (PublisherID));")
            
            if 'Authors' not in existing_tbls:
                mycursor.execute("CREATE TABLE Authors ( AuthorID INT NOT NULL, AuthorName VARCHAR(25), " + 
                                                        "AuthorSurname VARCHAR(25), PRIMARY KEY (AuthorID));")
            
            if 'Clients' not in existing_tbls:
                mycursor.execute("CREATE TABLE `Clients` ( ClientID INT NOT NULL, ClientName VARCHAR(25)," + 
                                                          "ClientSurname VARCHAR(25), PhoneNumber VARCHAR(25)," + 
                                                          "PRIMARY KEY (ClientID));")
          
            if 'Orders' not in existing_tbls:
                mycursor.execute("CREATE TABLE Orders ( OrderID INT NOT NULL, ClientID INT NOT NULL," + 
                                                       " Price FLOAT(10,2), PRIMARY KEY (OrderID)," + 
                                                       " FOREIGN KEY (ClientID) REFERENCES " + 
                                                       "Clients (ClientID) ON DELETE CASCADE) ENGINE=INNODB;")

            if 'Books' not in existing_tbls:
                mycursor.execute("CREATE TABLE Books (BookID INT NOT NULL, BookTitle VARCHAR(55), BookGenre VARCHAR(25)," + 
                                                      " AuthorID INT, PublisherID INT NOT NULL, Year_Of_Publication INT, Price FLOAT(10,2)," + 
                                                      " PRIMARY KEY (BookID), FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID) ON DELETE CASCADE," + 
                                                      " FOREIGN KEY (PublisherID) REFERENCES Publishers (PublisherID) ON DELETE CASCADE) ENGINE=INNODB ;")
           
            
            if 'OrderedBooks' not in existing_tbls:
                mycursor.execute("CREATE TABLE OrderedBooks ( OrderedBooksID INT NOT NULL UNIQUE, OrderID INT NOT NULL," + 
                                                             " BookID INT NOT NULL,  PRIMARY KEY (OrderedBooksID)," + 
                                                             " FOREIGN KEY (BookID) REFERENCES Books(BookID)," + 
                                                             " FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)) ENGINE=INNODB;")
           
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            
            if "publishers" in existing_tbls:

               lst = GMB.Publish_Table

               for el in lst:
                    sql = "INSERT INTO Publishers ( PublisherID,PublisherName, Year_Of_Establishing) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM publishers")
               myresult = mycursor.fetchall()
                
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM publishers")
                myresult = mycursor.fetchall()
 
                for x in myresult:
                    print(x)
                    
                    
            if "authors" in existing_tbls:

                 lst = GMB.Author_Table

                 for el in lst:
                    sql = "INSERT INTO Authors ( AuthorID, AuthorName, AuthorSurname) VALUES (%s, %s, %s)"
                    val = (el[2],el[0], el[1])
                    mycursor.execute(sql, val)
                 mycursor.execute("SELECT * FROM Authors")
                 myresult = mycursor.fetchall()
                 for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Authors")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
                    
                       
            if "clients" in existing_tbls:

                 lst = GMB.Clients_Table
                 for el in lst:
                    sql = "INSERT INTO Clients ( ClientID, ClientName, ClientSurname, PhoneNumber) VALUES (%s, %s, %s, %s)"
                    val = (el[0],el[1], el[2], el[3])
                    mycursor.execute(sql, val)
                 mycursor.execute("SELECT * FROM Clients")
                 myresult = mycursor.fetchall()
                 for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Clients")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)     
                    
            if "orders" in existing_tbls:

               lst = GMB.Order_Table
               for el in lst:
                    sql = "INSERT INTO Orders ( OrderID, ClientID, Price) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Orders")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Orders")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)   
                    
            if "books" in existing_tbls:

               lst = GMB.Books_Table
               for el in lst:
                    sql = "INSERT INTO Books (BookID, BookTitle, BookGenre, AuthorID, PublisherID, Year_Of_Publication, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (el[0],el[1], el[2], el[3], el[4], el[5], el[6])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Books")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Books")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)                      
                                        
                    
                    
            if "orderedbooks" in existing_tbls:

               lst = GMB.OrderedBooks_Table
               for el in lst:
                    sql = "INSERT INTO OrderedBooks ( OrderedBooksID, OrderID, BookID) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM OrderedBooks")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM OrderedBooks")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)   

                    

             
               
               
                


 
    except Error as e:
        print(e)
 
    finally:
        conn.commit()
        conn.close()
 
 
if __name__ == '__main__':
    
    
    connect()