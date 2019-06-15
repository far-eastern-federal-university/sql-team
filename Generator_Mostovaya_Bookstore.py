# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:45:01 2019

@author: User
"""

import numpy as np
import random
import csv
with open('books.csv', "r") as f:
    reader = csv.reader(f)
    your_list = list(reader)

#print(your_list)

Books = [your_list[i][0] for i in range(211)]
Author_Name = list(set([your_list[i][1] for i in range(211)]))
Author_Name.remove(' ')
Author_Surname = [' Jaideva', ' John', ' Stephen', ' Edward', ' Vladimir', ' V P', ' Leonard', ' Frank', ' Maria', ' Gutierrez', ' Kurt', ' Cedric', ' Gerald', ' Abraham', ' Frank', ' John', ' Robert', ' H. G.', ' Werner', ' Andy', ' Terence', ' Drew', ' Nate', ' Wes', ' Thomas', ' Siddhartha', ' Albert', ' Arthur Conan', ' Arthur Conan', ' Adam', ' Ken', ' Adolf', ' Fritjof', ' Richard', 'Hemingway', ' Frederick', ' Jeffery', ' Randy', ' Ayn', ' Michael', 'Steinbeck', ' Edgar Allen', ' Stephen', ' Fritjof', ' Will', ' P L', ' John', ' John', ' John', ' John', ' V. S.', ' Joseph', ' Prime', ' Bob', ' Madan', ' Alfred', ' W. H.', ' Gary', ' Andrew', 'Forsyth', ' Schilling', ' Yashwant', ' Jonathan', ' Fyodor', ' Dan', ' Amartya', ' Amitav', ' Amartya', 'Hansberry', ' Bob', 'Archer', ' Kuldip', ' Sunita', ' William', ' Gill', ' P L', ' P L', ' P L', ' Sanjay', ' Johns', ' V P', ' Shashi', ' Shashi', ' Dominique', ' Dominique', ' Dominique', ' John', ' Bertrand', ' Sam', ' Shashi', ' Earle Stanley', ' Stephen', ' Peter', ' David', ' Victor', ' John', ' Peter', ' Richard', ' George', ' Amartya', ' William']
Author_Surname = list(set(Author_Surname))
Genre = [ 'nonfiction', 'data_science', 'science', 'mathematics', 'comic', 'signal_processing',  'economics', 'history', 'fiction', 'philosophy', 'computer_science', 'psychology']

Publisher = ['New York Times' , 'Vintage', 'Wiley', 'Random House', 'Penguin', 'Fontana', 'Marinner Books', 'Bison Books', 'Love&Romance', 'Flowing', 'Limestine Press', 'Literary Guild']
PublisherIND = [i for i in range(len(Publisher))]


print(Year_Publish)

List_Pub = []

for i in range(len(Publisher)):    
    
    indY = np.random.randint(1890, 2018)
    temp = Publisher[i]
    List_Pub.append([temp, indY, PublisherIND[Publisher.index(temp)]])
    
print(List_Pub)    


np.random.seed(542)

ListOfBooks = []

for i in range(1,211):
    
    indB = np.random.randint(0, len(Books))
    indN = np.random.randint(0, len(Author_Name))
    indSE = np.random.randint(0, len(Author_Surname))
    indP = np.random.randint(0, len(Publisher))
    indG = np.random.randint(0, len(Genre))
    ListOfBooks.append([Books[indB], Author_Name[indN],Author_Surname[indSE], Publisher[indP],Genre[indG], np.random.randint(1918, 2018), format(np.random.uniform(5,95), '.2f')])

    

myset = set(tuple(x) for x in ListOfBooks)

ListOfBooks =[list(x) for x in myset]

for x in range(len(ListOfBooks)):
    for i in range(len(Publisher)):
        if  ListOfBooks[x][3] == Publisher[i]:
            ListOfBooks[x].insert(3, Publisher.index(ListOfBooks[x][3]))
            ListOfBooks[x].remove(ListOfBooks[x][4])

#print(ListOfBooks) 

namesM = ['Ilya', 'Constantine', 'Alexander', 'Aleksei', 'Dmitriy', 'Stan', 'Oliver', 'Lee']
namesF = ['Julia', 'Anastasia', 'Katherine', 'Irina', 'Maria', 'Deya', 'Freya', 'Lois', 'Gina']
surnameM = ['Reserford', 'Vakarian', 'Shepard', 'Stark', 'Miller', 'Laslo', 'Elias', 'Lockhart']
surnameF = ['Mostovaya', 'Petrova', 'Sozonova', 'Samohina', 'Lannister', 'Harllo', 'Piniata', 'Pier']
Duty = ['cashier', 'janitor', 'warehouse worker', 'director']
series = random.sample(range(1000,8900), 1000) 
number =  number = random.sample(range(11000000000,89000000000),20)
print(len(series), len(set(series)))
ListOfStaff = []

ListofCus = []

for i in range(20):
    coin = np.random.sample()
    if coin > 0.5:
 
        ListofCus.append([number[np.random.randint(0, 20)], surnameM[np.random.randint(0, len(surnameM))], namesM[np.random.randint(0, len(namesM))]])
            
    else:         

        ListofCus.append([number[np.random.randint(0, 20)], surnameF[ np.random.randint(0, len(surnameF))], namesF[ np.random.randint(0, len(namesF))]])

myset = set(tuple(x) for x in ListofCus)
ListofCus =[list(x) for x in myset]   
print(ListofCus)     
    
for i in range(8):
    coin = np.random.sample()
    if coin > 0.5:
        indN = np.random.randint(0, len(namesM))
        indS = np.random.randint(0, len(surnameM))
        indSER = np.random.randint(0, len(series))
        indDuty = np.random.randint(0, len(Duty))
        ListOfStaff.append([series[indSER], surnameM[indS], namesM[indN], Duty[indDuty]])
            
    else:         
        indN = np.random.randint(0, len(namesF))
        indS = np.random.randint(0, len(surnameF))
        indSE = np.random.randint(0, len(surnameF))
        indSER = np.random.randint(0, len(series))
        indDuty = np.random.randint(0, len(Duty))
        ListOfStaff.append([series[indSER], surnameF[indS], namesF[indN], Duty[indDuty]])
    
myset = set(tuple(x) for x in ListOfStaff)
ListOfStaff =[list(x) for x in myset]
#print(ListOfStaff)  