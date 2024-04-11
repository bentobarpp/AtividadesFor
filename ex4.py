soma = 0
idades= 0
media = 0
for i in range (0,5):
    idade = int(input(f"Informe sua {i+1}idade"))
    idades.append (idade)
    soma += idade
    media = soma/len(idades)
print(f"A media de suas idades é {media}")