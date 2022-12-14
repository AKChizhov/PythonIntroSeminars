import logging

logging.basicConfig(
    level=logging.INFO,
    filename='phonebook.log', # Файл для логгинг-сообщений
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s', # Формат сообщений
    #datefmt='%d.%m.%Y %H:%M:%S', # Без миллисекунд
)
