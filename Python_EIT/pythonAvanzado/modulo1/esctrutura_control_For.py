# for clasico
# los range en Python son datos inclusive, hasta no inclusive
for i in range (0,5):
    print(i)
    
print("*" * 10)
    
# range asume desde = 0 por defecto, entonces lo puedo omitir

for i in range(6):
    print(i)
    
print("*" * 10)

# puede cambiar el incremento
for i in range(0, 10, 2):
    print(i)
    
print("*" * 10)

for i in range(10, 0, -2):
    print(i)