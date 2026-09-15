# Strings

my_string = "mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " +my_other_string)

my_new_line_string = "Este es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulador"
print(my_tab_string)

my_scape_string = "\\tEste es un String con \nEscapado"
print(my_scape_string)

# Formateo
name, surname, age = "Alex", "Briceño",30
print(f'Mi nombre es {name} {surname} y mi edad es {age}')
print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname,age))

# Desempaquetado de caracteres

language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)

# División

language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[::3]
print(language_slice)

# Reverse

reversed_language = language[:: -1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.upper().isupper())
print(language.lower())
print(language.title())
print(language.count("P"))
print(language.startswith("Py"))