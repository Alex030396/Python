# Tuplas

my_tuple = tuple()
my_other_tuple = ("Viernes",11, 2023)

my_tuple = (35, 1.72, "Alex", "Briceño")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Alex"))
# Ver el numero del indice
print(my_tuple.index("Alex"))
print(my_tuple.index(1.72))
print(my_tuple.index("Briceño"))

# my_tuple[1] = 1.75 No se puede modificar las tuplas son inmutables
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:5])

my_other_tuple = list(my_other_tuple)
print(type(my_other_tuple))

my_other_tuple[2] = 2026
print(tuple(my_other_tuple))

del my_other_tuple[2] 
del my_other_tuple
# print(my_other_tuple) # NameError: name 'my_other_tuple' is not defined

