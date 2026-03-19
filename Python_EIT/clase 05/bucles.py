# Bucle For
clientes = ["roberto","maria","juan","damian"] 
for cliente in clientes:
    print(cliente + " ingreso al sistema")
print(cliente)
# 1ra forma
a = 1
while a < 15:
    print(a)
    a = a + 1

numero = 1
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)
    numero += 1


# 2da forma
for  numero in [2,5,1]:
    print(numero ** 3)
    
nombres = ["susana", "alejandro", "roberto"]
nombres.insert(2,"paula")
nombres.append("silvina")
print(nombres)
for nombre in nombres:
    print(nombre)
    # suma,multiplicacion y mayor
    
lista_num = [3,9,20,-10,5]
total = 0
for num in lista_num:
    total += num
print("suma: ", total)

total = 1
for num in lista_num:
    total *= num
print("multiplicacion: ", total)

mayor_valor = lista_num[0]
for num in lista_num:
    if num > mayor_valor:
        mayor_valor = num
print("mayor valor: ", mayor_valor)
# a = 1
# while True:
#     if a <5:
#         print("hola mundo")
#         a = a + 1
#     else:
#         break
# # otros ejemplos
# cant = 1
# while cant <=5:
#     print("servidor encendido")
#     cant = cant + 1
    
# cant = 1
# while True:
#     if cant <=3:
#         print("EVG")
#     else:
#         break
#     cant = cant + 1


# forma nº1
# clientes = ["roberto", "sofia", "mateo", "jorge", "maria"]
# for cliente in clientes:
#     print(cliente + " ingreso al sistema")

# numeros = [2, 8, 1]
# for numero in numeros:
#     print(numero ** 2)

# # forma nº2
# for numero in [2, 5, 1]:
#     print(numero **3)
# para muchos numero while
# numero = 1
# while numero <= 5:
#     print(numero)
#     numero += 1
# para pocos numero el for
# for numero in [1,2,3,4,5]:
#     print(numero)

# forma nº3
# range (inicio, final) --> {inicio , inicio +1 , inicio + 2....
# for num in range (1,6):
#     print(num)
# ingreso_1 = input("ingresa 1 numero: ")
# ingreso_2 = input("ingresa segundo numero: ")
# for num in range (ingreso_1, ingreso_2)

for numero in range(1,6):
    print(numero)
    
inicio = int(input("Ingresa un rango de numero: "))
fin = int(input("Ingresa un rango de numero: "))
multiplos = []
for numero in range(inicio,fin +1):
    print(ran)

# # practicos varios
# numeros = [3, 5, 10, 1]

# mayor = numeros[0]


# # puntoº1
# total = 0
# for numero in numeros:
#     total += numero
# print("suma", total)
# # punto nº2
# tuti_Multi = 1
# for num in numeros:
#     tuti_Multi *= num
# print("multiplicacion", tuti_Multi)


# # punto nº3
# for num in numeros:
#     if num > mayor:
#         mayor = num
# print("el numero mayor es:", mayor)

# menu con bucle while
while True:
    print(" *** MENÚ ***")
    print("1 - Alta de usuario")
    print("2 - Modificar usuario")
    print("3 - Eliminar usuario")
    print("4 - Listar")
    print("5 - Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("SE CARGA UN NUEVO USUARIO")
    elif opcion == 2:
        print("SE MODIFICA UN USUARIO EXISTENTE")
    elif opcion == 3:
        print("SE ELIMINA UN USUARIO EXISTENTE")
    elif opcion == 4:
        print("SE MUESTRA POR PANTALLA UN LISTADO DE CLIENTES")
    elif opcion == 5:
        print("Gracias por utilizar el sistema")
        break
    else:
        print("Opción incorrecta")
        
        
          