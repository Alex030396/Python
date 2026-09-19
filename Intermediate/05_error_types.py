### Error Types ###

# SyntaxError
# print "Hola Mundo" SyntaxError
print("Hola Mundo")

# NameError
# Falta crear la variable
# print(surname) NameError

# IndexError
my_list = ["Alex","Briceno",30,1.72]
# print(my_list[5]) IndexError
print(my_list[2])

# ModuleNotFoundError
# import maths Error ModuleNotFoundError
import math

# AttributeError
# print(math.PI) AttributeError
print(math.pi)

# KeyError
my_dict = {"Name":"Alex","Surname":"Briceño","Age":30}
# print(my_dict["Ages"]) KeyError
print(my_dict["Age"])

# TypeError
# print(my_list["Nombre"]) TypeError
print(my_list[0]) 

# ImportError
# from math import PI ImportError
from math import pi
print(pi)

# ValueError
# my_int = int("10 años") ValueError
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
# print(4/0) ZeroDivisionError
print(4/2)

