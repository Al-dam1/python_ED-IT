# funciones anonimas
def suma(a,b):
    return a + b

# esto es posible porque las funciones son objetos
suma = lambda a,b: a + b
print(suma(3,4))