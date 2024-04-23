import math
while True:
    print('Escolha uma opção')
    print('Para converter de Binario para base decimal [1]')
    print('Para converter de Hexadecimal para base decimal [2]')
    print('Para converter de Octadecimal para base decimal [3]')
    
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:

            binario = int(input('Digite seu numero Binario:  '))
            n = len(str(binario))
            valor_usuario = binario
            decimal = 0
            i = 0

            while n >=0:
            
                resto = binario % 10
                decimal = decimal + (resto * (2**i))
                n = n - 1
                i = i + 1
                binario = binario // 10
            print(f'O numero (Binario) {valor_usuario} na base decimal é {decimal}')
   
    elif opcao == 2:
        hexadecimal = input('Digite seu numero hexadecimal: ')
        decimal = int(hexadecimal, 16)
        print(f'.......{decimal}')

    elif opcao == 3:
        octal = input('Digite seu numero Octal: ')
        decimal = 0
        n = len(octal)
        
        if all (digito in '01234567' for digito in octal):
            
            for i in range(n):
                digito_octal = int(octal [n -1 -i])
                decimal += digito_octal * (8 **i)

        print(f'O numero Octal {octal} na base decimal é {decimal}')
    else:
        print('Entrada invalida. Coloque numeros de 0 á 7 apenas.')



    sair = input ('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
         print('Até mais!')
         break

    
