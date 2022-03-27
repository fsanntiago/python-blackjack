import random
import sys
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

    def play(self) -> None:
        while True:
            print("=========================================================")
            print(f"Your money: {convert_money(self.__player.money)}")

            if self.__player.money == 0:  # Check if the player has run out of money
                print("\nYou broke!")
                print("Good thing you weren't playing with real money.")
                print("Thanks for playing!")
                sys.exit()
            if not self.__player.place_bet():
                sys.exit()

            # Give the dealer and player two cards from the deck each:
            deck = Blackjack.get_deck(self)
            self.__player.cards = [deck.pop(), deck.pop()]
            self.__dealer.cards = [deck.pop(), deck.pop()]

            # Handle player actions:
            print(f"\nYour bet: {convert_money(self.__player.bet)}")
            while True:
                Blackjack.display_hands(
                    self, self.__player.cards, self.__dealer.cards, False
                )
                if self.__player.get_hand_value() > 21:
                    print("You bust!")
                    print(f"You lost {convert_money(self.__player.bet)}")
                    self.__player.money -= self.__player.bet
                    break
                elif self.__player.get_hand_value() == 21:
                    print("Blackjack!")
                    print(f"You won {convert_money(self.__player.bet)}")
                    self.__player.money += self.__player.bet
                    break
                else:
                    player_action = self.__player.getMove(
                        self.__player.cards, self.__player.money - self.__player.bet
                    )
                    # Double down
                    if player_action == "D":
                        self.__player.bet *= 2
                        print(f"\nBet increased to {convert_money(self.__player.bet)}")
                        print(f"Your bet: {convert_money(self.__player.bet)}")

            input("\nEnter to continue")
            print("\n")

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
        self, player_hand: List[tuple], dealer_hand: List[tuple], show_dealer_hand: bool
    ):
        """
        Show the player's and dealer's cards. Hide the dealer's first
        card if show_dealer_hand is False.
        """
        if not show_dealer_hand:
            print("\nDEALER: ???")
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

    def display_cards(self, cards: List[tuple]):
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
