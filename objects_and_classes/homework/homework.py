
import random
import uuid
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS


class Cesar:
    """Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів."""

    def __init__(self, name: str, garages=[]):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()

    def __str__(self):
        return 'name: {self.name}, garage: {self.garages}, id: {self.register_id}'.format(self=self)

    def hit_hat(self):
        car_price = 0.0
        for garage in self.garages:
            for car in garage.cars:
                car_price += car.price
        return car_price

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        car_amount = 0
        for garage in self.garages:
            len(garage.cars)
            car_amount += 1
        return car_amount

    def add_car(self, car, garage=None):
        if garage:
            if garage.free_places():
                garage.add_car(car)
                return f'Сar was added to garage: {garage}, town: {garage.town}'

            else:
                return 'no free places in the selected garage'
        maximum = 0
        max_garage = None
        for garage in self.garages:
            if garage.free_places() >= maximum:
                maximum = garage.free_places()
                max_garage = garage

        if max_garage in None:
            return 'No free places'

        max_garage.add_car(car)
        return f'Сar was added to garage: {max_garage}, town: {max_garage.town}'

    def __lt__(self, other):
        return other.hit_hat() < self.hit_hat()

    def __gt__(self, other):
        return other.hit_hat() > self.hit_hat()

    def __le__(self, other):
        return other.hit_hat() <= self.hit_hat()

    def __ge__(self, other):
        return other.hit_hat() >= self.hit_hat()

    def __eq__(self, other):
        return other.hit_hat() == self.hit_hat()


class Car:
    """Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
"""
    def __init__(self, producer: CARS_PRODUCER, car_type: CARS_TYPES, price: float, mileage: float):
        self.price = price
        self.number = uuid.uuid4()
        self.mileage = mileage
        self.producer = producer
        self.car_type = car_type if car_type in CARS_TYPES else None

    def __str__(self):
        return 'producer: {self.producer}, type: {self.type}, price: {self.price}, ' \
               'mileage: {self.mileage}, number: {self.number}'.format(self=self)

    def change_number(self):
        self.number = uuid.uuid4()

    def __lt__(self, other):
        return other.price < self.price

    def __eq__(self, other):
        return other.price == self.price

    def __le__(self, other):
        return other.price <= self.price

    def __ge__(self, other):
        return other.price >= self.price

    def __gt__(self, other):
        return other.price > self.price


class Garage:
    """Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
"""
    def __init__(self, town: TOWNS, cars, places, owner=None):
            self.town = town if town in TOWNS else None
            self.cars = cars
            self.places = places
            self.owner = owner if owner else uuid.uuid4()

    def __str__(self):
        return 'town: {self.town}, car: {self.cars}, place: {self.places}, ownerid: {self.owner}'.format(self=self)

    def add_car(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    def free_places(self):
        return self.places - len(self.cars)

    def remove_car(self, car: Car):
        self.cars.remove(car)

    def hit_hat(self):
        sum_car = 0
        for car in self.cars:
            sum_car = sum_car + car.price
        return sum_car


if __name__ == "__main__":
    cesar_id = uuid.uuid4()
    print("Let's define id of cesar: ", cesar_id)
    print(" ")

    garages = []

    for _ in range(5):
        garage = Garage(
            cars=[],
            town=random.choice(TOWNS),
            places=4,
            owner=cesar_id
        )
        garages.append(garage)

    cesar1 = Cesar('Rich', garages)
    cesar2 = Cesar('Super Rich', garages)

    cars = []
    for _ in range(10):
        car = Car(
            car_type=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            price=random.uniform(100000, 1000000),
            mileage=random.uniform(25, 10000)
        )
        cesar1.add_car(car, random.choice(garages))
        cesar2.add_car(car, random.choice(garages))

    print(f' Cesar name is: {cesar1.name}, \n'
          f'here is a list of garages {cesar1.name} owns: \n {cesar1.garages},\n '
          f'the id of {cesar1.name} is: {cesar1.register_id} if you are interested \n')

    print("Let's get the information about", cesar1.name, "garage details: \n", cesar1.garages[4], '\n')

    print("Here we will get the price of all cars in the", cesar1.name, "garages. \n"
          "So the total sum is:", cesar1.hit_hat(), "\n")

    print("Let's check amount of garages", cesar1.name, "has:", cesar1.garages_count(), "\n")

    print(cesar1.name, "has", cesar1.cars_count(), "cars")

    print(cesar1.name, "wants to add their car to the garage, let's see:", cesar1.add_car(2, garages[4]), "\n")

    print(f' Cesar name is: {cesar2.name}, \n'
          f'here is a list of garages {cesar2.name} owns: \n {cesar2.garages},\n '
          f'the id of {cesar2.name} is: {cesar2.register_id} if you are interested \n')

    print("Here we will get the price of all cars in the", cesar2.name, "garages. \n"
          "So the total sum is:", cesar2.hit_hat(), "\n")
    # print(cesar2.name)
    # print(cesar2.hit_hat())
    print("Compare if", cesar1.name, "spent more money than", cesar2.name, "-", cesar1.hit_hat() > cesar2.hit_hat())
    # print('cesar.сars_count = ', cesar2.cars_count())
    # #cesar2.garages[0].remove(cesar2.garages[0].cars[0])
    # print('cesar.сars_count = ', cesar2.cars_count())
