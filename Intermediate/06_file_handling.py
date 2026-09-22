# FILE HANDLING

import os

# .txt file

# text_file = open("Intermediate/my_file.txt" ,"r+")
# print(text_file.read())
# print(text_file.read(15))
# print(text_file.readline())
# print(text_file.readlines())

# for line in text_file.readlines():
    # print(line)

# text_file.write("\nAlex es el mejor")
# print(text_file.read())

text_files = open("Intermediate/my_files.txt","w+")
text_files.write("Alex es el mejor\nEn programacion y Analisis de datos\nSoy un buen amante")
text_files = open("Intermediate/my_files.txt","r")
print(text_files.read())

text_files.close()


# os.remove("Intermediate/my_files.txt")

# JSOM FILE

import json

json_file = open("Intermediate/my_file,json", "w+")
json_test = {
    "name" : "Alex",
    "surname" : "Briceno",
    "Age" : 30,
    "languaje":["Python","Dax","SQL"],
    "LinkedIn": "alexbh336"}

json.dump(json_test, json_file, indent =2)
