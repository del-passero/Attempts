from ctypes import *
import time
import random

valuta = "$"
money = 0
startMoney = 0
playGame = True
defaultMoney = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

# Вывод сообщения о выигрыше
def pobeda(result):
    color(14)
    print(f"Вы победили! Выигрыш составляет {result}{valuta}")
    print(f"На Вашем счету {money}{valuta}")


def main()
    global money, playGame

    money = loadMoney()
    startMoney = money

    while (playGame and money > 0):
        colorLine(10, "Приветствуем Вас в нашем казино!")
        color(14)
        print(f"На Вашем счету {money}{valuta}")

        color(6)
        print(f"Вы можете сыграть в:  {money}{valuta}")
        print(f"    1. Рулетку")
        print(f"    2. Кости")
        print(f"    3. Однорукого бандита")
        print(f"    0. Выход")

        x = getInput("0123", "    Ваш выбор? ")

        if (x == "0"):
            print("1231123123")
            playGame = False
        elif (x == "1"):
            roulette()
        elif (x == "2"):
            dice()
        elif (x == "3"):
            oneHandBandit()