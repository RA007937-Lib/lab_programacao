vetor = []

for i in range(5):
    valores = int(input(f"Digite o {i+1}° valor: "))
    vetor.append(valores)

x = int(input(f"Digite o valor à ser buscado: "))

if x in vetor:
    print(vetor.index(x))

else:
    print(-1)