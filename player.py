from baseplayer import BasePlayer
from utils.convert_money import convert_money


class Player(BasePlayer):
    """Respresent a human player"""

    def __init__(self, name) -> None:
        """Initialize a player"""
        super().__init__()
        self.__name = name
        self.__money = 5_000.00
        Player.greet_player(self)

    def greet_player(self):
        print(f"\nWelcome {self.__name}, join the fun!")
        print(f"Your money: {convert_money(self.__money)}")
