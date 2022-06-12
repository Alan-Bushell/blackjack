import random  # import random to shuffle deck of cards


# Move card values into global scope

suits = ["♠", "♥", "♣", "♦"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
         "K", "A"]
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

name = input("To start, please enter your name:\n")

playing = True


class Card:
    """
    Class for the card instances and their values
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        """
        A way to format and display the card while formatting the deck
        """
    def __str__(self):  # Using ascii to add card shape to terminal
        return f"""
.-------.
|{self.rank}.---. |
| : {self.suit} : |
| '---'{self.rank}|
`-------'
"""


class Deck:
    """
    Class to create and hold the deck
    """
    def __init__(self):
        self.deck = []
        # Build the cards using a for loop and push to deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """
        Method to shuffle cards in deck
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Takes the first card from the deck and removes it to be used
        as the next card in the game
        """
        single_card = self.deck.pop()
        return single_card


class Hand:
    """
    Creating the hand class to be able to assign cards, check score and 
    hold information
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
        self.value += values[card.rank]
        if card.values == "A":
            self.aces += 1

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
    global playing  # Access global scope

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


def first_round(player, dealer):
    """
    First round displays both user cards and only one of the
    dealers card
    """
    print("Dealers Hand:")
    print("Insert blank card ascii here")
    print('', dealer.cards[1])
    print("\nPlayers Hand = ", player.values)


def display_all_cards(player, dealer):
    """
    Final round once playerhas decided to stand or hit then
    the remaining dealer card is shown and scores can then
    be calculated
    """
    print("Dealers Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =", dealer.value)
    print("Player's Hand:", *player.cards, sep="\n")
    print("\nPlayers Hand = ", player.values)


def player_wins(player, dealer):
    """
    If the player wins then notify player and insert name into message
    """
    print(f"{name} wins!!")


def dealer_wins(player, dealer):
    """
    If the dealer wins then notify player and insert name into message
    """
    print(f"{name} loses!! The dealer has won this one")


def player_bust(player, dealer):
    """
    If the player busts then notify player and insert name into message
    """
    print(f"{name} has busted.")



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
    
    print(f"Welcome to Blackjack {name}.")


start()
