#Operadores logicos
# and, or, not
altura = 180
altura2 = 170

comparacion = altura == altura2 and altura > altura2 # Comparamos si altura es igual a altura2 y si altura es mayor a altura2, si se cumple ambas condiciones devuelve True
print(comparacion)
comparacion2 = altura == altura2 or altura > altura2 # Comparamos si altura es igual a altura2 o si altura es mayor a altura2, si se cumple alguna de las condiciones devuelve True
print(comparacion2)
comparacion3 = not altura2 >= altura # Comparamos si la negacion de altura2 es mayor o igual a altura, si se cumple la condicion devuelve True
print(comparacion3)