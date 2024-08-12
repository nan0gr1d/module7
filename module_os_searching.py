"""
module_os_searching
"""

import os
import time
directory = "."

os.chdir(directory)
for dirn, dirlist, filelist in os.walk(directory):
    for file in filelist:
        if not os.path.isfile(file):
            continue
        dir_ = os.getcwd()
        filepath = os.path.join(dir_, file)
        file_size = os.path.getsize(file)

        filetime = os.path.getmtime(file)
        formatted_time = (time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)))
        parent_dir = os.path.dirname(dir_)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, '
              f'\nВремя изменения: {formatted_time}, '
              f'\nРодительская директория: {parent_dir}\n')

"""
eof-module_os_searching
"""