# Домашняя работа №3

# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory

#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @property
#     def memory(self):
#         return self.__memory 



# 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory
 

#     def __make_computations(self):
#         add=self.__cpu+self.__memory
#         sub=self.__cpu-self.__memory
#         mult=self.__cpu*self.__memory
#         div=self.__cpu/self.__memory
#         print(f'результаты: сложение {add}, вычитание {sub}, умножение {mult}, деление {div}')

#     def info(self):
#         self.__make_computations()

# computer=Computer(10,5)
# computer.info()

# 3. Добавить геттеры к существующим атрибутам.
# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory

#     def get_cpu(self):
#         return print(self.__cpu)
     
#     def get_memory(self):
#         return print(self.__memory)
# computer=Computer(50,100)
# computer.get_cpu()
# computer.get_memory()
 
# 4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
   
# class Laptop(Computer):
#     def __init__(self, cpu, memory,memory_card):
#         super().__init__(cpu, memory)
#         self.__memory_card=memory_card   

#     @property
#     def memory_card(self):
#         return self.__memory_card

# 5. Добавить геттеры к существующему атрибуту.
#     def get_info(self):
#         return print(f'cpu equals: {self.cpu}, memory equals: {self.memory}, memory card equals: {self.memory_card}')
   
# 6. Распечатать информацию о созданных объектах с помощью метода info
# laptop=Laptop(30,50,100)
# laptop.info()

# 7. Опробовать все возможные методы каждого объекта
# class PublicComputer:
#     def __init__(self,cpu,memory,memory_card):
#         self.cpu=cpu
#         self.memory=memory
#         self.memory_card=memory_card

# class SecurityComputer:
#     def __init__(self,cpu,memory,memory_card):
#         self._cpu=cpu
#         self._memory=memory
#         self._memory_card=memory_card

# class PrivateComputer:
#     def __init__(self,cpu,memory,memory_card):
#         self.__cpu=cpu
#         self.__memory=memory
#         self.__memory_card=memory_card