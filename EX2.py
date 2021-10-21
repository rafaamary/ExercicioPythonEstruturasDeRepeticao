#2. Escreva um programa para encontrar o valor fatorial de um número 
#n digitado pelo usuário. O fatorial de um número n é da forma 
#n! = n* (n -1) * (n -2) * ... * 2* 1
# Exemplo: 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

n = int(input('Digite um numero: '))
fatorial = 1
i = 2
while i <= n:
    fatorial = fatorial * i
    i = i + 1
    
print('O valor de ', n,'! = ',fatorial) 
