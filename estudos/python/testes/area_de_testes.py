# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue

#     if i == 8:
#         print('i é 8, seu else não sera executado')
#         break

#     for j in range(1,3):
#         print(i, j)

# palavra = 'MACACO'

# palavra = palavra.lower()

# print(palavra)
#          -5        -4      -3       -2       -1
#           0         1       2        3        4
# lista = ['macaco', 'baleia', 'boi', 'gato', 'cachorro']
# inv_lista = []


# for i in range(-1,-len(lista)-1,-1):
#     inv_lista.append(lista[i])
    
    
# print(inv_lista)






# numeros = [1, 2, 3, 4, 5, 6, 7]


# i = 0
# while i <len(numeros):
#     if numeros[i] % 2 != 0:
#         del numeros[i]
#     else:
#         i +=1

# print(numeros)
# numeros.clear()

# numeros.append('lista limpa')
# macaco = "animal"
# numeros.insert(0, macaco)
# print(numeros)

# import random
# import os

# numero = random.randint(0, 3)

# if int(numero) == 0:
#     os.system('cls')
#     print("Opção Rerolar")
#     numero = random.randint(1, 3)
#     print(numero)


# else:
#     os.system('cls')
#     print(numero)

#  Programa de numeros aleatorios
# import random
# import os

# numero_aleatorio = random.randint(0,3)

# if numero_aleatorio == 0:
#     os.system('cls')
#     print("Selecione Opção Re Rolar")
#     numero_aleatorio = random.randint(1,3)
#     print(numero_aleatorio)

# else:
#     os.system('cls')
#     print(numero_aleatorio)

numeros = [2, 4, 6, 8]

while True:
    entrada = input(f'digite um numero para adicionar na lista ou digite "sair" para sair da lista: ')

    if entrada.isdigit():
        entrada = int(entrada)
        
        if numeros[len(numeros) - 1] < entrada:
            numeros.append(entrada)
            print(numeros)
            continue

        for i, item_lista in enumerate(numeros):
            if entrada > item_lista and entrada < numeros[i+1]:
                numeros.insert(i + 1, entrada)
        print(numeros)

    elif entrada.lower() == 'sair':
        print('saindo da lista, segue o que foi inserido até aqui: ')
        print(numeros)
        break

    else:
        print('entrada invalida')

