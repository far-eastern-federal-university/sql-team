import pandas as pd

data=pd.read_csv("F:/cars.csv", delimiter=";")


hpd=set(data["Hybrid"])
         
d={}
counter = 0
for i in hpd:
    d[counter] = i
    counter+=1  

d=pd.DataFrame.from_dict(d, orient='index')
d=d.rename(columns = { 0:'Hybrid'})
BC = {0: 70, 1: 55}
d['Battery Capacity'] = pd.Series(BC)
print('------------')
print('Информация о топливной системе')
print('------------')
print(d)

drv=set(data["Driveline"])
        
a={}
counter = 0
for i in drv:
    a[counter] = i
    counter+=1
a=pd.DataFrame.from_dict(a, orient='index')
a=a.rename(columns = { 0:'Driveline'})
PT = {0: 1.8, 1: 3.0, 2: 2.0, 3: 2.5}
a['Engine Volume'] = pd.Series(PT)
print('------------')
print('Информация о приводе')
print('------------')

print(a)

    
mr=set(data["Make"])
b={}
counter = 0
for i in mr:
    b[counter] = i
    counter+=1 
b=pd.DataFrame.from_dict(b, orient='index')
b=b.rename(columns = { 0:'Make'})
print('------------')
print('Информация о марках')
print('------------')

print(b)
 
    
mr1=list(mr) + ['Aston', 'Motorrad', 'Group', 'LLC', 'Martin','Land','Rover','Grand', 'Cherokee']    
my=set(data["Model Year"])  
mdl=[]
for i in my:
    k=i.split(" ")
    mdl.append(k)
ka = []    
for x in mr1:
    for i in range(len(mdl)):
        if x in mdl[i]:
            mdl[i].remove(x)
           
for i in range(len(mdl)):
     for j in range(2,len(mdl[i])):
         mdl[i][1] += ' ' + mdl[i][j]
         ka.append(mdl[i][j])       
         
for x in ka:
    for i in range(len(mdl)):
        if x in mdl[i]:
            mdl[i].remove(x) 
            
klon=list.copy(mdl)
            
rub=['2008','2009','2010','2011','2012','2013','2014']
      
for x in rub:
    for i in range(len(klon)):
        if x in klon[i]:
            klon[i].remove(x) 
            
mdl_1=set()

for i in range(len(klon)):
     for j in range(len(klon[i])):
         mdl_1.add(klon[i][j])             
        
s={}
counter = 0
for i in mdl:
    s[counter] = i
    counter+=1 

s=pd.DataFrame.from_dict(s, orient='index')
s=s.rename(columns = { 0:'Year'})
s=s.rename(columns = { 1:'Model'})

gas=set(data["Fuel Type"])       

p={}
counter = 0
for i in gas:
    p[counter] = i
    counter+=1
p=pd.DataFrame.from_dict(p, orient='index')
p=p.rename(columns = { 0:'Fuel Type'})
ET = {0: 'GE', 1: 'PE', 2: 'FFV', 3: 'DE'}
p['Engine Type'] = pd.Series(ET)
print('------------')
print('Информация о топливе')
print('------------')

print(p)

prepared_data_for_db=[]


for model in mdl_1:
    for i in range(len(data)):
        if model in data['Model Year'][i]:
            idx_in_make = list(b['Make']).index(data['Make'][i])
            idx_in_hybrid = list(d['Hybrid']).index(data['Hybrid'][i])
            idx_in_driveline = list(a['Driveline']).index(data['Driveline'][i])
            idx_in_fueltype = list(p['Fuel Type']).index(data['Fuel Type'][i])
            prepared_data_for_db.append([model, idx_in_hybrid, idx_in_driveline, idx_in_fueltype, idx_in_make])
            break
 
print('------------')
print('ОБРАБОТАННОЕ МАССИВИЩЕ ИЗ-ЗА КОТОРОГО МОЙ НОУТ ЧУТЬ НЕ УМЕР')
print('------------')       
for row in prepared_data_for_db:       
    print(row)
