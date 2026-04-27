hub_jogos = True
jogos = ['1 - forca']


import os

    
while hub_jogos:
    print(jogos)
    jogo = input('Eai meu consagrado, digite o numero do jogo que quer jogar: Caso queira sair digite "x": ')

    if jogo.lower() == 'x':
        print('Perfeito, volte quando quiser se divertir')
        hub_jogos = False

    elif jogo.isdigit() and int(jogo)== 1:
        palavra_secreta = input('Ola, vamos jogar forca, digite uma palavra: ')
        os.system('cls')
        letras_corretas = []
        letras_incorretas = []
        boneco = ['(/*-*)/']

        lista_letras_palavra_secreta = list(palavra_secreta.lower())
        form_palavra_secreta = ['*'] * len(palavra_secreta)

        while len(letras_incorretas) < 6 and form_palavra_secreta != lista_letras_palavra_secreta:
            nova_letra = input(f'Digite uma letra, você tem {6 - len(letras_incorretas)} tentativas: ')
            nova_letra = nova_letra.lower()
            os.system('cls')
            
    # ------------------------------- verificação de entrada de letra valida ----------------------------------
            if len(nova_letra) != 1:
                print('Você digitou mais de uma letra ou não digitou nada. :(')
                continue
    # ------------------------------- verificação de entrada de letra valida ----------------------------------

    # ---------------------------------- Validação de letra ja inclusa ----------------------------------------
            if nova_letra in letras_corretas or nova_letra in letras_incorretas:
                print('Você ja digitou essa letra. :(')
                print('\n'.join(boneco))
                print(f'Letras incorretas: {letras_incorretas}')
                print(f'Letras corretas: {letras_corretas}')
                print(''.join(form_palavra_secreta))
                continue
    # ---------------------------------- Validação de letra ja inclusa ----------------------------------------


    #----------------------------- Formação palavra para comparar com secreta----------------------------------
            if nova_letra in lista_letras_palavra_secreta:
                print(f'BOA, "{nova_letra}" esta na palavra secreta!!!')
                
                if nova_letra not in letras_corretas:
                    letras_corretas.append(nova_letra)

                for l in range(len(lista_letras_palavra_secreta)):
                    if nova_letra == lista_letras_palavra_secreta[l]:
                        form_palavra_secreta[l] = nova_letra
                        

            else:
                print(f'Sinto muito, a letra "{nova_letra}" não faz parte da palavra secreta :(')
                

                letras_incorretas.append(nova_letra)
                
    #----------------------------- Formação palavra para comparar com secreta----------------------------------
            
    #------------------------------------------Estilização erro -----------------------------------------------
            
            if len(letras_incorretas) == 1:
                boneco = [
                    " | ",
                    " O ",
                ]

                    
                    
            elif len(letras_incorretas) == 2:
                boneco = [
                    " | ",
                    " O ",
                    " | ",
                ]
                    
            elif len(letras_incorretas) == 3:
                boneco = [
                    " | ",
                    " O ",
                    "/|",
                ]
                    
            elif len(letras_incorretas) == 4:
                boneco = [
                    " | ",
                    " O ",
                    "/|\\",
                ]              
                    
            elif len(letras_incorretas) == 5:
                boneco = [
                    " | ",
                    " O ",
                    "/|\\",
                    "/"
                ]              

            elif len(letras_incorretas) == 6: 
                boneco = [
                    " | ",
                    " O ",
                    "/|\\",
                    "/ \\"
                ]
    
    #------------------------------------------Estilização erro -----------------------------------------------
            print('\n'.join(boneco))
            print(''.join(form_palavra_secreta))
            print(f'letras corretas até o momento: {letras_corretas}')
            print(f'letras incorretas até o momento: {letras_incorretas}')
    #----------------------------------- Consolidação do jogo -------------------------------------------------
        if form_palavra_secreta == lista_letras_palavra_secreta:
            os.system('cls')
            print("\n".join(boneco))
            print(f'Parabens!!! Você acertou a palavra secreta "{palavra_secreta}"')
            print(f'Você errou {len(letras_incorretas)} vezes. As letras incorretas foram {letras_incorretas}')

        else: 
            os.system('cls')
            print('Infelizmente você perdeu')
            print("\n".join(boneco))
            print(f'A palavra correta era {palavra_secreta}')


    else:
        print('Opção invalida')


# o que foi feio até agora:
# - validacao na listagem de letras ja digitadas
# - append em letras corretas e formaçao da palavra palavra_secreta
# - controle de erros 
# - game over com 6 erros 
# - estilização forca antiga
# - refatorção do boneco com a função join e \n pra quebra de linha do print
# - organizacao de estilização, para que não mostre as infos de como você ainda estivesse no jogo caso vc ganhe
# - Status de tentativas restantes 
# - entrada e saida do jogo

# Extra esse eu não esperava
# - Criado hub de jogas, apenas com a forca, mas pelo menos está estruturado, caso tenha um novo só subir na lista 

# Bugs encontrados durante o cod:
# seria utilizado o len(letras_incorretas) para contablizar a quantidade de erros, porem o while len(letras_incorretas) > 6 não está identificando
    # Resolução: Bug resolvido, antes estava efetuando a validação do numero de letras incorretas e nova palavra formada com ou, então se um dos dois estivesse valido o laço ainda continuaria rodando, alterado para função and