lista_carros = ['Fusca', 'Gol', 'Celta', 'Corolla', 'Ferrari']
lista_carros2 = ['Fusca', 'Gol', 'Celta', 'Corolla', 'Ferrari']

def test_lista_carros():
    """
    Definimos la funcion test_lista_carros, que compara si la lista_carros es igual a la lista_carros2,
    usamos la funcion assert para comparar si ambas listas son iguales. La palabra reservada assert se usa para
    comprobar si una condicion es True, si la condicion es False, se lanza una excepcion AssertionError.
    Usamos pytest para ejecutar el test. El comando sería: pytest testpy.py.
    """
    assert lista_carros == lista_carros2
    