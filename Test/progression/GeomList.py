#this program contains solutions to a geometric progression by formulas and its formulas

import colorama
from colorama import Fore, Back
colorama.init()

while True:
    print(Fore.GREEN)
    print('Если вам нужна решение, напишите \'решение\'\n', 'Если вам нужно формула, напишите \'формула\'')
    b = input('Поле для запроса: ')
    print(Fore.RESET)
    print(Fore.LIGHTRED_EX)
    print("------------------------------------------------------------------------")
    print(Fore.RESET)
    if b == 'решение':
        print(Fore.GREEN)
        print('Какая формула вам нужна?\n', 'Если вам нужно найти bn, напишите \'bn\'\n', 'Если вам нужно найти b1, напишите \'b1\'')
        a = input('Поле для запроса: ')
        print(Fore.RESET)
        if a == 'bn':
            print(Fore.YELLOW)
            b = int(input('Введите число b: '))
            q = int(input('Введите число q: '))
            n = int(input('Введите число n: '))
            length = int(input('Введите до каких пор показывать геометрическую прогрессию: '))
            print(Fore.RESET)

            print(Fore.MAGENTA)
            print('b = ', b)
            print('q = ', q)
            print('n = ', n)
            geometric = [b * q ** (n - 1) for n in range(1, length + 1)]
            print(Fore.RESET)
            print(Fore.RED)
            print(geometric)
            print(Fore.RESET)
            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)

        elif a == 'b1':
            print(Fore.YELLOW)
            bn = int(input('Введите ваше bn: '))
            n = int(input('Введите число n: '))
            q = int(input('Введите число q: '))
            print(Fore.RESET)

            b1 = bn / q ** (n - 1)

            print(Fore.MAGENTA)
            print('b1 =', b1)
            print(Fore.RESET)
            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)

        elif a == 2:
            print('')

    elif b == 'формула':
        print(Fore.GREEN)
        print('Какая формула вам нужна?\n', 'Если вам нужно найти bn, напишите \'bn\'\n', 'Если вам нужно найти b1, напишите \'b1\'')
        KakayaFormyla = input('Поле для запроса: ')
        print(Fore.RESET)
        if KakayaFormyla == 'b1':
            print(Fore.LIGHTCYAN_EX)
            print('b * q ** (n - 1)')
            print(Fore.RESET)
            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)

        elif KakayaFormyla == 'bn':
            print(Fore.LIGHTCYAN_EX)
            print('bn / q ** (n - 1)')
            print(Fore.RESET)
            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)
