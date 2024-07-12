# Funciones
def persona(nombre, edad): # Definimos la funcion persona con dos parametros, nombre y edad
    return f"Mi nombre es {nombre} y tengo {edad} años" # Retornamos un string con los parametros nombre y edad

variableFuncion = persona("Gustavo", 57) # Llamamos a la funcion persona y pasamos los parametros
print(variableFuncion) # Imprimimos la variable que contiene la funcion persona
print(persona("Blanca", 25)) # Imprimimos la funcion persona con los parametros nombre y edad

def domicilio(calle, numero): # Definimos la funcion domicilio con dos parametros, calle y numero
    persona_dato = persona("Gustavo", 57) # Llamamos a la funcion persona y pasamos los parametros
    return f"{persona_dato} y vivo en la calle {calle} con el numero {numero}" #Retornamos un string con los parametros calle y numero

print(domicilio("Av. Los Pinos", 123)) # Imprimimos la funcion domicilio con los parametros calle y numero

# Funciones lamda()
suma = lambda x, a : x + a #Funcion lambda que recibe dos parametros(x, a) y devuelve la suma de los mismos
print(suma(2,3)) #Imprimimos la funcion lambda con los parametros 2 y 3
