"""This module contains a two classes for creating pokemon."""

from random import randint


def repeat(m):
    """Decorator-function allows decorated function to repeat m times."""

    def inner(func_object):
        def wrapper(*args, **kwargs):
            print("Repeat ", m, " times")
            for i in range(m):
                func_object(*args, **kwargs)

        return wrapper

    return inner


class Pokemon(object):
    """
    This class Pokemon represents a pokemon character with several attributes.

     :param name: Name of pokemon
     :type name: str
     :param nickname: Nickname of pokemon
     :type nickname: str
     :param moves: list of 4 moves
     :type moves: list
    """

    repeat_max = 10

    def __init__(self, name, nickname):
        """Initialise Pokemon class."""
        self.name = name
        self.nickname = nickname
        self.moves = ["jump", "strike", "dash", "block"]

    @repeat(randint(0, repeat_max))
    def speak(self):
        """Pokemon say name and repeat random times."""
        print(self.name)

    def speak_once(self):
        """Pokemon say name once."""
        print(self.name)

    def learn_move(self, new_move):
        """Pokemon learn a new move."""
        self.moves.append(new_move)
        self.moves.pop(0)

    def print_details(self):
        """Print all details of pokemon."""
        print("\nNAME:", self.name)
        print("NICKNAME:", self.nickname)
        print("MOVES:", end=" ")
        for i in self.moves:
            print(i, end=" ")


class ElectricPokemon(Pokemon):
    """
    This class ElectricPokemon inherits from the base class Pokemon, and represents a specific type pokemon character with several attributes.

     :param name: Name of pokemon
     :type name: str
     :param nickname: Nickname of pokemon
     :type nickname: str
     :param moves: list of 4 moves
     :type moves: list
     :param pokemon_type: Type of pokemon
     :type pokemon_type: str
    """

    def __init__(self, name, nickname, pokemon_type):
        """Initialise ElectricPokemon class."""
        self.pokemon_type = pokemon_type
        super(ElectricPokemon, self).__init__(name, nickname)

    def print_details(self):
        """Print all details of pokemon."""
        # print("\nNAME:", self.name)
        # print("NICKNAME:", self.nickname)
        # print("MOVES:", end=" ")
        # for i in self.moves:
        #    print(i, end=" ")
        super(ElectricPokemon, self).print_details()
        print("\nSPECIES TYPE:", self.pokemon_type, "\n")


# p = Pokemon("pikachu", "pika")
# p.speak()
