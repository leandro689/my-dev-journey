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



lista = ['macaco','banana','maca']

for i, item in enumerate(lista, start= 1):
    print(i, item, sep= " - ")



