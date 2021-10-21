'''
7.A  sequência  de  Fibonacci  tem  papel  importante  na  explicação  de  
fenômenos  naturais. Ela  é também bastante utilizada para fins estéticos, 
pela sua reconhecida harmonia. Exemplo disso foi sua  utilização  na  construção 
do  Partenon,  em  Atenas.  A  sequência dá-se  inicialmente  por  dois números 1.
A partir do terceiro elemento usa-se a expressão: 
elemento n = elemento n-1 + elemento n-2.
Exemplo de sequência: 1, 1, 2, 3, 5,8, 13, ...
Construa um algoritmo que imprima na tela os n primeiros elementos da sequênciade Fibonacci, 
onde n é informado pelo usuário.
'''
n = int(input('Digite o valor de n: '))
i = 0
ProximoNum = 0
NumAnterior = 0
while(i < n):
    print(ProximoNum)
    ProximoNum = ProximoNum + NumAnterior
    NumAnterior = ProximoNum - NumAnterior
    if(ProximoNum == 0):
        ProximoNum = ProximoNum + 1
    i+=1

    