numeros = [1,2,3,4,5,6,7,8,9]
nombres = ["Carlos", "Maria", "Eduardo", "Catalina","Sol","Paco"]

alumnos = [
    {
        "nombre" : "carlos",
        "edad" : 35
    },
    {
        "nombre" : "maria",
        "edad" : 25
    },
    {
        "nombre" : "jose",
        "edad" : 40
    },
]

def filter_nombres(nombre):
    resultado = []
    
    #quiero quedarme con aquellos nombres de mas de 5 letras
    
    for nombre in nombres:
        if len(nombres) > 5:
            resultado.append(nombre)
            return resultado
print(filter_nombres)

# com,o podemos hacer un filtro sim necesidad de crear un algoritmo manual??
def mayor_a_4(nombre):
    return len(nombre) > 4
filtrado = filter(mayor_a_4, nombres)
print(list(filtrado))

# usando funciones lambda todos los elementos de una coleccion 
potencias_de_dos = map(lambda n: 2**n, numeros)
print(list(potencias_de_dos))

mayusculas = map(lambda nombre : nombre.upper(), nombres)
print(mayusculas)

# ya, sabemos que sort permite ordenar in-place los elementos de una lista.
nombres.sort()
print(nombres)

# como alumnos es una lista de diccionarios, no la puedo ordenar directamente.
# alumnos.sort() # ERROR

# lo que si puedo hacer es pasarla a sort una key (una funcion) que le indica al sort
# como obtener la clave de comparacion
alumnos.sort(key=lambda alumno: alumno["edad"], reverse=True)
print(alumnos) 