#  REGULAR EXPRESSIONS

import re

# MATCH 
my_string = "Esta es la leccion numero 7: La Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

match = re.match("Esta es la leccion", my_string,re.I)
print(match)
star,end = match.span()
print(my_string[star:end])

print(re.match("Esta es la leccion", my_string,re.I))
print(re.match("Expresiones Regulares", my_string))
print(re.match("Esta es la leccion", my_other_string))

matcha = re.match("Esta no es la leccion", my_other_string)
if not(matcha == None):
    print(matcha)
    star,end = matcha.span()
    print(my_other_string[star:end])

# SEARCH

search = re.search("Esta es la leccion", my_string,re.I)
print(search)
search = re.search("numero 7", my_string,re.I)
print(search)

# FINDALL

search = re.findall("numero 7", my_string,re.I)
print(search)

# SPLIT

print(re.split(":",my_string))

# SUB

print(re.sub("Expresiones","expresiones",my_string))
print(re.sub("Expresiones Regulares","RegGex",my_string))
print(re.sub("la|la","Alex",my_string))

# PATTERN
pattern = r"[l|L]a"
print(re.findall(pattern, my_string))
pattern = r"[lL]a|[0-9]"
print(re.findall(pattern, my_string))
pattern = r"La"
print(re.search(pattern, my_string))
pattern = r"R.*"
print(re.findall(pattern, my_string))

email = "albrix336@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.findall(pattern, email))
print(re.search(pattern, email))