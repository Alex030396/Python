# FUNCTIONS

def my_functions ():
    print("Esto es una funcion")
    
my_functions()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (7 , 3)
sum_two_values (542 , 458)
sum_two_values (1.5 , 1.3)

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

sum_two_values_with_return (8,2)
my_result = sum_two_values (1.5 , 1.3)
print(my_result)
my_result = sum_two_values_with_return (1.5 , 1.3)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name ("Alex","Briceno")
print_name (surname="Alex", name="Briceno")

def print_name_with_default (name, surname, alias="No Alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default ("Alex","Briceno","Albrix")
print_name_with_default ("Alex","Briceno")

def print_texts (*text):
    print(text)
    
print_texts ("Hola","Alex","Jose","Python","Victoria","Moto",5)

def print_texts1 (*texts):
    for text in texts:
        print(text.upper())

print_texts1 ("Hola","Alex","Jose","Python","Victoria","Moto")