"""
Python Blackjack command line game for porfolio 3 project
"""


def start():
    """
    Initial function to test connection to heroku
    """
    print("\n                              Welcome to:")
    banner = """
    .------..------..------..------..------..------..------..------..------.
    |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
    | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
    | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
    | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
"""
    print(banner)
    print("By Alan Bushell - Portfolio 3\n")
    print("Good luck and try not to lose to much!\n")
    name = input("To start, please enter your name:\n")
    print(f"Welcome {name}. Get ready to be dealt your cards!")


start()


class Deck():
    """
    A class for deck to create the cards, values, suits and to assign them
    """

    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value

    deck = []
    suit = ["Clubs", "Spades", "Diamonds", "Hearts"]
    value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
