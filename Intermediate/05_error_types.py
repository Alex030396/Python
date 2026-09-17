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
