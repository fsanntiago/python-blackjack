from abc import ABC


class BasePlayer(ABC):
    """Represent a model player(human player and "computer player"(dealer))"""

    def __init__(self) -> None:
        self.cards = []
