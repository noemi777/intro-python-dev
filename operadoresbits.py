#Operadores biterwise   
# &, |, ^, ~, <<, >>

tamaño = 60
tamaño2 = 30
#print(bin(tamaño))
#print(bin(tamaño2))

#Operador & (and)
resultado = tamaño & tamaño2
print(bin(resultado))
print(resultado)
resultado2 = tamaño | tamaño2
print(bin(resultado2))
resultado3 = tamaño ^ tamaño2
print(bin(resultado3))
resultado4 = ~tamaño
print(bin(resultado4))
print(resultado4)
resultado5 = tamaño << 2
print(bin(resultado5))
resultado6 = tamaño >> 2
print(bin(resultado6))

#Ejemplo 2
binario = b'\x48\x65\x6c\x6c\x6f' #Hello
binario2 = b'\x57\x6f\x72\x6c\x64' #World
print(binario)
print(binario2)
