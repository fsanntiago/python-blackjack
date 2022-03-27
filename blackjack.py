import random
from typing import List

import constants.suits as Suits
from dealer import Dealer
from player import Player


class Blackjack:
    def __init__(self, player: Player = None, dealer: Dealer = None) -> None:
        """Initialize Blackjack"""
        self.__player = player
        self.__dealer = dealer
        self.__player_hand = []
        self.__dealer_hand = []

        Blackjack.create_player(self)
        self.__dealer = Dealer()

    def play(self) -> bool:
        if self.__player.money == 0:  # Check if the player has run out of money
            print("\nYou broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            return False
        print("==============================================")
        self.__player.place_bet()

        # Give the dealer and player two cards from the deck each:
        deck = Blackjack.get_deck(self)
        self.__dealer_hand = [(deck.pop(), deck.pop())]
        self.__player_hand = [(deck.pop(), deck.pop())]

    def create_player(self) -> None:
        """Receives player name and create player"""
        name = input("What's your name? \n").strip()
        if not name:
            name = "Player"
        self.__player = Player(name.title())

    def get_deck(self) -> List[tuple]:
        """Return a list of (rank, suit) tuples for all 52 cards."""
        deck: List[tuple] = []

        for suit in (Suits.HEARTS, Suits.DIAMONDS, Suits.SPADES, Suits.CLUBS):
            for rank in range(2, 11):
                deck.append((str(rank), suit))
            for rank in ("J", "K", "Q", "A"):
                deck.append((rank, suit))
        random.shuffle(deck)
        return deck
