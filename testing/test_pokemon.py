"""Test module."""

import pokemon.pokemon as p
import unittest
import pytest

"""
This module contains a class for testing the pokemon module.

There are several test methods for testing the pokemon module.
"""


class TestPokemon(unittest.TestCase):
    """This is a class for testing the pokemon module."""

    def test_object_instantiation(self):
        """Test object is instance of class."""
        my_pokemon = p.Pokemon("pikachu", "pika")
        self.assertIsInstance(my_pokemon, p.Pokemon)

    def test_inheritance(self):
        """Test object is instance of base class."""
        my_pokemon = p.ElectricPokemon("slowpoke", "poke", "psychic")
        self.assertIsInstance(my_pokemon, p.ElectricPokemon)

    def test_learn_move(self):
        """Test a new move is learnt."""
        my_pokemon = p.Pokemon("charmander", "char")
        my_pokemon.learn_move("slice")
        assert my_pokemon.moves[3] == "slice"

    def test_name(self):
        """Test name."""
        my_pokemon = p.Pokemon("charmander", "char")
        assert my_pokemon.name == "charmander"

    def test_nickname(self):
        """Test nickname."""
        my_pokemon = p.Pokemon("charmander", "char")
        assert my_pokemon.nickname == "char"

    def test_no_moves(self):
        """Test the number of moves are 4."""
        my_pokemon = p.Pokemon("charmander", "char")
        assert len(my_pokemon.moves) == 4

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        """Output capture with pytest."""
        self.capsys = capsys

    def test_speak_once(self):
        """Test speak method output with pytest capture."""
        name = "charmander"
        my_pokemon = p.Pokemon(name, "char")
        my_pokemon.speak_once()
        captured = self.capsys.readouterr()
        self.assertEqual(name + "\n", captured.out)

    def test_species(self):
        """Test species type."""
        species = "psychic"
        my_pokemon = p.ElectricPokemon("slowpoke", "poke", species)
        assert my_pokemon.pokemon_type == species

    def test_no_of_repeats(self):
        """Checks the number of repeats of speak method does not exceed the maximum repeats."""
        name = "pikachu"
        my_pokemon = p.Pokemon(name, "pika")
        max_value = p.Pokemon.repeat_max
        my_pokemon.speak()
        captured = self.capsys.readouterr()
        num_speak = captured.out.count("pikachu")
        # print("Captured out: ", captured.out.count("pikachu"))
        # print("max_value ", max_value)
        # print("num_speak ", num_speak)
        assert num_speak <= max_value
