import random
nointervalo = []
foradointervalo = []

for i in range(0,10):
    numero = random.randint(0,30)
    if numero < 20 and numero > 10:
        nointervalo.append(numero)
    else:
        foradointervalo.append(numero)

print(f"Numeros dentro do intervalo entre [10,20]: {len(nointervalo)} ({nointervalo})")
print(f"Quantidade de numeros fora do intervalo entre [10,20]: {len(foradointervalo)} ({foradointervalo})")