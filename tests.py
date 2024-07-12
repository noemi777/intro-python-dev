#Funcion que recibe dos numeros como parametros (a, b) y devuelve la suma, resta, 
# multiplicacion y division de los mismos
def operaciones(a, b):
    #Esta funcion es usada en el archivo unittests.py para hacer pruebas unitarias usando unittest
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division =  a / b
    return suma, resta, multiplicacion, division
    
print(operaciones(10, 6))


def operaciones_dos(a, b):
    #Esta funcion es usada en el archivo tests.py para hacer pruebas unitarias manualmente
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division =  a / b
    #Puedes modificar los valores de los assert para que la prueba pase o los operadores de las variables
    assert suma == 12
    assert resta == 8  
    assert multiplicacion == 20
    assert division == 5
    
print(operaciones_dos(10, 2))

#Para realizar la prueba manual usa el comando python3 tests.py o python tests.py en la terminal