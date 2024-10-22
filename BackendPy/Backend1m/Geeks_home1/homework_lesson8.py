# 1. Чтение файла и вывод его содержимого:
#    Создайте программу, которая открывает текстовый файл и выводит его содержимое на экран.
# !!! сначала мы создаем info.txt
# file = open("info.txt",'w')  
# file.write('''any text first\nany text second\nany text third\nany text fours''')
# file=open("info.txt",'r')
# print(file.read())
# file.close()

# 2. Подсчет количества строк в файле:   Напишите программу, которая считает количество строк в текстовом файле и выводит это число.
# file = open("info.txt",'w')  
# file.write('''any text first\nany text second\nany text third\nany text fours''')
# file=open("info.txt",'r')
# col=file.readlines()
# stroka=len(col)
# print(stroka)
# file.close()

# 3. Поиск определенного слова в файле:   Создайте программу, которая открывает текстовый файл и проверяет, содержится ли в нем определенное слово. Если слово найдено, программа должна вывести сообщение об успешном поиске.
# file = open("info.txt",'w')  
# file.write('''any text first\nany text second\nany text third\nany text fours''')
# file=open('info.txt','r')
# some=file.read()
# word=input('введите слово : ')
# if word in some:
#     print('true')
# else:
#     print('false')

# 4. Запись в файл:   Попросите пользователя ввести некоторый текст и сохраните его в текстовом файле.
# file=open('info.txt','w')
# text=input('введите текст : ')
# file.write(f'{text}')

# 5. Копирование файла:
#    Напишите программу, которая копирует содержимое одного файла в другой файл.
# file = open("info.txt",'w')  
# file.write('''any text first\nany text second\nany text third\nany text fours''')
# with open('info.txt','r') as info, open('second.txt','w') as secondfile: 
#      for line in info:
#             secondfile.write(line) 
#             file.close()


# 6. Подсчет количества слов в файле:
#    Создайте программу, которая подсчитывает количество слов в текстовом файле и выводит это число.

# 7. Перезапись файла:
#    Напишите программу, которая открывает файл, перезаписывает его содержимое новым текстом и сохраняет изменения.



