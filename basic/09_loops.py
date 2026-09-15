# LOOPS

# WHILE

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual a 10")
    
    
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
if my_condition == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condicion es mayor o igual a 10")
    
    
my_condition = 0
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break
    print(my_condition)
    
    
# FOR

my_list = [35,24,62,52,30,30,17]
for element in my_list:
    print(element)
my_tuple= ("Alex","Briceño",30,1.72)
for element in my_tuple:
    print(element)
my_set= {"Alex","Briceño",30}
for element in my_set:
    print(element)
my_dict= {"Nombre":"Alex","Apellido":"Briceño","Edad":30,"Altura":1.72,"Cargo":"Analista"}

for element in my_dict.values():
    print(element)
    if element == 30:
        break
    print("Se ejecuta")
else:
    print("El bucle a terminado de imprimir")

    
for element in my_dict.values():
    print(element)
    if element == 1.72:
        continue
    print("Cuenta")
else:
    print("El bucle a terminado de imprimir")