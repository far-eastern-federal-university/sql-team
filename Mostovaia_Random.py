# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import numpy as np
#print(np.random.rand())
#np.random.seed(123)
namesM = ['Илья', 'Константин', 'Евгений', 'Алексей', 'Олег']
namesF = ['Юлия', 'Александра', 'Екатерина', 'Елена', 'Мария']
surnameM = ['Петров', 'Алексеев', 'Единорогов', 'Кеков', 'Горбатов']
surnameF = ['Мостовая', 'Петрова', 'Мышкова', 'Самохина', 'Курочкина']
listOfPpl = [[] for i in range(len(namesM)*4)]

coin = np.random.sample()
i = 0
while i < len(namesM)*4:
    if coin > 0.5 :
        listOfPpl[i].append(namesM[np.random.randint(0, len(namesM))])
        listOfPpl[i].append(surnameM[np.random.randint(0, len(surnameM))])
        i += 1
    else:
        listOfPpl[i].append(namesF[np.random.randint(0, len(namesF))])
        listOfPpl[i].append(surnameF[np.random.randint(0, len(surnameF))])    
        i += 1
print(listOfPpl)    