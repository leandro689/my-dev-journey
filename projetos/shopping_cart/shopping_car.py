# lista = ['macaco','baleia','cachorro','gato','tigre']
# inv_lista = []

# # for item_list in lista:
# #     inv_lista.insert(0,item_list)    

# # print(inv_lista)

# ranger_list = len(lista) - 1

# for i in range(-ranger_list):
#     print(i)
# 23:15

carrinho_compras = []
lista_completa = False

while lista_completa == False:

    # mostrar que o carrinho de compras está vazio
    if len(carrinho_compras) == 0:
        print('Seu carrinho de compras está vazio, vamos as compras (/*-*)/')
        

    add_carrinho = input('Digite o que deseja comprar, digite "sair" para sair da lista ou digite "remover" para excluir um item: ')

    # UX para sair do carrinho de compras
    if add_carrinho.lower() == 'sair':
        # Validação de itens dentro do carrinho
        if len(carrinho_compras) > 0:
            print('Seu carrinho ainda contempla alguns itens: ')
            for i in range(len(carrinho_compras)):
                print(i, carrinho_compras[i], sep="-")
            
            # Loop de saida
            conf_saida = False
            while conf_saida == False:
                # validação de saida
                val_saida = input('Tem certeza que deseja sair, a lista será deletada: S/N ')
                if val_saida.lower() == "s":
                    print('Perfeito, volte quando precisar!!')
                    conf_saida = True
                    lista_completa = True
                    continue
                
                elif val_saida.lower() == 'n':
                    print('Perfeito, vamos continuar, segue lista:')
                    for i in range(len(carrinho_compras)):
                        print(i, carrinho_compras[i], sep="-")

                    conf_saida = True
                    continue

                else:
                    print('Entrada invalida')
            continue

    # UX para remover item da lista
    elif add_carrinho.lower() == 'remover':
        print('Segue lista:')
        for i in range(len(carrinho_compras)):
            print(i, carrinho_compras[i], sep="-")
        exc_carrinho = input('Digite o numero do item à cima que deseja remover: ')
        
        if exc_carrinho.isdigit():
            print(f'Perfeito, "{carrinho_compras[int(exc_carrinho)]}" foi excluido da lista, segue lista atual: ')
            carrinho_compras.pop(int(exc_carrinho)) 
            for i in range(len(carrinho_compras)):
                print(i, carrinho_compras[i], sep="-")
            
        
        else:
            print('Você não digitou um numero')

        continue    
        


    # Validação dentro da lista
    if add_carrinho.lower() in carrinho_compras:
        print('Item já consta na lista, segue lista atual:')
        for i in range(len(carrinho_compras)):
            print(i, carrinho_compras[i], sep='-')
        continue

    carrinho_compras.append(add_carrinho)

    for i in range(len(carrinho_compras)):
        print(i, carrinho_compras[i], sep="-")




            

    

print('saiu')

    



    
    





    
            






    