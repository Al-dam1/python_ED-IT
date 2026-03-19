def function(args1):
    args1
lista = [1,2,3]
function(lista)  #pasa la lista por referencia
lista1 = [1,2,3]
lista2 = lista1   #Alias la lista, en lista2
lista2[0] = 10
lista2 = lista1.copy() #COPIA 10,2,3
#OPTRA FORMA DE COPIAR ES USANDO SLICING
lista3 = lista2[:]