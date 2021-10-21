'''
Escrever um algoritmo que leia uma quantidade números inseridos pelo usuário 
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], 
[51-75] e [76-100]. 
A entrada de dados deve terminar quando for lido um número negativo.
'''
n = 0
n0_25 = 0
n26_50 = 0
n51_75 = 0
n76_100 = 0
while (n >= 0):
    n = int(input('Digite um numero: '))
    if (n < 0):
        print('FIM!! Numero Negativo') 
    else:
        if(n>= 0 and n <= 25):
            n0_25 = n0_25 + 1
        elif (n>=26 and n<=50):
            n26_50 += 1
        elif (n>=51 and n<=75):
            n51_75 += 1
        elif (n>=76 and n<=100):
            n76_100 += 1
print('[0-25] = ', n0_25)
print('[26-50] = ', n26_50)
print('[51-75] = ', n51_75)
print('[76-100] = ', n76_100)