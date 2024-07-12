#Cadenas de texto o strings
nombre = "Juan"
numero = "1$%&/()="
comillasSimples = 'Casa'
comillasDobles = "Casa"
codena = """Casa"""
cadena2 = '''Casa'''
print(numero)
print(type(numero))
print(type(comillasSimples))
print(type(comillasDobles))
print(type(codena))
print(type(cadena2))

#Concatenación de texto
saludo = "Hola"
saludo2 = "Mundo"
cadenaConcatenada = saludo +  saludo2
print(saludo + " " + saludo2)
print(cadenaConcatenada)

cadena3 = "{} {}".format(saludo, saludo2)
print(cadena3)

cadena4 = f"{saludo} {saludo2}"
print(cadena4)
print(f"Hola {saludo2}")


#NoneType
nada = None
print(nada)