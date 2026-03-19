#FIRST CLASS CITIZEN
# este termino se refieren a que las funciones son objetos
# las funciones son un dato mas, es decir las puedo guardar y manipular como cualquier otro dato
# funciones de orden superior son aquellos q reciben y/o devuelven funciones
def suma (a,b):
    return a + b
def resta (a,b):
    return a - b
operaciones = {
    "+": lambda a, b : a + b,
    "-": lambda a, b : a - b
}
# FORMA CORRECTA
def calculadora(operaciones, a,b):
    return operaciones(a,b)

resuelto = calculadora(operaciones["+"],2,2)
resuel = calculadora(operaciones["-"],20,5) 
print(resuelto)
print(resuel)