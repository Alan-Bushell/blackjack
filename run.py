import random


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
        if self.value == 10:
            print(f"""
.-------.
|{self.value}.--. |
| : {self.suit} : |
| '--'{self.value}|
`-------'
""")
        else:
            print(f"""
.-------.
|{self.value}.---. |
| : {self.suit} : |
| '---'{self.value}|
`-------'
""")


class Deck:
    """
    Class to create and hold the deck
    """
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        A loop to build and populate each card
        """
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
                  "K"]
        for s in suits:
            for v in values:
                self.cards.append(Card(s, v))

    def show(self):
        """
        A way to display the cards
        """
        for c in self.cards:
            c.show()

    def shuffle(self):
        """
        Method to loop through the cards bearing in mind it is a 0 index,
        and swapping the order of the cards
        """
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        """
        Takes the first card from the deck and removes it to be used
        a the next card in the game
        """
        return self.cards.pop()


class Player:
    """
    Creating the player class to be able to assign cards, score and name
    """

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """
        Draw a card from the deck and add it to the players hand
        """

        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        """
        Method to show the players hand
        """
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()


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
    print(f"Welcome to Blackjack {name}.")
    card = deck.draw_card()
    card.show()


start()
