a=int(input("ingresa el numero de filas: "))
b=int(input("ingresa el numero de columnas: "))

matriz= [[a],[b]]
for fila in range(a):
    for columna in range(b): 
        valor= int(input(f"ingresar el valor, que esta en la posicion {fila+1}.{columna+1}: "))
        matriz.append(valor)
print(matriz)

aux=0
suma=0 
negativo= False
cadena= int(input("ingresa el numerio: "))
for i in cadena:
    if i == "-":
        negativo= True 
        continue
    aux=int(i)
    suma+=aux 

print("la suma es: ", suma)