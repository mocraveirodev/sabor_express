print('Python na Escola de Programação da Alura')
nome = input('Qual seu nome: ')
idade = input('Qual sua idade: ')
# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')
# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')
# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))
# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))
print('''
A
L
U
R
A
''')
print('\nA\nL\nU\nR\nA')
# Abordagem com sep='\n' para imprimir cada letra em uma linha
print('A','L','U','R','A',sep='\n')

pi = 3.14159
# Abordagem de f-string
print(f'O valor de pi é {pi:.2f}')
# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))
# Utilizando a função round()
print(f'O valor de pi é {round(pi, 2)}')