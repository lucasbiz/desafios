

def fibonacci (n):
    first = 0
    second = 1
    soma = 0
    while second <= n:
        soma = first + second
        second = first
        first = soma
    print(soma)

teste = int(input())
while teste < 0:
    print('O número deve ser maior ou igual a 0!')
    teste = int(input())

fibonacci(teste)
