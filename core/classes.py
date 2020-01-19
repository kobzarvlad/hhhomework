class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    def __repr__(self):
        return '{} {}'.format(self.manufacturer, self.model)


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __getitem__(self, position):
        return self.cars[position]

    def add(self, car):
        self.cars.append(car)

    def delete(self, position):
        self.cars.pop(position)



