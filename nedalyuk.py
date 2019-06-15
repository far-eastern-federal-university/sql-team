import numpy as np
import random
#print(np.random.rand())
np.random.seed(123)
namesM = ['Илья', 'Константин', 'Александр', 'Алексей', 'Дмитрий']
namesF = ['Юлия', 'Анастасия', 'Екатерина', 'Ирина', 'Мария']
surnameM = ['Резерфорд', 'Вакариан', 'Шепард', 'Старк', 'Миллер']
surnameF = ['Мостовая', 'Петрова', 'Созонова', 'Самохина', 'Легкая']
secnameM = ['Александрович', 'Прокопьевич', 'Константинович', 'Владимирович', 'Алексеевич']
secnameF = ['Олеговна', 'Андреевна', 'Константиновна', 'Вячеславовна', 'Артемовна']
series = random.sample(range(1000,8900), 1000) 
listOfPpl = []



i = 0
for i in range(25):
    coin = np.random.sample()
    if coin > 0.5:
        indN = np.random.randint(0, len(namesM))
        indS = np.random.randint(0, len(surnameM))
        indSE = np.random.randint(0, len(secnameM))
        indSER = np.random.randint(0, len(series))
        listOfPpl.append([series[indSER], surnameM[indS], namesM[indN], secnameM[indSE]])
            
    else:         
        indN = np.random.randint(0, len(namesF))
        indS = np.random.randint(0, len(surnameF))
        indSE = np.random.randint(0, len(surnameF))
        indSER = np.random.randint(0, len(series))
        listOfPpl.append([series[indSER], surnameF[indS], namesF[indN], secnameF[indSE]])
  
myset1 = set(tuple(x) for x in listOfPpl)
listOfPpl =[list(x) for x in myset1]
print(listOfPpl)  

fruits = ['апельсин', 'ананас', 'банан', 'яблоко', 'авокадо']
listFruit = []
for i in range(5):
    listFruit.append([i, fruits[i]])
print(listFruit)  

country = ['Китай', 'Индия', 'Бразилия', 'США', 'Индонезия', 'Россия', 'Египет', 'Франция', 'Бразилия','Эквадор']
listCountry = []
for i in range(10):
    listCountry.append([i, country[i]])
print(listCountry) 

nameFirms = ['Фитофрут', 'Агролэнд', 'Банкет Сервис', 'Кладовая солнца', 'Агро-ФТ', 'Сады Придонья', 'Лесничка', 'Ravema fruct', 'Натуральные сладости', 'Трейд Сервис']
price = [100, 110, 120, 130, 140]
listFirms = []
for i in range(25):
    Firms = np.random.randint(0, len(nameFirms))
    Price = np.random.randint(0, len(price))
    Fruits = np.random.randint(0, len(fruits))
    listFirms.append([i, nameFirms[Firms], fruits[Fruits],price[Price]])
myset2 = set(tuple(x) for x in listFirms)
listFirms =[list(x) for x in myset2]
print(listFirms) 

listTransactions = []
for i in range(25):
    a = np.random.randint(1,5)
    FRUIT = []
    p = 0
    for i in range(a):
        Fruit = np.random.randint(0, len(fruits))
        FRUIT.append(fruits[Fruit])
        Price = np.random.randint(0, len(price))
        p += price[Price]
    listTransactions.append ([FRUIT, p])

print(listTransactions)