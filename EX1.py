#1. Crie um algoritmo que, dado um número informado pelo 
# usuário, imprima a tabuadadele de 1 a 10. 
# Use o formato de apresentação (considerando que o 
# usuário informouo número 5):
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# etc...

n = 5
mult = 0
while mult < 10:
    mult += 1
    res = n * mult
    print(n, ' x ', mult, ' = ', res)