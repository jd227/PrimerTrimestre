
numero = int( input("ingresa el numero de la tabla que quieres: "))

if numero <= 0:
    print("multiplicacion no valida")
else:
    if numero > 0:
        print(f"tabla del multiplicar del numero {numero}")
valor=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for factor in valor:
    resultado = numero * factor
    print(f"{numero}*{factor} = {resultado}")
