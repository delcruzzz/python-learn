"""
    los bucles en Python como en cualquier lenguaje de programación permite hacer alguna 
    acción del código repetitivamente pero de forma controlada y poder repetirlo dinámicamente
"""

### bucle for
langs = ['en', 'es', 'fa', 'fi', 'fr']

for lang in langs: 
    print("lang =====> {}".format(lang))

for i in range(1, 11): 
    print("i =====> {}".format(i))

"""
    el bucle for es el que normalmente se usa cómo iterador, tanto para recorrer strings y 
    listas, un ejemplo es imprimir una lista de usuarios por consola
"""

### bucle while
a = 0
i = 0

while a < 10: 
    print("Hello")
    a += 1

while i < len(langs): 
    print(i)
    i += 1

"""
    en el ciclo while es necesario tener bastante cuidado ya que tiende a poder terminar 
    siendo un bucle infinito si no se controla bien, y este bucle solo para de ejecutarse 
    cuando la condición que hace que empiece ya no es verdadera o se cumple
"""