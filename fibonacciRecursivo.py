#Fibonacci Recursivo

def fibonacci(n):
    primeiroTermo = 0
    segundoTermo = 1
    cont = 0
    soma = 0
    while cont < n:
        soma = primeiroTermo + segundoTermo
        primeiroTermo = segundoTermo
        segundoTermo = soma
        cont +=1
    return primeiroTermo

def showFib():
    num = int(input('Informe a posição desejada: '))
    #Validacao do input
    while num < 0:
        print('O número deve ser maior ou igual a 0!')
        num = int(input('Informe a posição desejada: '))
    print(fibonacci(num))

#Chamando a funcao
showFib()