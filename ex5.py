import random
pares = []
impares = []

for i in range (0,10):
    numero = random.randint(0,100)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Os numeros pares: {len(pares)} ({pares})")
print(f"Os numeros impares: {len(impares)} ({impares})")