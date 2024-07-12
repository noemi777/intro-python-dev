#Operaciones de asignacion
numero = 20 
numero += 4 # numero = numero + 4, es decir 20 + 4 = 24
print(numero)
#-=, *=, /=, %=, **=, //=
numero -=2 # numero = numero - 2, es decir 24 - 2 = 22
print(numero)
numero *= 3 # numero = numero * 3, es decir 22 * 3 = 66
print(numero)
numero /= 2 # numero = numero / 2, es decir 66 / 2 = 33
print(numero)
numero %= 3 # numero = numero % 3, es decir 33 % 3 = 0
print(numero)
numero **=2 # numero = numero ** 2, es decir 0 ** 2 = 0
print(numero)
numero //=3 # numero = numero // 3, es decir 0 // 3 = 0
print(numero)

#Ejemplo 2
numero = 50
print(50/3) # 16.666666666666668
numero %= 3 # numero = numero % 3, es decir la division de 50/3 y el residuo es 2.
print(numero) # 2