from db.manage_database import add_entry, del_entry, find_entry, get_entries
from interface.check_input_format import (take_n_check_answer,
                                          take_n_check_int, take_n_check_name,
                                          take_n_check_number_entry,
                                          take_n_check_phone)
from interface.menu import make_screen, menu_entries


def cmd_add_entry() -> menu_entries:
    """
    Собирает с пользователя информацию по каждой категории и сохраняет в базу данных.
    Возвращает функцию вызова записей
    """
    print('\t\tДобавление записи:\n')
    first_name: str = take_n_check_name(text_for_input='Введите имя: ')
    last_name: str = take_n_check_name(text_for_input='Введите фамилию: ')
    org_name: str = take_n_check_name(text_for_input='Введите название организации (По умолчанию - отсутствует): ',
                                      org_name_mode=True)
    work_phone: str = take_n_check_phone(text_for_input='Введите номер рабочего телефона (По умолчанию - Неизвестен): ')
    pers_phone: str = take_n_check_phone(text_for_input='Введите номер личного телефона (По умолчанию - Неизвестен): ')
    add_entry(first_name, last_name, org_name, work_phone, pers_phone)
    print('\nЗапись успешно добавлена\n')
    return menu_entries()


def cmd_del_entry() -> menu_entries:
    """
    Удаляет запись из БД, по номеру из списка.
    Возвращает функцию вызова записей
    """
    table: dict = get_entries()
    number_entry: int = take_n_check_number_entry(table=table)
    del_entry(table=table, number_entry=number_entry)
    print('\nЗапись успешно удалена\n')
    return menu_entries()


def cmd_edit_entry():
    """
    Функция изменений существующей записи. Спрашивает пользователя о каждой категории, как при создании записи,
        но с возможностью сохранения старых данных
    Возвращает функцию вызова записей
    """
    table: dict = get_entries()
    number_entry: int = take_n_check_number_entry(table=table)
    first_name, last_name, org_name, work_phone, pers_phone = [i.split(': ')[1] for i in table[number_entry]]  # all str
    del_entry(table=table, number_entry=number_entry)
    first_name: str = take_n_check_name(
        text_for_input=f'Введите имя (По умолчанию - {first_name}): ',
        default=first_name
    )
    last_name: str = take_n_check_name(
        text_for_input=f'Введите фамилию (По умолчанию - {last_name}): ',
        default=last_name
    )
    org_name: str = take_n_check_name(
        text_for_input=f'Введите название организации (По умолчанию - {org_name}): ',
        org_name_mode=True, default=org_name
    )
    work_phone: str = take_n_check_phone(
        text_for_input=f'Введите номер рабочего телефона (По умолчанию - {work_phone}): ',
        default=work_phone
    )
    pers_phone: str = take_n_check_phone(
        text_for_input=f'Введите номер личного телефона (По умолчанию - {pers_phone}): ',
        default=pers_phone
    )
    add_entry(first_name, last_name, org_name, work_phone, pers_phone)
    return menu_entries()


def cmd_find_entries(search_screen: dict | None = None):
    """
    Функция поиска записей. Позволяет пользователю выбрать категорию для поиска (по одной), затем
        предлагает продолжить или добавить ещё категории (можно выбрать каждую).
    Возвращает функцию вызова записей, но с заготовленным списком
    """
    if search_screen is None:
        search_screen: dict = {
            'Имя': '',
            'Фамилия': '',
            'Организация': '',
            'Рабочий телефон': '',
            'Личный телефон': '',
        }
    categories: list = [*search_screen.keys()]
    str_search_screen: str = '\n'.join([f'{i+1} - {key_value[0]}: {key_value[1]}'
                                        for i, key_value in enumerate(search_screen.items())])
    main_screen: str = make_screen(main_info=str_search_screen)
    print(main_screen)
    category: int = take_n_check_int(range_int=5)
    category: str = categories[category]
    if category in categories[:2]:
        value: str = take_n_check_name(text_for_input='Введите слово целиком или часть: ')
    elif category in categories[2:3]:
        value: str = take_n_check_name(text_for_input='Введите слово целиком или часть: ', org_name_mode=True)
    else:  # category in categories[3:]:
        value: str = take_n_check_phone(text_for_input='Введите номер целиком или его часть :')
    search_screen[category]: str = value
    if take_n_check_answer():
        table: dict = find_entry(*search_screen.values())
        return menu_entries(table=table)
    return cmd_find_entries(search_screen=search_screen)


def cmd_next_page():
    """
    Функция изменения текущей страницы на следующую
    """
    return menu_entries(change_page=1)


def cmd_prev_page():
    """
    Функция изменения текущей страницы на предыдущую
    """
    return menu_entries(change_page=-1)


def cmd_back_menu():
    """
    Функция возврата к записям (главное меню), в основном необходимо для выхода из списка после поиска
    """
    return menu_entries(back=True)
