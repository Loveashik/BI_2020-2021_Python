def calc(n, op, m):
    possible_operations = ['+', '-', '*', '/', '^', '**']
    if op in possible_operations:
        if op == '+':
            result = n + m
        elif op == '-':
            result = n - m
        elif op == '*':
            result = n * m
        elif op == '/':
            result = n / m
        elif (op == '^') or (op == '**'):
            result = n ** m
            op = '^'

        print(result)
    else:
        print(f'Такой операции как {op} я не знаю')


print("введите число, затем операцию, которую вы хотите применить, "
      "затем второе число:\n")
x, op, y = input(), input(), input()

try:
    calc(float(x), op, float(y))
except ValueError:
    raise Exception('Возможно, вы ввели не числа')
