# en general, cuando no se de antemano cuantas veces necesito hacer un loop,
# uso la esctrucutra WHILE

# por el contrario, cuando ya se de antemano cuantas vueltas necesito dar,me conviene un for

a = 0
while a < 5:
    print(a)
    a+= 1
print("Termino")

continuar = True

while continuar:
    print("Ingrese un numero del 1 al 5")
    respuesta = int(input("> "))
    if 1 <= respuesta <=5:
        print("Numero correcto")
        continuar = False
    else:
        print("numero invalido")
print("termine")