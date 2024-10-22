# Задачи на set и frozenset:

# 1. Напишите функцию, которая принимает два множества и возвращает новое множество, содержащее элементы, которые есть только в одном из них.
# def SetProg(users,users2):     
#     users3 = users.union(users2)
#     return users3   
# set_end=SetProg({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"},{"Gulzina", "Arsen","Temur"})
# print(set_end)

# 2. Создайте функцию, которая проверяет, является ли одно множество подмножеством другого.
# a = {1,2}
# b = {1,2,3}
# res=a.issubset(b) 
# print(res)

# 3. Напишите программу, которая объединяет два множества без повторяющихся элементов.
# def SetProg():  
#     users={"Nurgeldi", "Bekbolot", "Ainura","Gulzina"} 
#     users2=  {"Gulzina", "Arsen","Temur"}
#     users3 = users.union(users2)
#     print(users3)   
# SetProg()

# 4. Напишите функцию, которая принимает неопределенное количество множеств и возвращает их пересечение.
# def SetProg(fist_set,second_set):
#     res=fist_set.intersection(second_set)
#     print(res)
# SetProg({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"},{"Gulzina", "Arsen","Temur"})

# 5. Создайте программу, которая удаляет все дубликаты из списка и преобразует его в множество.
# def NoneDuble(name):
#     any=set(name)
#     print(any)
# NoneDuble([2,5,1,7,4,8,9,4,3,5,7,2])

# 6. Напишите функцию, которая проверяет, являются ли два множества дизъюнктивными (не имеют общих элементов).
# def SetProg():  
#     users={"Nurgeldi", "Bekbolot", "Ainura","Gulzina"} 
#     users2=  {"Gulzina", "Arsen","Temur"}
#     users3 = users.union(users2)
#     users=list(users)
#     num1=len(users)
#     users2=list(users2)
#     num2=len(users2)
#     users3=list(users3)
#     num3=len(users3)
#     us4=num1+num2
#     if num3==us4:
#         print('не имеет общих элементов')
#     else:
#         print('имеет общих элементов')  
# SetProg()

# 7. Создайте программу, которая находит симметрическую разность двух множеств.
# first={"Nurgeldi", "Bekbolot", "Ainura","Gulzina"}
# second={"Gulzina", "Arsen","Temur"}
# res=first.symmetric_difference(second)
# print(res)

# 8. Напишите функцию, которая принимает множество и возвращает список его элементов в отсортированном порядке.
# def SortList(any_set):
#     any_list=list(any_set)
#     any_list.sort()
#     print(any_list)
# SortList({"Nurgeldi", "Bekbolot", "Ainura","Gulzina"})

# 9. Напишите программу, которая проверяет, являются ли два множества равными.
# users= {"Arsen","Temur","Gulzina"}             #{"Nurgeldi", "Bekbolot", "Ainura","Gulzina"} 
# users2=  {"Gulzina", "Arsen","Temur"}
# if users==users2:
#     print('множества равны .')
# else:
#     print('множества не равны .')

# 10. Создайте функцию, которая принимает два множества и возвращает True, если первое множество является подмножеством второго, иначе False.
# def Prog(a,b):    
#     res=a.issubset(b) 
#     print(res)
# Prog({1,2,},{1,2,3})

# Задачи на функции:
# 1. Напишите функцию для вычисления факториала числа.
# def Factorial(k):
#     n=0
#     sum=1
#     while n<k:
#         n+=1
#         sum=sum*n
#     print(sum)
# Factorial(4)

# 2. Создайте функцию для нахождения наибольшего общего делителя (НОД) двух чисел.
# import math
# def Gcd():
#     a=int(input('введите первое число :'))
#     b=int(input('введите второе число :'))
#     print(math.gcd(a,b))
# Gcd()

# 3. Напишите программу, которая определяет, является ли число простым, используя функцию.
# def is_prime (n): 
#     if n <= 1: return False 
#     for i in range (2, int (n**0.5) + 1): 
#         if n % i == 0: return False 
#         return True
# print(is_prime(601))

# 4. Создайте функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа.
# def Number(nums):
#     new_nums=[]
#     for i in nums:
#         if i%2==0:
#             new_nums.append(i)
#     print(new_nums)
# Number([3,6,5,7,4,8,1])

# 5. Напишите функцию, которая принимает строку и возвращает ее в обратном порядке.
# def ReverseString(s):
#     return s[::-1]
# print(ReverseString('hello world'))

# Задачи на *args и **kwargs:
# 1. Напишите функцию, которая принимает неопределенное количество аргументов и возвращает их сумму.
# def ArgSum(*k):    
#     sum=0   
#     for i in k:      
#         sum=sum+i
#     return sum
# print(ArgSum(4,8,12,30))

# 2. Создайте функцию, которая принимает неопределенное количество именованных аргументов и выводит их в алфавитном порядке.
# def Sort(my_dict):
#     sorted_dict = dict(sorted(my_dict.items()))
#     print(sorted_dict)
# Sort({'b': 2, 'a': 1, 'c': 3})

# 3. Напишите программу, которая принимает неопределенное количество аргументов и возвращает их произведение.
# args={1,2,3,4,5}
# sum=1
# for arg in args:
#      sum=sum*arg
# print(sum)

# 4. Создайте функцию, которая принимает неопределенное количество именованных аргументов и возвращает словарь, где ключами будут названия аргументов, а значениями - их значения.
# def My_Dict(**kwargs):
#     print(kwargs)   
# My_Dict(name="Donier", age="42", study="Geeks",married="yes",bently="not yet")

# 5. Напишите программу, которая принимает неопределенное количество аргументов и возвращает список квадратов этих аргументов.
# args={1,2,3,4,5}
# my_list=[]
# sum=1
# for arg in args:
#      arg=arg*arg
#      my_list=my_list+[arg]
# print(my_list)

