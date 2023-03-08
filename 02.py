# 2.     Leia um vetor de 6 valores reais e exiba a média, o maior e o menor valor. 

import random

vetor = [] 
soma = 0
maior = 0
menor = 0

for i in range(6):  
  vetor.append(random.random() * random.randint(0, 100))
  if (vetor[i] <= vetor[menor]):
    menor = i
  elif (vetor[i] >= vetor[maior]):
    maior = i
  
print(f"Vetor completo: {vetor}")
print(f"Menor: {vetor[menor]}\nMaior: {vetor[maior]}\nMédia: {sum(vetor) / 6}")