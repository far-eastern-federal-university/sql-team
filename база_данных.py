# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:34:47 2019

@author: v-lazer
"""
import toolos_12_fake as pl
import mysql.connector
from mysql.connector import Error


 
 
def connect():
    """ Connect to MySQL database """
    try:
        
        
        conn = mysql.connector.connect(host='127.0.0.1',
                                      # database='Fruits',
                                       user='root',
                                       password='root')
        
        if conn.is_connected() and conn.database == None:
            if  'Fruits' != conn.database:
                conn.cursor().execute("CREATE DATABASE Fruits")
            conn.database = 'Fruits'
            
        if conn.is_connected():
            print(conn.database)
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
           # print(existing_tbls)
            if 'fruit' in existing_tbls:
                print('Done')
            else:    
                mycursor.execute("CREATE TABLE fruits ( FruitID INT NOT NULL, fruits VARCHAR(25)," + 
                                                           "Price INT, PRIMARY KEY (FruitID));")
            
            if 'country' not in existing_tbls:
                mycursor.execute("CREATE TABLE country ( CountryID INT NOT NULL, country VARCHAR(25), " + 
                                                        " PRIMARY KEY (CountryID));")
            
            if 'firm' not in existing_tbls:
                mycursor.execute("CREATE TABLE `Firm` ( FirmID INT NOT NULL, nameFirms VARCHAR(25)," + 
                                                          "PRIMARY KEY (FirmID));")
          
            if 'staff' not in existing_tbls:
                mycursor.execute("CREATE TABLE staff ( staffID INT NOT NULL, surnameF VARCHAR(25)," + 
                                                       " namesF VARCHAR(25), surnameM VARCHAR(25)," + 
                                                       " namesM VARCHAR(25), staff VARCHAR(25) " + 
                                                       "PRIMARY KEY (staffID);")

            if 'transport' not in existing_tbls:
                mycursor.execute("CREATE TABLE transport (transportID INT NOT NULL, transport VARCHAR(55)," + 
                                                      " PRIMARY KEY (transportID) ;")
           
            
            if 'advertising' not in existing_tbls:
                mycursor.execute("CREATE TABLE advertising ( AdvertisingID INT NOT NULL,  advertising VARCHAR(25)," + 
                                                             " FruitsID INT NOT NULL,  PRIMARY KEY ( AdvertisingID)," + 
                                                             " FOREIGN KEY (FruitsID);")
            if 'transactions' not in existing_tbls:
                mycursor.execute("CREATE TABLE transactions ( TransactionsID INT NOT NULL,  number INT, " + 
                                                             " FruitsID INT NOT NULL,  UserID INT NOT NULL," + 
                                                             " IDSeller INT, price int, quantity INT" + "PRIMARY KEY(TransactionsID), FOREIGN KEY(FruitsID);")       
            if 'user' not in existing_tbls:
                mycursor.execute("CREATE TABLE user (UserID INT NOT NULL,surnameM VARCHAR(55), namesM VARCHAR(25)," + 
                                                      " surnameF VARCHAR(25), namesF VARCHAR(25), secnameF VARCHAR(25)," + "PRIMARY KEY(UserID) ;")
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            
            if "Fruit" in existing_tbls:

               lst = pl.Fruit_Table

               for el in lst:
                    sql = "INSERT INTO Fruit (FruitID,fruits, Price) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Fruit")
               myresult = mycursor.fetchall()
                
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Fruit")
                myresult = mycursor.fetchall()
 
                for x in myresult:
                    print(x)
                    
                    
            if "Country" in existing_tbls:

                 lst = pl.Country_Table

                 for el in lst:
                    sql = "INSERT INTO Country ( CountryID, country) VALUES (%s, %s)"
                    val = (el[0],el[1])
                    mycursor.execute(sql, val)
                 mycursor.execute("SELECT * FROM Country")
                 myresult = mycursor.fetchall()
                 for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Country")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
                    
                       
            if "Firm" in existing_tbls:

                 lst = pl.Firm_Table
                 for el in lst:
                    sql = "INSERT INTO Firm ( FirmID, nameFirms ) VALUES (%s, %s)"
                    val = (el[0],el[1])
                    mycursor.execute(sql, val)
                 mycursor.execute("SELECT * FROM Firm")
                 myresult = mycursor.fetchall()
                 for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Firm")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)     
                    
            if "staff" in existing_tbls:

               lst = pl.staff_Table
               for el in lst:
                    sql = "INSERT INTO staff ( staffID, surnameF,namesF,surnameM,namesM,staff ) VALUES (%s, %s, %s,%s,%s,%s)"
                    val = (el[0],el[1], el[2], el[3], el[4], el[5])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM staff")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM staff")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)   
                    
            if "transport" in existing_tbls:

               lst = pl.transport_Table
               for el in lst:
                    sql = "INSERT INTO transport (transportID, Transport) VALUES (%s, %s)"
                    val = (el[0],el[1])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM transport")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM transport")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)                      
                                        
                    
                    
            if "Advertising" in existing_tbls:

               lst = pl.Advertising_Table
               for el in lst:
                    sql = "INSERT INTO Advertising ( AdvertisingID, Advertising, FruitsID) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Advertising")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Advertising")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)   

            if "Transactions" in existing_tbls:

               lst = pl.Transactions_Table
               for el in lst:
                    sql = "INSERT INTO Transactions (TransactionsID,  number, FruitsID, UserID, IDSeller, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (el[0],el[1], el[2], el[3], el[4], el[5])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Transactions")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Transactions")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x) 
                    
            if "User" in existing_tbls:

               lst = pl.User_Table
               for el in lst:
                    sql = "INSERT INTO User (UserID,  surnameM, namesM, surnameF, namesF, secnameF) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (el[0],el[1], el[2], el[3], el[4], el[5])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM User")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM User")
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