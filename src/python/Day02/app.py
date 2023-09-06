class Person:
    __slots__ = ['__name', '__age']
    
    def __init__(self, name='홍길동', age=20) :
        self.__name = name
        self.__age = age
        pass
    
    def getName(self):
        return self.__name
    def setName(self, value):
        self.__name = value
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
        

    def show(self): 
        print(f"이름 : {self.__name}, 연령 : {self.__age}")
    def __str__(self):
        return f"이름: { self.__name}, 연령 : {self.__age}"
        
person = Person('남성희', 32)  # 1.객체가 생성됨. 
person.show()

print(person.__str__())
print(isinstance(person, Person))
print(isinstance(person, object))

print(Person.__name)
