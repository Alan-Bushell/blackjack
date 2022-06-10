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
    age = input("Please provide your age:\n")
    print(f"Welcome to Blackjack {name}.")
    print(f"As you are {age} years old you are old enough to play!")


start()


class Card:
    """
    Class for the card instances and their values
    """
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        """
        A way to format and display the card while formatting the deck
        """
        print(f"{self.value} of {self.suit}")


deck = []
suits = ["♠", "♥", "♣", "♦"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for c in cards:
    for s in suits:
        deck.append()

print(deck)

card_template = f"""
.-------.
|{c}.---. |
| : {s} : |
| '---'{c}|
`-------'
"""
