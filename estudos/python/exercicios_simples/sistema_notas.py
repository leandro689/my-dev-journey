# Desafio bônus (nível "quase projeto")
# Sistema de notas
# •	usuário digita várias notas 
# •	armazena em uma lista 
# •	no final: 
# o	média 
# o	maior nota 
# o	menor nota


sistema_on = True

while sistema_on:
    print ('Bem vindo ao sistema de notas, o sistema te ajuda a organizar suas notas para avaliar média.')
    entrar_programa = input('Gostaria da avaliar suas notas? S/N: ')

    if len(entrar_programa) > 1:
        print('Opção invalida')
        continue
    
    
    if entrar_programa.lower() == 's':
        notas = []
        
        calculando_notas = True

        while calculando_notas:
            nota_add = input(f'Digite a {len(notas) + 1}º nota por favor, caso queira consolidar as notas, digite "c": ')
            

            if nota_add.isdigit() and int(nota_add) <= 10:
                notas.append(int(nota_add))
                print(notas)

            elif nota_add.lower() == 'c':
                
                if len(notas) == 0:
                    print('Nenuma nota foi inserida')
                    saida = True
                    while saida:
                        val_saida = input('Deseja sair do programa? S/N: ')
                        
                        if val_saida.lower() == 's':
                            print('Perfeito, volte quando precisar')
                            saida = False
                            sistema_on = False
                            calculando_notas = False
                            

                        elif val_saida == 'n':
                            break

                        else:
                            print('Opção de saida invalida invalida')
                    continue

                soma_notas = 0
                maior_nota = notas[0]
                menor_nota = notas[0]

                for i in notas:
                    if i > maior_nota:
                        maior_nota = i
                    soma_notas += i

                for i in notas:
                    if i < menor_nota:
                        menor_nota = i


                media_notas = soma_notas / len(notas)

                print(f'Segue consolidação das notas:')
                print(f'Quantidade de notas {len(notas)}')
                print(f'Média final é {media_notas:.2f}')
                print(f'Sua maior nota foi {maior_nota}')
                print(f'Sua menor nota foi {menor_nota}')
                
                calculando_notas = False

            else:
                print('Entrada invalida')
                

    
    elif entrar_programa.lower() == 'n':
        print('Perfeito, volte quando precisar!')
        break
    
    else:
        print('Opção invalida')


#feito até agora:
#- controle de entrada e apresentação do programa
#- media e soma total de notas
#-informe de menor e maior nota 


