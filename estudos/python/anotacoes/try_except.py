#pode-se utilizar o try para tentar executar um codigo e o except para tratativas de erros.

entrada = input('Digite um numero: ')

try:
    int(entrada)
    print('Entrada Valida')


except ValueError:
    print('entrada invalida')
