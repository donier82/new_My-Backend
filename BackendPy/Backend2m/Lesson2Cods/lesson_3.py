"Инкапсуляция"

class Person:
    def __init__(self, name, age, height):
        self.name = name # Публичный
        self._age = age # Зашишенный 
        self.__height = height # Приватный 

    "@ - декоратор"
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        self.height = new_height

    def info(self):
        print(f"Имя-{self.name}, возраст-{self._age}, рост-{self.__height}")
        self._seciurity() 
        self.__private_method() 

    def _seciurity(self):
        print("Защищенная информация")

    def __private_method(self):
        print("Приватная информация")

    def isko(self):
        return self.__private_method()

human = Person("Janbolot", 15, 171)
human.info()
human._seciurity()
human.isko()

# human.__private_method()
# print(human._Person__height)

# print(human.name) 
# print(human._age) 
# print(human.height) 
# print(human.__height) 