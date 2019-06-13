import os
import unittest
import uuid
from os.path import isfile

from homework5 import Car, Garage, Cesar


class TestHomework(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.car = Car.from_json_file('fixtures/cars_file.json')
        self.register_id = uuid.uuid4()
        self.owner = uuid.uuid4()
        self.garage = Garage(5, 'Berlin', self.owner, [self.car])
        self.register_id = uuid.uuid4()
        self.cesar = Cesar('Rich', [self.garage])

    def test_other_car_expensive(self):
        other_car = Car('Toyota', 'Disel', 200, 13)
        self.assertLess(self.car, other_car, 'Other car is greater than the car')

    def test_our_car_expensive(self):
        other_car = Car('Toyota', 'Disel', 112, 13)
        self.assertGreater(self.car, other_car, 'Our car price is bigger than the other car price')

    def test_change_car_number_positive_flow(self):
        old_number = self.car.number
        new_number = self.car.change_number()
        self.assertNotEqual(old_number, new_number)

    def test_change_car_number_negative(self):
        old_number = self.car.number
        new_number = self.car.number
        self.assertEquals(old_number, new_number, 'Test failed as actual result does not meet requirements')

    def test_add_car_to_garage_positive(self):
        owner_id = uuid.uuid4()
        other_car = Car('Toyota', 'Disel', 112, 13)
        other_garage = Garage(4, 'Rome', owner_id, [other_car])
        other_garage.add_c(self.car)
        self.assertEquals(other_garage.free_places(), 2)

    def test_remove_car_from_garage_positive(self):
        owner_id = uuid.uuid4()
        other_garage = Garage(3, 'Rome', owner_id, [self.car])

        other_garage.remove_c(self.car)
        self.assertEqual(len(other_garage.cars), 0)

    def test_remove_car_from_garage_negative(self):
        owner_id = uuid.uuid4()
        other_garage = Garage(3, 'Rome', owner_id, [self.car])
        car_not_in_garage = Car('Ford', 'Diesel', 250, 86)
        self.assertEqual(other_garage.remove_c(car_not_in_garage), 'car is not in the garage')

    def test_hit_hat_in_garage(self):
        self.assertEqual(self.garage.hit_hat(), 150)

    def test_cesar_hit_hat(self):
        self.assertEqual(self.cesar.hit_hat(), 150)

    def test_cesar_garages_count_positive(self):
        self.assertEqual(self.cesar.garages_count(), 1)


class TestToJson(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.car = Car.from_json_file('fixtures/cars_file.json')

    def test_to_json_file(self):
        car = Car('Porsche', 'Diesel', 240, 112)
        car.to_json_file('test_cars_file.json')
        self.assertTrue(isfile('test_cars_file.json'))
        os.remove('test_cars_file.json')

    def test_from_json_file(self):
        car_data = self.car
        expected_result = self.car.from_json_file('fixtures/cars_file.json')
        self.assertEqual(car_data, expected_result)


if __name__ == '__main__':
    unittest.main()



