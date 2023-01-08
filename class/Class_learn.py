class Citizen():
    '''Класс жителя'''

    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def show_licence(self):
        '''Показывает информацию о доме'''
        print(f'\nИмя: {self.name}, возраст: {self.age}, Пол: {self.sex}')


class Private_house():
    '''Класс Личный дом'''

    def __init__(self, street, address, floors, residents, info_residents=list()):
        self.street = street
        self.address = address
        self.floors = floors
        self.residents = residents
        self.info_residents = info_residents

    def show_info(self):
        '''Показывает информацию о доме'''
        print(f'\nУлица: {self.street}, номер дома: {self.address},'
              f'\nЭтажи: {self.floors}')

    def add_flours(self, quantity):
        '''Добавляет этажи'''
        self.floors += quantity

    def add_residents(self, quantity):
        '''Добавляет этажи'''
        self.residents += quantity


    def describe_residents(self, list_of_citizen=list()):
        for i in range(len(list_of_citizen)):
            name, age, sex = list_of_citizen[i]
            self.info_residents.append(Citizen(name, age, sex))

    def show_residents(self):
        print('Жители дома:')
        for i in self.info_residents:
            print(f'Name: {i.name} '
                  f'Age: {i.age} '
                  f'Sex: {i.sex}\n')

    def draw_house(self):
        '''Рисует дом'''
        flour = '-------------\n' \
                '|           |\n'
        print(flour * self.floors + '-------------\n')

# class Apartment(Private_house):
#     '''Класс Квартира'''
#
#     def __init__(self, street, address, floors, flats, entrance):
#         super().__init__(street, address, floors)
#         self.flats = flats
#         self.entrance = entrance
#
#     def show_info(self):
#         '''Показывает информацию о доме'''
#         print(f'\nУлица: {self.street}, номер дома: {self.address},'
#               f'\nЭтажи: {self.floors}, Количество квартир: {self.flats},'
#               f'\nПодъезды: {self.entrance}')
#
#     def add_flats(self, quantity):
#         '''Добаляет квартиры'''
#         self.flats += quantity
#
#     def draw_house(self):
#         '''Рисует дом'''
#         roof = '-------------' * self.entrance
#         flour = '\n' + '|           |' * self.entrance + '\n'
#         print((roof + flour) * self.floors + roof)
