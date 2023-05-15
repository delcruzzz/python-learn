"""
    las funciones en Python cómo en cualquier otro lenguaje sirven para ahorrarnos 
    código y tiempo, manejar orden y ser recursivos, además utilizar código dinámico

    las funciones, pueden recibir parámetros como puede que no, los parámetros son como 
    variables en un scope en especifico que solo se pueden utilizar dentro de esa función, 
    también pueden retornar un valor o no pueden retornar nada
"""

### funciones
def add_two_numbers_without_parameters(): 
    print(1 + 1) # solo imprime el valor y no retorna ningún valor

add_two_numbers_without_parameters()

"""
    esta función no retorna ningún valor ni usa parámetros, solo hace 
    una operación, esto nos ayuda si en más de una parte necesitamos hacer 
    esa operación, solo sería llamarla y listo, el código se ejecuta solo
"""

def add_two_numbers_with_parameters(num_one, num_two): 
    print(num_one + num_two)

add_two_numbers_with_parameters(1, 3) # solo imprime el valor y no retorna ningún valor

"""
    esta función no retorna nigún valor pero si usa parámetros, estos 
    se declaran al momento de crear la función y se operan dentro de ella, 
    los valores a los parámetros se los pasamos cuando llamamos a la función 
    y listo imprime el valor por consola
"""

def token_for_role_user(role_user): 
    if(role_user == "superuser"): 
        return "Aklo346.9.uijkKOLLLpp"
    elif(role_user == "user"): 
        return "AAAmmko3.4.5kiii.9"
    else: 
        return "not found role user {}".format(role_user)
    
token = token_for_role_user("admin")
print("token: {}".format(token))

"""
    esta función si retorna y además si usa parámetros, es bastante completa 
    entonces recibimos un parámetro que se opera dentro de condicionales para 
    evaluar su valor, además dependiendo del role devuelvo un token diferente 
    entonces esta función si retorna un valor, este valor lo podemos imprimir 
    al momento de llamar la función con el método print() o lo podemos guardar 
    en una variable y seguir utilizandolo a lo largo del proyecto
"""

def default_params(name, age = 2): 
    print("my name is {} and age {}".format(name, age))

default_params("leonardo", 20)
default_params("sebastian")

"""
    esta función recibe dos parámetros pero hay uno que ya viene con un valor 
    asignado, eso viene siendo un valor por default, o sea que si al momento de 
    llamar a la función no se le cambia el valor parámetro toma el valor que se 
    le asigno al momento de crear la función
"""