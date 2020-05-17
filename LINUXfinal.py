# THIS IS FOR LINUX OS
from random import randint
from os import system, name
import readchar


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def is_number(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
    return False


def print_game(game):
    for i in range(0, len(game)):
        for j in range(0, len(game)):
            digits = 0
            num = int(game[i][j] / 10)
            while num > 0:
                digits += 1
                num = int(num / 10)
            if game[i][j] != 0:
                print(game[i][j], end=" " * (4 - digits))
            else:
                print("-", end=" " * (4 - digits))
        print("")


def check_pow2(n):
    temp = n
    p = 0
    while (not n % 2) and (n != 0):
        n /= 2
        p += 1
    if temp == 2**p:
        return True
    else:
        return False


def spawn(game, n):
    count = 0
    while count == 0:
        rand1 = randint(0, n - 1)
        rand2 = randint(0, n - 1)
        if game[rand1][rand2] == 0:
            game[rand1][rand2] = 2
            count += 1


def new_game():
    n = input("enter the size 'n' of the board\n")
    while type(n) != int or not int(n) > 1:
        if n == '':
            n = 5
        elif is_number(n):
            if int(n) > 1:
                n = int(n)
            else:
                n = input("enter an integer > 1\n")
        else:
            n = input("enter an integer >1\n")
    w = input("enter the target score 'w'\n")
    while type(w) != int or (not check_pow2(w)):
        if w == '':
            w = 2048
        elif is_number(w) and not check_pow2(int(w)):
            w = input("enter a number which is positive power of 2\n")
        elif is_number(w) and check_pow2(int(w)):
            w = int(w)
        else:
            w = input("enter a number which is positive power of 2\n")
    game = [[0 for i in range(0, n)]for i in range(0, n)]
    spawn(game, n)
    clear()
    print_game(game)
    global won, lost, move_possible
    won = False
    lost = False
    move_possible = True
    while (not won) and (not lost):
        move = readchar.readkey()
        while move not in ('a', 'A', 's', 'S', 'd', 'D', 'w', 'w'):
            print("enter a valid move")
            move = readchar.readkey()
        count = 0
        column = 0
        if move == 'w' or move == 'W':
            while 0 <= column < n:
                k = 0
                row = 1
                while 0 < row < n:
                    j = row
                    while j > k:
                        if (not game[j][column] == 0) and (game[j-1][column] == 0):
                            game[j-1][column] = game[j][column]
                            game[j][column] = 0
                            count += 1
                        elif (not game[j][column] == 0) and (game[j-1][column] == game[j][column]):
                            game[j-1][column] = 2*game[j-1][column]
                            game[j][column] = 0
                            k = j
                            count += 1
                        j -= 1
                    row += 1
                column += 1
        column = 0
        if move == 's' or move == 'S':
            while 0 <= column < n:
                k = n - 1
                row = n - 2
                while 0 <= row < n - 1:
                    j = row
                    while j < k:
                        if (not game[j][column] == 0) and (game[j + 1][column] == 0):
                            game[j + 1][column] = game[j][column]
                            game[j][column] = 0
                            count += 1
                        elif (not game[j][column] == 0) and (game[j + 1][column] == game[j][column]):
                            game[j + 1][column] = 2 * game[j + 1][column]
                            game[j][column] = 0
                            k = j
                            count += 1
                        j += 1
                    row -= 1
                column += 1
        row = 0
        if move == 'a' or move == 'A':
            while 0 <= row < n:
                k = 0
                column = 1
                while 0 < column < n:
                    j = column
                    while j > k:
                        if (not game[row][j] == 0) and (game[row][j-1] == 0):
                            game[row][j-1] = game[row][j]
                            game[row][j] = 0
                            count += 1
                        elif (not game[row][j] == 0) and (game[row][j-1] == game[row][j]):
                            game[row][j-1] = 2*game[row][j-1]
                            game[row][j] = 0
                            k = j
                            count += 1
                        j -= 1
                    column += 1
                row += 1
        row = 0
        if move == 'd' or move == 'D':
            while 0 <= row < n:
                k = n-1
                column = n - 2
                while 0 <= column < n:
                    j = column
                    while j < k:
                        if (not game[row][j] == 0) and (game[row][j+1] == 0):
                            game[row][j+1] = game[row][j]
                            game[row][j] = 0
                            count += 1
                        elif (not game[row][j] == 0) and (game[row][j+1] == game[row][j]):
                            game[row][j+1] = 2*game[row][j]
                            game[row][j] = 0
                            k = j
                            count += 1
                        j += 1
                    column -= 1
                row += 1
        clear()
        non_zero = 0
        if count == 0:
            print(move+"- move is not possible")
        elif count != 0:
            spawn(game, n)
        for i in range(0, n):
            for j in range(0, n):
                if game[i][j] >= w:
                    won = True
                    print('YOU WIN!')
                if game[i][j] != 0:
                    non_zero += 1
        print_game(game)
        if non_zero == (n**2):
            move_possible = False
            for i in range(0, n-1):
                for j in range(0, n - 1):
                    if game[i][j] == game[i][j+1] or game[i][j] == game[i+1][j]:
                        move_possible = True
                    elif game[n-1][n-1] == game[n-1][n-2] or game[n-1][n-1] == game[n-2][n-1]:
                        move_possible = True
        if not move_possible:
            lost = True
            print("YOU LOST!!")


clear()
given = input("press 1 - PLAY ||  2 - QUIT\n")
while given != str(1) and given != str(2):
    given = input("ENTER A VALID OPTION\n")
while given == str (1):
    new_game()
    given = input("press 1 - PLAY AGAIN\n     2 - QUIT\n")
    while given != str(1) and given != str(2):
        given = input("ENTER A VALID OPTION\n")
