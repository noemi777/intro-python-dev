from funciones import persona, domicilio

"""
Los modulos en Python son archivos que contienen funciones, variables y declaraciones que se pueden utilizar en otros programas.
Para importar un modulo se utiliza la palabra reservada import seguido del nombre del modulo, o por medio de la palabra reservada from
seguido del nombre del modulo importar la funcion o variable que se desea utilizar.
"""
usarfuncion = persona("Gustavo", 57) #Llamando a la funcion persona y pasando los parametros
usardomucilio = domicilio("Av. Los Pinos", 123) #Llamando a la funcion domicilio y pasando los parametros
print(usarfuncion) 
print(usardomucilio)