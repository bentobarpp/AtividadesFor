numero = int(input("Insira um numero para verificar a divisão: "))
divisao = []
for i in range(1, (numero + 1)):
    if numero % i == 0:
        divisao.append(i)

print(f"divisores: {divisao}")