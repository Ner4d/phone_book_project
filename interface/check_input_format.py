def take_n_check_name(text_for_input: str, org_name_mode: bool = False, default: str = '') -> str:
    """
    Допустимы лишь пробелы, буквы русского и английского алфавита (в org_name_mode дополнительно допускаются цифры,
    кавычки и тире)
    """
    user_input = input(text_for_input)
    if not user_input:
        return default
    check_list = [' '] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('а'), ord('я') + 1)]
    if org_name_mode:
        check_list += [str(i) for i in range(10)] + ['-', '"', '(', ')']
    for elem in user_input:
        if elem.lower() not in check_list:
            print('Обнаружены неподходящие символы.'
                  'Используйте только буквы английского/русского алфавита для имени/фамилии'
                  '(Для наименований организаций также допускаются символы "-()')
            return take_n_check_name(text_for_input=text_for_input, org_name_mode=org_name_mode)
    return user_input


def take_n_check_phone(text_for_input: str, default: str = ''):
    """
    Просто берёт пользовательский ввод и пытается обратить в int, в случае неудачи вызывает сама себя для
        последующего ввода
    Возвращает число в виде строки
    """
    user_input = input(text_for_input)
    if not user_input:
        return default
    try:
        number_phone = abs(int(user_input))
    except ValueError:
        print('Неверный формат номера телефона.\nПожалуйста используйте цифры')
        return take_n_check_phone(text_for_input=text_for_input)
    return str(number_phone)


def take_n_check_int(range_int: int) -> int:
    """
    Просто берёт пользовательский ввод и пытается обратить в int и проверяет число на вхождение в range_int,
        в случае неудачи вызывает сама себя для последующего ввода.
    Возвращает число в виде строки
    """
    user_input = input("Введите соответствующую цифру: ")
    try:
        user_input = int(user_input)
        if user_input not in range(1, range_int + 1):
            print('Некорректный ввод')
            return take_n_check_int(range_int=range_int)
    except ValueError:
        print('Некорректный ввод')
        return take_n_check_int(range_int=range_int)
    return user_input - 1


def take_n_check_number_entry(table: dict) -> int:
    """
    Просто берёт пользовательский ввод и пытается обратить в int и проверяет число на существование.
    Возвращает число в виде строки
    """
    user_input = input('Введите номер записи: ')
    try:
        user_input = int(user_input)
    except ValueError:
        print('Некорректный ввод. Пожалуйста используйте номер записи')
        return take_n_check_number_entry(table=table)
    if user_input not in table.keys():
        print('Некорректный ввод. Пожалуйста введите существующий номер записи')
        return take_n_check_number_entry(table=table)
    return user_input


def take_n_check_answer() -> bool:
    """
    Берёт и проверяет пользовательский ввод на соответствие варианта ответа да/нет yes/no
    Возвращает булево значение в соответствии с ответом

    """
    answer: str = input('Этого достаточно? (да/нет): ')
    if answer.lower() in 'даyes':
        return True
    elif answer.lower() in 'нетno':
        return False
    else:
        print('Некорректный ответ')
        return take_n_check_answer()
