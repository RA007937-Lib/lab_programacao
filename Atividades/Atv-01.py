vetor = []

for i in range(10):
    valores = int(input(f"Digite o valor número {i+1}: "))
    vetor.append(valores)

valorDif = len(set(vetor))

print(f"Quantidade de números diferentes: {valorDif}")