#alumnoNota = int(input('Hola Alumno ingresa tu nota: '))
#if (alumnoNota == 10):
#   print('Excelente Nota')
#elif (alumnoNota >7 and alumnoNota <9):
#    print('Muy bien')
#elif (alumnoNota > 4 and alumnoNota <6):
#    print('Mal')
#else:
#    print('La nota ingresada es INCORRECTA!!')

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento)

m1 = [
    [3.3,6.1,4.0,20],
    [4.9,5.7,6.41,150]
]
imprimir_matriz(m1)

#mostrar estrella por la cantidad

def mostrar_estrella(cantidad):
    for numero in range(1,cantidad +1):
        print('*' * numero)

mostrar_estrella(10)

print('*************************')
print('while')
def estrella(cantidad):
    total = 1
    while total <= cantidad:
        print('*' * cantidad)
        total += 1

estrella(5)


#funciones con valor de retorno
def sumar(num1, num2):
    resultado = num1 + num2
    return resultado
print(sumar(10,69))

total = sumar(10,60)
print(total)


def rango(inicio,final):
    resultado=[]
    while inicio < final:
        resultado.append(inicio)
        inicio +=1
    return resultado

lista = rango(10,21)
print(lista)



def sumar(numeros):

    resultado = 0

    for numero in numeros:
        resultado += numero

    return resultado


print(sumar([1, 50, 90, 29, 5.1]))