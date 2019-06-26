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
            
    else:         
        indN = np.random.randint(0, len(namesF))
        indS = np.random.randint(0, len(surnameF))
        indSE = np.random.randint(0, len(surnameF))
        listUser.append([i+100000, surnameF[indS], namesF[indN], secnameF[indSE]])
  
myset1 = set(tuple(x) for x in listUser)
listUser =[list(x) for x in myset1]
#print(listUser)  

fruits = ['апельсин', 'ананас', 'банан']
price = [50, 80, 40]
listFruit = []
for i in range(3):
    listFruit.append([i+1, fruits[i], price[i]])
#print(listFruit)  

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
t2 = 0
for i in range(10):
    t2 += np.random.uniform(2222.0, 11111.9)
    T = dt.datetime.fromtimestamp(time.time()+t2)
    DATE = T.strftime("%d.%m.%Y %H:%M")
    USER = np.random.randint(0, len(IDuser))
    IDTrans+=1
    for a in range(3):
        quantity = np.random.randint(0,5)
        if (quantity > 0):
            listTransactions.append([IDTrans, DATE, IDfruit[a], IDuser[USER], price[a]*quantity, quantity])

    
print(listTransactions)