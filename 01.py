# Leia um vetor de 10 valores inteiros e exiba todos os valores ímpares. 
import random

vetor = [] 

for i in range(10):  
  vetor.append(random.randint(0, 900))

vetorImpares = []
for i in vetor:
  if ((i % 2) != 0):
    vetorImpares.append(i)
    
print(f"Todos os valors: {vetor}")    
print(f"Valores impares: {vetorImpares}")