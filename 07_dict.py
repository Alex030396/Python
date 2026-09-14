# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Alex", "Edad":30, "Apellido":"Briceño", 1 : "Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Alex", 
    "Edad":30, 
    "Apellido":"Briceño", 
    "Lenguajes" : {"Python","SQL","Dax"}
    }

print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Lenguajes"])
my_dict["Edad"] = 31
print(my_dict["Edad"])
print(my_dict)

my_dict["Vehiculo"] = "Moto BR200"
print(my_dict)

del my_dict["Vehiculo"]
print(my_dict)

print("Nombre" in my_dict)
print("Alex" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.fromkeys(("Nombre", "Edad"))
print(my_new_dict)
my_list = ["Nombre", "Edad"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Alex")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))