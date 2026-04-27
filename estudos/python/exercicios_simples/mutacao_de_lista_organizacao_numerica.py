lista_num = [47, 12, 89, 5, 63, 28, 94, 31, 7, 56, 73, 18, 40, 99, 22, 61, 3, 85, 10, 36]

maior_num = 0
segundo_maior_num = 0


for i in lista_num:
    if i > maior_num:
        maior_num = i
       
    
    for i in lista_num:
        if i < maior_num and i > segundo_maior_num:
            segundo_maior_num = i

print(maior_num, segundo_maior_num)

    
    