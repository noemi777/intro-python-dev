#Operaciones binarios de comparación biterwise
binario = 0b1010
# &=, |=, ^=, >>=, <<=
binario &= 0b1100
print(bin(binario))
binario |= 0b1010
print(bin(binario))
binario ^= 0b1010
print(bin(binario))
binario >>= 3
print(bin(binario))
binario <<= 4
print(bin(binario))