# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 00:13:48 2019

@author: axmatov.ari
"""

# Create dataframe
import sqlalchemy 
import pandas as pd

FRAME = pd.read_csv('list_Books.csv', sep=';')
print(FRAME)

database_username = 'root'
database_password = 'zhil,p@ss'
database_host    = 'localhost'
database_name     = 'billing_simple'
#Чтобы соединиться с СУБД, мы используем функцию create_engine():
conn = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(database_username, 
                                                      database_password, 
                                                      database_host,
                                                      database_name))
#
#if conn.is_connected() and conn.database == None:
#    print("Connected")
#    if  database_name != conn.database:
#        conn.cursor().execute("CREATE DATABASE " + database_name)
#    conn.database = database_name
    
    
# Удалите таблицу, если она уже существует с помощью метода execute()  
result = conn.execute('DROP TABLE IF EXISTS list_Books')
FRAME.to_sql( name='list_Books', con=conn, if_exists='replace')


print('____XXXXXX__________­____________________­____XXX__XXХ') 
print('___XX_XXXXXXX______­____________________­__XXXXX_XX_XX') 
print('___XX___XXXXXXX____­____________________­XXXXX_X____XX') 
print('___XX_____XXXXXXX__­___________________X­XXXXXX_____XX') 
print('__XXX__XX___XXXXXXX­_________________XXX­XXXX___XX__XX')
print('__XXX_____X___XXXXX­XX_____XX______XXXXX­XXX__X_____XX') 
print('__XXXXX_____X__XXXX­XXXXXXXXXXXXXXXXXXXX­X__X___XXX_XX') 
print('___XX___XX___XX_XXX­XXXXXXXXXXXXXXXXXXXX­XX__XX_____XX') 
print('___XX_X____XX_XXXXX­XXXXXXX___XXXXXXXXXX­XXX___XXXX_XX') 
print('___XX____XX_XXXXXXX­XXXXX_`````_XXXXXXXX­XXXXX_____XXX') 
print('___XXXXXX__XXX_```_­XXXX_```````_XXX_```­```_XXXX__XX')
print('____XX____XX```````­_`X``````````_X`````­`````XXXXXXX')
print('____XX___X_```_$$$$­$__X`````````X`_$$$$­$$````XXXXX')
print('_____XX_XX```$$$$$$­$$$_X```````_`_$$$$$­$$$````XXXX')
print('______XXX_``_$$$$$$­$$$_X```````X_$$$$$$­$$$_```XXX')
print('______XXX_``_$$$$$$­$$$__```````X_$$$$$$­$$$_``_XXXX')
print('______XXXX```$$$$$$­$$$__```````X`_$$$$$­$$$```_XXXX')
print('______XXXXX___$$$$$­$$`__`___```_X``_$$$­$__``XXXXXX')
print('______XXXXXXXXXX_$$­$$__`__XXX___``_XXX_­XXXXXXXXXXX')
print('______XXXXXX__`````­``___XXXXXXX__``````­````_XXXXXX')