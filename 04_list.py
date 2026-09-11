# List

my_list = list()
my_other_list = []
print(len(my_list))

my_list = [35,24,62,52,30,30,17]
print(my_list)
print(len(my_list))

my_other_list = [30, 1.72, "Alex","Briceño"]
print(type(my_list))

print(my_list[4])
print(my_list[0])
print(my_other_list[1])
print(my_other_list[-1])
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError
print(my_other_list.count("Alex"))
print(my_list.count(30))
print(my_list[0:4])
print(my_other_list[0:1])

print("-----------------------------")
age, height, name, surname = my_other_list
print(name)
print(age)
print(surname)
print(height)

print("-----------------------------")
surname, height,age, name  = my_other_list[3], my_other_list[1], my_other_list[0], my_other_list[2]

print(name)
print(age)
print(surname)
print(height)

print(my_list + my_other_list)
print("-----------------------------")

my_list = ["Hola Victoria"]
print(my_list)
print("-----------------------------")

# Agregar elementos a la lista
my_other_list.append("Victoria")
print(my_other_list)
# Insertar un elemento a la lista en una posición específica
my_other_list.insert(2, "Analisis")
print(my_other_list)
# Remover un elemento de la lista
my_other_list.remove("Analisis")
print(my_other_list)
# Eliminar el último elemento de la lista
my_other_list.pop()
print(my_other_list)
# Eliminar un elemento de la lista en una posición específica
my_pop_element = my_other_list.pop(2)
print(my_pop_element)
my_other_list.insert(2, my_pop_element)
print(my_other_list)
# Delete el elemento en la posición 1 de la lista
del my_other_list[1]
print(my_other_list)
# Limpiar toda la lista
my_list.clear()
print(my_list)
# Sustituir un elemento en una posición específica
my_other_list[0] = 29
print(my_other_list)
# Poner la lista en reverso
my_other_list.reverse()
print(my_other_list)
# Ordenar la lista en orden ascendente
my_list = [21,45,32,27,59,6,67,20]
my_list.sort()
print(my_list)