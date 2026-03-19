# #condicioales
# num = 9
# if num <= 10:
#     print("El numero es menor a 10")
#     print("Dentro del condicional")
#     estado = "encendido"
#     if estado == "encendido":
#         print("servidor activo")

# print("eje principal")
# print("linea del servidor: " + estado)

numer = 15
if numer <= 10:
    print("el numero es menor o igual a 10")
else:
    print("el numero es mayor a 10")

# ejercicios 1
ingreso_cadena1 = input("Ingresa la contraseña: ")
ingreso_cadena2 = input("repit la contraseña: ")
if ingreso_cadena1 != ingreso_cadena2:
    print("la contraseña es diferente")
else:
    print("la contraseña han coincidido!")


# ejercicio 2
# obtener_nombre = input("Hola , ingresa tu nombre: ")
# if obtener_nombre == "":
#     print("Error. Intenta de nuevo")
# else:
#     print("Has ingresado al campus!")

# edad = int(input("Ingresa tu edad: "))
# if edad <=18:
#     print("eres menor de edad!")
# else:
#     print("eres mayor de edad!!")
    

# user = input("hola , ingresa tu nombre: ")
# ingreso_contraseña = input("Hola," + user + " ingresa la contraseña: ")
# verificar_contraseña = input("ingresa de nuevo la contraseña: ")

# if ingreso_contraseña == verificar_contraseña:
#     print("Contraseñas correctas!")
# else:
#     print("Error.vuelve a intentar la contraseña")

# ejercicio 2
# ingreso_contraseñ = input("Ingresa tu nombre: ")
# if ingreso_contraseñ != "":
#     print(
#         "hola,"
#         + ingreso_contraseñ
#         + " eres alumno nuestro y estas en la Introduccion de Python!"
#     )
# else:
#     print("Error.Has ingresado una cadena vacia!")

# usuario_edad = int(input("hola, ingresa tu edad: "))
# if usuario_edad <= 18:
#     print("eres menor de edad.no puedes ingresar!!")
# else:
#     print("eres mayor de edad.Puedes ingresar al evento")

numero = 4
if numero == 1:
    print("el numero es 1")
elif numero == 2:
    print("el numero es 2")
elif numero >= 3 and numero <= 10:
    print("el numero varia entre 3 y 10")
else:
    print("el numero es mayor a 10")
# ejercicio de elifs
# categoria_usuario = input("Hola ingresa la categoria de tu trabajo: ")
# if categoria_usuario == "administrador":
#     print("ingreso correcto!!")
#     print("Acceso a todos los recursos del clientes")
# elif categoria_usuario == "operador1":
#     print("ingreso correcto!!")
#     print("Acceso a alta y baja de los clientes")
# elif categoria_usuario == "operador2":
#     print("ingreso correcto!!")
#     print("Acceso a listado")
# elif categoria_usuario == "medios":
#     print("ingreso correcto!!")
#     print("Acceso a todos los medios multimedia")
# elif categoria_usuario == "developer":
#     print("ingreso correcto!!")
#     print("Acceso al sistema informatico")
# else:
#     print("ACCESO DENEGADO!")

# otra forma
categoria_usuario = input("Hola ingresa la categoria de tu trabajo: ")
if categoria_usuario == "administrador" or categoria_usuario == "operador1" or categoria_usuario == "operador2" or categoria_usuario == "medios" or categoria_usuario == "developer":
    print("Ingreso Correcto")
    if categoria_usuario == "administrador":
        print("Acceso a alta y baja de los clientes")
    elif categoria_usuario == "operador1":
        print("Acceso a alta y baja de los clientes")
    elif categoria_usuario == "operador2":
        print("Acceso a listado")
    elif categoria_usuario == "medios":
        print("Acceso a todos los medios multimedia")
    else: 
        print("Acceso al sistema informatico")
else:
    print("ACCESO DENEGADO!")

#hacer ejercicios asi
enero_junio = 300
julio_octubre = 500
noviembre_diciembre = 700

meses6 = enero_junio * 6
meses4 = julio_octubre * 4
meses2 = noviembre_diciembre * 2
total = meses6 + meses4 + meses2
promedio = int(total / 12)
print("sueldo promedio: ", promedio)
if promedio <300:
    print("SUELDO BAJO")
elif promedio <= 900:
    print("SUELDO NORMAL")
else:
    print("SUELDO MEJOR DE LO NORMAL!")

#laboratorio 5
# usuario_nota = int(input("Hola ingresa tu nota: "))
# if usuario_nota == 10:
#     print("EXCELENETE")
# elif usuario_nota  <= 9 and usuario_nota >= 7:
#     print("MUY BIEN")
# elif usuario_nota  <=6 and  usuario_nota>=4:
#     print("BIEN")
# elif usuario_nota <=3 and usuario_nota >= 0:
#     print("MAL")
# else:
#     print("la nota ingresada es incorrecta")
nota = int(input("ingresa tu nota: "))
if nota <= 10 and nota >= 0:
    if nota == 10  :
        print("excelente")
    elif nota <= 7 and nota >= 9:
        print("muy bien")  
    elif nota <= 6 and nota >= 4:
        print("bien")   
else:
    print("nota invalida")
    