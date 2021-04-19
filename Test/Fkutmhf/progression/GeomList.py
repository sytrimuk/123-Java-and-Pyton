#this program contains solutions to a geometric progression by formulas and its formulas

#решение
#формула

import colorama
from colorama import Fore, Back
colorama.init()

GREEN = Fore.GREEN
RED_LX = Fore.LIGHTRED_EX
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
RESET_F = Fore.RESET

while True:

    print(GREEN + 'Если вам нужна решение, напишите \'решение\'\n',
    'Если вам нужно формула, напишите \'формула\'' + RESET_F)
    b = input('Поле для запроса: ')

    print(RED_LX + "------------------------------------------------------------------------" + RESET_F)

    if b == 'решение':

        print(GREEN + 'Какая формула вам нужна?\n',
        'Если вам нужно найти bn, напишите \'bn\'\n',
        'Если вам нужно найти b1, напишите \'b1\'\n',
        'Если вам нужно найти Sn, напишите \'Sn\'\n',
        'Если вам нужно найти q, напишите \'q\'' + RESET_F)
        a = input('Поле для запроса: ')

        if a == 'bn':

            print(YELLOW)
            b = int(input('Введите число b: '))
            q = int(input('Введите число q: '))
            n = int(input('Введите число n: '))
            length = int(input('Введите до каких пор показывать геометрическую прогрессию: '))
            print(RESET_F)

            qwe = MAGENTA + 'b = ', b + '\nq = ', q + '\nn = ', n + RESET_F

            #print('b = ', b)
            #print('q = ', q)
            #print('n = ', n)
            print(qwe)
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
        
        elif a == 'Sn':

            b1 = int(input('Введите ваше b1: '))

            Sn = (b1 * (q ** n - 1)) / (q -1)

            print(Fore.LIGHTBLUE_EX)
            print()
            print(Fore.RESET)

        elif a == 'q':

            bna = int(input('Введите ваше bnb: '))
            bnb = int(input('Введите ваше bna: '))

            q2 = bnb / bna
            q = q2 ** 0.5
            
            print()

    elif b == 'формула':

        print(GREEN + 'Какая формула вам нужна?\n',
        'Если вам нужно найти bn, напишите \'bn\'\n',
        'Если вам нужно найти b1, напишите \'b1\'\n',
        'Если вам нужно найти Sn, напишите \'Sn\'\n' + RESET_F)
        KakayaFormyla = input('Поле для запроса: ')

        if KakayaFormyla == 'b1':

            print(Fore.LIGHTCYAN_EX)
            print('bn / q ** (n - 1)')
            print(Fore.RESET)

            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)

        elif KakayaFormyla == 'bn':

            print(Fore.LIGHTCYAN_EX)
            print('b1 * q ** (n - 1)')
            print(Fore.RESET)

            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)
      
        elif KakayaFormyla == 'Sn':

            print(Fore.LIGHTCYAN_EX)
            print('(b1 * (q ** n - 1)) / (q -1)\nпри q ≠ 1')#Аркаша дурак
            print(Fore.RESET)

            print(Fore.LIGHTRED_EX)
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
            print(Fore.RESET)

        elif KakayaFormyla == 'q':
            print('bnb(2) / bna(1)')
            print("------------------------------------------------------------------------")
            print("------------------------------------------------------------------------")
