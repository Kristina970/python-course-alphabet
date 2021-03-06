from __future__ import annotations
import pickle


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Position: {self.position} developer"

<<<<<<< HEAD
    def __setstate__(self, state):      # deserialize object
        self.__dict__ = state

    def __getstate__(self):         # serialize object
        return self.__dict__
=======
    # def __setstate__(self, state):
    #     self.__dict__ = state
    #
    # def __getstate__(self):
    #     return self.__dict__
>>>>>>> f07bec3747a40695b27082ca48aae333e38da811


if __name__ == "__main__":
    programmer = Programmer("Captain America")
    programmer.enough_coffee = True
    # Lets dump object to pickle
    with open("data.txt", "wb") as file:
        pickle.dump(programmer, file)

    # Lets load it
    with open("data.txt", "rb") as file:
        restore_obj = pickle.load(file)
        print(restore_obj)
