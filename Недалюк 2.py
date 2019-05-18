import numpy as np
#np.random.seed(123)
#print(np.random.rand())
Textbooks1 = ['математика', 'физика', 'химия', 'биология', 'информатика']
Textbooks2 = ['микроэкономика', 'право', 'графы', 'база данных', 'физ-ра']
Class = ['6', '7', '8', '9', '10']
course = ['1', '2', '3', '4']

def one(Textbooks1,Class):
    
    lst = []
    for i in range(45):
        lst.append([np.random.choice(Textbooks1), np.random.choice(Class)])
    
    return lst

def two(Textbooks2,course,list2):
    list2.append(np.random.choice(Textbooks2))
    list2.append(np.random.choice(course))
    return list2


#for i in range(45):
#    if np.random.rand() < 0.5:
#        one(Textbooks1,Class,list1)
#    else:
#        two(Textbooks2,course,list2)
#        

list1 = one(Textbooks1, course)
print(list1)