def calculation():
    print('Введите первое число: ', end='')
    a = float(input())
    print('Введите второе число: ', end='')
    b = float(input())
    print('Что выполнить? (+-*/)', end=' ')
    c = input()

    if c == '+':
        rez = a + b
    elif c == '-':
        rez = a - b
    elif c == '*':
        rez = a * b
    elif c == '/':
        rez = a / b
    else:
        print('Неверный знак')

    print(a, '+', b, '=', rez)
    print(a)
    print(b)
    print(rez)


calculation()
