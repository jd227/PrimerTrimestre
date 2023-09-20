import random
def oper(eleccion):
    a=random.randint(1,1000000)
    b=random.randint(1,1000000)
    if eleccion=="1":
        print("la suma es:",a,"+",b,"=",a+b)
    elif eleccion=="2":
        print("la resta es:",a,"-",b,"=",a-b)
    else:
        print("Valor erroneo, escoge 1, 2 o 3")
#bucle While
a=""
while a!='3':
    a=(input("Ingresa 1, para sumar, 2 para restar ó 3 para salir:"))
    if a=="3":
        break
    oper(a)
print("Gracias por utilizar nuestros servicios")