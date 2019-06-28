import numpy as np
import pandas as pd

questions = pd.read_csv("list_of_questions.txt", delimiter='\n', header=0)
questions = list(questions['Список вопросов'])


print('-------------------')
print("Список вопропросов")
print('-------------------')
for i in range(len(questions)):
	questions[i] = questions[i][3:len(questions[i])]
	questions[i] = questions[i].replace('.', '')
	print(questions[i])

print('-------------------')
print("Выбранные числа")
print('-------------------')

try:	
	f = open("nums.txt", 'r')

	lst_nums = []
	for line in f:
		print(line)
		lst_nums.append(line.split(': ')[1][:-1])

	f.close()
except:
	lst_nums = []

print('-------------------')
print("Иллюзия выбора")
print('-------------------')

surname = input('Представьтесь, пожалуйста: ')

if len(lst_nums) > 0:
	print(lst_nums)
	a = input("Введите число, которого нет в списке: ")
else:
	a = input("Введите произвольное целое число: ")


while a in lst_nums:
	print('такое число уже есть')
	a = input("Введите число, которого нет в списке ")

f = open("nums.txt", 'a')

f.write(surname + ': ' + a + '\n')

f.close()

np.random.seed(int(a))	

qst = np.random.choice(questions)

print(qst)