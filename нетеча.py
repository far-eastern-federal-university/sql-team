import numpy as np

#print(np.random.rand())
#np.random.seed(123)
illenes=['Анемия','Гепатит','Депрессия','Корь','Грипп']
docNamesF=['Елена','Александра','Юлия','Алина','Дарья']
docNamesM=['Андрей','Олег','Николай']
docSurnamesF=['Неежко','Недалюк','Прусс','Ананко','Артемьева']
docSurnamesM=['Абрамов','Белов','Вдовкин']
for a in range(25):
    a=[(i,np.random.choice(docSurnamesF)) for i in docNamesF]
    print(a)




