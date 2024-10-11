#coding: utf-8

def script():
     #lista = list(range(6,13))
     for i in range (6,18,2):
          print(i)
          #print(lista)

def script2():
     soma = 0
     quantidade = 0
     n = float(input("Entre com o valor inical de n: "))
     while (n!=0):
        soma+=n
        quantidade=quantidade+1
        n = float(input("Entre com o valor de n, zero para sair: "))
        print("(Média = {:.2f})".format(soma/quantidade))

if __name__ == "__main__":
     script2()