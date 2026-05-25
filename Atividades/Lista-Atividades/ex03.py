vetor = [1,2,3,4]
vetor2 = [10,20,30,40,50,60]

if len(vetor) <= len(vetor2):
    menor, maior = vetor, vetor2
else:
    menor, maior = vetor2, vetor
    
lista_intercalada =[]
for i in range(len(maior)):
    if (i < len(menor)):
        lista_intercalada.append(menor[i])
    lista_intercalada.append(maior[i])

print(f"Primeira lista: {vetor}")
print(f"Segunda lista: {vetor2}")
print(f"Lista intecalada: {lista_intercalada}")