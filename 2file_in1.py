#чтение 1 го файла и получение данных для записи в общий файл
failname1 = 'first.txt'
with open(failname1, encoding = 'utf-8') as file:
	first_lines = file.readlines()
	counting_rows1 = len(first_lines)
	first_lines.append(str(counting_rows1))
	first_lines.append(failname1)
	first_lines.reverse()

#чтение 2 го файла и получение данных для записи в общий файл	
failname2 = 'second.txt'
with open(failname2, encoding = 'utf-8') as file:
	second_lines = file.readlines()
	counting_rows2 = len(second_lines)
	second_lines.append(str(counting_rows2))
	second_lines.append(failname2)
	second_lines.reverse()

#запись данных в общтй файл	
if counting_rows2 < counting_rows1:
	with open('union.txt','w', encoding = 'utf-8') as file:
		#file.writelines(second_lines)
		#file.writelines(first_lines)
		for element in second_lines:
			file.write(element)
			file.write('\n')
		for element in first_lines:
			file.write(element)
			file.write('\n')
   
#проверка файла         
with open('union.txt', "r", encoding = 'utf-8') as file: 
	union_lines = file.readlines()
for line in union_lines:	
	print(line)