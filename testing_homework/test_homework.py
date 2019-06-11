import unittest
import uuid
from hw5 import Car, Garage, Cesar


class TestHomework(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.car = Car('BMW', 'Diesel', 150, 86)
        self.register_id = uuid.uuid4()
        self.garage = Garage(self.car, 5, 'Berlin')
        self.register_id = uuid.uuid4()
        self.cesar = Cesar('Rich', self.garage)

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
        self.assertNotEquals(old_number, new_number, 'Test failed as actual result does not meet requirements')

    def test_add_car_to_garage_positive(self):
        other_garage = Garage(['BMW', 'Diesel', 150, 86], 3, 'Rome')
        other_garage.add_c(self.car)
        actual_result = other_garage.town
        expected_result = other_garage.town
        self.assertEquals(actual_result, expected_result)

    def test_add_car_to_garage_negative(self):
        other_garage = Garage(['BMW', 'Diesel', 150, 86], 2, 'Rome')
        other_garage.add_c(self.car)
        actual_result = other_garage.town
        expected_result = 'Las Vegas'
        self.assertEquals(actual_result, expected_result, 'Test failed as actual result does not meet requirements')

    def test_remove_car_from_garage_positive(self):
        other_garage = Garage(self.car, 3, 'Rome')

        other_garage.remove_c(self.car)
        self.assertEqual(len(other_garage.cars), 1)

    def test_remove_car_from_garage_negative(self):
        other_garage = Garage(self.car, 3, 'Rome')
        car_not_in_garage = Car('Ford', 'Diesel', 250, 86)
        other_garage.remove_c(car_not_in_garage)
        self.assertIn(car_not_in_garage, other_garage.cars, 'This car is not in the garage')

    def test_hit_hin_in_garage(self):
        self.garage.hit_hat()
        self.assertEqual(self.garage.hit_hat(), 300)


if __name__ == '__main__':
    unittest.main()



