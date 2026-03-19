# las funciones pueden recibir 0 o mas argumentos de entrada
# y siempre devuelve 1 valor

# definicion
def saludar():  # esta funcion no recibe arumento
    print("Hola, bienvenido.")
    
def saludar_nombre(nombre):  # esta funcion no recibe arumento
    print(f"Hola,{nombre} bienvenido.")  
    
def function_x(a, b):  #funcion definida pero no implementada
     pass   
  
def suma_promedio(a,b,c):
    suma = a + b+ c
    promedio = suma / 3
    return suma, promedio  #si quiero devolver mas de un valor, podemos hacerlos asi
# invocacion
saludar()
saludar_nombre("carlos")
resultado = suma_promedio(5,6,7)
print(resultado)