nome = input('Qual o seu nome? ')
qte_letras_nome = len(nome)

if qte_letras_nome <= 4:
    print(f'Seu nome tem {qte_letras_nome}, e é pequeno em man!')

elif qte_letras_nome <= 6:
    print(f'Seu nome tem {qte_letras_nome} letras e é normal cara, ta na media')

else:
    print(f'Seu nome tem {qte_letras_nome} letras e é grandão em :p')


