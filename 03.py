# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.

def custoFinal(valorFabrica, pctDistribuidor=28, impostos=45):
    distribuidor = valorFabrica + ((valorFabrica * pctDistribuidor) / 100)
    valorImpostos = valorFabrica + ((valorFabrica * impostos) / 100)
    valorFinal = valorFabrica + distribuidor + valorImpostos
    return valorFinal

print("Calcular valor final do carro\n")
valorFabrica = float(input("Digite o custo de fábrica do carro: "))
print(f"Custo final ao consumidor: R$ {round(custoFinal(valorFabrica), 2)}")
    