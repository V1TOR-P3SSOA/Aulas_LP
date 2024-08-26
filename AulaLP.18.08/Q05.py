op = ""
while op != "0":
    print('''
          ----------Calculadora.py----------
          1 - Adição
          2 - Subtração
          3 - Multiplicação
          4 - Divisão
          5 - Elevado ao Quadrado
          0 - Sair
          ----------------------------------
          ''')
    op = input('Informe a operação: ')
    if op == '0':
        print('Infelizmente a calculadora se foi :( ')
    elif op == "1":
        n1_1 = int(input('Digite o primeiro número: '))
        n2_1 = int(input('Digite o segundo número: '))
        print(f'{n1_1} + {n2_1} = {n1_1 + n2_1}')
    elif op == "2":
        n1_2 = int(input('Digite o primeiro número: '))
        n2_2= int(input('Digite o segundo número: '))
        print(f'{n1_1} - {n2_2} = {n1_2 - n2_2}')
    elif op == "3":
        n1_3 = int(input('Digite o primeiro número: '))
        n2_3= int(input('Digite o segundo número: '))
        print(f'{n1_3} x {n2_3} = {n1_3 * n2_3}')
    elif op == "4":
        n1_4 = int(input('Digite o primeiro número: '))
        n2_4= int(input('Digite o segundo número: '))
        print(f'{n1_4} / {n2_4} = {n1_4 / n2_4}')
    elif op == "5":
        n1_5 = int(input('Digite o número: '))
        print(f'{n1_5} ^ 2 = {n1_5 * n1_5}')
    else:
        print('operação inválida, tente novamente...')
