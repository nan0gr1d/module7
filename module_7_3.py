"""
module_7_3
"""
class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = []
        for filename in filenames:
            self.file_names.append(filename)

    def get_all_words(self):
        all_words = {}
        for fn in self.file_names:
            all_words[fn] = []
            with open(fn, encoding='utf-8') as file:
                buffer = file.read()
            lines = buffer.split("\n")
            for line in lines:
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(char, '')
                words = line.lower().split()
                all_words[fn].extend(words)
        return all_words

    def find(self, word):
        """
        метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        :param word:
        :return: dictionary
        """
        word = word.lower()
        rdict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                rdict[name] = words.index(word) + 1 # индекс нумерует вхождения с нуля
        return rdict

    def count(self, word):
        """
        метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла.
        :param word:
        :return: dictionary
        """
        word = word.lower()
        rdict = {}
        for name, words in self.get_all_words().items():
            if word in words:
                rdict[name] = words.count(word)
        return rdict


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

#-eof-module_7_3