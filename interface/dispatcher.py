from interface.common_cmd import (cmd_add_entry, cmd_back_menu, cmd_del_entry,
                                  cmd_edit_entry, cmd_find_entries,
                                  cmd_next_page, cmd_prev_page)


def distributor():
    """
    Принимает команды и вызывает соответствующие им функции. После окончания которых вызывает себя вновь,
    для приёма новых команд
    """
    command: str = input()
    common_table_command: dict = {
        ':a': cmd_add_entry,
        ':d': cmd_del_entry,
        ':r': cmd_edit_entry,
        ':f': cmd_find_entries,
        '>>': cmd_next_page,
        '<<': cmd_prev_page,
        ':b': cmd_back_menu,
    }
    if command not in common_table_command.keys():
        print('Некорректная команда. Пожалуйста используйте только предложенные варианты.')
    else:
        common_table_command[command]()
    return distributor()
