import operator
mayores = {}
menores = {}
edadAP= {'johao': 25, 'julian' : 20, 'adriana' : 16, 'dayan':31, 'sara': 16}
ordenado= dict(sorted(edadAP.items(), key=operator.itemgetter(0)))
for i,j in edadAP.items():
    if j < 18: 
        menores[i] = j 
    else:
        mayores[i] = j
    print(f"Aprendiz {i}, tiene {j} años. ")
print(mayores)
print(menores)