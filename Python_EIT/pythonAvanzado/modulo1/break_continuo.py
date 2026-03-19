# Break termina inmediatamente los bucles for y while 
a = 0
while True:
    print(a)
    a+= 1
    if a >=5:
        break
print("Termina el while")

for i in range(10):
    print(i)
    if i == 5:
        break
print("termina el for")

# Continue = termina la iteraccion actual, haciendo de la condicion se resuleva
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)