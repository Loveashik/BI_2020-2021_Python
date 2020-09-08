def calc(N,OP,M):
    possible_operations = ['+', '-', '*', '/', '^', '**']
    if OP in possible_operations:
        if OP == '+':
            result = N + M
        elif OP == '-':
            result = N - M
        elif OP == '*':
            result = N * M
        elif OP == '/':
            result = N / M
        elif (OP == '^') or (OP == '**'):
            result = N ** M
            OP = '^'

        print(result)
    else:
        print(f'Такой операции как {OP} я не знаю')


print("введите число, затем операцию, которую вы хотите применить, затем второе число:\n")
x, op, y = input(), input(), input()

try:
    calc(float(x), op, float(y))
except:
    print('Возможно, вы ввели не числа')



