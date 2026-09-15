# EXCEPTION HANDLING

numberOne = 5
numberTwo = "4"

if numberOne < 3:
    print(numberOne + numberTwo)
else:
    print("No se cumple")

# Try Except    
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta cuando ocurre una excepcion
    print("Se ha producido un error")
    
print("------------------------")
    
# Try Except Else
numberTwo = 4
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta cuando no hay excepcion
    print("La ejecución continúa correctamente")

print("------------------------")

# Try Except Else Finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")
    
print("------------------------")
    
numberTwo = "4"
# Excepciones por tipo 
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un valueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)