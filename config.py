from os import getcwd

BASE_DIR: str = getcwd()
DB_NAME = 'phone_book.txt'
DB_NAME_W_PATH = BASE_DIR + '/' + DB_NAME
