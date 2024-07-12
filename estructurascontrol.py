# if, elif, else, for, while, try, except, finally

ano = 2020
ano2 = 2024
 
"""
La condicion es si año es igual a 2021 entonces imprime "Es el año 2021", en caso que no se cumpla la condicion,
entonces se evalua si año2 es igual a 2022, si se cumple la condicion entonces imprime "Es el año 2022", en caso
contrario imprime "No es el año 2023"
"""
if ano == 2021:
    print("Es el año 2021")
elif ano2 == 2022:
    print("Es el año 2022")
else:
    print("No es el año 2023")


# For
biblioteca = ["Libro", "Revista", "Periodico", "Comic", "Novela", "Cuento", "Poesia"]

# Recorre la lista biblioteca y muestra cada uno de los elementos.
for item in biblioteca:
    print(item)

textos = "Hola Mundo"
# Recorre el texto y muestra cada uno de los elementos.
for letra in textos:
    print(letra)

# While
contador = 0
# Mientras contador sea menor a 10, imprime el valor de contador y le suma 1
while contador < 10:
    print(contador)
    contador += 2

contador = 10 
# Mientras contador sea mayor a 0, imprime el valor de contador y le resta 1
while contador > 0:
    print(contador)
    contador -= 1

# Try, except, finally
ano = 2024

"""
    Intenta ejecutar el bloque de codigo, si se cumple la condicion imprime "Es el año 2021", en caso contrario imprime "No es el año 2021"
    Si se produce un error imprime "Error" 
    Finalmente imprime "Finalizado", independientemente si se cumple la condicion o no.
"""
try:
    if ano == 2021:
        print("Es el año 2021")
    else:
        print("No es el año 2021")
except Exception:
    print("Error")
finally:
    print("Finalizado")

