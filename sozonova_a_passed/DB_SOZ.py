import pandas as pd
import mysql.connector
from mysql.connector import Error
import sys

data=pd.read_csv("cars.csv", delimiter=";")


hpd=set(data["Hybrid"])
         
d={}
counter = 1
for i in hpd:
    d[counter] = i
    counter+=1  

d=pd.DataFrame.from_dict(d, orient='index')
d=d.rename(columns = { 0:'Hybrid'})
BC = {1: 70, 2: 55}
d['Battery Capacity'] = pd.Series(BC)
print('------------')
print('Информация о топливной системе')
print('------------')
print(d)


drv=set(data["Driveline"])
        
a={}
counter = 1
for i in drv:
    a[counter] = i
    counter+=1
a=pd.DataFrame.from_dict(a, orient='index')
a=a.rename(columns = { 0:'Driveline'})
PT = {1: 1.8, 2: 3.0, 3: 2.0, 4: 2.5}
a['Engine Volume'] = pd.Series(PT)
print('------------')
print('Информация о приводе')
print('------------')

print(a)

    
mr=set(data["Make"])
b={}
counter = 1
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
counter = 1
for i in mdl:
    s[counter] = i
    counter+=1 

s=pd.DataFrame.from_dict(s, orient='index')
s=s.rename(columns = { 0:'Year'})
s=s.rename(columns = { 1:'Model'})

gas=set(data["Fuel Type"])       

p={}
counter = 1
for i in gas:
    p[counter] = i
    counter+=1
    
p=pd.DataFrame.from_dict(p, orient='index')
p=p.rename(columns = {0: 'Fuel Type'})

print(p)

ET = {1: 'GE', 2: 'PE', 3: 'FFV', 4: 'DE'}
p['Engine Type'] = pd.Series(ET)
print('------------')
print('Информация о топливе')
print('------------')

print(p)
#sys.exit()
#for i in range(len(p)):
#    print(list(p.loc[i,:]))


prepared_data_for_db=[]

for model in mdl_1:
    for i in range(len(data)):
        if model in data['Model Year'][i]:
            idx_in_make = list(b['Make']).index(data['Make'][i])
            idx_in_hybrid = list(d['Hybrid']).index(data['Hybrid'][i])
            idx_in_driveline = list(a['Driveline']).index(data['Driveline'][i])
            idx_in_fueltype = list(p['Fuel Type']).index(data['Fuel Type'][i])
            prepared_data_for_db.append([model, idx_in_hybrid + 1, idx_in_driveline+1, 
                                         idx_in_fueltype+1, idx_in_make+1])
            break
 
print('------------')
print('ОБРАБОТАННОЕ МАССИВИЩЕ ИЗ-ЗА КОТОРОГО МОЙ НОУТ ЧУТЬ НЕ УМЕР') # отличный заголовок
print('------------')       
for row in prepared_data_for_db:       
    print(row)

    
def connect(hyb, make, fuel, drive, models):
    """ Connect to MySQL database """
    try:
        
        
        conn = mysql.connector.connect(host='localhost',
                                      # database='cars',
                                       user='root',
                                       password='zhil,p@ss')
        try:    
            conn.cursor().execute("DROP DATABASE cars")
            conn.cursor().execute("CREATE DATABASE cars")
            conn.database = 'cars'
        except:
            conn.cursor().execute("CREATE DATABASE cars")
            conn.database = 'cars'
            
