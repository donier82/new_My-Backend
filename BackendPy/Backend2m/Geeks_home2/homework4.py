# Домашняя работа №5
# Создать класс MagicCalculator с атрибутами number_1 и number_2, в котором будут реализованы магические методы
# для арифметических вычислений между аргументами класса  MagicCalculator ( +, -, *, /, // )

# class MagicCalculator:

#     def __init__(self,number_1,number_2):
#         self.number_1=number_1
#         self.number_2=number_2

#     def __str__(self):
#         return f'первое число {self.number_1}, второе число {self.number_2}'

#     def __add__(self, other):
#         return MagicCalculator(self.number_1+other.number_1, self.number_2+other.number_2)    

#     def __sub__(self, other):
#         return MagicCalculator(self.number_1-other.number_1, self.number_2-other.number_2)

#     def __mul__(self, other):
#         return MagicCalculator(self.number_1*other.number_1, self.number_2*other.number_2)

#     def __truediv__(self, other):
#         return MagicCalculator(self.number_1/other.number_1, self.number_2/other.number_2)

#     def __floordiv__(self, other):
#         return MagicCalculator(self.number_1//other.number_1, self.number_2//other.number_2)

# magic_1=MagicCalculator(50,100)
# magic_2=MagicCalculator(5,7)
# print(magic_1+magic_2)
# print(magic_1-magic_2)
# print(magic_1*magic_2)
# print(magic_1/magic_2)
# print(magic_1//magic_2)

# Доп задание:
#
# Вы разрабатываете программу для управления библиотекой книг. Вам необходимо создать класс Book, который будет
# представлять отдельную книгу. Книги могут иметь различные атрибуты, такие как название, автор, год издания и т. д.
# Кроме того, вы хотите, чтобы книги можно было сравнивать между собой на основе их года издания.
#
# Ваша задача - создать класс Book, который реализует методы для сравнения книг между собой по году издания,
# а также выводить информацию о книге в удобном формате.
#
# Условия:
# Реализуйте методы lt, le, gt, ge, eq, ne для сравнения книг между собой на основе года издания.
# Реализуйте метод str для вывода информации о книге в удобном формате.
# class Book:
#     def __init__(self,name,author,year):
#         self.name=name
#         self.author=author
#         self.year=year

#     def __eq__(self,other):
#         return Book(self.year==other.year)

   # def __str__(self):
   #    return f'название книг: {self.name}, автор книг: {self.author}, год издание: {self.year}'
    

       
    #self.number_1+other.number_1, self.number_2+other.number_2
c1=Book('dff','efs',1945)
c2=Book('asd','hdf',1950)
print(c1==c2)