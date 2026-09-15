# Variables

MyVariable = "My string variable"
print(MyVariable)

my_string_variable = "My string variable"
print(my_string_variable)

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en print
print(my_string_variable,my_bool_variable,str(my_int_variable))
print("Este es el valor:", my_bool_variable)

#Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea
name, surname, alias, age = "Alex", "Briceño", "Jimmy", 30
print("Mi nombre es:", name , surname ,".Mi alias es:", alias,". Mi edad:", age)

# Inputs
"""
name = input("¿Cual es tu nombre? ")
age = input("¿Cual es tu edad? ")

print(name)
print(age)
"""
# Cambiamos su tipo
name = 30
age = "Alex"

print(name)
print(age)

# Forzamos el tipo
address : str = "Mi direccion"
# address = 32
print(type(address))