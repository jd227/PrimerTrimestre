#operadores de comparacion
"""
== igual  
!=  diferente 
< menor que 
> mayor que 
<= menor o igual que
>= mayor o igual que 

"""

nombre = input("Cuál es tu nombre?: ")
ciudad = input(f"De dónde eres {nombre}?: ")
país = input(f"En qué país queda {ciudad}?: ")
edad = int(input("Cuántos años tienes?: "))
requisito = 18

if edad >= requisito:
    if ciudad == "Medellín":
        print(f"Señor {nombre}, puedes ingresar a la discoteca y a la zona VIP.")
    else:
        print(f"Señor {nombre}, puedes ingresar a la discoteca.")
else:
    print(f"Señor {nombre}, no eres mayor de edad y por ser de {ciudad} no podrás ingresar a la discoteca.")