### CLASSES ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print("1-----------")
print(MyEmptyPerson())
print("2-----------")

class Person:
    def __init__(self,name, surname):
        self.name = name
        self.surname1 = surname

my_person = Person("Alex","Briceno")
print("3-----------")
print(my_person)
print("4-----------")
print(my_person.name)
print("5-----------")
print(my_person.surname1)
print("6-----------")
print(f"{my_person.name} {my_person.surname1}")
print("7-----------")


class Person1:
    def __init__(self,name, surname):
        self.full_name = f"{name} {surname}"
        
my_person = Person1("Alex","Briceño")
print(my_person.full_name)

class Person2:
    def __init__(self,name, surname,alias = "No Alias"):
        self.full_name = f"{name} {surname} {alias}"
        self.__name = name # Propiedad Privada
    def get_name(self):
        return self.__name
    def walk(self):
        print(f"{self.full_name} Esta Caminando")

my_person = Person2("Alex J.","Briceño H.","Albrix")
print(my_person.full_name)
my_person.walk()
my_person.full_name = "Victoria Quesada (Mi amor Bello)"
print(my_person.full_name)
print(my_person.get_name())