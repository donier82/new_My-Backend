# Домашняя работа №2

# 1.	Создать класс Person с атрибутами fullname, age, is_married
# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married

# 2. Добавить в класс Person метод introduce_myself(представиться), который бы распечатывал всю информацию о человеке
# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married
#     def introduce_myself(self):
#         print(f'ФИО : {self.fullname} \nВозраст: {self.age}\nЖенатый(замужем): {self.is_married}')  
        

# Дониёр=Person('Эргашов Дониёр Холматович',42,True)
# Дониёр.introduce_myself()

#3.	Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом объекта experience.
# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married
#         def introduce_myself(self):
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married}') 
# class Teacher(Person):
#     def __init__(self,fullname,age,is_married,experience):  
#         super().__init__(fullname,age,is_married)
#         self.experience=experience
#     def introduce_myself(self):
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married} \nОпыт работы: {self.experience}') 
# Дониёр=Teacher('Эргашов Дониёр Холматович',42,True,'три года')
# Дониёр.introduce_myself()

# Доп. Задание:

# 1. Добавить в класс Teacher атрибут класса salary = 0
# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married
#         def introduce_myself(self):
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married}') 

# class Teacher(Person):    
#     def __init__(self,fullname,age,is_married,experience,salary): 
#         super().__init__(fullname,age,is_married)
#         self.experience=experience
#         self.salary=salary
#     def introduce_myself(self):
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married} \nОпыт работы: {self.experience} \nЗарплата: {self.salary}') 
# Дониёр=Teacher('Эргашов Дониёр Холматович',42,True,'три года',100)
# Дониёр.introduce_myself()


# 2. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждые три года опыта.
# 3. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

# class Person:
#     def __init__(self,fullname,age,is_married):
#         self.fullname=fullname
#         self.age=age
#         self.is_married=is_married
#         def introduce_myself(self):
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married}') 

# class Teacher(Person):    
#     def __init__(self,fullname,age,is_married,experience,salary): 
#         super().__init__(fullname,age,is_married)
#         self.experience=experience
#         self.salary=salary
#         self.salary=self.salary+self.experience//3*3000
#     def introduce_myself(self):
          
#             print(f'ФИО : {self.fullname} \nВозраст: {self.age} \nЖенатый(замужем): {self.is_married} \nОпыт работы: {self.experience} \nЗарплата: {self.salary}') 
# Дониёр=Teacher('Эргашов Дониёр Холматович',42,True,12,100)
# Дониёр.introduce_myself()


