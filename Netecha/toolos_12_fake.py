import numpy as np
import datetime as dt
import time
#import random
#print(np.random.rand())



np.random.seed(123)
namesM = ['Илья', 'Константин', 'Александр', 'Алексей', 'Дмитрий']
namesF = ['Юлия', 'Анастасия', 'Екатерина', 'Ирина', 'Мария']
surnameM = ['Резерфорд', 'Вакариан', 'Шепард', 'Старк', 'Миллер']
surnameF = ['Мостовая', 'Петрова', 'Созонова', 'Самохина', 'Легкая']
secnameM = ['Александрович', 'Прокопьевич', 'Константинович', 'Владимирович', 'Алексеевич']
secnameF = ['Олеговна', 'Андреевна', 'Константиновна', 'Вячеславовна', 'Артемовна']


i = 0
listUser = []
for i in range(5):
    coin = np.random.sample()
    if coin > 0.5:
        indN = np.random.randint(0, len(namesM))
        indS = np.random.randint(0, len(surnameM))
        indSE = np.random.randint(0, len(secnameM))
        listUser.append([i+100000, surnameM[indS], namesM[indN], secnameM[indSE]])
nameFirms = ['Фитофрут', 'Агролэнд', 'Кладовая солнца', 'Сады Придонья',  'Натуральные сладости']
fruits = ['апельсин', 'ананас', 'банан']
country = ['Китай', 'Индия', 'Бразилия']
price = [50, 80, 40]

def User():
    listUser = []
    for i in range(5):
        coin = np.random.sample()
        if coin > 0.5:
            indN = np.random.randint(0, len(namesM))
            indS = np.random.randint(0, len(surnameM))
            listUser.append([i+100000, surnameM[indS], namesM[indN]])

        else:         
            indN = np.random.randint(0, len(namesF))
            indS = np.random.randint(0, len(surnameF))
            indSE = np.random.randint(0, len(surnameF))
            listUser.append([i+100000, surnameF[indS], namesF[indN], secnameF[indSE]])

    myset1 = set(tuple(x) for x in listUser)
    listUser =[list(x) for x in myset1]
    #print(listUser)  
    myset1 = set(tuple(x) for x in listUser)
    listUser = sorted([list(x) for x in myset1])
    for i in range(0, len(listUser)):
        listUser[i].append(i)
        return(listUser)

fruits = ['апельсин', 'ананас', 'банан']
price = [50, 80, 40]
listFruit = []
for i in range(3):
    listFruit.append([i+1, fruits[i], price[i]])
#print(listFruit)  
User_Table = User()

country = ['Китай', 'Индия', 'Бразилия']
listCountry = []
for i in range(3):
    listCountry.append([i+300, country[i]])
#print(listCountry) 

nameFirms = ['Фитофрут', 'Агролэнд', 'Кладовая солнца', 'Сады Придонья',  'Натуральные сладости']
listFirms = []
for i in range(5):
    listFirms.append([i+990, nameFirms[i]])
#print(listFirms) 


listTransactions = []
IDfruit = [1, 2, 3]
IDuser = [100000, 100001, 100002, 100003, 100004]
IDTrans = 0
number = 0
t2 = 0
for i in range(10):
    t2 += np.random.uniform(2222.0, 11111.9)
    T = dt.datetime.fromtimestamp(time.time()+t2)
    DATE = T.strftime("%d.%m.%Y %H:%M")
    USER = np.random.randint(0, len(IDuser))
    number += 1
    for a in range(3):
        quantity = np.random.randint(0,5)
        if (quantity > 0):
            listTransactions.append([IDTrans, number, DATE, IDfruit[a], IDuser[USER], price[a]*quantity, quantity])
            IDTrans+=1
def Fruit():
    listFruit = []
    for i in range(3):
        listFruit.append([i+1, fruits[i], price[i]])
    return(listFruit)

Fruit_Table = Fruit()


def Country():
    listCountry = []
    for i in range(3):
        listCountry.append([i+300, country[i]])
    return(listCountry)

Country_Table = Country()


def Firm():
    listFirms = []
    for i in range(5):
        listFirms.append([i+990, nameFirms[i]])
    return(listFirms)

Firms_Table = Firm() 

def staff():
    listStaff = []
    Staff = ['Уборщица','Водитель','Бухгалтер','Продавец']
    for i in range(10):
        indN = np.random.randint(0, len(namesF))
        indS = np.random.randint(0, len(surnameF))
        if(i < 2):
            listStaff.append([i+500, surnameF[indS], namesF[indN], Staff[0]])
        if(i >= 2 and i <= 4):
            indN = np.random.randint(0, len(namesM))
            indS = np.random.randint(0, len(surnameM))
            listStaff.append([i+600, surnameM[indS], namesM[indN], Staff[1]])
        if(i == 5):
            listStaff.append([i+700, surnameF[indS], namesF[indN], Staff[2]])
        if(i > 5):
            listStaff.append([i+800, surnameF[indS], namesF[indN], Staff[3]])
    return(listStaff)
Staff_table = staff()

def transport():
    listTransport = []
    Transport = ['Cтандартная Еврофура', 'JUMBO', 'MEGA']
    for i in range(3):
        listTransport.append([i+2990, Transport[i], i+602])
    return(listTransport)
transport_table = transport()

def Advertising():
    listAdvertising = []
    Advertising = ['Реклама в СМИ', 'Наружная', 'На местах продаж', 'В интеренете']
    for i in range(8):
        adverstising = np.random.randint(0,len(Advertising))
        IDFruits = np.random.randint(0,len(fruits))
        listAdvertising.append([i+100000, Advertising[adverstising], IDFruits+1])
    return(listAdvertising)
Advertising_table = Advertising()

print(listTransactions) 
def Transactions():
    listTransactions = []
    IDfruit = [1, 2, 3]
    IDuser = [100000, 100001, 100002, 100003, 100004]
    
    IDTrans = 0
    number = 0
    t2 = 0
    for i in range(10):
        t2 += np.random.uniform(2222.0, 11111.9)
        T = dt.datetime.fromtimestamp(time.time()+t2)
        DATE = T.strftime("%d.%m.%Y %H:%M")
        USER = np.random.randint(0, len(IDuser))
        number += 1
        for a in range(len(fruits)):
            quantity = np.random.randint(0,5)
            
            if (quantity > 0):
                listTransactions.append([IDTrans, number, DATE, IDfruit[a], IDuser[USER],  quantity])
                IDTrans+=1
    return(listTransactions)

Transactions_Table = Transactions()
    
