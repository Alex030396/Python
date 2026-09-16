# CHALLENGES

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos y con un salto de linea entre 
cada impresion ), sustituyendo los siguientes: 
- Multiplos de 3 por la palabra "fizz"
- Multiplos de 5 por la palabra "buzz"
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz ():
    for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)
        
# fizzbuzz()
        
"""
¿ES UN ANAGRAMA
Escribe una funcion que reciba dos palabras (Strings) y retorne
verdadero o falso (bool) segun o no anagramas.
- Un Anagram consiste en formar una palabra retornando TODAS
las letras de otra palabra inicial
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama
"""        

def is_anagrama (wordOne, wordTwo):
    if wordOne.lower() == wordTwo.lower():
        return False
    return sorted(wordOne.lower()) == sorted(wordTwo.lower())

print(is_anagrama("Alex","Lexa"))
print(is_anagrama("ria","ira"))
print(is_anagrama("Mesa","Sema"))
print(is_anagrama("Mesa","mesa"))

"""
LA SUCESION DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesion de numero en 
   la que el siguiente siempre es la suma de los dos anteriores.
   0,1,1,2,3,5,8,13
"""
def fibonacci():
    numero_first = 0
    numero_second = 1
    for index in range(0,51):
        print(f"{index} : {numero_first}")
        fibo = numero_first + numero_second
        numero_first = numero_second
        numero_second = fibo

# fibonacci()
  

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primo entre 1 y 100.
"""

def is_prime():
    for number in range(1,101):
        if number >= 2:
            is_divisible = False
            for index in range(2,number):
                if number % index == 0:
                    is_divisible = True
            if not is_divisible:                    
                print(number)
  
# is_prime()  

"""
INVIRTIENDO CADENAS
Crear un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica.
- Si le pasamos "Hola mundo" nos retornaria "odnum aloh"
"""

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text.lower()

print(reverse("Hola Mundo"))
print(reverse("Estamos aqui volteando todo"))
print(reverse("Reconocer"))