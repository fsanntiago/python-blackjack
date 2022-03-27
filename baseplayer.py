class BasePlayer(object):
    """Represent a model player(human player and "computer player"(dealer))"""

    __cards = []

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        self.__cards = value

    def get_hand_value(self) -> int:
        """
        Returns the value of the cards. Face cards are worth 10, aces are
        worth 11 or 1 (this function picks the most suitable ace value).
        """
        value = 0
        number_of_aces = 0

        # Add the value for the non-ace cards:
        for card in self.cards:
            rank = card[0]  # card is a tuple like (rank, suit)
            if rank == "A":
                number_of_aces += 1
            elif rank in ("J", "K", "Q"):
                value += 10
            else:
                value += int(rank)

        # Add the value for the aces:
        value += number_of_aces  # Add 1 per ace.
        if number_of_aces:
            for i in range(number_of_aces):
                if value + 10 <= 21:
                    value += 10

        return value
