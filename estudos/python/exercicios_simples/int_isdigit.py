# num_int = input('Digite um numero inteiro: ')
# cal_par_imp = None

# try:
#     int(num_int)
#     cal_par_imp = (int(num_int)%2)

#     if cal_par_imp == 0:

#         print(f'O numero que você digitou {num_int} é par')

#     else:
#         print(f'O numero que você digitou {num_int} é impar')


# except:
#     print(f'Você não digitou um numero inteiro ')


numero = input('Digita ai um numero ai: ')

if numero.isdigit():
    print(f'você digitou um numero {numero}')

else:
    print(f'Você não digitou um numero')