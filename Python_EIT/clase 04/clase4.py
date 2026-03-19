# contador = 0
# while contador <=9:
#     print(contador)
#     contador = contador + 1
   
# ingreso_user = input("hola , ingresa tu nombre: ")
# while ingreso_user == "":
#     print("ingreo unvalido")
#     ingreso_user = input("ingrese un nombre: ")
# print("hola ", ingreso_user  ) 
# edad = input("ingresa tu edad: ")
# while edad.isdecimal() == False:
#     print("Error, debe ingresar una edad valida")
#     edad= input("reintente: ")
# if int(edad) >= 18:
#     print("mayor de edad")
# else:
#     print("menor de edad")
    # BUCLES FOR  
# alumnos = ["matias", "jorge", "martin", "pablo"]
# for alumno in alumnos:
#     print("hola mundo")
numero = input("Ingresa un numero: ")
if numero.isdecimal() == True:
    resultado = int(numero) ** 3
    print(resultado)
else:
    print("error")

ingreso_edad = input("Ingresa la edad: ")
while ingreso_edad.isdecimal() == False:
    print("errro!")
    ingreso_edad = input("ingresa la edad de nuevo : ")
print("tu edad es ", ingreso_edad)
if int(ingreso_edad) >= 18:
    print("eres mayor")
else:
    print("eres menor!")
    
contador = 5
while contador <= 15:
    print(contador)
    contador =contador +  1
validar_numero = input("Ingresa un numero positivo: ")
while validar_numero.isdecimal() == False:
    print("Error vuelve a intentar con numero positivo!")
    validar_numero = input("Ingresa un numero positivo: ")
print("el numero es ", validar_numero) 

ingreso_apellido = input("Ingresa tu apellido: ")
while ingreso_apellido == "":
    print("Error. Ingreso invalido")
    ingreso_apellido = input("Vuelve a ingresar tu apellido: ")
print(ingreso_apellido.capitalize(), "Ingreso correctamente!")
#  RANGE
# i = 1
# while i <=10:
#     print(i)
#     i = i +1
    
#     # ALTERNATIVA FOR
# for i in [1,2,3,4,5,6]:
#     print(i)