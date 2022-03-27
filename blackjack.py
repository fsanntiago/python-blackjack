import random
from typing import List

import constants.suits as Suits
from dealer import Dealer
from player import Player
from utils.convert_money import convert_money


class Blackjack:
    """Reprensent Blackjack"""

    BACKSIDE = "backside"

    def __init__(self, player: Player = None, dealer: Dealer = None) -> None:
        """Initialize Blackjack"""
        self.__player = player
        self.__dealer = dealer
        # self.__player_hand = []
        # self.__dealer_hand = []

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
        self.__player.cards = [deck.pop(), deck.pop()]
        self.__dealer.cards = [deck.pop(), deck.pop()]

        # Handle player actions:
        print(f"\nYour bet: {convert_money(self.__player.bet)}")

    def create_player(self) -> None:
        """Receives player name and create player"""
        name = input("What's your name? \n").strip()
        if not name:
            name = "Player"
        self.__player = Player(name.capitalize())

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

    def display_hands(
        self, player_hand: list[tuple], dealer_hand: list[tuple], show_dealer_hand: bool
    ):
        """
        Show the player's and dealer's cards. Hide the dealer's first
        card if show_dealer_hand is False.
        """
        if not show_dealer_hand:
            print("DEALER: ???")
            # Hide the dealer's first card
            Blackjack.display_cards(self, [Blackjack.BACKSIDE] + dealer_hand[1:])
        else:
            dealer_hand_value = self.__dealer.get_hand_value()
            print(f"DEALER: {dealer_hand_value}")
            Blackjack.display_cards(self, dealer_hand)

        # Show the player's cards:
        player_hand_value = self.__player.get_hand_value()
        print(f"{self.__player.name.upper()}: {player_hand_value}")
        Blackjack.display_cards(self, player_hand)

    def display_cards(self, cards: list[tuple]):
        """Display all the cards in the cards list."""
        rows = ["", "", "", "", ""]  # The text to display on each row.

        for i, card in enumerate(cards):
            rows[0] += " ___ "
            if card == Blackjack.BACKSIDE:
                # Print a card's back:
                rows[1] += "|#  |"
                rows[2] += "| # |"
                rows[3] += "|__#|"
            else:
                rank, suit = card
                # Print a card's front:
                if len(rank) < 2:
                    rows[1] += f"|{rank}  |"
                    rows[2] += f"| {suit} |"
                    rows[3] += f"|__{rank}|"
                else:
                    rows[1] += f"|{rank} |"
                    rows[2] += f"| {suit} |"
                    rows[3] += f"|_{rank}|"

        # Print each row on the screen
        for row in rows:
            print(row)
