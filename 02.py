# Ler uma medida em polegadas e imprimir a equivalente em centímetros, sabendo que 2.54 cm equivale a 1 polegada.

def polegadaParaCm(medida):
    cm = medida / 2.54
    return cm

print("Converter polegada para centimetro\n") 

medida = float(input("Digite a medida em polegada: "))
print(f"{medida} em centimetros é igual a: {polegadaParaCm(medida)}")