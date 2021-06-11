"""This module contains a two classes for creating pokemon."""

from random import randint


def repeat(m):
    """Decorator-function allows decorated function to repeat random number of times, ranging from 0 to m.

    Parameters
    ----------
    m : int
        The value of the maximum random number allowed to be generated.
    """

    def inner(func_object):
        def wrapper(*args, **kwargs):
            rand_num = randint(0, m)
            print(f"Repeat {rand_num} times")
            for i in range(rand_num):
                func_object(*args, **kwargs)
        return wrapper
    return inner


class Pokemon(object):
    """
    This class Pokemon represents a pokemon character with several attributes.

    Attributes
    ----------
    name : str
        Name of pokemon.
    nickname : str
        Nickname of pokemon.
    moves : list
        A list of 4 pokemon moves.
    """

    repeat_max = 10

    def __init__(self, name, nickname):
        """Initialise Pokemon class object with a name and nickname.

        Parameters
        ----------
        name : str
            Name of pokemon.
        nickname : str
            Nickname of pokemon.
        """
        self.name = name
        self.nickname = nickname
        self.moves = ["jump", "strike", "dash", "block"]

    @repeat(repeat_max)
    def speak(self):
        """Print the name of pokemon and repeat number of random times."""
        print(self.name)

    def speak_once(self):
        """Print the name of pokemon once."""
        print(self.name)

    def learn_move(self, new_move):
        """Add a new move to the list of the pokemon moves. The first item in list is removed.

        Parameters
        ----------
        new_move : str
            The name of the new move to be added to the list of moves.
        """
        self.moves.append(new_move)
        self.moves.pop(0)

    def print_details(self):
        """Print all details of pokemon."""
        print(f"NAME: {self.name}")
        print(f"NICKNAME: {self.nickname}")
        print("MOVES:", end=" ")
        for i in self.moves:
            print(i, end=" ")
        print()


class ElectricPokemon(Pokemon):
    """
    This class ElectricPokemon inherits from the base class Pokemon, and represents a specific type pokemon character with several attributes.

    Attributes
    ----------
    name : str
        Name of pokemon.
    nickname : str
        Nickname of pokemon.
    moves : list
        A list of 4 pokemon moves.
    pokemon_type : str
        Type of pokemon.
    """

    def __init__(self, name, nickname, pokemon_type):
        """Initialise ELectricPokemon class object with a name, nickname and type.

        Parameters
        ----------
        name : str
            Name of pokemon.
        nickname : str
            Nickname of pokemon.
        pokemon_type : str
            Type of pokemon.
        """
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
        print(f"SPECIES TYPE: {self.pokemon_type}")

if __name__ == '__main__':
    p = Pokemon("pikachu", "pika")
    p.speak()
    p.speak()
    p.speak()
    p.learn_move("glide")
    p.print_details()

    e = ElectricPokemon("charmander", "char", "fire")
    e.speak()
    e.speak()
    e.speak()
    e.print_details()
