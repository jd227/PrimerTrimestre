#simular usuario contraseña y salir de la ejecucion del programa 
from getpass import getpass
import sys
usuario= {"jj":"lospollitos", "jp" : "alobebe123"}
print(" bienvenido al sistema de credencial.")
contador=0 
while contador <=3: 
    contador=+1
    user= input("ingresa tu nombre de usuario: ")
    clave=getpass("contraseña")
    if user == "jj" and clave == "lospollitos":
        print("manolete este es su cuenta. ")
        sys.exit()
    elif contador==1: 
        print(f"manito aqui no es. quedara yuka en dos intentos")
    elif  contador==2:
         print(f"manito aqui no es. quedara yuka en un intentos")
    elif contador ==3:
         print(f"manito aqui no es. quedo yuka mi papa ")
        
