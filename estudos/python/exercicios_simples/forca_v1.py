# palavra_secreta = input('Ola jogador, vamos jogar forca? Digite uma palavra e não mostre a ninguém: ')
# conversao = (len(palavra_secreta)*"*")
# palavra_formatada = ''
# tentativa_acerto = 0
# tentativa_erro = 0
# letras_acertadas = ''
# letras_faltantes = conversao.count('*')
# jogando = True





# while palavra_formatada.lower() != palavra_secreta.lower() and tentativa_erro <= 5:
#     entrada_letra = input('Digite uma letra: ')

#     if len(entrada_letra) == 1:
            
#         if entrada_letra.lower() in palavra_secreta.lower():
#             tentativa_acerto += 1
#             letras_acertadas += entrada_letra.lower()

#             palavra_formatada = ''
                
#             for letra in palavra_secreta.lower():
#                 if letra in letras_acertadas.lower():
#                         palavra_formatada += letra
#                 else:
#                     palavra_formatada += "*"
#             print(palavra_formatada)
#             letras_faltantes = palavra_formatada.count('*')
#             if letras_faltantes > 0:
#                 print(f'Ainda faltam {letras_faltantes} letras')
                        
                        

#         else:
#             print('não tem a letra')
#             tentativa_erro += 1
#             if tentativa_erro == 1:
#                 print(' | ')
#                 print(' O ')
#                 print(f'ainda faltam {letras_faltantes} letras')
#             elif tentativa_erro == 2:
#                 print(' | ')
#                 print(' O ')
#                 print('/|')
#                 print(f'ainda faltam {letras_faltantes} letras')
#             elif tentativa_erro == 3:
#                 print(' | ')
#                 print(' O ')
#                 print('/|\\')
#                 print(f'ainda faltam {letras_faltantes} letras')
#             elif tentativa_erro == 4:
#                 print(' | ')
#                 print(' O ')
#                 print('/|\\')
#                 print('/ ')
#                 print(f'ainda faltam {letras_faltantes} letras')
#             elif tentativa_erro == 5:
#                 print(' | ')
#                 print(' O ')
#                 print('/|\\')
#                 print('/ \\')
#                 print(f'Você perdeu, faltando "{letras_faltantes}" letras... A palavra correta era "{palavra_secreta.lower()}"')
#                 break
                
                    

#     else:
#         print('Você não digitou apenas uma letra: ')


# if tentativa_erro == 5:
#     print("Sinto muito!!!")
#     tentativa_erro = 0
#     tentativa_acerto = 0
    

        
# else:
#     print(f'BOA, VOCÊ CONSEGUIU, A PALAVRA SECRETA É "{palavra_secreta.lower()}"!!! Você resolveu em {tentativa_acerto+tentativa_erro} tentativas')
#     tentativa_erro = 0
#     tentativa_acerto = 0

import os
jogando = True

while jogando == True:
    palavra_secreta = input('Ola jogador, vamos jogar forca, digite uma palavra: ')
    conversao = len(palavra_secreta)*'*'
    palavra_formatada = conversao
    tentativas_acerto = 0
    tentativas_erro = 0
    palavra_secreta = palavra_secreta.lower()
    letras_acertadas = ''
    letras_erradas = ''
    formatacao_erro = ''

    while palavra_formatada != palavra_secreta and tentativas_erro <= 6:
        entrada_letra = input('Digite apenas uma letra: ')
        entrada_letra = entrada_letra.lower()

        if len(entrada_letra) > 1:
            print('Você digitou mais de uma letra!!')
            continue

        if entrada_letra in palavra_secreta:
            if entrada_letra in letras_acertadas:
                print('Você ja digitou essa letra anteriormente!!')
                continue

            letras_acertadas += entrada_letra
            palavra_formatada = ""
            tentativas_acerto += 1

            

            for letra in palavra_secreta:
                if letra in letras_acertadas:
                    palavra_formatada += letra
                else:
                    palavra_formatada += '*'
            print(palavra_formatada)
            
        
        else:
            if entrada_letra in letras_erradas:
                print('Você ja digitou essa letra anteriormente!!')
                continue
            tentativas_erro +=1
            letras_erradas += entrada_letra
            formatacao_erro += entrada_letra + '-'

            
            

            
            if tentativas_erro == 1:
               print(' | ')
               print(' O ')
               print(palavra_formatada)
               print(f'letras erradas até o momento: {formatacao_erro}')
            elif tentativas_erro == 2:
                print(' | ')
                print(' O ')
                print(' |')
                print(f'letras erradas até o momento: {formatacao_erro}')
            elif tentativas_erro == 3:
                print(' | ')
                print(' O ')
                print('/|')
                print(palavra_formatada)
                print(f'letras erradas até o momento: {formatacao_erro}')
            elif tentativas_erro == 4:
                print(' | ')
                print(' O ')
                print('/|\\')
                print(palavra_formatada)
                print(f'letras erradas até o momento: {formatacao_erro}')
            elif tentativas_erro == 5:
                print(' | ')
                print(' O ')
                print('/|\\')
                print('/')
                print(palavra_formatada)
                print(f'letras erradas até o momento: {formatacao_erro}')
            elif tentativas_erro == 6:
                print(' | ')
                print(' O ')
                print('/|\\')
                print('/ \\')
                break



        if palavra_formatada.count('*') > 0:
            print(f'Ainda faltam {palavra_formatada.count('*')} letras')
               

            

    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, você acertou a palavra secreta: "{palavra_secreta}", número de tentativas: {tentativas_acerto+tentativas_erro}')
        voltar = True
        


    else:
        print(f'Infelizmente você errou... Sinto muito, a palavra secreta era: "{palavra_secreta}" e você perdeu faltando {palavra_formatada.count('*')} letras') 
        voltar = True
            

    while voltar == True:
        novamente = input('Gostaria de jogar novamente? S/N: ')
        novamente = novamente.lower()
        if novamente == 's':
            os.system('cls')
            voltar = False
        elif novamente == 'n':
            jogando = False
            voltar = False
            os.system('cls')
        else:
            print('Digite uma opção valida')
