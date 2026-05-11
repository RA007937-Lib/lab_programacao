import random 

vetor =[]
contador = 0 

for i in range(50):
    dado = random.randint(1,6)
    vetor.append(dado)
    
    if dado == 6:
        contador +=1
        
porcentagem = (contador/50) * 100

print("Lançamentos", vetor)
print(f"Quantidade de vezes que o número 6 apareceu: {contador}")
print(f"Porcentagem:{porcentagem:.2f}%")