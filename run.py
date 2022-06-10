import random  # import random to shuffle deck of cards


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
    def __str__(self):
        if self.value == 10:  # Using ascii to add card shape to terminal
            return f"""
.-------.
|{self.value}.---. |
| : {self.suit} : |
| '---'{self.value}|
`-------'
"""


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
        value = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                      "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
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
        Method to loop through the cards
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Takes the first card from the deck and removes it to be used
        a the next card in the game
        """
        single_card = self.cards.pop()
        return single_card


class Hand:
    """
    Creating the hand class to be able to assign cards, check score and hold 
    information
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # Tracking aces as they can be 11 or 1

    def add_card(self, card):
        """
        Draw a card from the deck and add it to the players hand
        """
        self.cards.append(card)
        self.value += value[card.values]
        if card.values == "A":
            self.aces += 1

    def show_hand(self):
        """
        Method to show the players hand
        """
        for card in self.hand:
            card.show()

    def adjust_for_ace(self):
        """
        Update value based on number of aces as 2 aces would mean 22 and bust
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    """
    Function to add a single card to the users hand, call the check_for_aces
    function and adjust score accordingly
    """
    hand.add_card(deck.deak())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """
    Function to start the loop of asking the payer to hit or stand
    """

    while True:
        game_loop = input("Press H for hit or S for stand: 'H'/ 'S'")

        if game_loop.lower() == "h":
            hit(deck, hand)

        elif game_loop.lower() == "s":
            print("You have chosen Stand. Now its the dealers turn:")

        else:
            print("Invalid entry. Please try again")
            continue
        break


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
