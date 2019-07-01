
import csv
import random
import numpy as np

"------------------------------------------------------------------"
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
              
"------------------------------------------------------------------"


SQL = ["операторы_определения_данных", "операторы_манипуляции_данными", "операторы_определения_доступа_к_данным"]
Functions_SQL = ["Функции LOG и EXP", "Функция DATEDIFF", "Функция CONCAT", "Функции LAG и LEAD", "Функция EOMONTH","Функция DATEADD"]
Operator_SQL = ["Операторы PIVOT и UNPIVOT", "Оператор TRUNCATE TABLE", "Оператор CROSS APPLY", "Простой оператор SELECT", "Оператор PIVOT", "Оператор INSERT"]
n = [10, 20, 100, 200, 500]
sql_list = [];
new_sql = [];

secure_random = random.SystemRandom()
for i in range(10):
    new_sql.append(secure_random.choice(SQL))
    coin = np.random.sample()
    if (coin > 0.5):
        new_sql.append(secure_random.choice(Functions_SQL))
    else:
        new_sql.append(secure_random.choice(Operator_SQL))
    new_sql.append(secure_random.choice(n))
    sql_list.append(new_sql)
    new_sql = []

if __name__ == "__main__":
    data =[sql_list," \n "]
    
    path = "output.csv"
    csv_writer(data, path)

'''for i in range(len(sql_list) - 1):
    for j in range (i + 1, len(sql_list)):
        if (sql_list[i] == sql_list[j]):
            print(sql_list[i], sql_list[j], "ПОВТОРЕНИЕ!!!")
            del sql_list[j];
            
print(sql_list)'''

