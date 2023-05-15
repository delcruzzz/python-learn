"""
    operadores en Python son los que nos permiten operar entre variables o valores 
    para pbtener un resultado que necesitemos más dinámicamente
"""

### operadores aritméticos
print(1 + 1) # suma => +
print(12 - 5) # resta => -
print(2 * 2) # multiplicación => *
print(4 / 2) # división => /
print(4 % 2) # módulo o resto de la división
print(2 ** 2) # exponensiación

### operadore de incrementación y decrementación
# 1++ se incrementa de uno en uno
# 1-- se decrementa de uno en uno

### operadores de asignación
a = 1 # asignación simple
a += 1 # asignación con suma => a = a + 1
a -= 1 # asignación con resta => a = a - 1
a *= 1 # asignación con multiplicación => a = a * 1
a /= 1 # asignación con división => a = a / 1
a %= 1 # asignación con módulo => a = a % 1
a **= 1 # asignación con exponensiación => a = a ** 1

### operadores de comparación
# exclaimer(solo imprime un valor booleano True o False)
print(1 == 2) # son iguales?
print(2 != 3) # son diferentes?
print(1 < 2) # es menor qué
print(2 <= 1) # es menor o igual qué
print(1 > 0.2) # es mayor qué
print(2 >= 3) # es mayor o igual qué

### operadores lógicos
# exclaimer(solo imprime un valor booleano True o False)
print(1 > 0 and 2 < 9) # and, solo retorna True si todas las condiciones se cumplen, si no retorna False
print(1 < 0 or 3 > 2) # or, retorna False si ninguna condición se cumple, si se cumple al menos una retorna True
print(not(1 < 3)) # not, niega el valor que retorna la condición, si retorna la condición retorna False, 
# devuelve True y así en viceversa