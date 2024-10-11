def script():
    flag = False

    while True:
        if flag==True:
            break
        i=int(input("Escreva um número inteiro menor que 10: "))

        if (i<10):
            flag=True
            contador = 0
            while (i<20):
                i+=1
                print(i)
                contador+=1
            else:
                print (f"Total de sucessores = {contador}")
        else:
            print("O número tinha que ser menor que 10. ")

if __name__=="__main__":
    script()