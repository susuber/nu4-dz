"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

from colorama import Fore, Style, init
init()


class Personal_account():
    def __init__(self):
        self.__account = 0
        self.__history = []

    def add(self, num):
        self.__account += num

    def buy(self, num):
        self.__account -= num
        self.__history.append(num)

    def print_history(self):
        if len(self.__history) > 0:
            n = 0
            print(f'{Fore.BLUE}История покупок{Style.RESET_ALL}')
            print('-' * 20)
            for num in self.__history:
                n += 1
                print(f'Покупка №{n}: {num}')
            print('-' * 20)
            print('', end='\n\n')
        else:
            print('Вы еще не совершали покупок', end='\n\n')


def menu() -> int:
    '''
    Выбор действия
    :return: выбранный пункт
    '''
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print()
        choice = input(f'Выберите пункт меню: {Fore.LIGHTGREEN_EX}')
        print(Style.RESET_ALL, end='\n\n')

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                return choice
            else:
                print(f'{Fore.RED}[ERROR 2] Неверный пункт меню{Style.RESET_ALL}', end='\n\n')
        else:
            print(f'{Fore.RED}[ERROR 1] Ошибка ввода{Style.RESET_ALL}', end='\n\n')


def input_sum() -> float:
    while True:
        try:
            num = float(input(f'Введите сумму: {Fore.LIGHTGREEN_EX}'))
            print(Style.RESET_ALL, end='')
        except ValueError:
            print(f'{Fore.RED}[ERROR 1] Ошибка ввода{Style.RESET_ALL}', end='\n\n')
        else:
            return num


def main():
    account = Personal_account()
    while True:
        choice = menu()

        if choice == 1:
            account.add(input_sum())
        elif choice == 2:
            account.buy(input_sum())
        elif choice == 3:
            account.print_history()
        elif choice == 4:
            break
        else:
            print(f'{Fore.RED}[ERROR 3] Неизвестная ошибка{Style.RESET_ALL}', end='\n\n')


if __name__ == '__main__':
    main()
