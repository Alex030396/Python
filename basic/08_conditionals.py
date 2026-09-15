# Conditionals

my_condition = False

if my_condition:
    print("Se ejecuta la condición del IF")


my_condition = 5*2
if my_condition == 11:
    print("Se ejecuta la condición del IF multiplicado")
    
if my_condition <= 10:
    print("Se ejecuta la condición del IF multiplicado 2")

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")


my_condition = 4*4

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y es menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

my_condition = 1

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y es menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto no es vacia")

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")