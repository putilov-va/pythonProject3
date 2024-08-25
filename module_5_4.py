class House:
    "Задача История строительства"
    houses_history = []

    def __new__(cls, *args):
        # print(args)
        cls.houses_history.append(*args[:1])

        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
#
# # Удаление объектов
del h2
del h3
#
print(House.houses_history)