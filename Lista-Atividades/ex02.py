vetor = [2.5,7.5,10.0,4.0]
soma = 0 

for valor in vetor:
    soma += valor
    
media = soma / len(vetor)

mais_proximo = min(vetor, key=lambda x: abs(x - media))

print(f"Média: {media}")
print(f"Valor mais próximo da média: {mais_proximo}")