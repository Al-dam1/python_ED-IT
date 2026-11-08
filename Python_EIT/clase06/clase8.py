import random

lista_numeros = []
while len(lista_numeros ) < 10:
    lista_numeros.append(random.randint(10,50))

cadena = ''
for numero in lista_numeros:
    cadena += str(numero) + -

print(cadena)