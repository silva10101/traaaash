from random import randint


# 1-камень 2-ножницы 3-бумага
# Перевод в слово

def word(a):
    if a == 1:
        res = 'Камень'
    elif a == 2:
        res = 'Ножницы'
    else:
        res = 'Бумага'
    return res


# Процесс выбора
def game():
    usz = int(input('Су-е-фа: '))
    pcz = randint(1, 3)

    uszw = word(usz)
    pczw = word(pcz)

    if (usz == 1 and pcz == 2) or (usz == 2 and pcz == 3) or (usz == 3 and pcz == 1):
        win = 1
    elif usz == pcz:
        win = 0
    else:
        win = -1

    print('Игрок: ', uszw)
    print('Компьютер: ', pczw)

    if win == 1:
        print('Ты выйграл!')
    elif win == 0:
        print('Ничья!')
    else:
        print('Ты проиграл!')


while True:
    game()
    print()
