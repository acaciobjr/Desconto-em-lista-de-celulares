# Desconto-em-lista-de-celulares
Descontos aplicados em preços de uma lista 

import funcao as funcao

celulares = ['iphone11', 3989, 'iphone12', 4369, 'iphone12Pro', 7000,
              'galaxyS20', 3133, 'galaxyS21', 3400, 'galaxyS21Ultra', 4304,
              'MotoG10', 1259, 'MotoG30', 2222, 'MotoG60', 2117]

print('#'*35)
print(f'{"LISTA DE PREÇOS":>25}')
print('#'*35)

for pos in range(0, len(celulares)):
    if pos % 2 == 0:
        print(f'{celulares[pos]:<23}', end='')
    else:
        print(f'R${celulares[pos]:>7.5f}')

print('Esses são os aparelhos e seus preços em nossa loja.\nNo mês de nosso aniversário, qualquer aparelho acima de 3200 reais tem 10% de desconto.\nAbaixo de 3200, qualquer aparelho com 5%.')

divisao = input('Escolha seu aparelho:')
if divisao == 'iphone11':
    print('O valor do aparelho ficou', 'R$',celulares[1]*0.9)
elif divisao == 'iphone12':
    print('O valor do aparelho ficou', 'R$',celulares[3]*0.9)
elif divisao == 'iphone12Pro':
    print('O valor do aparelho ficou', 'R$',celulares[5]*0.9)
elif divisao == 'galaxyS20':
    print('O valor do aparelho ficou', 'R$',celulares[7]*0.95)
elif divisao == 'galaxyS21':
    print('O valor do aparelho ficou', 'R$',celulares[9]*0.9)
elif divisao == 'galaxyS21Ultra':
    print('O valor do aparelho ficou', 'R$',celulares[11]*0.9)
elif divisao == 'MotoG10':
    print('O valor do aparelho ficou', 'R$',celulares[13]*0.95)
elif divisao == 'MotoG30':
    print('O valor do aparelho ficou', 'R$',celulares[15]*0.95)
elif divisao == 'MotoG60':
    print('O valor do aparelho ficou', 'R$',celulares[17]*0.95)

else:
    print("Desculpe não entendi!")
    return funcao()
funcao()
