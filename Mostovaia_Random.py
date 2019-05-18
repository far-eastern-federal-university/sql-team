# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import numpy as np
import itertools
#print(np.random.rand())
#np.random.seed(123)
namesM = ['Илья', 'Константин', 'Евгений', 'Алексей', 'Олег']
namesF = ['Юлия', 'Александра', 'Екатерина', 'Елена', 'Мария']
surnameM = ['Петров', 'Алексеев', 'Единорогов', 'Кеков', 'Горбатов']
surnameF = ['Мостовая', 'Петрова', 'Мышкова', 'Самохина', 'Курочкина']
listOfPpl = []


i = 0
for i in range(25):
    coin = np.random.sample()
    if coin > 0.5:
        indN = np.random.randint(0, len(namesM))
        indS = np.random.randint(0, len(surnameM))
        listOfPpl.append([namesM[indN], surnameM[indS]])
            
    else:         
        indN = np.random.randint(0, len(namesF))
        indS = np.random.randint(0, len(surnameF))
        listOfPpl.append([namesF[indN], surnameF[indS]])
print(listOfPpl,'\n')     
myset = set(tuple(x) for x in listOfPpl)
listOfPpl =[list(x) for x in myset]
print(listOfPpl   
