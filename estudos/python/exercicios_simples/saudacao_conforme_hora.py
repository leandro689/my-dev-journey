horas = input('Eae irmão que horas são? ')

try:
    int(horas)

    if int(horas) <= 11:
        print(f'{horas}?... Orbigado, bom dia!!!')

    elif int(horas) <=17:
        print(f'{horas}?... Orbigado, boa tarde!!!')

    elif int(horas) <= 23:
        print(f'{horas}?... Orbigado, boa noite!!!')

    else:
        print('mano que horas é essa? ')

except:
    print('Mano que? ')
    