from math import ceil

from db.manage_database import get_entries

curr_page: int = 1


def paginator(table: dict) -> dict[int, list]:
    """
    Функция переводящая table в list, для слайсинга по страницам.
    Возвращает соответствующий странице dict
    """
    list_table = list()
    new_table = dict()
    for key, value in table.items():
        str_key_value = str(key) + '@' + '_'.join(value)
        list_table.append(str_key_value)
    start_slice: int = curr_page * 10 - 10
    for elem in list_table[start_slice:start_slice + 10]:
        key, value = elem.split('@')
        value = value.split('_')
        new_table[int(key)] = value
    return new_table


def make_screen(main_info: str | list = '') -> str:
    """
    Функция заготовки шаблона экрана
    """
    screen_template = """
{}
{}
{}
""".format('=' * 44, main_info, '_' * 44)
    return screen_template


def make_kb() -> str:
    """
    Функция заготовки шаблона клавиатуры
    """
    basic_navigation: list[str] = [
        ':a - Добавить запись;',
        ':d - Удалить запись;',
        ':r - Редактировать запись;',
        ':f - Поиск по категориям;',
        ':b - К записям;',
    ]
    basic_kb = [elem + '\n' if i % 2 else elem + '\t' for i, elem in enumerate(basic_navigation)]
    return '{}\n{}'.format(''.join(basic_kb), '=' * 44)


def menu_entries(table: dict | None = None, change_page: int | None = None, back: bool = False):
    """
    Главная функция вызова записей
    :param table: Может использовать заранее подготовленный словарь
    :param change_page: Принимает -1 или +1 для работы с пагинацией
    :param back: если True, функция вернёт изначальный список
    """
    data_entries: dict[int, list] = get_entries() if not table else table
    global curr_page
    if back:
        curr_page = 1
    len_table = len(data_entries)
    if not len_table:
        print(make_screen(main_info='Список пуст'))
        return print(make_kb())
    if len_table > 10:
        max_pages = ceil(len_table / 10)
        if change_page:
            if (curr_page == 1 and change_page == -1) or (curr_page == max_pages and change_page == 1):
                return print('Некорректный ввод')
            curr_page += change_page
        data_entries = paginator(data_entries)
    main_info: str = 'Записи:\n'
    for key, value in data_entries.items():
        main_info += '{}: {};\n'.format(key, ', '.join(value))
    screen = make_screen(main_info=main_info)
    print(screen)
    if len_table > 10:
        print(f'\t\tСтр.{curr_page}/{max_pages}\n')
        if curr_page == max_pages:
            page_button = '<< - Предыдущая страница'
        elif curr_page == 1:
            page_button = '>> - Следующая страница'
        else:
            page_button = '<< / >> - Предыдущая страница / Следующая страница'
        print(f'{page_button}\n')
    print(make_kb())
    return
