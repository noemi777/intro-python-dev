#Funciones
def persona(nombre, edad):
    return f"Mi nombre es {nombre} y tengo {edad} años"

variableFuncion = persona("Gustavo", 57)
print(variableFuncion)
print(persona("Blanca", 25))

def domicilio(calle, numero):
    persona_dato = persona("Gustavo", 57)
    return f"{persona_dato} y vivo en la calle {calle} con el numero {numero}"

print(domicilio("Av. Los Pinos", 123))
#Funciones lamda()
suma = lambda x, a : x + a
print(suma(2,3))