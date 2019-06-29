import pandas as pd
import mysql.connector
from mysql.connector import Error

data=pd.read_csv("cars.csv", delimiter=";")


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

#for i in range(len(p)):
#    print(list(p.loc[i,:]))
    
def connect():
    """ Connect to MySQL database """
    try:
        
        
        conn = mysql.connector.connect(host='localhost',
                                      # database='Cars',
                                       user='root',
                                       password='root')
        
        if conn.is_connected() and conn.database == None:
            if  'Cars' != conn.database:
                conn.cursor().execute("CREATE DATABASE Cars")
            conn.database = 'Cars'
            
        if conn.is_connected():
            print(conn.database)
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
           # print(existing_tbls)
            if 'Hybrid' not in existing_tbls:
                mycursor.execute("CREATE TABLE Hybrid ( HybridID INT NOT NULL, HybridPR VARCHAR(25)," + 
                                                           "Battery_Capacity INT, PRIMARY KEY (HybridID));")
            
            if 'Driveline' not in existing_tbls:
                mycursor.execute("CREATE TABLE Driveline ( DrivelineID INT NOT NULL, DrivelineName VARCHAR(25), " + 
                                                        "Engine_Volume VARCHAR(25), PRIMARY KEY (DrivelineID));")
            
            if 'Make' not in existing_tbls:
                mycursor.execute("CREATE TABLE Make ( MakeID INT NOT NULL, MakeName VARCHAR(25), PRIMARY KEY (MakeID));")
          
            if 'FuelType' not in existing_tbls:
                mycursor.execute("CREATE TABLE FuelType ( FuelTypeID INT NOT NULL, FuelTypeName VARCHAR(25)," +
                                                         "Engine_Type VARCHAR(25), PRIMARY KEY (FuelTypeID));")
                
            if 'Models' not in existing_tbls:
                mycursor.execute("CREATE TABLE Models (ModelID INT NOT NULL, ModelName VARCHAR(55)," + 
                                                      "PRIMARY KEY(ModelID ),"+
                                                      "FOREIGN KEY(HybridID) REFERENCES Hybrid(HybridID)," +  
                                                      "FOREIGN KEY(DrivelineID) REFERENCES Driveline(DrivelineID)," +
                                                      "FOREIGN KEY(MakeID) REFERENCES Make(MakeID)," +
                                                      "FOREIGN KEY(FuelTypeID) REFERENCES FuelType(FuelTypeID))ENGINE=INNODB ;")
           
            
       
           
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            
            hyb=[]
            if "Hybrid" in existing_tbls:
                
                for i in range(len(p)):
                    hyb.append(p.loc[i,:])
                    

                for el in hyb:
                    sql = "INSERT INTO Hybrid ( HybridID, HybridPR, Battery_Capacity) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
                    
                mycursor.execute("SELECT * FROM Hybrid")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
            else:
                 mycursor.execute("SELECT * FROM Hybrid")
                 myresult = mycursor.fetchall()
                 
                 for x in myresult:
                     print(x)
                    
            drvl=[]        
            if "Driveline" in existing_tbls:
                
                for i in range(len(a)):
                    drvl.append(a.loc[i,:])
                

                for el in drvl:
                    sql = "INSERT INTO Driveline ( DrivelineID, DrivelineName, Engine_Volume) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
                    
                mycursor.execute("SELECT * FROM Driveline")
                myresult = mycursor.fetchall()
                for x in myresult:
                    
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Driveline")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
                    
            mak=[]           
            if "Make" in existing_tbls:
                
                for i in range(len(b)): 
                    mak.append(b.loc[i,:])
                
                for el in mak:
                    sql = "INSERT INTO Make ( MakeID, MakeName) VALUES (%s, %s, %s, %s)"
                    val = (el[0],el[1])
                    mycursor.execute(sql, val)
                    
                mycursor.execute("SELECT * FROM Make")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Make")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)     
            
            FT=[]
            if "FuelType" in existing_tbls:

               for i in range(len(p)):
                   FT.append(p.loc[i,:])
                   
               for el in FT:
                    sql = "INSERT INTO FuelType ( FuelTypeID, FuelTypeName, Engine_Type) VALUES (%s, %s, %s)"
                    val = (el[0],el[1], el[2])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM FuelType")
               myresult = mycursor.fetchall()
               for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM FuelType")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
                    
            model=[]        
            if "Models" in existing_tbls:
                
                for i in range(len(s)):
                    model.append(s.loc[i,:])

                for el in model:
                    sql = "INSERT INTO Books (ModelID, ModelName, HybridID, DrivelineID, MakeID, FuelTypeID)) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (el[0],el[1], el[2], el[3], el[4], el[5])
                    
                    mycursor.execute(sql, val)
                mycursor.execute("SELECT * FROM Models")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
            else:
                mycursor.execute("SELECT * FROM Models")
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)                      
                                        

 
    except Error as e:
        print(e)
 
    finally:
        conn.commit()
        conn.close()
 
 
if __name__ == '__main__':
    
    
    connect()
"""
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
print('ОБРАБОТАННОЕ МАССИВИЩЕ ИЗ-ЗА КОТОРОГО МОЙ НОУТ ЧУТЬ НЕ УМЕР') # отличный заголовок
print('------------')       
for row in prepared_data_for_db:       
    print(row)
"""