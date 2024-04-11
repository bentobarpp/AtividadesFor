while True:
    numero = int(input("Insira um valor de 1 a 10"))

    if numero > 10:
        print("Não aceito")
    elif numero < 1:
        print("Nao aceito")
    else:
        for i in range (1,11):
            print(f"{numero} x {i} = {numero * i}")

            break