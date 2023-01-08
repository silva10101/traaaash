from random import randint

DIST_BEG = 1
DIST_END = 67773
ENCODER = "utf-8"


# Choose the word
def randword():
    rword = randint(DIST_BEG, DIST_END)
    with open('dict.txt', 'r', encoding=ENCODER) as dic:
        for xi in range(rword - 1):
            dic.readline()
        w = dic.readline()
    return w


def draw(att):
    arr = [
        '''            ___________
            |         |
                      |
                      |
                      |
                      |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
                      |
                      |
                      |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
            |         |
            |         |
                      |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
            |7        |
            |         |
                      |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
           /|7        |
            |         |
                      |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
           /|7        |
            |         |
             L        |
                      |
        ______________|''',
        '''            ___________
            |         |
            O         |
           /|7        |
            |         |
           / L        |
                      |
        ______________|''']
    print(arr[att])


def game():
    # Prepare
    word = randword()
    ans = word
    WordS = (list(word))
    list.pop(WordS)  # List of literals
    lng = len(WordS)  # Lenght of list
    UserW = ['_' for c in WordS]  # List of User word
    # print(word); print(WordS);
    attempt = 0
    rightl = 0
    wrong = []
    # Game
    print(' Your word:\n', UserW)
    draw(attempt)
    print('       Your attempts: ', 6 - attempt)
    input(' \nAre you ready?\nPress enter to continue ')
    while attempt < 6 and rightl < lng:
        x = input('\nChoose a letter [ru]: \n')
        if x in WordS:
            print('Right!!!!')
            for i in range(WordS.count(x)):
                rightl += 1
                UserW.pop(WordS.index(x))
                UserW.insert(WordS.index(x), x)
                WordS.insert(WordS.index(x), '1')
                WordS.remove(x)
                # print(WordS)
        else:
            attempt += 1
            draw(attempt)
            print('Wrong!!!! Your attempts: ', 6 - attempt)
            wrong.append(x)
        print('Wrong letters', wrong)
        print(UserW)
    # Result
    if rightl == lng:
        print('\nYou are winner)')
    else:
        print('\nYou are loser(\n Right word: ', ans)


print(' Hi!!!')
PlayAgain = True
while PlayAgain:
    game()
    a = input('\nWanna play again?\nPress д to play or any button to exit\n')
    if a == "д" or a == "Д":
        PlayAgain = True
        print('\nNICE CHOSE!!!')
    else:
        PlayAgain = False
        print('BYE!!!')
