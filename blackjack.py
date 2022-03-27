from player import Player


class Blackjack:
    def __init__(self, player: Player = None) -> None:
        """Initialize Blackjack"""
        self.__player = player

        Blackjack.create_player(self)

        while Blackjack.play(self):
            pass

    def play(self):
        if self.__player.money == 0:  # Check if the player has run out of money
            print("\nYou broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            return False
        print("==============================================")
        # Place bet

    def create_player(self) -> None:
        """Receives player name and create player"""
        name = input("What's your name? \n").strip()
        if not name:
            name = "Player"
        self.__player = Player(name.title())
