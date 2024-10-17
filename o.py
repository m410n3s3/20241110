
# a=float(input())
# b=float(input())
# x=a+b
# print("X = {:.0f}".format(x))

N = int(input("Escreva o número de repetições: "))
contador = 0

def funcao():
    S = int(input("Escreva o número real: "))
    QT = int(input("Escreva a quantidade de alunos: "))
    while True:
        palpites = list(map(int, input(f"Digite {QT} palpites, separados por espaço: ").split()))
        if len(palpites) == QT:
            break
        else:
            print(f"Repete, insira exatamente {QT} palpites.")

    melhor_palpite = None
    menor_diferenca = float('inf')
    
    for palpite in palpites:
        diferenca = abs(S - palpite)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            melhor_palpite = palpite
            
    print(f"O melhor palpite é: {melhor_palpite}")

if __name__ == "__main__":
    while contador < N:
        funcao()
        contador += 1
