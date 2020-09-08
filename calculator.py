def calc(N,OP,M):
    possible_operations = ['+', '-', '*', '/', '^']
    if OP in possible_operations:
        if OP == '+':
            print(f'{N}{OP}{M} = {float(N) + float(M)}')
        elif OP == '-':
            print(f'{N}{OP}{M} = {float(N) - float(M)}')
        elif OP == '*':
            print(f'{N}{OP}{M} = {float(N) * float(M)}')
        elif OP == '/':
            print(f'{N}{OP}{M} = {float(N) / float(M)}')
        elif OP == '^':
            print(f'{N}{OP}{M} = {float(N) ** float(M)}')
    else:
        print(f'Такой операции как {OP} я не знаю')


final = True
while final:
    print("введите через пробел число, затем операцию, которую вы хотите применить, затем второе число:\n"
          "для выхода из программы введите exit")
    z = input()
    if z == 'exit':
        final = False
    else:
        values = z.split(' ')
        if len(values) == 3:
            x, op, y = values
            try:
                float(x) and float(y)
                calc(x, op, y)
            except:
                print('Возможно, вы ввели не числа')
        else:
            print('Пожалуйста, введите 3 элемента через пробел')


