"""
Adivinhar a palavra secreta
propor uma palacra secreta
uma entrada por letra 
contagem de tentativas - vamos utilizar o esquema de forca
se a letra estiver na palavra, mostrar a letra
se a letra não estiver na palavra, mostrar mensagem de erro
"""

palavra_secreta = input('Ola jogador, vamos jogar forca? Digite uma palavra e não mostre a ninguém: ')
conversao = (len(palavra_secreta)*"*")
palavra_formatada = ''
tentativa_acerto = 0
tentativa_erro = 0
letras_acertadas = ''
letras_faltantes = conversao.count('*')
jogando = True


while palavra_formatada.lower() != palavra_secreta.lower() and tentativa_erro <= 5:
    entrada_letra = input('Digite uma letra: ')

    if len(entrada_letra) == 1:
            
        if entrada_letra.lower() in palavra_secreta.lower():
            tentativa_acerto += 1
            letras_acertadas += entrada_letra.lower()

            palavra_formatada = ''

            if entrada_letra.lower() in letras_acertadas:
                print('Você ja digitou essa letra, estou desconsiderando seu acerto!!')
                tentativa_acerto -= 1
                break
                
            for letra in palavra_secreta.lower():
                if letra in letras_acertadas.lower():
                        palavra_formatada += letra
                else:
                    palavra_formatada += "*"
            print(palavra_formatada)
            letras_faltantes = palavra_formatada.count('*')
            if letras_faltantes > 0:
                print(f'Ainda faltam {letras_faltantes} letras')
                        
                        

        else:
            print('não tem a letra')
            tentativa_erro += 1
            if tentativa_erro == 1:
                print(' | ')
                print(' O ')
                print(f'ainda faltam {letras_faltantes} letras')
            elif tentativa_erro == 2:
                print(' | ')
                print(' O ')
                print('/|')
                print(f'ainda faltam {letras_faltantes} letras')
            elif tentativa_erro == 3:
                print(' | ')
                print(' O ')
                print('/|\\')
                print(f'ainda faltam {letras_faltantes} letras')
            elif tentativa_erro == 4:
                print(' | ')
                print(' O ')
                print('/|\\')
                print('/ ')
                print(f'ainda faltam {letras_faltantes} letras')
            elif tentativa_erro == 5:
                print(' | ')
                print(' O ')
                print('/|\\')
                print('/ \\')
                print(f'Você perdeu, faltando "{letras_faltantes}" letras... A palavra correta era "{palavra_secreta.lower()}"')
                break
                
                    

    else:
        print('Você não digitou apenas uma letra: ')


if tentativa_erro == 5:
    print("Sinto muito!!!")
    tentativa_erro = 0
    tentativa_acerto = 0


        
else:
    print(f'BOA, VOCÊ CONSEGUIU, A PALAVRA SECRETA É "{palavra_secreta.lower()}"!!! Você resolveu em {tentativa_acerto+tentativa_erro} tentativas')
    



# primeira dificuldade, começar o codigo, demorei para relembrar as logicas e como ter uma idea de como começar, mas notei que depois que comecei, até criar a parte de tentativas foi fluindo.
# codigo montado até o for, porém não consegui adicionar a letra à str e substituir o '*'. Estou indo ver o exercicio do professor... Estou frustrado kkkkk
