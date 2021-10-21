'''
Escreva  um  programa  que  leia  um  conjunto  de  inteiros  e,  
em  seguida,  imprima  a  soma  dos inteiros pares e ímpares.
'''
lista = list(map(int, (input('Digite um conjunto de numeros inteiros: '))))
print(lista)
qtd = len(lista) #qtd de itens na lista
somaPar = 0
somaImpar = 0
n = 0
while n <= qtd: 
    for n in range(n, qtd):
        valor = lista[n]
        if (valor%2==0):
            somaPar = somaPar + valor
            n += 1
            continue
        if (valor%2!=0):
            somaImpar = somaImpar + valor
            n += 1
        else:
            continue
    break
print('A soma dos numeros pares: ', somaPar)
print('A soma dos numeros impares: ', somaImpar)