#      #DESAFIO 1
# semana = 1
# minutos = 60
# dia = 24  
# semana_dias = 7 
# suma= semana * semana_dias * dia * minutos 
# print(suma)

nota_uno = 10
nota_dos = 6
nota_tres = 8
suma_de_notas = int((nota_uno + nota_dos + nota_tres) / 3)
print("EL promedio de las 3 notas es: " , suma_de_notas)
 
# payaso = 10
# muñeca = 10

# user_pay = int(input("Ingrese la cantidad de payaso comprados: "))
# user_muñ = int(input("Ingrese la cantidad de muñeca comprados: "))

# total_pay =  user_pay * payaso
# total_muñ = user_muñ * muñeca
# print("El total de los payasos comprados es de: ", total_pay , "kg")
# print("El total de las muñecas comprados es de: " , total_muñ , " kg")

# peso = total_pay + total_muñ
# print("el peso total de los paquetes de payasos y muñecas es: ", peso)

# ingres_user = input("Bienvenido, ingrese su nombre: ")
# notas_user= int(input("hola " + " " + ingres_user + " Ingrese su primera calificacion: "))
# notas_user_2= int(input("Ingrese su  seguna calificacion: "))
# notas_user_3= int(input("Ingrese su  tercera calificacion: "))
# suma_notas = int((notas_user + notas_user_2 + notas_user_3) / 3)

# print("el promedio de las notas es: ", suma_notas)

# # #nombre del alumno
# alumno = input("hola, ingresa tu nombre: ")
# cursos = input("ingresa la cantidad de  cursos q tienes: " )
# print("El alumno " + alumno + " tiene un total de " + str(cursos) + " cursos!")

# minutos_por_hora = 60
# ingreso = int(input("Ingresa la cantidad de minutos: "))
# total_horas = ingreso / minutos_por_hora
# print("Equivale a:",int(total_horas),  "horas")


# dolar = 1100
# ingreso_user = int(input("ingresa el peso argentino: "))
# cambio = ingreso_user / dolar 
# print("el cambio de peso argentino a dolar es:", cambio)

# # Sistema de bienvenida a empleados
# nombre = input("hola ingresa tu nombre: ")
# apellido = input("hola ingresa tu apellido: ")
# edad = input("hola ingresa tu edad: ")
# puesto = input("hola ingresa tu puesto de trabajo: ")
# print("hola ", nombre , apellido +  " , tu edad es ",  edad, "y tu puesto de trabajo es ", puesto)

# # Calcular sueldo semanal
# ingreso_trabajo = int(input("ingresa la cantidad de horas trabajadas: "))
# ingreso_semana = int(input("ingresa la cantidad de dias  trabajados: "))
# ingreso_pago = int(input("ingresa el monto q te pagan por hora: "))
# sueldo_final = (ingreso_trabajo * ingreso_semana) / ingreso_pago
# print("el sueldo total es de: ", sueldo_final)
cantidad_semanas = 1
semana = 7 
dia = 24
minutos = 60
calcular_minutos =  cantidad_semanas * semana * dia * minutos  
print(calcular_minutos)

Goku = 115
Vegetta = 75
ingreso_1 = int(input("hola ingresa la cantidad de Goku comprados: "))
ingreso_2 = int(input("ingresa la cantidad de Vegeta comprados: "))
ingreso_1_suma = ingreso_1 * Goku
ingreso_2_suma = ingreso_2 * Vegetta
peso_paquete = ingreso_1_suma + ingreso_2_suma
print("El peso del paquete con los muñecos de Goku y Vegetta es de : ", peso_paquete)

# 🔟 “Ficha técnica” de persona nombre


print("   ***   FICHA TECNICA   ***   ")
nombre = input("ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu pais: ")
hobby = input("Ingresa tu hobby: ")

print("----- FICHA COMPLETA -----")

print("nombre:", nombre.title())
print("apellido: ", apellido.title())
print("edad:", edad , " años")
print("pais:", pais.title())
print("hobby: ", hobby)
print("<--------------------->")
     
     
