#if, elif, else, for, while, try, except, finally

ano = 2020
ano2 = 2024

#Usar para test manual

if ano == 2021:
    print("Es el año 2021")
elif ano2 == 2022:
    print("Es el año 2022")
else:
    print("No es el año 2023")


#For
biblioteca = ["Libro", "Revista", "Periodico", "Comic", "Novela", "Cuento", "Poesia"]

for item in biblioteca:
    print(item)

textos = "Hola Mundo"
for letra in textos:
    print(letra)

#While
contador = 0
while contador < 10:
    print(contador)
    contador += 2

contador = 10 
while contador > 0:
    print(contador)
    contador -= 1

#Try, except, finally
ano = 2024

try:
    if ano == 2021:
        print("Es el año 2021")
    else:
        print("No es el año 2021")
except Exception:
    print("Error")
finally:
    print("Finalizado")

