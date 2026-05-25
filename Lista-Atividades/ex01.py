import random
lista1=[]
lista2=[0,0,0,0,0,0]

for e in range(100):
    lista1.append (random.randint(1,6))
print (lista1)
for i in range (6):
    lista2[i] = lista1.count(i+1)
print(lista2)
