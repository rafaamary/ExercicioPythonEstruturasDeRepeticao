'''Escreva um programa para imprimir todos os números Armstrong entre 1 e 500. 
Se a soma dacada dígito elevado a n, onde n é quantidade de dígitos que o número
possui,for igual ao próprio número, então o número é chamado de número Armstrong.
Por exemplo, 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3)
'''

for n in range(1,500+1):
    lista = len(str(n))
    conta = 0
    num = n
    while num > 0:
        digito = num % 10
        conta += digito ** lista 
        num //= 10
    if n == conta:
        print('{} - Armstrong'.format(n))