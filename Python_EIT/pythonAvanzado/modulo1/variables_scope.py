#scope global
a = 10    #<=> Me doy cuenta q es GLOBAL porque no tiene TABULACION
def funcion_x():
    b = 20
    #scope local
    print(b)

print(a)
# print(b)  <=> Error!! Intentando acceder a una variable LOCAL por fuera de su SCOPE