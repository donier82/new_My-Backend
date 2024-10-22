# Dict задачи:

# 1. **Создание словаря:** Создайте словарь, представляющий информацию о вас, включая имя, возраст и любимый цвет.
# my_info={"name":"Donier","age":42,"color":"green"}
# print(my_info["color"])

# 2. **Добавление элемента:** Добавьте в предыдущий словарь информацию о вашем любимом хобби.
# my_info={"name":"Donier","age":42,"color":"green"}
# my_info["hobby"]="voleyball"
# print(my_info["hobby"])

# 3. **Извлечение значения:** Извлеките возраст из словаря, созданного в первой задаче, и выведите его.
# my_info={"name":"Donier","age":42,"color":"green"}
# print(my_info['age'])

# 4. **Обновление значения:** Измените значение вашего любимого цвета в словаре на новый цвет.
# my_info={"name":"Donier","age":42,"color":"green"}
# my_info["color"]="orange"
# print(my_info["color"])

# 5. **Удаление элемента:** Удалите информацию о вашем любимом хобби из словаря.
# my_info={"name":"Donier","age":42,"color":"green","hobby":"voleyball"}
# del my_info["hobby"]
# print(my_info)

# Set:
# Уникальные элементы:
# Создайте функцию, которая принимает список и возвращает множество уникальных элементов из этого списка.
# numbers = [1, 2, 2, 3, 3, 4, 5]
# def any_num(numbers):
#     my_list= []
#     my_num = set(numbers)

#     for number in my_num:
#         my_list.append(number)

#     return  my_list

# print(any_num(numbers))

# Объединение множеств:
# Напишите программу, которая объединяет два множества и выводит результат.
# my_set1 = {"Nurgeldi", "Bekbolot", "Ainura"}
# my_set2 = {"Gulzina", "Arsen", "Temur"}
 
# result_set = my_set1.union(my_set2)
# print(result_set)   

# Пересечение множеств:
# Напишите функцию, которая находит и возвращает пересечение двух множеств.
# my_set1 = {"Nurgeldi", "Bekbolot", "Ainura","Gulzina"}
# my_set2 = {"Gulzina", "Arsen","Nurgeldi", "Temur"}
# result_set=my_set1.intersection(my_set2)
# print(result_set)

# Удаление дубликатов из списка:
# Создайте функцию, которая принимает список и возвращает новый список без повторяющихся элементов, используя множество.
# my_list= ["Ош","Бишкек","Ош","Чуй","Лондон","Москва","Дубай","Феррари","Ауди","Мерседес","Жентра","Нексия","Ноокат","Араван","Ниссан","Тойота"]
# def get_set(my_list):
#     my_set=set(my_list)
#     return my_set
# print(get_set(my_list))
    
# Проверка подмножества:
# Напишите функцию, которая проверяет, является ли одно множество подмножеством другого.
# a = {1,2}
# b = {1,2,3}
# isTrue=a.issubset(b) 
# print(isTrue)
  
# Frozenset:
# Создание frozenset:
# Создайте frozenset из списка чисел и попробуйте изменить его (вставить новый элемент), чтобы увидеть, что это неизменяемый объект.
# my_frozenset=frozenset({"3,7,5,8,1,9"})
# #my_frozenset["12"]
# try:
#     my_frozenset[12]
# except:
#     print('здесь не работает никаких изменение !')
# print(my_frozenset)
# Пересечение frozenset:

# Напишите функцию, которая находит и возвращает пересечение двух frozenset.
# my_frset1 = frozenset({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"})
# my_frset2 = frozenset({"Gulzina", "Arsen","Temur"})
# result_frset=my_frset1.intersection(my_frset2)
# print(result_frset)

# Сравнение frozenset:
# Напишите программу, которая сравнивает два frozenset и выводит результат.
# my_frset1 = frozenset({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"})
# my_frset2 = frozenset({"Gulzina", "Arsen","Temur"})
# try: 
#     my_frset1==my_frset2
#     print('true')
# except:
#     print('False')

# Преобразование frozenset в список:
# Создайте frozenset и преобразуйте его в список.
# my_frset= frozenset({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"})
# my_list=list(my_frset)
# print(my_list)

# Сложение frozenset:
# Напишите программу, которая создает новый frozenset, добавляя элементы из двух существующих frozenset.
# my_frset1 = frozenset({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"})
# my_frset2 = frozenset({"Gulzina", "Arsen","Temur"})
# my_frset3=my_frset1.union(my_frset2)
# print(my_frset3) 

# ДОП задание


# Индекс в списке:

# 	Создайте список и запросите у пользователя индекс элемента, который он хочет получить. Обработайте исключение, которое может возникнуть при вводе индекса, выходящего за пределы списка.
# my_list= ["Ош","Бишкек","Чуй","Лондон","Москва","Дубай","Феррари","Ауди","Мерседес","Жентра","Нексия","Ноокат","Араван","Ниссан","Тойота"]
# try:
#     user=int(input('введите желаемое индекс списка :'))
#     num=my_list[user]
#     print(num)
# except:
#     print('такого индекса нету!')

# Конвертация строки в число:
# Запросите у пользователя ввод строки, которую вы затем попробуете преобразовать в целое число. Обработайте исключение, которое может возникнуть, если введенная строка не может быть корректно преобразована в число.
# try:
#     verb=input('введите строка :')
#     my_num=int(verb)
#     print(my_num)
# except:
#     print('не преобразовать строку в число!')

# Работа с словарем:
# Создайте словарь и запросите у пользователя ключ, по которому вы попытаетесь получить значение из словаря. Обработайте исключение, которое может возникнуть, если введенного ключа нет в словаре.
# my_info={"name":"Donier","age":42,"color":"green"}
# try:
#     key=input('введите ключ :')
#     user=my_info[key]
#     print(user)
# except:
#     print('в словаре такого кляч не существует :')


