import random

digitos_cpf = []


# gerador 9 primeiros digitos CPF.
for i  in range(9):
    novo_digito = random.randint(0,9)
    digitos_cpf.append(novo_digito)


# # gerador 1 digito de autentiação
multiplicador_regressivo = 10
resultado = 0

for digito in digitos_cpf:
    resultado += digito * multiplicador_regressivo
    multiplicador_regressivo -= 1

resultado = (resultado * 10) % 11
primeiro_digito = 0 if resultado > 9 else resultado

# gerador 2 digito de autenticação
digitos_cpf.append(primeiro_digito)
multiplicador_regressivo = 11
resultado = 0


for digito in digitos_cpf:
    resultado += digito * multiplicador_regressivo
    multiplicador_regressivo -=1

resultado = (resultado * 10) % 11
segundo_digito = 0 if resultado > 9 else resultado

digitos_cpf.append(segundo_digito)

novo_cpf = ''
for posicao_digito, digito in enumerate(digitos_cpf):
    novo_cpf += str(digito)

    if posicao_digito == 2 or posicao_digito == 5:
        novo_cpf += "."

    elif posicao_digito == 8:
        novo_cpf += '-'

print(novo_cpf)

