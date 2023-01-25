

def fibonacci (n):
    first = 0
    second = 1
    soma = 0
    while first <= n:
        soma = first + second
        first = second
        second = soma
    print(first)


teste = int(input('Informe a posição desejada: '))
while teste < 0:
    print('O número deve ser maior ou igual a 0!')
    teste = int(input())

fibonacci(teste)
