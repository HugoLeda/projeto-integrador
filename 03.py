# 3.     Leia um vetor de 12 posições e em seguida ler também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y. 

import random

vetor = [] 

for i in range(12):  
  vetor.append(random.randint(0, 900))
  
print(f"Vetor completo: {vetor}") 
x = int(input("Digite uma posição do vetor para x: "))
y = int(input("Digite uma posição do vetor para y: "))

if (x < 0 or x > 11 or y < 0 or y > 11):
  print("Posição não encontrada no vetor!")
else:
  soma = vetor[x] + vetor[y]
  print(f"Soma das duas posições: {soma}")