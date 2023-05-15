"""
    métodos del lenguaje o del tipo de dato, como en cualquier lenguaje de programación 
    tienen métodos que ya vienen primitivos en el lenguaje y otros que dependen del tipo 
    de dato y Python no es la excepción
"""

### métodos primitivos
print("Hello World") # imprime cualquier cosa por la consola
len("Leonardo") # da la longitud de una lista, string, etc...
range(1, 11) # da la lista de números en el rango que se especificó
## etc...

### métodos dependientes del tipo de dato

## algunos métodos de strings
"leonardo".capitalize() # hace que la o las primeras letras de cada palabra sean mayúsculas+
"leonardo".upper() # vuelve toda la cadena en mayúscula
"leonardo".lower() # vuelve toda la cadena en minúscula
"leonardo".find("a") # retorna la posición en la que por primera vez aparece lo señalado y si no aparece retrona -1
"leonardo".rfind("e") # retorna la posición en la que por última vez aparece lo señalado y si no aparece retorna -1
"leonardo".count("e") # retorna la cantidad de veces que aparece lo señalado en el string
"leonardo".join(" josé") # retorna un nuevo string concatenado con el otro string señalado
"leonardo".startswith("l") # retorna True o False si el string empieza con lo señalado
"leonardo".endswith("o") # retorna True o False si el string termina con lo señalado
"leonardo".split("") # retorna una lista de todo el string separado de la forma que se quizo por lo señalado

## cortar strings y otras cosas
"leonardo"[::-1] # retorna el string al revés
"leonardo"[0] # retorna el caracter que se encuentra en la posición señalada (siempre se empieza desde 0)
"leonardo"[3:] # retorna el string cortado desde la posición señalada en adelante
"leonardo"[:2] # retorna el string cortado desde el principio hasta la posición señalada
"leonardo"[1:4] # retorna el string cortado en cierto intervalo señalado, pero sin contar la última posición del intervalo señalado

## algunos métodos de las listas
[1, 2, 3, 4, 5].append(6) # añade un elemento a lo último de la lista
[1, 2, 3, 4, 5].index(2) # retorna la posición en la que aparece pro primera vez el elemento señalado
[1, 2, 3, 4, 5].clear() # limpia la lista por completo y la deja vacia
[1, 2, 3, 4, 5].copy() # crea una copia exacta de la lista
[1, 2, 3, 4, 5].pop() # elimina el último elemento de la lista y lo retorna
[1, 2, 3, 4, 5].insert(3, 4.5) # añade un elemento señalado en la lista en una posición especifica ya señalada+
[1, 2, 3, 4, 5].remove(2) # elimina el elemento de la lista que primero coincida con el elemento señalado
[1, 2, 3, 4, 5].count(1) # retorna la cantidad de veces que aparece el elemento señalado en la lista
[1, 2, 3, 4, 5].reverse() # vuelve a la lista organizada al revés o en orden contrario
[1, 2, 3, 4, 5].sort() # vuelve a la lista ordenada
[1, 2, 3, 4, 5].extend([6, 7, 8]) # modifica la lista y le añade la lista señalada