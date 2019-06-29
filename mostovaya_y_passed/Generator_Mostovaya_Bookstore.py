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


np.random.seed(542)
    
def Author():
    Author_Name = list(set([your_list[i][1] for i in range(211)]))
    Author_Name.remove(' ')
    Author_Name.remove(' A Modern Approach')
    Author_Surname = [' Jaideva', ' John', ' Stephen', ' Edward', ' Vladimir', ' V P', ' Leonard', ' Frank', ' Maria', ' Gutierrez', ' Kurt', ' Cedric', ' Gerald', ' Abraham', ' Frank', ' John', ' Robert', ' H. G.', ' Werner', ' Andy', ' Terence', ' Drew', ' Nate', ' Wes', ' Thomas', ' Siddhartha', ' Albert', ' Arthur Conan', ' Arthur Conan', ' Adam', ' Ken', ' Adolf', ' Fritjof', ' Richard', 'Hemingway', ' Frederick', ' Jeffery', ' Randy', ' Ayn', ' Michael', 'Steinbeck', ' Edgar Allen', ' Stephen', ' Fritjof', ' Will', ' P L', ' John', ' John', ' John', ' John', ' V. S.', ' Joseph', ' Prime', ' Bob', ' Madan', ' Alfred', ' W. H.', ' Gary', ' Andrew', 'Forsyth', ' Schilling', ' Yashwant', ' Jonathan', ' Fyodor', ' Dan', ' Amartya', ' Amitav', ' Amartya', 'Hansberry', ' Bob', 'Archer', ' Kuldip', ' Sunita', ' William', ' Gill', ' P L', ' P L', ' P L', ' Sanjay', ' Johns', ' V P', ' Shashi', ' Shashi', ' Dominique', ' Dominique', ' Dominique', ' John', ' Bertrand', ' Sam', ' Shashi', ' Earle Stanley', ' Stephen', ' Peter', ' David', ' Victor', ' John', ' Peter', ' Richard', ' George', ' Amartya', ' William']
    Author_Surname = list(set(Author_Surname))
    Author_List = []
    for i in range(0,len(your_list)):
         indN = np.random.randint(0, len(Author_Name))
         indSE = np.random.randint(0, len(Author_Surname))
         Author_List.append([Author_Name[indN], Author_Surname[indSE]])
        
    myset = set(tuple(x) for x in Author_List)
    Author_List =sorted([list(x) for x in myset])   
    
    for i in range(0, len(Author_List)):
        Author_List[i].append(i)
    return(Author_List)

Author_Table = Author()   
#print((Author_Table))  

def Publish():
    Publisher = ['New York Times' , 'Vintage', 'Wiley', 'Random House', 'Penguin', 'Fontana', 
                 'Marinner Books', 'Bison Books', 'Love&Romance', 'Flowing', 'Limestine Press', 
                 'Literary Guild', 'HarperCollins', 'Simon & Schuster','Hachette Book Group',
                 'Macmillan','Scholastic','Houghton Mifflin Harcourt','Workman','Sterling',
                 'Abrams','Dover','Candlewick','W.W. Norton','Kensington','Chronicle','Sourcebooks',
                 'B&H Publishing','Tyndale House','BloomsBury', 'London Press' ]
    PublisherIND = [i for i in range(len(Publisher))]
    List_Pub = []
    for i in range(len(Publisher)):    
    
        indY = np.random.randint(1890, 2018)
        temp = Publisher[i]
        List_Pub.append([PublisherIND[Publisher.index(temp)], temp, indY])
        
    return(sorted(List_Pub))    

Publish_Table = Publish()

print((Publish_Table))    

  
    
def books():
    
    Books = [your_list[i][0] for i in range(len(your_list))]
    Genre = [ 'nonfiction', 'data_science', 'science', 'mathematics', 'comic', 'signal_processing',  'economics', 'history', 'fiction', 'philosophy', 'computer_science', 'psychology']    
    ListOfBooks = []
    for i in range(len(your_list)):
    
        indB = np.random.randint(0, len(Books))
        ID_Author = np.random.randint(0, len(Author_Table))
        indP = np.random.randint(0, len(Publish()))
        indG = np.random.randint(0, len(Genre))
        tmp = Publish()
        ListOfBooks.append([i, Books[indB], Genre[indG], ID_Author, tmp[indP][0],  np.random.randint(1918, 2018), format(np.random.uniform(5,95), '.2f')])
    
    myset = set(tuple(x) for x in ListOfBooks)
    ListOfBooks =sorted([list(x) for x in myset]) 
    return(ListOfBooks)
    
Books_Table = books()

print((Books_Table))

def phone():
    n = str(random.randint(11000000000, 89000000000))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

def clients():
    with open('Names.csv', "r") as f:
        reader = csv.reader(f)
        Names = list(reader)
        
    name = []  
    
    for i in range(0,200):
        name.append([i, Names[i][1], Names[i][2], phone()])
        
    myset = set(tuple(x) for x in name)
    name = sorted(([list(x) for x in myset])) 
    return(name)
    
Clients_Table = clients()
#print((Clients_Table))

def OrderedBooks(): 
    OrderBooks = []
    bks = books()
    BookID = [bks[x][0] for x in range(len(Books_Table))]
    Price = []
    for i in range(200):
        
        coin = np.random.sample()
        
        if coin <= 0.7:
            a = (1,4)
        else:
            a = (5,10)
            
        a = np.random.randint(*a)
    
        listbook = [BookID[np.random.randint(len(Books_Table))] for i in range(a)]
        cost = 0
        for x in range(a):
            OrderBooks.append([int(str(listbook[x])+str(i)+str(a)),i, listbook[x]])
            cost += float(Books_Table[listbook[x]][6])
        Price.append([i, format(cost, '.2f')])
        
    myset = set(tuple(x) for x in OrderBooks)
    OrderBooks =sorted([list(x) for x in myset])         
    return(OrderBooks, Price)       

OrderedBooks_Table, Prices = OrderedBooks()

#print(OrderedBooks_Table)


def Orders():
    ClientID = random.sample(range(len(Clients_Table)), len(Clients_Table))
    OrderID = list(set([OrderedBooks_Table[x][1] for x in range(len(OrderedBooks_Table))]))
    Order = []
    for i in range(len(OrderID)):
        Order.append([OrderID[i], ClientID[i], float(Prices[i][1])])
        
    return(Order)

Order_Table = Orders()    
    
#print((Orders()))    
    
        
    

