import random

import colorama
from colorama import Fore, Back
colorama.init()

while True:
    print(Fore.MAGENTA)
    Random = random.randint(0, 100)
    a = int(input('Введите число: '))
    print(Fore.RESET)

    if  a == Random:
        print(Fore.WHITE)
        print(Back.RED)
        print('Вы ввели число: ', a, 'Иииииииииии... Это был правильный ответ!!\nЗагаданное число: ', Random)
        print(Fore.RESET)
        print(Back.RESET)
    elif 0 <= a <= 100:
        print('Вы ввели число: ', a, '\nЗагаданное число находилось в диапозоне 0 – 100\nВот это число: ', Random, '\n------------------------------------------------------------------------')
    else:
        print(Fore.YELLOW)
        print('Вы ввели число, которое не находится в диапозоне 0 – 100, попробуйте ещё раз\n------------------------------------------------------------------------')
        print(Fore.RESET)
