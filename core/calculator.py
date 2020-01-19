from decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b
    elif operation == '**':
        return a ** b
    else:
        return 'Некорректный оператор'


if __name__ == '__main__':
    while True:
        try:
            a = int(input('Введите первое число: '))
            break
        except:
            print('Некорректное значение!')

    while True:
        try:
            b = int(input('Введите второе число: '))
            break
        except:
            print('Некорректное значение!')

    operation = input('Введите операцию: ')

    try:
        print('Результат: ', calculator(a, b, operation))
    except Exception as e:
        print(e)
