

# Função multiplicar numeros

# def multiplicador_numeros (*args):
#     total = args[0]

#     for item, numero in enumerate(args):
#         if item > 0:
#          total *= numero

#     return total

# print(2*2*3*4*5)
# multiplicacao = multiplicador_numeros (2*2*3*4*5)
# print(multiplicacao)

# --------- versão professor -------
# def multiplicador_numeros (*args):
#     total = 1

#     for numero in args:
#         total *= numero

#     return total

# print(2*2*3*4*5)

# resultado = multiplicador_numeros (2,2,3,4,5)
# print(resultado)



def gerar_relatorio_notas(*notas):
    quantidade_notas = len(notas)
    maior_nota = 0
    soma_notas = 0

    for nota in notas:
        if nota > maior_nota:
            maior_nota = nota

    menor_nota = maior_nota

    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota

    for nota in notas:
        soma_notas += nota

    media = soma_notas / quantidade_notas

    return f'Quantidade: {quantidade_notas} \nMaior nota: {maior_nota}\nMenor nota: {menor_nota} \nMédia: {media}'

print(gerar_relatorio_notas(10, 8, 7 ,9))