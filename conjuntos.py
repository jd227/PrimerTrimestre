import random

a = set()
b = set()
repeticiones = [0]  *10  # Crear una lista para contar las repeticiones de cada número

for i in range(random.randint(100, 500)):
    n = random.randint(0, 9)
    a.add(n) #el add es para agregar valores a los conjuntos 
    repeticiones[n] += 1

print("repeticiones de cada número en conjunto a:")
for i in range(10):
    print(f"Número {i}: {repeticiones[i]}")

for i in range(random.randint(100, 500)):
    n = random.randint(0, 9)
    b.add(n)
    repeticiones[n] += 1

print("repeticiones de cada número en conjunto b:")
for i in range(10):
    print(f"Número {i}: {repeticiones[i]}")

print("conjunto 'a':", a)
print("conjutno 'b':", b )

