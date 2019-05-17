import math


class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()

    * Add to class saturation_level variable with value 50

    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100

    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2

    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run more or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers"

    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is died :("

    * Implement get_average_speed and return average_speed

    """

    average_speed = 0
    _saturation_level = 50

    def __init__(self, age):
        self.age = age
        # we need to set average speed based on a definite  age of object
        self._set_average_speed()

    def eat(self, product: str):
        if product == 'fodder':
            self._increase_saturation_level(10)
        elif product == 'apple':
            self._increase_saturation_level(5)
        elif product == 'milk':
            self._increase_saturation_level(2)
        else:
            'Such product does not bring you nay value'

    def _reduce_saturation_level(self, value: int):
        self._saturation_level -= value
        if self._saturation_level < 0:
            self._saturation_level = 0

    def _increase_saturation_level(self, value: int):
        self._saturation_level += value
        if self._saturation_level > 100:
            self._saturation_level = 100


    def _set_average_speed(self):
        if self.age <= 7:
             self.average_speed = 12

        elif 7 < self.age <= 10:
            self.average_speed = 9

        elif self.age > 10:
            self.average_speed = 6

    def run(self, hours: int):
        distance = round(self.average_speed*hours)
        if distance <= 25:
            self._reduce_saturation_level(2)
            return f'cat run  {distance}'
        elif 25 < distance <= 50:
            self._reduce_saturation_level(5)
        elif 50 < distance <= 100:
            self._reduce_saturation_level(15)
            return f'cat run  {distance}'
        elif 100 < distance <= 200:
            self._reduce_saturation_level(25)
            return f'cat run  {distance}'
        else:
            self._reduce_saturation_level(50)
            return f'cat run  {distance}'

    def get_saturation_level(self):
        if self._saturation_level <= 0:
            return 'Your cat is died :('
        else:
            return self._saturation_level

    def get_average_speed(self):
        return self.average_speed

class Cheetah(Cat):
    """
    * Inherit from class Cat

    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15

    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 90
      if age grosser 15(not including) return 40

    """
    def eat(self, product: str):
        if product == 'gazelle':
            self._increase_saturation_level(30)
        elif product == 'rabbit':
            self._increase_saturation_level(15)
        else:
            "The product will not increase your saturation level, please watch one's calories"

    def _set_average_speed(self):
        if self.age <= 5:
            self.average_speed = 90
            return self.average_speed
        elif 5 < self.age <= 15:
            self.average_speed = 75
            return self.average_speed
        else:
            self.average_speed = 40
            return self.average_speed


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide  count of lines in roll
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def wall_square(self):
        square = self.width*self.height
        return int(square)

    def number_of_rolls_of_wallpaper(self, roll_width_m: float, roll_length_m: float):
        count_of_lines_in_roll = math.floor(roll_length_m/self.height)
        count_of_lines = math.floor(self.width/roll_width_m)
        general_amount = count_of_lines/count_of_lines_in_roll
        return general_amount


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"

    """

    def __init__(self, roof_width: float, roof_height: float, roof_type: str):
        self.roof_width = roof_width
        self.roof_height = roof_height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == 'gable':
            r_square = self.roof_width*self.roof_height*2
            return round(r_square)
        elif self.roof_type == "single-pitch":
            r_square = self.roof_width * self.roof_height
            return round(r_square)
        else:
            'No roof type defined'
            try:
                raise ValueError
            except ValueError:
                return "Sorry there is only two types of roofs"


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle

    """

    def __init__(self, window_width: float, window_height: float):
        self.window_width = window_width
        self.window_height = window_height

    def window_square(self):
        rectangle_square = self.window_width*self.window_height
        return rectangle_square


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_square which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price

    """
    wood_price = 10
    metal_price = 3

    def __init__(self, door_width: float, door_height: float):
        self.door_width = door_width
        self.door_height = door_height

    def door_square(self):
        d_square = self.door_width * self.door_height
        return d_square

    def door_price(self, material: str):
        if material == 'wood':
            return self.door_square()*self.wood_price
        elif material == 'metal':
            return self.door_square()*self.metal_price

        else:
            return "Sorry we don't have such material"

    def update_wood_price(self, new_wood_price: int):
        self.wood_price = new_wood_price
        return self.wood_price

    def update_metal_price(self, new_metal_price: int):
        self.metal_price = new_metal_price
        return self.metal_price


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """
    __walls = []
    __windows = []
    __roof = None
    __door = None

    def __init__(self):
        pass
        # self.__walls = []
        # self.__windows = []
        # self.__roof = None
        # self.__door = None

    def create_wall(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Value must be not 0")
        elif self.get_count_of_walls() >= 4:
            raise ValueError("Our house can not have more than 4 walls")
        else:
            self.__walls.append(Wall(width, height))

    def create_roof(self, roof_width, roof_height, roof_type: str):
        if roof_width <= 0 or roof_height <= 0:
            raise ValueError("Value must be not 0")
        elif self.__roof is not None:
            raise ValueError("The house can not have two roofs")
        else:
            self.__roof = Roof(roof_width, roof_height, roof_type)

    def create_window(self, window_width: float, window_height: float):
        if window_width <= 0 or window_height <= 0:
            raise ValueError("Value must be not 0")
        else:
            self.__windows.append(Window(window_width, window_height))

    def create_door(self,  door_width: float, door_height: float):
        if door_width <= 0 or door_height <= 0:
            raise ValueError("Value must be not 0")
        elif self.__door is not None:
            raise ValueError("The house can not have two doors")
        else:
            self.__door = (Door(door_width, door_height))

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material: str):
        return self.__door.door_price(material)

    def update_wood_price(self, new_wood_price: int):
         return self.__door.update_wood_price(new_wood_price)


    def update_metal_price(self, new_metal_price: int):
        return self.__door.update_metal_price(new_metal_price)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        wall_sum_square = 0
        for wall in self.__walls:
            wall_sum_square += wall.wall_square()
        return wall_sum_square

    def get_windows_square(self):
        return sum([window.window_square() for window in self.__windows])

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m: float, roll_length_m: float):
        if roll_width_m <=0 or roll_length_m <=0:
            raise ValueError("Sizes should be more than 0")
        return sum(wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for wall in self.__walls)

    def get_room_square(self):
        room_square = self.get_walls_square() - self.get_door_square() - self.get_windows_square()
        return room_square


# wall = Wall(5, 2.7)
# wall1 = Wall(5, 2.7)
# wall2 = Wall
# print('wall', wall.wall_square())
# print(wall.number_of_rolls_of_wallpaper(1, 10))
#
# roof = Roof(4, 2, 'single-pitch')
# print(roof.roof_square())
# window = Window(12, 35)
#
# door = Door(2, 4)
# print('square', door.door_square())
# print('new price', door.update_metal_price(56))
#
# house = House()
# print('Creare wall', house.create_wall(5, 3))
# print('create 2 wall', house.create_wall(5, 3))
# print('create roof', house.create_roof(23, 45, 'gable'))
#
# print('window', house.create_window(23, 45))
# print('Get count of walls', house.get_count_of_walls())
# print('door', house.create_door(12, 2))
#
# print('count of walls', house.get_count_of_walls())
# print('door price', house.get_door_price('metal'))
# print('update wood price', house.update_wood_price(12))
# print('roof square', house.get_roof_square())
# print('walls square', house.get_walls_square())
# print('get_number_of_rolls_of_wallpapers', house.get_number_of_rolls_of_wallpapers(0.7, 10))
#print('door square', house.get_door_square())
# print(house.get_count_of_walls())