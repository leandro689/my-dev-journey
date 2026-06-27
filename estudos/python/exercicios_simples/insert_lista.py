lista = ['macaco','batata']
item_lista = input("Digite um item para sua lista: ")

if len(lista) == 0:
    lista.insert(0, item_lista)

else:
    posicao_lista = input(f'Sua lista tem "{len(lista)}" item(s), deseja escolher uma posição pro item adicionado?(caso digite "n", o item será inserido no final da lista) s/n: ')
    confirmar_posicao_lista = True

    while confirmar_posicao_lista:

        if posicao_lista.lower() == "s":
            confirmar_escolher_posicao_lista = True

            while confirmar_escolher_posicao_lista:
                escolher_posicao_lista = input('Digite a posição que deseja que o item fique: ')

                if not escolher_posicao_lista.isdigit():
                    print('Você só pode inserir digitos.')

                elif int(escolher_posicao_lista) <= 0 or int(escolher_posicao_lista) > (len(lista) + 1):
                    print("posicao inválida")

                else:
                    lista.insert(int(escolher_posicao_lista) - 1, item_lista)
                    confirmar_escolher_posicao_lista = False
            
            confirmar_posicao_lista = False

        elif posicao_lista.lower() == "n":
            lista.insert(len(lista), item_lista)
            confirmar_posicao_lista = False
        
        else: 
            print('Você não digitou uma opção válida. ')



for i, item in enumerate(lista, start=1):
    print(i, item)