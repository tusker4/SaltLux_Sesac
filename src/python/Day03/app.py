
from abc import ABCMeta

class Person(metaclass = ABCMeta): # 추상클래스는 객체로 못만듬. 
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        print("Call Person")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._name

    @age.setter
    def age(self, value):
        self._age = value


class Student(Person): # 로직은 자기자식에게 
    def __init__(self, name, age, major) -> None:
        super().__init__(name, age)  # 부모에게 전달해준다.
        # 즉 여기서 정의하는게 아니라 부모인 Person에게
        self._major = major
        print("Call Student")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    def staticshow():
        print("static 메서드 호출")

    @classmethod
    def classshow(cls):  # cls라는 이름으로 자동저장 됩니다.
        print(cls)

    static_method = staticmethod(staticshow)

    def show(self):
        print(f"{self._name, self._age, self._major}")

    @classmethod
    def clone(cls, obj):
        return cls(obj._name, obj._age, obj._major)


class Employee:
    def __init__(self) -> None:
        super().__init__()  # 상속으로 호출
        print("Call Employee")


p = Person("남성희", 32)
s = Student("a", 22, major="회계학과")
e = Employee()

s.show()
Student.static_method()
Student.classshow()
s2 = Student.clone(s)
print(id(s), type(s))
print(id(s2), type(s2))
