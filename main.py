from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.seach_in_dict import fucntion_by_seach
from src.utils import by_process_json
from src.utils_by_pandas import by_processing_csv, by_processing_exe
from src.witget import get_date, mask_account_card


def sorted_dict():

    while True:
        info_by_user_need = input(
            """
            Привет добро пожаловать в программу работы с банковскими транзакцими
            выберите необходимый пункт в меню:
            1. получить информацию из JSON файла
            2. получить информацию из CSV файла
            3. получить информацию из XLSX файла
            """
        )
        if info_by_user_need == "1":
            print("Для обработки выбран JSON файл")
            new_file_dict_list = by_process_json("data/test.json")
            break
        elif info_by_user_need == "2":
            print("Для обработки выбран CSV файл")
            new_file_dict_list = by_processing_csv("data/transactions.csv")
            break
        elif info_by_user_need == "3":
            print("Для обработки выбран XLSX файл")
            new_file_dict_list = by_processing_exe("data/transactions_excel.xlsx")
            break
        else:
            print("выбран неверный формат")

    while True:
        user_1 = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        if user_1.lower() == "executed":
            sorted_file = filter_by_state(new_file_dict_list)
            break
        elif user_1.lower() == "canceled":
            sorted_file = filter_by_state(new_file_dict_list, "CANCELED")
            break
        elif user_1.lower() == "pending":
            sorted_file = filter_by_state(new_file_dict_list, "PENDING")
            break
        else:
            print(f"Статус операции {user_1} недоступен")

    while True:
        user_answer_one = input("Отсортировать операции по дате? Да/Нет")
        if user_answer_one.lower() == "да":
            while True:
                user_answer_two = input("Отсортировать по возрастанию или по убыванию?")
                if user_answer_two.lower() == "по возрастанию":
                    sorted_by_data_file = sort_by_date(sorted_file, False)
                    break
                elif user_answer_two.lower() == "по убыванию":
                    sorted_by_data_file = sort_by_date(sorted_file, False)
                    break
                else:
                    print("напишите либо 'по возрастанию' либо 'по убыванию'")
            break
        elif user_answer_one.lower() == "нет":
            sorted_by_data_file = sorted_file
            break
        else:
            print("введите либо да либо нет")

    while True:
        user_answer_three = input("Выводить только рублевые транзакции? Да/Нет")
        if user_answer_three.lower() == "да":
            sorted_by_rubles = [x for x in filter_by_currency(sorted_by_data_file)]
            break
        elif user_answer_three.lower() == "нет":
            sorted_by_rubles = sorted_by_data_file
            break
        else:
            print("введите только да или нет")

    while True:
        user_answer_four = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        if user_answer_four.lower() == "да":

            user_answer_five = input("введите слово для сортировки")
            sorted_by_info = fucntion_by_seach(sorted_by_rubles, user_answer_five)
            break
        elif user_answer_four.lower() == "нет":
            sorted_by_info = sorted_by_rubles
            break
        else:
            print("введите только да или нет")

    if len(sorted_by_info) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(sorted_by_info)}")

        for i in sorted_by_info:
            print(f"{get_date(i["date"])} {i["description"]}")

            if (
                i["description"] == "Перевод с карты на карту"
                or i["description"] == "Перевод организации"
                or i["description"] == "Перевод со счета на счет"
            ):
                print(f"{mask_account_card(i["from"])} -> {mask_account_card(i["to"])}")
            else:
                print(mask_account_card(i["to"]))
            print(f"Cумма: {i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}")


sorted_dict()
