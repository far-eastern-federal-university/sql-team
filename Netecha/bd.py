# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:34:47 2019

@author: v-lazer
"""
import toolos_12_fake as pl
import mysql.connector


DB_NAME = 'fruits'


def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS fruit (
                        id INT NOT NULL PRIMARY KEY,
                        fruits VARCHAR(25),
                        price FLOAT
                    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS country (
                        id INT NOT NULL PRIMARY KEY,
                        country VARCHAR(25)
                    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS firm (
                        id INT NOT NULL PRIMARY KEY,
                        nameFirms VARCHAR(25)
                    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS staff (
                        id INT NOT NULL PRIMARY KEY,
                        surnameF VARCHAR(25),
                        namesF VARCHAR(25), surnameM VARCHAR(25),
                        namesM VARCHAR(25), staff VARCHAR(25)
                    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS transport (
                        id INT NOT NULL PRIMARY KEY,
                        transport VARCHAR(55)
                    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS advertising (
                        id INT NOT NULL PRIMARY KEY,
                        advertising VARCHAR(25),
                        FruitsID INT NOT NULL,

                        FOREIGN KEY (FruitsID) REFERENCES fruit(id)
            );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                            id INT NOT NULL PRIMARY KEY,
                            surnameM VARCHAR(55), namesM VARCHAR(25),
                            surnameF VARCHAR(25), namesF VARCHAR(25),
                            secnameF VARCHAR(25)
                        ) ;""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS transaction (
                        id INT NOT NULL PRIMARY KEY,
                        number INT,
                        FruitsID INT NOT NULL,
                        UserID INT NOT NULL,
                        quantity INT NOT NULL,

                        FOREIGN KEY(FruitsID) REFERENCES fruit(id),
                        FOREIGN KEY(UserID) REFERENCES user(id)
                    );""")


def show_tables(cursor):
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    existing_tbls = [x[0] for x in tables]
    print(existing_tbls)


def insert_data(cursor):
    print("= fruit =")

    for el in pl.Fruit_Table:
        sql = "INSERT INTO fruit (id,fruits, Price) VALUES (%s, %s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM fruit")
    res = cursor.fetchall()

    for x in res:
        print(x)

    print("= country =")

    for el in pl.Country_Table:
        sql = "INSERT INTO country (id, country) VALUES (%s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM country")
    for x in cursor.fetchall():
        print(x)

    print("= firm =")

    for el in pl.Firm_Table:
        sql = "INSERT INTO firm (id, nameFirms ) VALUES (%s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM firm")

    for x in cursor.fetchall():
        print(x)

    print("= staff =")

    for el in pl.staff_Table:
        sql = "INSERT INTO staff (id, surnameF,namesF,surnameM,namesM,staff ) VALUES (%s, %s, %s,%s,%s,%s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM staff")

    for x in cursor.fetchall():
        print(x)

    print("= transport =")

    for el in pl.transport_Table:
        sql = "INSERT INTO transport (id, Transport) VALUES (%s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM transport")
    for x in cursor.fetchall():
        print(x)

    print("= advertising =")

    for el in pl.Advertising_Table:
        sql = "INSERT INTO advertising (id, Advertising, FruitsID) VALUES (%s, %s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM advertising")

    for x in cursor.fetchall():
        print(x)

    print("= user =")

    for el in pl.User_Table:
        sql = "INSERT INTO user (id, surnameM, namesM, surnameF, namesF, secnameF) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM user")
    for x in cursor.fetchall():
        print(x)

    print("= transaction =")

    for el in pl.Transactions_Table:
        sql = "INSERT INTO transaction (id, number, FruitsID, UserID, quantity) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, el)

    cursor.execute("SELECT * FROM transaction")

    for x in cursor.fetchall():
        print(x)


def run():
    """ Connect to MySQL database """

    conn = mysql.connector.connect(host='127.0.0.1',
                                   database='fruits',
                                   user='root',
                                   password='root')

    if not conn.is_connected():
        raise Exception('Not connected')

    if conn.database != DB_NAME:
        conn.cursor().execute('CREATE DATABASE {}'.format(DB_NAME))
        conn.database = DB_NAME

    print(conn.database)
    cursor = conn.cursor()

    create_tables(cursor)
    show_tables(cursor)
    insert_data(cursor)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    run()
