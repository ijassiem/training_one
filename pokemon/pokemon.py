"""This module contains a two classes for creating pokemon."""


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

    def __init__(self, name, nickname):
        """Initialise Pokemon class."""
        self.name = name
        self.nickname = nickname
        self.moves = ["jump", "strike", "dash", "block"]

    def speak(self):
        """Pokemon say name."""
        print("\n" + self.name.upper() + " " + self.name.upper() + "!")

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


p = Pokemon("pikachu", "pika")
p.speak()
p.print_details()
print("")
p.learn_move("glide")
p.print_details()
print("")
e = ElectricPokemon("slowpoke", "poke", "psychic")
e.speak()
e.print_details()
