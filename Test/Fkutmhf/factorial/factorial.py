import colorama
from colorama import Fore, Back
colorama.init()
#что по бесконечности?
while True:
    # заготовки
    f = Fore.RESET
    b = Back.RESET
    #Дальше всё понятно
    print(Fore.GREEN)
    n = int(input('Чему равен n: '))
    print(f)
    

    factorial = 1

    while n > 1:
        factorial *= n
        n -= 1
    
    print(Fore.CYAN)
    print(factorial)
    print(f)
    print(Fore.LIGHTMAGENTA_EX)
    print("====================================================")
    print(f)
