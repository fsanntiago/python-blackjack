from player import Player


class Blackjack:
    def __init__(self, player: Player = None) -> None:
        """Initialize Blackjack"""
        self.__player = player
        Blackjack.play(self)

    def play(self):
        print("Blackjack".center(57))
        print("=========================================================")
        print(
            """\
        Rules:
        •Try to get as close to 21 without going over.
        •Kings, Queens, and Jacks are worth 10 points.
        •Aces are worth 1 or 11 points.
        •Cards 2 through 10 are worth their face value.
        •(H)it to take another card.
        •(S)tand to stop taking card.
        •On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        •In case of a tie, the bet is returned to the player.
        •The dealer stops hitting at 17."""
        )
        print("=========================================================")

        Blackjack.create_player(self)

    def create_player(self) -> None:
        """Receives player name and create player"""
        name = input("What's your name? \n").strip()
        if not name:
            name = "Player"
        self.__player = Player(name.title())
