while True:
    try:
        a = input()
        if a == 10:
            print("Вы нашли одно из чисел, поздравляем!\nВаше число" + a)
        elif a == 400:
            print("Вы нашли одно из чисел, поздравляем!\nВаше число" + a)
        elif a == 638:
            print("Вы нашли одно из чисел, поздравляем!\nВаше число" + a)
        elif a == 2:
            print("Вы нашли одно из чисел, поздравляем!\nВаше число" + a)
        else:
            print("Вы ввели:" + a + ", это не правильное число, повторите попытку")
    except ValueError:
        print('Что-то не правильно, повторите попытку')
        