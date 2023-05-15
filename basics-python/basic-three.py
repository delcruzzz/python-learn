"""
    En Python cómo en cualquier lenguaje existen tipos de datos aunque 
    Python no sea un lenguaje de programación fuertemente tipado y no 
    se puede establecer el tipo de dato de la variable, pero el mismo 
    lenguaje se encarga de darle el tipo de dato a la variable
"""

var_one = 1 ### int
var_two = 2.89 ### float
var_three = "Cadena de texto" ### string
var_four = False ### boolean
var_five = 2j ### complex !!!no se va a explicar todavía
var_six = [1, 2, 3, "leonardo", False, True, 4j] ### list
var_seven = {
    "name": "leonardo", 
    "age": 20
} ### dictionary
var_eight = ("hello", 3, True) ### tuple
var_nine = {"item 1", "item 2", "item 3", "item 4", "item 5", "item 6",} ### set

"""
    explicación de cada uno de los tipos de datos

    int => números enteros
        =====> cómo su nombre lo dice, eso son, números positivos o negativos pero enteros
    
    float => números de coma flotante
        =====> son números que tienen una coma entre ellos

    string => cadena de texto
        =====> cómo su nombre, cierta cantidad de caracteres dentro de unas comillas simples 
        o dobles

    boolean => booleanos
        =====> son dos tipos de datos, verdadero = True o falso = False

    list => lista
        =====> cómo su nombre lo dice, es una lista o array que recibe cualquier tipo de datos 
        y que se puede utilizar para varias cosas y es solo valor, y se busca por posición

    dictionary => diccionario
        =====> es un tipo de dato clave valor, cada valor tiene su identificador, se busca por 
        su identificador, el identificador es un string, y el valor puede ser cualquier tipo de 
        dato

    tuple => tupla
        =====> es un tipo de dato el cual es un conjunto inmutable y ordenado de elementos del 
        mismo o diferente tipo de dato

    set => set
        =====> es un tipo de dato que se utiliza para guardar una colección de datos sin orden 
        alguno, pero todos sus datos son únicos
"""