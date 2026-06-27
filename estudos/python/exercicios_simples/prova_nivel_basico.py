# # Parte 2 — Exercícios práticos básicos
# Questão 5 — Validador de número positivo

# Crie um programa que peça um número ao usuário.

# O programa deve:

# Verificar se o usuário digitou apenas números.
# Converter para inteiro.
# Dizer se o número é positivo, negativo ou zero.

# Observação: pense no problema do sinal -.

# Valor: 10 pontos

import os

rodando = True
menu_programa = ['1 - Adicionar item na lista.','2 - Remover item da lista','3 - Listar itens','4 - Sair']
lista_compras = ["macaco","banana",'folha']
# estado do protrama
while rodando:
# apresentação menu
    print('Menu lista de compras: ')
    for i in menu_programa:
        print(i)

#escolha da opção desejada
    opcao_desejada = input("Digite o numero da opção desejada à cima: ")

# tratamento da entrada
    if not opcao_desejada.isdigit() or int(opcao_desejada) > len(menu_programa):
        print("você não digitou uma opção valida")
        continue

    opcao_desejada = int(opcao_desejada)     
#opções

    #Opção sair (4)
    if opcao_desejada == 4:
        validacao_saida = True
        
        # Validacao saida
        while validacao_saida:
            confirmacao_saida = input('Você esta saindo do programa, dese realmente sair? s/n: ')
            confirmacao_saida = confirmacao_saida.lower()

            if confirmacao_saida == "s":
                print('Perfeito, volte quando precisar')
                validacao_saida = False
                rodando = False

            elif confirmacao_saida == "n":
                confirmacao_saida = False
                break

            else:
                print("você não digitou uma opção valida")
        
    #Opção listar intens(3)
    elif opcao_desejada == 3:
        if len(lista_compras) == 0:
            print('Sua lista está vazia.')
        
        else:
            print('Os itens da sua lista são:')
            for i, item in enumerate(lista_compras, start = 1):
                print(i , item)


    #Opção remover item da lista(2)
    elif opcao_desejada == 2:
        validacao_remocao = True
        print('Segue itens da sua lista: ')
        for i, item in enumerate(lista_compras, start = 1):
                print(i , item)
        

        while validacao_remocao:
            remover_item = input(f'Digite o número do item que quer remover: ')

            if not remover_item.isdigit() or int(remover_item) > len(lista_compras):
                print("você não digitou uma opção válida")
                continue
            
            remover_item = int(remover_item)
            item_a_remover = lista_compras[remover_item - 1]
            confirmacao_remocao = True

            while confirmacao_remocao:
                remocao = input(f'O item selecionado a ser removido é o "{item_a_remover}", deseja seguir com a remoção? (S)im, (N)ão ou X para sair do menu de remoção. ')
                remocao = remocao.lower()

                if remocao == "s":
                    print(f'Perfeito, "{item_a_remover}" foi removida da sua lista. Segue lista atual:')
                    del lista_compras[remover_item - 1]

                    for i, item in enumerate(lista_compras, start = 1):
                        print(i , item)
                    confirmacao_remocao = False
                    validacao_remocao = False

                elif remocao == "n":
                    confirmacao_remocao = False
                
                elif remocao == "x":
                    confirmacao_remocao = False
                    validacao_remocao = False
                else:
                    print('Você digitou uma opção inválida')

    #Opção adicionar item na lista(1)
    if opcao_desejada == 1:
        adicionar_item = True

        while adicionar_item:
            item_a_adicionar = input('Digite um item para adicionar: ')

            if len(item_a_adicionar) <= 1:
                print('Você digitou não digitou um item ou digitou apenas uma letra, digite um item valido.')
                continue

            if item_a_adicionar.strip() in lista_compras:
                print('Item já consta na lista')
                continue

            lista_compras.append(item_a_adicionar)
            adicionar_item = False


print('Saiu do prgrama')