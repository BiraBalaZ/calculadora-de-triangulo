lado1 = input('Valor do lado 1: ')
lado2 = input('Valor do lado 2: ')
lado3 = input('Valor do lado 3: ')

print('\nDe acordo com os dados fornecidos, é um:')

if (lado1 == lado2 and lado2 == lado3 and lado3 == lado1) :
    print('Triângulo Equilátero')
elif (lado1 != lado2 and lado2 != lado3 and lado3 != lado1) :
    print('Triângulo Escaleno')
else :
    print('Triângulo Isósceles')
