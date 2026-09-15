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
        
fizzbuzz()
        
        
        
        
        
        
        
        
# for numbre in list(range(100)):
#     print(numbre)

# my_list = list(range(100))
# print(my_list)