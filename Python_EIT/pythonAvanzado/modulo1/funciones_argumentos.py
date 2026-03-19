# argumentos por defectos

def function_x(a, b,c=0):
    print(a,b,c)
 
# argumentos de longitud variables
# argumentos como tupla

# por convencion, la variable se llama args
def sumatoria(*args):
    print(type(args))
    suma = 0
    for valor in args:
        suma += valor
 
    if "clave1" in args:
        print("procesamiento de la clave 1")
    elif "clave2" in args:
        print("procesamiento en la clave 2")
print("hola mundo" )

    
function_x(1,2,3)
function_x(1,2)
#1 argumentos posicionales obligatorios
#2 argumentos por defectos
#3 argumentos de longitud
#4 argumentos como diccionarios
def mega_funcion(a,b,c, d=0, *args, **kargs):
    print(f"a: {a},b: {b},c: {c},d: {d},args: {args},kargs: {kargs}")
print("*" * 10)  
mega_funcion(1,2,3,4,5,6,7,clave1=266, clave2=263)
