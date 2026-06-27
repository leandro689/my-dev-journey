
carrinho_compras = []
lista_completa = False

while not lista_completa:

    # mostrar que o carrinho de compras está vazio
    if len(carrinho_compras) == 0:
        print('Seu carrinho de compras está vazio, vamos as compras (/*-*)/')
        

    add_carrinho = input('Digite o que deseja comprar, digite "sair" para sair da lista ou digite "remover" para excluir um item: ')

    # UX para sair do carrinho de compras
    if add_carrinho.lower() == 'sair':
        # Validação de itens dentro do carrinho
        if len(carrinho_compras) > 0:
            print('Seu carrinho ainda contempla alguns itens: ')
            for i, item in enumerate(carrinho_compras, start=1):
                print(i, item, sep=" - ")
            
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
                    for i, item in enumerate(carrinho_compras, start=1):
                        print(i, item, sep=" - ")

                    conf_saida = True
                    continue

                else:
                    print('Entrada invalida')
            continue
        
        else:
            print('Perfeito, volte quando precisar!!')
            lista_completa = True
            continue

    # UX para remover item da lista
    elif add_carrinho.lower() == 'remover':
        print('Segue lista:')
        for i, item in enumerate(carrinho_compras, start=1):
            print(i, item, sep=" - ")
        exc_carrinho = input('Digite o numero do item na lista à cima que deseja remover: ')

        if exc_carrinho.isdigit():

            if int(exc_carrinho) > len(carrinho_compras) or int(exc_carrinho) == 0:
                print(f'O numero "{exc_carrinho}" não consta na lista')
                for i, item in enumerate(carrinho_compras, start=1):
                    print(i, item)
                continue

            print(f'Perfeito, "{carrinho_compras[int(exc_carrinho) - 1]}" foi excluido da lista, segue lista atual: ')
            carrinho_compras.pop(int(exc_carrinho) - 1) 
            for i, item in enumerate(carrinho_compras, start=1):
                print(i, item, sep=" - ")
            
        
        else:
            print('Você não digitou um numero')

        continue    
        


    # Validação dentro da lista
    if add_carrinho.lower() in carrinho_compras:
        print('Item já consta na lista, segue lista atual:')
        for i, item in enumerate(carrinho_compras, start=1):
            print(i, item, sep=" - ")
        continue

    carrinho_compras.append(add_carrinho)

    for i, item in enumerate(carrinho_compras, start=1):
        print(i, item, sep=" - ")



print('saiu')
