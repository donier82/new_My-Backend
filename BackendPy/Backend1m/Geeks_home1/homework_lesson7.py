# Задачи на lambda функции
# Фильтрация списка четных чисел: Напишите lambda функцию, которая принимает список чисел и возвращает список только четных чисел.
# users=[1,2,3,4,5,6,7,8,9]
# res= list(filter(lambda x: (x % 2 == 0), users))
# print(res)

# Возведение в квадрат: Напишите lambda функцию, которая принимает список чисел и возвращает список этих чисел, возведенных в квадрат.
# users=[1,2,3,4,5,6,7,8,9]
# info=list(map(lambda user: user*user,users))
# print(info)

# Сумма двух чисел: Напишите lambda функцию, которая принимает два числа и возвращает их сумму.
# my_lam=lambda a,b: a+b
# print(my_lam(2,6))

# Проверка на палиндром: Напишите lambda функцию, которая принимает строку и возвращает True, если строка является палиндромом, и False в противном случае.
# palindrom=lambda s: s==s[::-1] 
# print(palindrom('потоп'))

# Задачи на работу с модулями
# Создание модуля для работы с матрицами: Создайте модуль matrix.py с функциями для сложения, вычитания и умножения матриц.
# этот пример матрицы для всех операции
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# функциями для сложения
# for i in range(len(matrix1)): 
#          for j in range(len(matrix1[0])): 
#                   result[i][j] = matrix1[i][j] + matrix2[i][j] 
#print(result)

# функциями для вычитание
# for i in range(len(matrix1)): 
#          for j in range(len(matrix1[0])): 
#                   result[i][j] = matrix1[i][j] - matrix2[i][j] 
# print(result)

# функциями для умножение
# for i in range(len(matrix1)): 
#          for j in range(len(matrix1[0])): 
#                   result[i][j] = matrix1[i][j] * matrix2[i][j] 
# print(result)

# Создание модуля для математических операций: Создайте модуль math_operations.py с функциями для вычисления факториала, нахождения наибольшего общего делителя и наименьшего общего кратного.
# 1.Функцию для вычисления факториала.
# def Factorial(k):
#     n=0
#     sum=1
#     while n<k:
#         n+=1
#         sum=sum*n
#     print(sum)
# Factorial(5)

# 1.Функцию для нахождение НОД.
# import math
# def Gcd():
#     a=int(input('введите первое число :'))
#     b=int(input('введите второе число :'))
#     print(math.gcd(a,b))
# Gcd()

# 1.Функцию для нахождение НОК.
# def lcm(a, b):
#     m = a * b
#     while a != 0 and b != 0:
#         if a > b:
#             a %= b
#         else:
#             b %= a
#     return m // (a + b)
# while 1:
#     try:
#         x = int(input('a = '))
#         y = int(input('b = '))
#         print('НОК:', lcm(x, y))
#     except ValueError:
#         break

# Использование модуля random: Напишите скрипт, который использует модуль random для генерации случайного пароля
#  длиной 10 символов, состоящего из букв и цифр.
# from random import sample 
# symbols = 'ABCDabc123' 
# def generate_password(m):
#     return ''.join(sample(symbols,m)) 
# def main(m):
#     a = set()
#     a.add(generate_password(m))
#     return a
# print(main(10))