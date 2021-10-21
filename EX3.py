#Construa  um  algoritmo  que,  dado  o  primeiro  elemento a1 e  a  razão r
# de  uma  progressão aritmética (PA), imprima todos os n primeiros elementos 
# da PA, onde a1, r e n são informados pelo usuário. 
# Lembre-se que uma PA pode ser crescente ou decrescente.

a1 = int(input('Digite um elemento: '))
r = int(input('Digite um valor para razao(r): '))
n = int(input('Digite um numero: '))
seq = input('Sequencia crescente ou decrescente? ')
i = 0
while i < n:
    if (seq == 'crescente'):
        print(a1, end=' ')
        a1 = a1 + r
        i += 1
    elif (seq == 'decrescente'):
        print(a1, end=' ')
        a1 = a1 - r
        i += 1