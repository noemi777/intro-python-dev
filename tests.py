def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division =  a / b
    return suma, resta, multiplicacion, division
    #assert suma != 12
    #assert resta == 8  
    #assert multiplicacion == 20
    #assert division == 5
    
print(operaciones(10, 6))
