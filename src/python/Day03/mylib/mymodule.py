PI = 3.14

def hello():
    print('Hello')
    
class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"이름 : {self.name}"
    
p = Person("남성희", 32)
print(p)
    
    