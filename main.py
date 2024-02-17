from db.manage_database import check_create_table
from interface.dispatcher import distributor
from interface.menu import menu_entries

if __name__ == '__main__':
    check_create_table()
    menu_entries()
    distributor()
