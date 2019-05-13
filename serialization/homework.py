"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

from __future__ import annotations
import pdb
import codecs
import pickle
import random
import uuid
from builtins import str
from collections import OrderedDict

from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import json
from ruamel.yaml import YAML

yaml = YAML()


class Cesar:
    def __init__(self, name: str, garages=[]):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()
        self.yaml = YAML()

    def __repr__(self):
        return 'name: {self.name}, garage: {self.garages}, register_id: {self.register_id}'.format(self=self)


    def to_json(obj: Cesar):
        data = {"name": obj.name, "garages": str(obj.garages), "register_id": str(obj.register_id)}
        return data

    @classmethod
    def from_json(cls, data):
        name = data['name']
        garages = data['garages']
        register_id = data['register_id']
        return Cesar(name=name, garages=garages)

    def to_json_string(self):
        cesar_json_string = json.dumps(self, default=Cesar.to_json)
        return cesar_json_string

    def from_json_string(self, cesar_json_string):
        return json.loads(cesar_json_string, object_hook=Cesar.from_json)

    """method to convert python object to json file"""

    def to_json_file(self):
        with open('cesar_file.json', "w") as write_file:
            return json.dump(self, write_file, default=Cesar.to_json, indent=6)


    def from_json_file(cls):
        with open('cesar_file.json', "r") as file:
            return json.load(file, object_hook=Cesar.from_json)


    """Yaml"""
    def to_yaml(obj: Cesar):
        data = {"name": obj.name, "garages": str(obj.garages), "register_id": str(obj.register_id)}
        return data

    def from_yaml(cls, data):
        name = data['name']
        garages = data['garages']
        register_id = data['register_id']
        return Cesar(name=name, garages=garages)

    def to_yaml_string(self):
        cesar_yaml_string = self.to_yaml
        return str(cesar_yaml_string)

    def from_yaml_string(self, cesar_yaml_string):
        return Cesar.from_yaml(self, yaml.load(cesar_yaml_string))

    def to_yaml_file(self, file_name):
        with open(file_name, 'w') as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    def from_yaml_file(self, file_name):
        with open(file_name, 'r') as read_file:
            return Cesar.from_yaml(self, yaml.load(read_file))

    """Pickle"""
    def to_pickle_string(self):
        cesar_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return cesar_pickle_string

    @staticmethod
    def from_pickle_string(cesar_pickle_string):
        return pickle.loads(codecs.decode(cesar_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('cesar_pickle.file.txt', "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def from_pickle_file():
        with open('cesar_pickle.file.txt', "rb") as file:
            return pickle.load(file)


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

class Car:
    def __init__(self, producer: CARS_PRODUCER, car_type: CARS_TYPES, price: float, mileage: float):
        self.price = price
        self.number = uuid.uuid4()
        self.mileage = mileage
        self.producer = producer
        self.car_type = car_type if car_type in CARS_TYPES else None

    def __repr__(self):
        return 'producer: {self.producer}, type: {self.car_type}, price: {self.price}, ' \
               'mileage: {self.mileage}, number: {self.number}'.format(self=self)

    def to_json(obj: Car):
        data = {"name": obj.producer, "garages": obj.car_type, "price": round(obj.price), "mileage": round(obj.mileage)}
        return data

    @classmethod
    def from_json(cls, data):
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        return Car(producer=producer, car_type=car_type, price=price, mileage=mileage)

    """method to convert python object to json string"""
    def to_json_string(self):
        car_json_string = json.dumps(self, default=Car.to_json)
        return car_json_string

    def from_json_string(self, car_json_string):
        return json.loads(car_json_string, object_hook=Car.from_json)

    """method to convert python object to json file"""

    def to_json_file(self):
        with open('cars_file.json', "w") as write_file:
            json.dump(self, write_file, default=Car.to_json, indent=6)


    def from_json_file(self):
        with open('cars_file.json', "r") as file:
            restored_cars_file = json.load(file,object_hook=Car.from_json)
            return restored_cars_file

    """Pickle"""

    def to_pickle_string(self):
        car_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return car_pickle_string

    @staticmethod
    def from_pickle_string(car_pickle_string):
        return pickle.loads(codecs.decode(car_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('car_pickle.file.txt', "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def from_pickle_file():
        with open('car_pickle.file.txt', "rb") as file:
            return pickle.load(file)


    """Yaml"""
    def to_yaml(obj: Car):
        data = {"name": obj.producer, "garages": obj.car_type, "price": round(obj.price), "mileage": round(obj.mileage)}
        return data

    def from_yaml(cls, data):
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        return Car(producer=producer, car_type=car_type, price=price, mileage=mileage)

    def to_yaml_string(self):
        car_yaml_string = str(self.to_yaml)
        return car_yaml_string

    def from_yaml_string(self, car_yaml_string):
        return Car.from_yaml(yaml.load(car_yaml_string))

    def to_yaml_file(self, file_name):
        with open(file_name, "w") as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    def from_yaml_file(self, file_name):
        with open(file_name, "r") as read_file:
            return Car.from_yaml(self, yaml.load(read_file))



class Garage:
    def __init__(self, cars, places, town: TOWNS, owner=None):
            self.town = town if town in TOWNS else None
            self.cars = cars
            self.places = places
            self.owner = owner if owner else uuid.uuid4()

    def __repr__(self):
        return 'town: {self.town}, car: {self.cars}, place: {self.places}, ownerid: {self.owner}'.format(self=self)

    def add_car(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    """custome method to convert python object to json"""
    def to_json(obj: Garage):
        data = {"cars": obj.cars, "places": obj.places, "town": obj.town, "owner": obj.owner}
        return data

    """custom method to convert from json to python object"""
    @classmethod
    def from_json(cls, data):
        cars = data['cars']
        places = data['places']
        town = data['town']
        owner = data['owner']
        return Garage(cars=cars, places=places, town=town, owner=owner)

    """method to convert python object to json string"""
    def to_json_string(self):
        garage_json_string = json.dumps(self, default=Garage.to_json)
        return garage_json_string


    """method to convert python object to json file"""
    def to_json_file(self):
        with open('garage_file.json', "w") as write_file:
            json.dump(self, write_file, default=Garage.to_json, indent=6)

    def from_json_string(self, garage_json_string):
        return json.loads(garage_json_string, object_hook=Garage.from_json)

    def from_json_file(self):
        with open('garage_file.json', "r") as file:
            restored_garage_file = json.load(file, object_pairs_hook=Garage.from_json)
            return restored_garage_file




if __name__ == "__main__":
    cesar_id = uuid.uuid4()
    car = Car(producer='Ford', car_type='Sedan', price=24, mileage=678)
    print("Let's define id of cesar: ", cesar_id)
    print(" ")

    garages = []

    for _ in range(2):
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
    for _ in range(2):
        car = Car(
            car_type=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            price=round(random.uniform(100, 200)),
            mileage=round(random.uniform(25, 100))
        )
        cars.append(car)

        cesar1.add_car(car, random.choice(garages))
        cesar2.add_car(car, random.choice(garages))

    print("CESAR", "\n", cesar1, "\n")
    print("JSON", "\n")
    print("Convert Cesar object to JSON string", "\n", cesar1.to_json_string(), "\n")
    cesar_string = cesar1.to_json_string()
    print("Convert JSON Cesar string back", "\n", cesar1.from_json_string(cesar_string), "\n")
    print("Cesar JSON to file")
    cesar1.to_json_file()
    print("Cesar JSON from file", type(cesar1.from_json_file()),cesar1.from_json_file(), "\n")
    print("Pickle", "\n")
    print("Convert Cesar object to pickle string", "\n", cesar1.to_pickle_string(), "\n")
    cesar_pickel_string = cesar1.to_pickle_string()
    print("Convert from pickle back", "\n", cesar1.from_pickle_string(cesar_pickel_string))
    print("Cesar object to pickle file", "\n")
    cesar1.to_pickle_file()
    print("Back from pickle file", type(cesar1.from_pickle_file()), cesar1.from_pickle_file(), "\n")
    print("YAML", "\n")
    yaml_string = cesar1.to_yaml_string()
    print("Cesar object to yaml string", yaml_string, "\n")
    print("YAML file", cesar1.to_yaml_file("yaml.test.yaml"))
    car1 = Car('Ford', 'Sedan', 34, 67)
    print("Test car", car1.to_yaml_string())
    car_test = car1.to_yaml_string()


