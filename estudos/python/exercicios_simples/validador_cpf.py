# cpf = "532.301.666-39"
# cpf_digitos = []
# multiplicadores = [10,9,8,7,6,5,4,3,2,]



# # -- Tratamento do dado CPF para ter somente digitos
# for i in cpf:
#     if i.isdigit():
#         cpf_digitos.append(i)

# if len(cpf_digitos) == 11:
    

#     # -- Multiplicar digitos CPF pelos multiplicadores
#     digitos_multiplicados = []
#     for indice, multiplicador in enumerate(multiplicadores):
#         mult_digi = int(cpf_digitos[indice]) * multiplicador
#         digitos_multiplicados.append(mult_digi)


#     # -- Calculo dos digitos 
#     calculo_digito = 0
#     for i_digitos_multiplicados in digitos_multiplicados:
#         calculo_digito += (i_digitos_multiplicados)
#     calculo_digito = calculo_digito * 10
#     calculo_digito = calculo_digito % 11

#     validacao_digito_1 = 0 if calculo_digito > 9 else calculo_digito


#     #-- Resposta Validação
#     if validacao_digito_1 == int(cpf_digitos[9]):
#         print("Primeiro digito CPF válido")

#     else:
#         print('Primeiro digito CPF inválido')

# else:
#     print("CPF Invalido")


"""
1 etapa - Tirar traços e pontos do CPF - ok
2 etapa - Multiplicar todos os digitos do CPF em uma escala de 10 para baixo. - ok
3 etapa - Somar todos os resultados - ok
4 etapa - Multiplicar o resultado obtido com a soma dos resultados por 10 - ok
5 etapa - Obter o resto da divisão (resultado anterior/11) - ok

Se resultado > 9
    resultado = 0

caso contrario
    resultado valor do resto
"""

# cpf = "532.301.666-39"
# cpf_digitos = []

# for digito in cpf:
#     if digito.isdigit():
#         cpf_digitos.append(int(digito))


# if len(cpf_digitos) != 11:
#     print('Cpf inválido')

# else:
#     digitos_multiplicados = []
#     multiplicador_regressivo = 10

#     for digito_cpf in cpf_digitos:
#         if multiplicador_regressivo >= 2:
#             digito_cpf = digito_cpf * multiplicador_regressivo
#             digitos_multiplicados.append(digito_cpf)
#             multiplicador_regressivo -= 1

#     calculo_digito_1 = 0
    
#     for digito_digitos_multiplicados in digitos_multiplicados:
#         calculo_digito_1 += digito_digitos_multiplicados
    
#     calculo_digito_1 = calculo_digito_1 * 10
#     calculo_digito_1 = calculo_digito_1 % 11

#     validacao_digito_1 = 0 if calculo_digito_1 > 9 else calculo_digito_1

    
#     if validacao_digito_1 == int(cpf_digitos[9]):
#         print('Primeiro digito Valido')

#     else:
#         print("Cpf inserido invalido")
        

#------------------------------------------------------ Outra versão --------------------

# cpf = "532.301.666-39"
# cpf_digitos = []
# validacao_primeiro_digito = ""

# # -------- Tratamento Digitos CPF ---- Validação da quantidade de digitos ---------------
# for digito in cpf:
#     if digito.isdigit():
#         cpf_digitos.append(int(digito))

# if len(cpf_digitos) != 11:
#     print("CPF digitado, com quantidade de digitos inválida")
    

# #--------- Calculo algoritmo primeiro digito --------------------------------------------
# else:
    
#     resultado = 0
#     multiplicador_decrescente = 10

#     for digito_cpf in cpf_digitos:

#         if multiplicador_decrescente >=2:
#             resultado += digito_cpf * multiplicador_decrescente
#             multiplicador_decrescente -= 1
            
    
#     resultado = (resultado * 10) % 11

#     validacao_primeiro_digito = 0 if resultado > 9 else resultado

# #-------- Validação primeiro digito ---------------------------------------------------    
# if validacao_primeiro_digito != cpf_digitos[9]:
#     print('CPF inválido.')

# #------- Inicio do algoritmo segundo digito -------------------------------------------
# else:
#     resultado = 0
#     multiplicador_decrescente = 11

#     for digito_cpf in cpf_digitos:
        
#         if multiplicador_decrescente >=2:
#             resultado += digito_cpf * multiplicador_decrescente
#             multiplicador_decrescente -= 1
            
#     resultado = (resultado * 10) % 11
    
#     validacao_segundo_digito = 0 if resultado >9 else resultado

#     if validacao_segundo_digito != cpf_digitos[10]:
#         print('CPF inválido.')

#     else:
#         print(f'{cpf} válido, seguir com procedimento.')

#-------------- Versão final ---------------------


cpf = "411.728.805-90"
cpf_digitos = []
cpf_apto_validacao = True


# -------------- tratamento CPF ----------------
for caracter in cpf:
    if caracter.isdigit():
        cpf_digitos.append(int(caracter))

if len(cpf_digitos) != 11:
    print("CPF não tem a quantidade de digitos necessários")
    cpf_apto_validacao = False
# -------------- tratamento CPF ----------------

# -------------- Calculo primeiro digito -------
if cpf_apto_validacao:
    
    resultado = 0
    multiplicador_decrescente = 10

    for digito in cpf_digitos:
        if multiplicador_decrescente >=2:
            resultado += digito * multiplicador_decrescente
            multiplicador_decrescente -= 1
    
    resultado = resultado * 10
    resultado = resultado % 11
    validacao_primeiro_digito = 0 if resultado >9 else  resultado
# -------------- Calculo primeiro digito -------

# Validacao primeiro digito
    if validacao_primeiro_digito != cpf_digitos[9]:
        print('CPF inválido, digite um cpf válido')

    else:
        resultado = 0
        multiplicador_decrescente = 11
        for digito in cpf_digitos:
            if multiplicador_decrescente >=2:
                resultado += digito *  multiplicador_decrescente
                multiplicador_decrescente -= 1
        
        resultado = resultado *10
        resultado = resultado % 11
        validacao_segundo_digito = 0 if resultado > 9 else resultado

        if validacao_segundo_digito == cpf_digitos[10]:
            print(f'{cpf} valido, dar continuidade ao procedimento')
        
        else:
            print("CPF inválido, digite um cpf válido")
        

