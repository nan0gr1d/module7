"""
module_7_1
"""
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        """
        Инициализация файла базы,
        поскольку обработку исключительных состояний Еше не изучали
        """
        file = open(self.__file_name, 'a')
        file.write('')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        file.seek(0)
        buffer = file.read()
        file.close()
        return buffer

    def add_record(self, record):
        file = open(self.__file_name, 'a')
        file.write(record)
        file.flush()
        file.close()

    def add(self, *products: Product):
        for product in products:
            buffer = self.get_products()
            if buffer.count(f"{product.name},") > 0:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                self.add_record(f"{str(product)}\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

#eof-module_7_1