#        if conn.is_connected() and conn.database == None:
#            if  'Cars' != conn.database:
#                conn.cursor().execute("CREATE DATABASE Cars")
#            conn.database = 'Cars'
            
        if conn.is_connected():
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
           # print(existing_tbls)
            if 'hybrid' not in existing_tbls:
                mycursor.execute("CREATE TABLE hybrid ( HybridID INT NOT NULL AUTO_INCREMENT, HybridPR INT, " + 
                                                       "Battery_Capacity INT, PRIMARY KEY (HybridID));")
            
            if 'driveline' not in existing_tbls:
                mycursor.execute("CREATE TABLE Driveline ( DrivelineID INT NOT NULL AUTO_INCREMENT, DrivelineName VARCHAR(25), " + 
                                                        "Engine_Volume VARCHAR(25), PRIMARY KEY (DrivelineID));")
            
            if 'make' not in existing_tbls:
                mycursor.execute("CREATE TABLE Make ( MakeID INT NOT NULL AUTO_INCREMENT, MakeName VARCHAR(25), PRIMARY KEY (MakeID));")
          
            if 'fueltype' not in existing_tbls:
                mycursor.execute("CREATE TABLE FuelType ( FuelTypeID INT NOT NULL AUTO_INCREMENT, FuelTypeName VARCHAR(25)," +
                                                         "Engine_Type VARCHAR(25), PRIMARY KEY (FuelTypeID));")
                
            if 'models' not in existing_tbls:
                mycursor.execute("CREATE TABLE Models (ModelID INT NOT NULL AUTO_INCREMENT, ModelName VARCHAR(255), HybridID INT NOT NULL, " +
                                                      "DrivelineID INT NOT NULL, MakeID INT NOT NULL, FuelTypeID INT NOT NULL, " + 
                                                      "PRIMARY KEY(ModelID ), " +
                                                      "FOREIGN KEY(HybridID) REFERENCES Hybrid(HybridID), " +  
                                                      "FOREIGN KEY(DrivelineID) REFERENCES Driveline(DrivelineID), " +
                                                      "FOREIGN KEY(MakeID) REFERENCES Make(MakeID), " +
                                                      "FOREIGN KEY(FuelTypeID) REFERENCES FuelType(FuelTypeID)) ENGINE=INNODB ;")
           
            
            hyb = hyb.replace({False : 0, True : 1})
            #hyb['idx'] = range(1, len(hyb)+1)
            print(hyb)
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)
            
            if "hybrid" in existing_tbls:
                
                print('val')
#                for i in range(len(hyb)):
#                    prox = list(hyb.loc[i, :])
#                    val = (prox[2], str(prox[0]), prox[1])
#                    print(val)
                
                for i in range(1, len(hyb) + 1):
                    prox = list(hyb.loc[i, :])
                    print(prox)
                    sql = "INSERT INTO hybrid (HybridPR, Battery_Capacity) VALUES (%s, %s)"
                    val = (prox[0], prox[1])
                    print(val)
                    mycursor.execute(sql, val)
                    
                mycursor.execute("SELECT * FROM hybrid")
                myresult = mycursor.fetchall()
                
                print('cursor_x')
                for x in myresult:
                    print(x)
            else:
                 mycursor.execute("SELECT * FROM Hybrid")
                 myresult = mycursor.fetchall()
                 
                 for x in myresult:
                     print(x)
                    
            drvl=[]        
            if "driveline" in existing_tbls:
                
                for i in range(1,len(drive)+1):
                    drvl.append(list(drive.loc[i,:]))
                

                print(drvl)
                
                for el in drvl:
                    sql = "INSERT INTO Driveline (DrivelineName, Engine_Volume) VALUES (%s, %s)"
                    val = (el[0],el[1])
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
#                    
            mak=[]           
            if "make" in existing_tbls:
                
                for i in range(1,len(make)+1): 
                    mak.append(list(make.loc[i,:]))
                print(mak)
                for el in mak:
                    sql = "INSERT INTO Make (MakeName) VALUES (%s)"
                    val = (el[0],)
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
            if "fueltype" in existing_tbls:
                print(fuel)
                for i in range(1,len(fuel)+1):
                    FT.append(list(fuel.loc[i,:]))
               
                print(FT)
               
                for el in FT:
                    sql = "INSERT INTO FuelType (FuelTypeName, Engine_Type) VALUES (%s, %s)"
                    val = (el[0],el[1],)
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
                      
            if "models" in existing_tbls:
                
#                for i in range(len(models)):
#                    model.append(list(models.loc[i,:]))
                print(models)
                for el in models:
                    sql = "INSERT INTO Models ( ModelName, HybridID, DrivelineID, FuelTypeID, MakeID) VALUES (%s, %s, %s, %s, %s)"
                    val = (el[0], el[1], el[2], el[3], el[4],)
                    print(val)
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
    
    
    connect(hyb=d, make=b, fuel=p, drive=a, models=prepared_data_for_db)
