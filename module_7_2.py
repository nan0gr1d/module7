"""
module_7_2
"""
def custom_write(file_name: str, strings: list):
    """
    принимает аргументы file_name - название файла для записи, strings - список строк для записи.
    Функция должна:
    Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
    """
    file = open(file_name, 'w', encoding='utf-8')
    istr = 0
    dict_ = {}
    for string in strings:
        istr += 1
        ipos = file.tell()
        key = (istr, ipos)
        file.write(f"{string}\n")
        dict_[key] = string
    file.close()
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

#-eof-module_7_2