# 4.     Crie um programa que copie um vetor de 10 posições de inteiros (preenchidos aleatoriamente), de trás para frente, em um segundo vetor. 

import random

vetor = [] 
vetorInverso = []

for i in range(10):  
  vetor.append(random.randint(0, 900))
  
for i in range(9, -1, -1):
  vetorInverso.append(vetor[i])
  
print(f"Vetor: {vetor}\nVetor Inverso: {vetorInverso}")