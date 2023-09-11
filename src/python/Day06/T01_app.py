numbers = [1, 23, 4, 5, 5]
print(all(number >= 1 for number in numbers))
print(any(number >= 1 for number in numbers))


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


numbers = [5, 2, 4, 6, 3]
persons = [Person('홍길동', 20), Person('심청이', 16), Person('에디슨', 55)]
print(all(p.age >= 19 for p in persons))


def isAdult(p):
    return p.age >= 19


adults = (filter(lambda p: p.age >= 19, persons))
for p in adults:
    print(p)


class Studnet(Person):
    def __init__(self, name, age, major) -> None:
        super().__init__(name, age)
        self.major = major

    def __str__(self) -> str:
        return super().__str__() + f"전공 : {self.major}"


persons = [Person('홍길동', 44), Person('에디슨', 10)]
p = Person('이순신', 50)
s = Studnet('강감찬', 44, '장군')

print(isinstance(s, Studnet))
print(isinstance(s, Person))
print(isinstance(p, Studnet))


def func(person):
    person = Person(person.name, person.age)
    if person.age >= 19:
        person.isAdult = True
    else:
        person.isAdult = False
    return person


newPersons = map(func, persons)

map(func, persons)

newPersons = map(func, persons)
for p in newPersons:
    print(f"이름 : {p.name}, 성인 : {p.isAdult}")

numers = [1, 2, 3, 4, 5]
print(list(map(str, (numers))))
print(list(map(lambda x: str(x), numers)))
