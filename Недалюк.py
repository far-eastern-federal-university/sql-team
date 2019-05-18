import numpy as np
#np.random.seed(123)
#print(np.random.rand())
Textbooks1 = ['математика', 'физика', 'химия', 'биология', 'информатика']
#Textbooks2 = ['микроэкономика', 'право', 'графы', 'база данных', 'физ-ра']
Class = ['6', '7', '8', '9', '10']
#course = ['1', '2', '3', '4']
n = 0
#while n <=45:
if np.random.rand() < 0.5: 
    a = np.random.uniform(0,5)
    b = np.random.uniform(0,5)
    print(Textbooks1,Class)
   # else:
       #print(Textbooks2,course)
        #a = np.random.uniform(0,4)
       # b = np.random.uniform(0,4)
    n+=1