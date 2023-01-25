#Primos linear

def primos(n):
    contadorExt = 0
    listaP = []
    #Os dois laços avaliam para cada um dos números anteriores a n se são primos
    while contadorExt <=n:
        contadorInt = 1
        divisores = 0
        while contadorInt <= contadorExt:
            if contadorExt % contadorInt == 0:
                divisores +=1
            contadorInt+=1
    # Se possuirem apenas 2 divisores serão adicionados a lista de primos
        if divisores == 2:
            listaP.append(contadorExt)
        contadorExt+=1
    print(listaP)


num = int(input('Informe o número desejado: '))
#Validacao do input
while num < 0:
    print('O número deve ser maior ou igual a 0!')
    num = int(input('Informe o número desejado: '))
#chamada da funcao
primos(num)