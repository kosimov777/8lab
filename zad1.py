#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
# отдельной функции.

import sys

if __name__ == '__main__':
    # Функции
    def add():
        # Запросить данные .
        payer = input("Расчетный счет плательщика")
        recipient = input("Расчетный счет получателя")
        summ = input("Перечисляемая сумма в руб.")

        # Создать словарь.
        transfer = {
            'payer': payer,
            'recipient': recipient,
            'summ': summ,
        }

        # Добавить словарь в список.
        transfers.append(transfer)
        # Отсортировать список в случае необходимости.
        if len(transfers) > 1:
            transfers.sort(key=lambda item: item.get('payer', ''))


    def list():
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 30,
            '-' * 30
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^30} | {:^30} |'.format(
                "No",
                "Расчетный счет плательщика;",
                "Рсчетный счет получателя;",
                "Перечисляемая сумма в руб.",
            )
        )
        print(line)

        # Вывести данные о всех рейсах.
        for idx, transfer in enumerate(transfers, 1):
            print(
                '| {:>4} | {:<30} | {:<30} | {:>30} |'.format(
                    idx,
                    transfer.get('payer', ''),
                    transfer.get('recipient', ''),
                    transfer.get('summ', 0)
                )
            )

        print(line)


    def select():
        parts = command.split(' ', maxsplit=2)
        sel = (parts[1])

        count = 0
        for transfers in transfers:
            if transfers.get('payer') == sel:
                count = "Сумма, снятая с расчетного счета плательщика"
                print(
                    '{:>4}: {}'.format(count, transfers.get('summ', ''))
                )
                print('Расчетный счет получателя;', transfers.get('recipient', ''))
                print('Расчетный счет плательщика;', transfers.get('payer', ''))

        # Если счетчик равен 0, то рейсы не найдены.
        if count == 0:
            print("Рейс не найден.")


    def help():
        # Вывести справку о работе с программой.
        print("Список команд:\n")
        print("add - добавить операцию;")
        print("list - вывести список транзакций;")
        print("select <товар> - информация о расчетном счете плательщика;;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    # Список .
    transfers = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
            help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
