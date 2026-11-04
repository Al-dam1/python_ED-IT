from datetime import date
# Ejercicio 1. Sistema de acceso

# Crear un programa que solicite usuario y contraseña.
# - Usuario correcto: programador
# - Contraseña correcta: python123
# - Si son correctos, mostrar: Bienvenido al sistema.
# - Si son incorrectos, mostrar: Acceso denegado.
# Usuario = 'programador'
# Contraseña = 'python123'

# ingresoUser = input('Ingresa tu usuario: ')
# ingresoPassword = input('Ingresa tu usuario: ')

# if (ingresoUser == Usuario and ingresoPassword == Contraseña):
#     print('Bienvenido al sistema.')
# else:
#     print('Acceso denegado.')

# ------------------
# Ejercicio 2. Control de números

# Crear un programa que solicite números infinitamente hasta que el usuario ingrese 0.
# - Si ingresa un número positivo, mostrar Número positivo.
# - Si ingresa uno negativo, mostrar Número negativo.
# - Si ingresa 0, finalizar el programa.
#print('Bienvenidos al programa')
# while True:
#     ingreso = int(input('Ingresa un numero: '))
#     if (ingreso == 0):
#         print('Programa finalizado')
#         print('gracias por usarlo')
#         break
#     elif (ingreso >0):
#         print('numero positivo')
#     else:
#         print('numero negativo')

# -----------------
# Menú de operaciones

# Crear un menú que se repita hasta seleccionar la opción 4.
# 1 - Saludar.
# 2 - Mostrar fecha.
# 3 - Mostrar mensaje.
# 4 - Salir.
# Cada opción debe mostrar un mensaje diferente.
while True:
    print('1 - Saludar')
    print('2 - Mostrar fecha')
    print('3 - Mostrar mensaje')
    print('4 - Salir')
    opcion = int(input('Ingresa una opcion: '))
    if (opcion == 1):
        print('Bienvenido a mundoMania')
    elif (opcion == 2):
        hoy=  date.today()
        print(hoy)
    elif (opcion == 3):
        print('Haciendo prueba piloto')
    elif (opcion == 4):
        print('gracias por usar esta apps')
        break
    else:
        print('Error 404')
