import random

import colorama
from colorama import Fore, Back
colorama.init()

while True:
    n = random.randint(2, 99999999)
    print('Чему равен n: ', n)

    factorial = 1

    while n > 1:
        factorial *= n
        n -= 1

    print(factorial)
    print("====================================================")