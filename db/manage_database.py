from config import DB_NAME_W_PATH


def add_entry(
        first_name: str,
        last_name: str,
        org_name: str | None = None,
        work_phone: None | str = None,
        personal_phone: None | str = None
) -> None:
    with open(DB_NAME_W_PATH, 'a', encoding='UTF-8') as phone_book:
        raw_string_entry: list[str] = [
            f'Имя: {first_name}',
            f'Фамилия: {last_name}',
            'Организация: {}'.format(org_name or 'Отсутствует'),
            'Раб.телефон: {}'.format(work_phone or 'Неизвестен'),
            'Лич.телефон: {}'.format(personal_phone or 'Неизвестен'),
        ]
        string_entry: str = ';'.join(raw_string_entry) + '\n'
        phone_book.write(string_entry)  # Добавляет нашу запись в книгу
    return


def get_entries() -> dict[int, list[str]]:
    result_table = dict()
    count_entry = 1
    with open(DB_NAME_W_PATH, 'r+', encoding='UTF-8') as phone_book:
        book_as_list: list[list[str]] = [row.rstrip().split(';') for row in phone_book.readlines()]
        for row in book_as_list:
            result_table[count_entry] = row
            count_entry += 1
    return result_table


def del_entry(number_entry: int, table: dict[int, list]):
    if number_entry in table.keys():
        del table[number_entry]
    with open(DB_NAME_W_PATH, 'w', encoding='UTF-8') as phone_book:
        for raw_entry in table.values():
            entry: str = ';'.join(raw_entry) + '\n'
            phone_book.write(entry)
    return


def find_entry(
        first_name: str | None = None,
        last_name: str | None = None,
        org_name: str | None = None,
        work_phone: str | None = None,
        personal_phone: str | None = None,
) -> dict:
    result_table = dict()  # Здесь мы будем хранить то, что отвечает требованиям
    phone_book: dict[int, list] = get_entries()  # Читаем по новой "книгу", чтобы иметь актуальные значения
    check_list: list = [first_name, last_name, org_name, work_phone, personal_phone]
    for key, entry in phone_book.items():
        if all([elem.lower() in entry[i].lower() for i, elem in enumerate(check_list) if elem]):  # Проверяем соответствия
            result_table[key] = entry
    return result_table


def check_create_table():
    """
    Функция создания базы данных в режиме добавления, необходимо для создания, в случае отсутствия
    """
    file = open(DB_NAME_W_PATH, 'a', encoding='UTF-8')
    file.close()
    return
