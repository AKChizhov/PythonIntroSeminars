import base_create as dg
import u_i as ui
import logger as lg
import crud

dg.start() # генерация базы данных
lg.logging.info('Start') # Модуль logging («logger»), для логирования сообщений, которые  хотим видеть.
crud.init_data_base('base_phone.csv') # Модуль работы с базой данных
ui.ls_menu() # Модуль пользовательского интерфейса