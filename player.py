from baseplayer import BasePlayer
from utils.convert_money import convert_money


class Player(BasePlayer):
    """Respresent a human player"""

    def __init__(self, name) -> None:
        """Initialize a player"""
        super().__init__()
        self.__name = name
        self.__money = 5_000.00
        self.__bet = 0
        Player.greet_player(self)

    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, value):
        self.__bet = value

    def greet_player(self):
        print(f"\nWelcome {self.__name}, join the fun!")

    def place_bet(self) -> bool:
        """
        Allows to player place your bet.
        Return False if player wants to quit or an error occurs.
        """
        convert_player_money = convert_money(self.__money)

        prompt_bet = f"\nPlace your bet {self.__name}"
        prompt_bet += f" ($1.00-{convert_player_money} or QUIT)\n$"
        player_bet = input(prompt_bet).strip()

        if player_bet.lower() != "quit":
            player_bet = float(player_bet)
            while player_bet == 0 or player_bet > self.__money:
                convert_bet = convert_money(player_bet)
                if player_bet == 0:
                    print("\nPlease bet some amount.")
                    print(f"Please bet again ($1.00-{convert_player_money}):")
                    player_bet = float(input("$"))
                elif player_bet > self.__money:
                    print(f"\nYou don't have this amount {convert_bet}")
                    print(f"You have {convert_player_money}")
                    print("Please bet again:")
                    player_bet = float(input("$"))
            self.__bet = player_bet
            return True
        # If player 'quit'
        return False

    def getMove(self, player_hand, money):
        """
        Asks the player for their move, and returns 'H' for hit, 'S' for
        stand, and 'D' for double down.
        """
        while True:  # Keep looping until the player enters a correct move.
            # Determine what moves the player can make
            moves = ["(H)it", "(S)tand"]

            # Get the player's move:
            if len(player_hand) == 2 and money > 0:
                moves.append("(D)ouble down")
            move_prompt = ", ".join(moves) + " > "
            move = input(move_prompt).strip().upper()
            if move in ("H", "S"):
                return move
            if move == "D":
                return move
