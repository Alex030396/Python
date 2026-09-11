# SETS

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario, no un set

my_other_set = {"Alex", "Briceño",30}
print(type(my_other_set)) 

print(len(my_other_set)) 

my_other_set.add("Victoria")
print(my_other_set) # Un set no es una estructura ordenada.

my_other_set.add("Victoria")
print(my_other_set) # Un set no permite duplicados

print("Alex" in my_other_set)
print("alex" in my_other_set)

my_other_set.remove(30)
print(my_other_set)

my_other_set.clear()
print(my_other_set)

# del my_other_set # Elimina todo el set.
print(my_other_set)

my_set = {"Alex", "Briceño",30}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"Dora","Oswaldo","Dante"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"Victoria","Luis","Dayana"}))

print(my_new_set.difference(my_set))