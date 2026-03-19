#los flotantes son imprecisos , algunos no se represenyamn exactamente en las computadoras
a= 0.1 + 0.2
print(a)
# q sentido tiene esto

# 1.Analizar cuando tiene sentido usar float
# si lo q estoy haciendo no requiere decimales, me quedo con INT
# 2.Para ciertos decimales, existen otros tipos como decimal

# 3.En muchos casos, este pequeño error no cambia el resultado final

# 4.Otra cosa que podemos hacer mostrar el numero formateado


print(f"El resultado es: {a:.2f}")
