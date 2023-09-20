def descomponer_numero(numero):
    factores = {}  # Un diccionario para almacenar los factores y sus potencias
    divisor = 2
    
    while numero > 1:
        while numero % divisor == 0:
            if divisor in factores:
                factores[divisor] += 1  # Si el divisor ya está en el diccionario se incrementa la potencia
            else:
                factores[divisor] = 1  # Si es la primera vez, agregar el divisor con potencia 1
            numero //= divisor
        divisor += 1
    
    return factores

items = descomponer_numero(54)
print(items.keys())
print(items.values())
print (descomponer_numero(54))
