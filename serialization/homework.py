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
import codecs
import pickle
import random
import uuid
import pdb
from builtins import str

from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import json
from ruamel.yaml import YAML

yaml = YAML()


class Cesar:
    def __init__(self, name: str, garages=None):
        if garages is None:
            garages = []
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()

    def __repr__(self):
        return 'name: {self.name}, garage: {self.garages}, register_id: {self.register_id}'.format(self=self)

    @staticmethod
    def to_json(obj: Cesar):
        garages = [garage.to_json_string() for garage in obj.garages]
        data = {'name': obj.name,
                'garages': garages,
                'register_id': str(obj.register_id)}
        return data

    @staticmethod
    def from_json(data):
        name = data['name']
        #register_id = data["register_id"]
        garages1 = [Garage.from_json_string(garage) for garage in data['garages']]
        return Cesar(name=name, garages=garages1)

    def to_json_string(self):
        cesar_json_string = json.dumps(self, default=Cesar.to_json)
        formatted_string = json.JSONDecoder().decode(cesar_json_string)
        return formatted_string

    @staticmethod
    def from_json_string(cesar_json_string):
        try:
            return json.loads(cesar_json_string, object_hook=Cesar.from_json)

        except TypeError as e:
            print(e)

    def to_json_file(self):
        with open('cesar_file.json', "w") as write_file:
            return json.dump(self, write_file, default=Cesar.to_json)

    @classmethod
    def from_json_file(cls):
        with open('cesar_file.json', "r") as f:
            return json.load(f, object_hook=Cesar.from_json)

    def to_yaml(self):
        garages = [garage.to_yaml_string() for garage in self.garages]
        data = {'name': self.name, 'garages': garages, 'register_id': str(self.register_id)}
        return data

    @classmethod
    def from_yaml(cls, data):
        name = data['name']
        garages1 = [Garage.from_yaml_string(garage) for garage in data['garages']]
        return Cesar(name=name, garages=garages1)

    def to_yaml_string(self):
        cesar_yaml_string = self.to_yaml()
        return cesar_yaml_string

    @staticmethod
    def from_yaml_string(cesar_yaml_string):
        return Cesar.from_yaml(yaml.load(cesar_yaml_string))

    def to_yaml_file(self, file_name):
        with open(file_name, 'w') as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    @staticmethod
    def from_yaml_file(file_name):
        with open(file_name, 'r') as read_file:
            return Cesar.from_yaml(yaml.load(read_file))

    def to_pickle_string(self):
        cesar_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return cesar_pickle_string

    @staticmethod
    def from_pickle_string(cesar_pickle_string):
        return pickle.loads(codecs.decode(cesar_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('cesar_pickle.file.dat', "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle_file():
        with open('cesar_pickle.file.dat', "rb") as f:
            return pickle.load(f)

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

    @staticmethod
    def to_json(obj: Car):
        data = {'producer': obj.producer, 'car_type': obj.car_type, 'price': str(obj.price),
                'mileage': obj.mileage}
        return data

    @staticmethod
    def from_json(data):
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        return Car(producer=producer, car_type=car_type, price=price, mileage=mileage)

    def to_json_string(self):
        car_json_string = json.dumps(self, default=Car.to_json, indent=6)
        return car_json_string

    @staticmethod
    def from_json_string(car_json_string):
        return json.loads(car_json_string, object_hook=Car.from_json)

    def to_json_file(self):
        with open('cars_file.json', "w") as write_file:
            json.dump(self, write_file, default=Car.to_json)

    @staticmethod
    def from_json_file():
        with open('cars_file.json', "r") as f:
            restored_cars_file = json.load(f, object_hook=Car.from_json)
            return restored_cars_file

    """
    Pickle
    """

    def to_pickle_string(self):
        car_pickle_string = codecs.encode(pickle.dumps(self), "base64").decode()
        return car_pickle_string

    @staticmethod
    def from_pickle_string(car_pickle_string):
        return pickle.loads(codecs.decode(car_pickle_string.encode(), "base64"))

    def to_pickle_file(self):
        with open('car_pickle.file.dat', "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def from_pickle_file():
        with open('car_pickle.file.dat', "rb") as f:
            return pickle.load(f)

    """
    
    Yaml
    """

    def to_yaml(self):
        data = {"producer": self.producer, "car_type": self.car_type, "price": round(self.price),
                "mileage": round(self.mileage)}
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

    def to_yaml_file(self, file_name):
        with open(file_name, "w") as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    @staticmethod
    def from_yaml_file(file_name):
        with open(file_name, "r") as read_file:
            return Car.from_yaml(yaml.load(read_file))


class Garage:
    def __init__(self, places, town: TOWNS, owner=None, cars=[]):
        self.town = town if town in TOWNS else None
        self.cars = cars
        self.places = places
        self.owner = owner if owner else uuid.uuid4()

    def __repr__(self):
        return 'cars: {self.cars}, place: {self.places}, town: {self.town}, ownerid: {self.owner}'.format(self=self)

    def add_car(self, car: Car):
        if len(self.cars) < self.places:
            self.cars.append(car)
            return f'Car was added to garage: {self.town}'

    """
    custom method to convert python object to json
    """

    @staticmethod
    def to_json(obj: Garage):
        cars = [car.to_json_string() for car in obj.cars]
        data = {'places': obj.places, 'town': obj.town, 'owner': str(obj.owner), 'cars': cars}
        return data

    """
    custom method to convert from json to python object
    """

    @staticmethod
    def from_json(data):
        places = data["places"]
        town = data["town"]
        owner = data["owner"]

        cars1 = [Car.from_json_string(item) for item in data['cars']]

        return Garage(places=places, town=town, owner=owner, cars=cars1)

    """
    method to convert python object to json string
    """

    def to_json_string(self):
        garage_json_string = json.dumps(self, default=Garage.to_json)
        return garage_json_string

    """
    method to convert python object to json file
    """

    def to_json_file(self, file_name):
        with open(file_name, "w") as write_file:
            json.dump(self, write_file, default=Garage.to_json)

    @staticmethod
    def from_json_string(garage_json_string):
        return json.loads(garage_json_string, object_hook=Garage.from_json)

    @staticmethod
    def from_json_file(file_name):
        with open(file_name, "r") as f:
            restored_garage_file = json.load(f, object_hook=Garage.from_json)
            return restored_garage_file

    """
    Yaml
    """

    def to_yaml(self: Garage):
        cars = [car.to_json_string() for car in self.cars]
        data = {'cars': cars, 'places': self.places, 'town': self.town, 'owner': str(self.owner)}
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

    def to_yaml_file(self, file_name):
        with open(file_name, 'w') as write_data:
            return yaml.dump(self.to_yaml(), write_data)

    @staticmethod
    def from_yaml_file(file_name):
        with open(file_name, 'r') as read_file:
            return Garage.from_yaml(yaml.load(read_file))


if __name__ == "__main__":
    cesar_id = uuid.uuid4()
    car = Car(producer='Ford', car_type='Sedan', price=24, mileage=678)
    print("Let's define id of cesar: ", cesar_id)
    print(" ")

    garages = []

    for _ in range(2):
        garage = Garage(
            places=4,
            town=random.choice(TOWNS),
            owner=cesar_id,
            cars=[]
        )
        garages.append(garage)

    cesar1 = Cesar('Rich', garages)
    cesar2 = Cesar('Super Rich', garages)

    cars = []
    for _ in range(4):
        car = Car(
            car_type=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            price=round(random.uniform(100, 200)),
            mileage=round(random.uniform(25, 100))
        )
        cars.append(car)

        cesar1.add_car(car, random.choice(garages))
        cesar2.add_car(car, random.choice(garages))

    print('GARAGE', garages[0])
    gar_to = garages[0].to_json_string()
    print("\n GARAGE TO JSON STR", gar_to)
    print('\n FROM', garages[0].from_json_string(gar_to))
    print('\n type', type(garages[0]))
    print('\n to json str', garages[0].to_json_string())
    print('\n to json', garages[0].to_json_file('test.json'))
    print('\n from', garages[0].from_json_file('test.json'))
    print("CESAR", "\n", cesar1, "\n")
    print("JSON", "\n")
    print("Convert Cesar object to JSON string", "\n", cesar1.to_json_string(), "\n")
    cesar_string = cesar1.to_json_string()
    print(cesar_string)
    print("Convert JSON Cesar string back", Cesar.from_json_string(cesar_string))
    print("Cesar JSON to file")
    cesar1.to_json_file()
    print("\nCesar JSON from file", type(cesar1.from_json_file()), cesar1.from_json_file(), "\n")
    print("Pickle", "\n")
    print("\nConvert Cesar object to pickle string", "\n", cesar1.to_pickle_string(), "\n")
    cesar_pickel_string = cesar1.to_pickle_string()
    print("Convert from pickle back", "\n", cesar1.from_pickle_string(cesar_pickel_string))
    print("Cesar object to pickle file", "\n")
    cesar1.to_pickle_file()
    print("Back from pickle file", type(cesar1.from_pickle_file()), cesar1.from_pickle_file(), "\n")
    print("YAML", "\n")
    yaml_string = cesar1.to_yaml_string()
    car1 = Car('Ford', 'Sedan', 34, 67)
    car_test = car1.to_yaml_string()
    print("From yaml", cars[1].from_yaml_string(car_test))
    yaml_string = cesar1.to_yaml_string()
    print("Cesar object to yaml string", yaml_string, "\n")
    print("YAML file")
    cesar1.to_yaml_file("yaml.test.yaml")
    print("Cesar from yaml file", cesar1.from_yaml_file('yaml.test.yaml'))
    print("Garage to json string", garage.to_json_string())
    garage_json_string = garage.to_json_string()
    print("Garage from json string", garage.from_json_string(garage_json_string))
    print('Car json to srt', car.to_json_string())
    car_to_str = car.to_json_string()
    print('CAR TO JSON STR', car.from_json_string(car_to_str))
    print("GARaGE to JSON", type(garages[0].to_json_string()), garages[0].to_json_string())
    gar_json = garages[0].to_json_string()
    print('GARAGE FROM', garages[0].from_json_string(gar_json))
    print("Garage to yaml staring", garages[0].to_yaml_string())
    print("Garage to yaml file", garages[0].to_json_file('myfile.yaml'))
    print("Cesar to json string", cesar1.to_json_string())
    s=cesar1.to_json_string()
    print('CESAR TO JSON', s)
    print("Cesar from json", cesar1.from_json_string(s))
