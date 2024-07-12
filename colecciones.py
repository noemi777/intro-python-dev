#Colecciones, lista, tuplas, diccionarios, conjuntos(sets)
#Listas []
lista = ["hola", 1, 1.2, True, None]
#print(lista)
#print(type(lista))

tupla = ("hola", 1, 1.2, True, None)
tuple = "hola", 1, 1.2, True, None
#print(type(tupla))
#print(type(tuple))

conjuntos = {"hola", 1, 1.2, True, None}
#print(type(conjuntos))

diccionario = {"nombre": "Gustavo", "edad" : 25, "cursos": "Python"}
#print(diccionario)

#Acceder a lista items
lista_verduras = ["tomate", "papa", "cebolla", "lechuga", "zanahoria", "pepino", "calabaza"]
#Posiciones
#print(lista_verduras[0])
#print(lista_verduras[-1])
#Index
#print("Index")
#print(lista_verduras[:2]) #Tomate, papa
#print(lista_verduras[:4])
#print(lista_verduras[3:])
#print(lista_verduras[5:])


#Acceder a tupla items
tupla_biblioteca = ("libro", "revista", "periodico", "comic", "novela", "cuento", "poesia") #7 indices y 6 posiciones
print(tupla_biblioteca[0])
print(tupla_biblioteca[:3])

#Diccionarios
print(diccionario["nombre"])

#Conjuntos o sets
print(conjuntos) #No se puede acceder a los elementos por posición, ya que es elemento inmutable

#Agregando y eliminando elementos
lista_verduras.append("brocoli")
print(lista_verduras)

tupla_biblioteca = tupla_biblioteca + ("ensayo",)
print(tupla_biblioteca)
nueva_tupla = list(tupla_biblioteca)
nueva_tupla.append("carta")
print(nueva_tupla)


conjuntos.add("brocoli")
print(conjuntos)

diccionario["pais"] = "Peru"
print(diccionario)
