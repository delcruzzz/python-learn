"""
    las condicionales en Python cómo en cualquier lenguaje de programación sirven 
    para evaluar condiciones o restricciones y tener más control sobre el código

    un ejemplo, digamos que tenemos un programa dónde los usuarios tiene roles, pero 
    ciertos roles pueden ingresar a la ruta de panel de administrador, solo superadmin 
    y admin, entoces necesitamos validar el rol del usuario con una condicional y de 
    ahí validar, y tenemos más control sobre el código y el programa
"""

### sentencias

## if, elif, else

"""
    if ====> si pasa esto
    elif ====> pero si pasa esto
    else ====> no pasó ninguna de las anteriores, que pase esta
"""

role_user = "superadmin"

if role_user == "superadmin" or role_user == "admin": 
    print("puedes acceder a: \n api/dashboard/protected")
elif role_user == "expert":
    print("todavía no tiene los permisos necesario para acceder al dasboard")
else: 
    print("rol desconocido")