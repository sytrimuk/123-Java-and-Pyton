import random
import colorama
from colorama import Fore, Back
colorama.init()

while True:
    a = input("Задайте вопрос - услышите ответ\n(Вопрос должен быть такое, на который можно ответить \"Да\" или \"Нет\")\nВаш вопрос: ")
    spisok = ["Да!", "Нет!", "Определённо да!", "Ни в коем случае!", "Конечно да!"]
    SpisokColor = ['RED', 'GREEN', 'CYAN', 'WHITE']
    print("Ответ на вопрос: ", random.choice(spisok))
    #print(random.choice(Fore.SpisokColor))
    print("------------------------------------------------------------------------")

