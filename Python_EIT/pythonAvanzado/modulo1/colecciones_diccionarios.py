# los diccinarios son coleciones de pares clave-valor

# los diccionarios no tienen orden

alumnos = {
    "carlos": 7,
    "maria": 8,
    "jose": 9
}

# acceso

print(alumnos)
print(alumnos["carlos"])

# agregar
alumnos["Roberto"] = 8
print(alumnos)

# modificar
alumnos["Roberto"] = 10
print(alumnos)

# eliminar
del alumnos["Roberto"]
print(alumnos)

# iteracion
for clave in alumnos:
    print(clave, alumnos[clave])
    
print("*" * 10)
# keys
for clave in alumnos.keys():
    print(clave, alumnos[clave])

print("*" * 10)
# values
for valor in alumnos.values():
    print(valor)
    
print("*" * 10)
# items
for clave, valor in alumnos.items():
    print(clave, valor)
# pertenencia

print("maria" in alumnos)
print("roberto" in alumnos)