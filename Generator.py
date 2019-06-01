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
print(len(series), len(set(series)))
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
#print(listOfPpl,'\n')     
myset = set(tuple(x) for x in listOfPpl)
listOfPpl =[list(x) for x in myset]
print(listOfPpl)  
