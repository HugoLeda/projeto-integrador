# Fazer um algoritmo que leia um número inteiro e escreva o seu antecessor e o seu sucessor

i = 0
while (i != 1):
    def printAntecessorSucessor(numero):
        antecessor = numero - 1
        sucessor = numero + 1    
        print(f"O antecessor é: {antecessor}\nO sucessor é: {sucessor}")
        
    print("Mostar antecessor e sucessor\n")
    numero = int(input("Digite um número: "))

    printAntecessorSucessor(numero)    

    i = int(input("Digite 1 para sair: "))
