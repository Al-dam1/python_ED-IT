# ingreso_usuario_columna = int(input("ingrese una columna: "))
# ingreso_usuario_fila = int(input("ingrese una fila: "))

# matriz = [[3.3, 6.1, 4.0],
#           [4.9, 5.7, 6.4]]

# matriz_final =  matriz [ingreso_usuario_columna] [ingreso_usuario_fila]

# if ingreso_usuario_columna <=3 and ingreso_usuario_fila:
#     print("la matriz es: ", matriz_final)
# else:
#     print("error")
#hacer ejercicios asi
# ingreso_1 = int(input("ingresa una columna: "))
# ingreso_2 = int(input("ingreso una fila: "))
# matriz = [[3.3, 6.1, 4.6],
#           [4.9, 5.7, 6.4]
#           ]
# columna_fila_matriz = matriz [ingreso_1] [ingreso_2]
# if ingreso_1 == 0 and  ingreso_2 <=2 :
#     print("la matriz es: ", columna_fila_matriz)
# else:
#     print("ERROR!!!") 
dato = 0
while dato <= 10:
    print(dato)
    dato += 1
    
ingreso_nombre = input("Hola ingresa tu nombre: ")
while ingreso_nombre == "":
    print("Error ingresa de nuevo!")
    ingreso_nombre =input("Ingresa tu nombre: ")
print("Hola", ingreso_nombre)