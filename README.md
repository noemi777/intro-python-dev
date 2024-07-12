# 💻 Introducción a Python

Este repositorio contiene ejercicios y ejemplificaciones de sintaxis de Python, estructuras de control, operadores, etc. 
La finalidad es proporcionar una introducción al lenguaje de programación de Python, de forma que la interación y aprendeiza fuera practica. 

## :gear: Instalación 
Para usar el repositorio, realiza un **FORK** del repositorio y clona el repositorio localmente. Sigue las siguientes instrucciones:

1. Realiza un fork del repositorio.
2. Clona el repositorio localmente:

```
git clone <link del repositorio>
```
3. En VSCode crea un ambiente virtual para Python, asegúrate de haber instalado Python.

```
python --version
```
```
pip --version
```
```
python -m venv env
```
4. Activa el entorno virtual
   
   (Windows)
   ```env/Scripts/activate```
   
  (Ubuntu)
  ```source env/bin/activate```

   
## :pushpin: Uso

Para comenzar a usar cada uno de los archivos, abre tu terminal en VSCode o usa la terminal de PowerShell o Ubuntu. 
> El VSCode puedes abrir la terminal usando el comando ```Ctrl+Shift+ñ``` o en la barra superior busca ```...``` y selecciona ```Terminal```
> No olvides guardar el archivo antes de usar el comando, puedes activar el Auto Save de VSCode, o simplemente usar ```CTRL+S```
* Usa el siguiente comando:
  ``` python <nombredelarchivo>.py```
  > Ejemplo: ```python cadenas.py```

### Para las pruebas en Python

Los ficheros que corresponden a las pruebas unitarias son los siguientes:
  > tests.py
> 
  > unittests.py
> 
  > testpy.py

***Usa los siguientes comandos respectivamente para cada uno de los ficheros.***

  > Para el fichero tests.py usa:
> 
   ``` python tests.py ```
   
  > Debes visualizar lo siguiente en la terminal.
   ```
(16, 4, 60, 1.6666666666666667)
None
```
  > Para el fichero unittests.py
> 
  ```python unittests.py```
> Debes visualizar lo siguiente en la terminal.

```
(16, 4, 60, 1.6666666666666667)
None
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
> Para el fichero de testpy.py
 >
> 
   ```pytest testpy.py```

> Debes visualizar lo siguiente en la terminal.
```
================================================================= test session starts =================================================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: C:\Users\annco\Documents\intropython
collected 1 item

testpy.py .                                                                                                                                      [100%]

================================================================== 1 passed in 0.03s ==================================================================
```
## Documentación de Python :link:

Los siguientes recursos es documentación de Python.

[Entornos virtuales](https://docs.python.org/es/3/tutorial/venv.html)

[W3School Python Tutorial](https://www.w3schools.com/python/default.asp)

[Python Tutorial](https://docs.python.org/3/tutorial/index.html)

[Estructuras listas, tuplas, diccionarios, sets](https://docs.python.org/3/tutorial/datastructures.html)

[Modulos en Python](https://docs.python.org/3/tutorial/modules.html)

[Errores y excepciones](https://docs.python.org/3/tutorial/errors.html)

[Clases en Python](https://docs.python.org/3/tutorial/classes.html)

[Estructuras de control](https://docs.python.org/es/3/tutorial/controlflow.html)

[Libro de Python](https://ellibrodepython.com/)

## :pencil: Recursos para prácticar con ejercicios 

Ofrecer ejercicios de python por niveles desde básicos hasta avanzados, puedes acceder a otros lenguajes de programación [CodeSignal](https://app.codesignal.com/)

Juego para aprender Python, también cuenta con la opción de jugar con otros lenguajes de programación [Codedex](https://www.codedex.io/python)

Te proporciona ejercicios para ejercicios para mejorar tu lógica de programación [Codewars](https://www.codewars.com/)

Crea juegos mientras aprendes a programar [Codinggame](https://www.codingame.com/start/)

## :nerd_face: Algunos ejercicios básicos y sencillos de práctica

Crea los ficheros necesarios, o crea un solo fichero llamado  ```actividades.py```

1. Declara una variable con tu nombre completo.
2. Declara dos variables con cadenas, el contenido puede ser a tu gusto, y concaténalas. Puedes usar cualquier formato para concatenar. 
3. Declara una variable con un número entero y otra variable con un número flotante. 
   - Realiza una operación de suma entre el entero y el flotante. 
   - Convierte el número flotante a entero y realiza la misma operación de suma.
4. Calcula la suma de 15 y 20, crea dos variables para almacenar los números.
5. Calcula el producto de 7 y 8, crea dos variable para almacenar los números.
6. Divide 56 entre 8 y muestra el resultado, crea dos variable para almacenar los números.
7. Calcula el módulo de 15 dividido entre 4, crea las variables correspondientes.
8. Verifica si 10 es mayor que 7.
9. Verifica si 3 es igual a 5.
10. Comprueba si 8 es diferente de 8.
11. Verifica si 12 es menor o igual a 12.
12. Usa el operador not para invertir el resultado de una comparación: 5 es mayor que 10.
13. Crea una lista con los números del 1 al 10.
14. Agrega el número 11 al final de la lista.
15. Elimina el primer elemento de la lista.
17. Crea un diccionario que contenga la información de un libro: título, autor, año de publicación y género.
18. Agrega una clave "ISBN" con un valor adecuado.
19. Modifica el año de publicación.
20. Elimina la clave "género".
21. Crea un conjunto con los números pares del 1 al 10.
22. Añade el número 12 al conjunto.
23. Elimina el número 4 del conjunto.
24. Crea una tupla con los días de la semana.
25. Accede y muestra el tercer día de la semana.
26. Intenta cambiar el valor del primer día de la semana (observa qué sucede).
26. Crea una lista de frutas.
27. Usa el método .append() para agregar una nueva fruta a la lista.
28. Usa el método .remove() para eliminar una fruta específica.

***No olvides que puedes usar la palabra reservada print()***

