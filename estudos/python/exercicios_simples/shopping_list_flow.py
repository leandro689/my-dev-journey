# Nível 1 — Aquecimento (for + lista básico)
# 1. Lista reversa manual

# Crie uma lista com alguns nomes.
# Use for para criar uma nova lista invertida (sem usar [::-1]).


import os
programa_rodando = True
while programa_rodando == True:
    entrar_programa = input('Olá meu caro, vamos fazer as compras do Mês: S/N ')

    if entrar_programa.lower() == "n":
        print('Perfeito, volte quando precisar!! :)')
        programa_rodando = False

    elif entrar_programa.lower() == "s":
        lista_compras = []
        comp_list_final = False
        print('Perfeito, vamos começar, primeiro vamos decidir o que vamos comprar, vamos fazer uma lista.')
        
        while comp_list_final == False:
            list_add = input('Adicione um item na lista, ou digite "sair" para finalizar a lista: ')

            if list_add in lista_compras:
                print('Item já foi adicionado a lista anteriormente')
                continue

            if list_add.lower() == "sair":
                print('aqui encerramos a lista, seus itens são: ')
                print(lista_compras)
                comp_list_final = True
                continue

            lista_compras.append(list_add)
            print(f'Sua lista de compras já tem {len(lista_compras)} itens e os itens são: ')
            print(lista_compras)

        itens_comprados = []
        itens_comprar = len(lista_compras)
        os.system('cls')

        while len(itens_comprados) < itens_comprar:
            for itens_faltantes in range(len(lista_compras)):
                print(itens_faltantes, lista_compras[itens_faltantes])

            compra_item = input('Qual item vamos comprar? Digite o numero do item na lista: ')

            try:
                int(compra_item)

            except:
                print('Você não digitou um numero')
                continue
            
            if int(compra_item) > len(lista_compras):
                print('O numero digitado não está na lsita!!!')
                continue

            encontrou_item = input(f'encontrou o item "{lista_compras[int(compra_item)]}"? ')

            if encontrou_item.lower() == 's':
                itens_comprados.append(lista_compras[int(compra_item)])
                print(f'itens comprados {itens_comprados}')
                del lista_compras[int(compra_item)]
                print(f'itens faltantes {lista_compras}')
                programa_rodando = False
                
        print('Compras finalizadas, foi comprado:')
        print(itens_comprados)

                


    else:
        print('Opção invalida')



