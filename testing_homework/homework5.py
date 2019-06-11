from __future__ import annotations
from ruamel.yaml import YAML
import json
import pickle
import codecs
import uuid
from builtins import str
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS


yaml = YAML()


class Cesar:
    def __init__(self, name: str, garages=[]):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()
        self.yaml = YAML()

    def __repr__(self):
        return 'name: {self.name}, garage: {self.garages}, ' \
               'register_id: {self.register_id}'.format(self=self)

    def hit_hat(self):
        car_price = 0
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
        if garage is None:
            maximum = 0
            max_garage = None
            for garage in self.garages:
                if garage.free_places() >= maximum:
                    maximum = garage.free_places()
                    max_garage = garage
            return max_garage.add_car(car) if garage else 'no free places found'
        else:
            return garage.add_car(car)

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def to_json(obj: Cesar):
        garages = [garage.to_json() for garage in obj.garages]
        data = {"name": obj.name,
                "garages": garages,
                "register_id": str(obj.register_id)}
        return data

    @staticmethod
    def from_json(data):
        name = data["name"]
        garages1 = [Garage.from_json(garage) for garage in data['garages']]
        return Cesar(name=name, garages=garages1)

    def to_json_string(self):
        cesar_json_string = json.dumps(self, default=Cesar.to_json)
        return cesar_json_string

    @staticmethod
    def from_json_string(cesar_json_string):
        try:
            return json.loads(cesar_json_string)

        except TypeError as e:
            print(e)

    def to_json_file(self):
        with open('cesar_file.json', "w") as write_file:
            return json.dump(self, write_file, default=Cesar.to_json)

    @staticmethod
    def from_json_file():
        with open('cesar_file.json', "r") as f:
            return json.load(f)

    def to_pickle_string(self):
        cesar_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return cesar_pickle_string

    @staticmethod
    def from_pickle_string(cesar_pickle_string):
        return pickle.loads(codecs.decode(cesar_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('cesar_pickle.dat', "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle_file():
        with open('cesar_pickle.dat', "rb") as f:
            return pickle.load(f)


class Car:
    def __init__(self, producer: CARS_PRODUCER, car_type: CARS_TYPES,
                 price: float, mileage: float):
        self.price = price
        self.number = uuid.uuid4()
        self.mileage = mileage
        self.producer = producer
        self.car_type = car_type if car_type in CARS_TYPES else None

    def __repr__(self):
        return 'producer: {self.producer}, type: {self.car_type}, price: {self.price}, ' \
               'mileage: {self.mileage}, number: {self.number}'.format(self=self)

    def change_number(self):
        self.number = uuid.uuid4()

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __gt__(self, other):
        return self.price > other.price

    def to_json(self: Car):
        data = {"producer": self.producer,
                "car_type": self.car_type,
                "price": str(self.price),
                "mileage": self.mileage}
        return data

    @classmethod
    def from_json(cls, data):
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        return cls(producer=producer, car_type=car_type, price=price, mileage=mileage)

    def to_json_string(self):
        car_json = Car.to_json(self)
        car_json_string = json.dumps(car_json)
        return car_json_string

    @staticmethod
    def from_json_string(car_json_string):
        return json.loads(car_json_string, object_hook=Car.from_json)

    def to_json_file(self):
        with open("cars_file.json", 'w') as write_file:
            json.dump(self, write_file, default=Car.to_json)

    @staticmethod
    def from_json_file():
        with open('cars_file.json', "r") as f:
            restored_cars_file = json.load(f, object_hook=Car.from_json)
            return restored_cars_file

    def to_pickle_string(self):
        car_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return car_pickle_string

    @staticmethod
    def from_pickle_string(car_pickle_string):
        return pickle.loads(codecs.decode(car_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('car_pickle.dat', "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle_file():
        with open('car_pickle.dat', "rb") as f:
            return pickle.load(f)

    def to_yaml(self: Car):
        data = {"producer": self.producer, "car_type": self.car_type,
                "price": round(self.price), "mileage": round(self.mileage)}
        return data

    @staticmethod
    def from_yaml(data):
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        return Car(producer=producer, car_type=car_type, price=price, mileage=mileage)

    def to_yaml_string(self):
        car_yaml_string = str(self.to_yaml())
        return car_yaml_string

    @staticmethod
    def from_yaml_string(car_yaml_string):
        return Car.from_yaml(yaml.load(car_yaml_string))

    def to_yaml_file(self):
        with open('car_file.yaml', "w") as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    @staticmethod
    def from_yaml_file():
        with open('car_file.yaml', "r") as read_file:
            return Car.from_yaml(yaml.load(read_file))


class Garage:
    def __init__(self, places, town: TOWNS, owner=None, cars=[]):
        self.town = town if town in TOWNS else None
        self.cars = cars
        self.places = places
        self.owner = owner if owner else uuid.uuid4()

    def __repr__(self):
        return 'cars: {self.cars}, place: {self.places}, ' \
               'town: {self.town}, ownerid: {self.owner}'.format(self=self)

    def add_car(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    def free_places(self):
        return self.places - len(self.cars)

    def remove_c(self, car: Car):
        try:
            self.cars.remove(car)
        except ValueError:
            return 'car is not in the garage'

    def hit_hat(self):
        sum_car = 0
        for car in self.cars:
            sum_car = sum_car + car.price
        return sum_car

    def add_c(self, car: Car):
        if len(self.cars) <= len(self.places):
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    def to_json(self: Garage):
        cars = [car.to_json() for car in self.cars]
        data = {"places": self.places, "town": self.town,
                "owner": str(self.owner), "cars": cars}
        return data

    @staticmethod
    def from_json(data):
        places = data["places"]
        town = data["town"]
        owner = data["owner"]
        cars1 = [Car.from_json(item) for item in data['cars']]

        return Garage(places=places, town=town, owner=owner, cars=cars1)

    def to_json_string(self):
        garage_json = Garage.to_json(self)
        garage_json_string = json.dumps(garage_json)
        return garage_json_string

    def to_json_file(self):
        with open('garage_file.json', "w") as write_file:
            json.dump(self, write_file, default=Garage.to_json)

    @staticmethod
    def from_json_string(garage_json_string):
        return json.loads(garage_json_string)

    @staticmethod
    def from_json_file():
        with open('garage_file.json', "r") as f:
            restored_garage_file = json.load(f)
            return restored_garage_file

    def to_yaml(self: Garage):
        cars = [car.to_yaml() for car in self.cars]
        data = {"cars": cars, "places": self.places, "town": self.town,
                "owner": str(self.owner)}
        return data

    @classmethod
    def from_yaml(cls, data):
        cars = data['cars']
        places = data['places']
        town = data['town']
        owner = data['owner']
        return Garage(cars=cars, places=places, town=town, owner=owner)

    def to_yaml_string(self):
        garage_yaml_string = self.to_yaml()
        return str(garage_yaml_string)

    @staticmethod
    def from_yaml_string(garage_yaml_string):
        return Garage.from_yaml(yaml.load(garage_yaml_string))

    def to_yaml_file(self):
        with open('garage_yaml.yaml', 'w') as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    @staticmethod
    def from_yaml_file():
        with open('garage_yaml.yaml', 'r') as read_file:
            return Garage.from_yaml(yaml.load(read_file))



