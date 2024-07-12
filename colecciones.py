#Colecciones, lista, tuplas, diccionarios, conjuntos(sets)
#Listas []
lista = ["hola", 1, 1.2, True, None]
print(lista)
print(type(lista))
print("-" * 20 ) #Separador
# Tuplas ()
tupla = ("hola", 1, 1.2, True, None)
tuple = "hola", 1, 1.2, True, None
print(type(tupla))
print(type(tuple))
print("-" * 20 ) #Separador

#Sets o conjuntos {}
conjuntos = {"hola", 1, 1.2, True, None}
print(type(conjuntos))
print("-" * 20 ) #Separador 

#Diccionarios {"clave": "valor"}
diccionario = {"nombre": "Gustavo", "edad" : 25, "cursos": "Python"}
print(diccionario)
print("-" * 20 ) #Separador

#Acceder a lista items
lista_verduras = ["tomate", "papa", "cebolla", "lechuga", "zanahoria", "pepino", "calabaza"]
#Posiciones
print(lista_verduras[0])
print(lista_verduras[-1])
#Index
print("Index")
print(lista_verduras[:2]) #Tomate, papa
print(lista_verduras[:4]) #Tomate, papa, cebolla, lechuga
print(lista_verduras[3:]) #Lechuga, zanahoria, pepino, calabaza
print(lista_verduras[5:]) #Pepino, calabaza
print("-" * 20 ) #Separador

#Acceder a tupla items
tupla_biblioteca = ("libro", "revista", "periodico", "comic", "novela", "cuento", "poesia") #7 indices y 6 posiciones
print(tupla_biblioteca[0])
print(tupla_biblioteca[:3])
print("-" * 20 ) #Separador

#Diccionarios
print(diccionario["nombre"])
print("-" * 20 ) #Separador

#Conjuntos o sets
print(conjuntos) #No se puede acceder a los elementos por posición, ya que es elemento inmutable
print("-" * 20 ) #Separador

#Agregando y eliminando elementos
lista_verduras.append("brocoli")
print(lista_verduras)
print("-" * 20 ) #Separador
tupla_biblioteca = tupla_biblioteca + ("ensayo",)
print(tupla_biblioteca)
nueva_tupla = list(tupla_biblioteca)
nueva_tupla.append("carta")
print(nueva_tupla)
print("-" * 20 ) #Separador

conjuntos.add("brocoli")
print(conjuntos)
print("-" * 20 ) #Separador

diccionario["pais"] = "México"
print(diccionario)
