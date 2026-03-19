# dia= "02/11/2025"
# print(dia)
# a=5
# b=9
# c=10
# resultado= a + b + c
# print("a:")
# print(a)
# print("b:")
# print(b)
# print("c:")
# print(c)
# print("resultado:")
# print(resultado)
dia = "15/12/2025"
print(dia)
# #clase 2 
        # tipos de variables
# num1 = 10              # INT 
# num2 = 5      
# num3 = 3.1415          # DECIMAL
# texto = "javascript"   # STR 
# articulo = ""          #CADENA VACIA
# resultado = num1 + num2 
# print(resultado)
# resultado = num2 ** 3    #POTENCIA 
# print(resultado) 
# a= 20 
# b = 10
# suma= a + b
# resta = a - b
# divi = a / b
# multi = a * b
# print("La suma total es:", suma)
# print("La resta total es:", resta)
# print("La division total es:", divi)
# print("La multiplicacion total es:", multi)
x = 7
x+= 2
print(x)

k = 11
j = 30
multi = k * j
suma = k + j
rest = k - j
divi = k / j
print("El primer nuemero es: ", k)
print("El segundo numero es: ", j)
print("La suma de los numeros es: " , suma)
print("La resta es: ", rest)
print("La division es: ",  divi)
print("La multiplicacion es: ", multi)

a = 15
b = 10 
c = 7
print("a:")
print(a)
print("b:")
print(b)
print("c:")
print(c)
resultado= a + b +c
print("El resultado es:")
print(resultado)

base = 10 
altura = 5
resultado = base * altura
# area= "El resultado del area de la base por altura es: ",resultado 
print("El resultado del area de la base por altura es:",resultado )

# texto1 = "potente"
# texto2 = "sol"
# texto3 = " triunfo"
# textofinal= "El " + texto2  + " radia su " + texto1 + texto3 
# print(textofinal)
texto_uno = "Expreso villa Galicia"
texto_dos = "Ramal 4"
texto_tres = "Empresa de colectivos"
oracion = "La " + texto_tres + " " + texto_uno + " posee el " + texto_dos + " que va a Ministro Rivadavia!"
print(oracion)

saludo = "hola"
nombre = "Damian"
cadena = saludo + " " + nombre
print(cadena)
# #funcion de conversion
# num4=8
# numer = "EL NUMERO ES: " + str(num4) 
# print(numer)
# #interacion (input)
# nombre =input("ingresa tu nombre: ")
# apellido = input("ingresa tu apellido: ")
# edad = input("ingresa tu edad: ")
# texto_nombre = "Bienvenido " + apellido + " " + nombre + " usted tiene " + edad + " años"
# print(texto_nombre)
# ejercicio 1
saludo = "hola, "
nombre = "jitomion" 
saludo_nombre = saludo + nombre
print(saludo_nombre.upper()) #mayuscula
print(saludo_nombre.lower()) #minuscula
print(saludo_nombre.capitalize()) #Transforma el primer caracter en mayuscula
print(saludo_nombre.title())
print(saludo_nombre.strip())
#encadenar metodos str
print(saludo_nombre.strip().capitalize())
print(saludo_nombre.find("ia")) #si encuentra el valor , me devuelve el indice
print(saludo_nombre.replace("dam", "k")) #cambia el valor
print("ia" in saludo_nombre) #verifica si existe el caracter en la dena 
print("da" not in  saludo_nombre) #niega 
# curso = "Ultimate "Python""
# print(curso)

#operaciones logicas  
num1 = 10
num2 = "10"
resultado = num1 == num2
print(resultado)
resultado = num1 != num2
print(resultado)

            # concatenacion 

texto1 = "Encendido"
texto2 = "Servidor"
num5 = 5
num5 = str(num5)
texto3 = texto2 + " " + texto1 + " a las " + num5
print(texto3)

texto2 = texto2 + " "     # multiplicacion de string 
texto4 = texto2 * 5
print(texto4)

base = 15
altura = 5
area = base * altura 
print("el area del rectangulo es ", area)

tex_1 = "La gran vigilia"
tex_2 = "Este miercoles 31/12/2025"
text_3 = "En la Universal mas cercana a su casa se hara"
cadena_string = text_3 + " " + tex_1 + " " + tex_2
print(cadena_string)

print(text_3 + " " + tex_1+ " " + tex_2) 

numero = 16
# conjunccion (AND) retorna verdadero si ambos son verdaderos
resul = numero >=1 and numero <=10
# disyunccion  (OR) RETORNA TRUE SI UNO DE LOS 2 ES VERDADERO, SINO ES FALSO
categoria_usuario = "administrador"
resul = categoria_usuario == "administrador" or categoria_usuario == "operador"
print(not resul)
print(resul)