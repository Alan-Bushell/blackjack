import random  # import random to shuffle deck of cards
import os

# Move card values into global scope

suits = ["♠", "♥", "♣", "♦"]  # Took characters from computer keyboard
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
         "K", "A"]
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
          "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


def clear():
    """
    Create function to clear terminal at specific points to give the
    game a clean and clear view.
    """
    os.system('cls||clear')


BANNER = """
                                    Welcome to:
    .------..------..------..------..------..------..------..------..------.
    |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
    | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
    | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
    | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
    `------'`------'`------'`------'`------'`------'`------'`------'`------'
"""

ENDBANNER = """
    .------..------..------..------..------.     .------..------..------.
    |T.--. ||H.--. ||A.--. ||N.--. ||K.--. |     |Y.--. ||O.--. ||U.--. |
    | :/\: || :/\: || (\/) || :(): || :/\: |     | (\/) || :/\: || (\/) |
    | (__) || (__) || :\/: || ()() || :\/: |     | :\/: || :\/: || :\/: |
    | '--'T|| '--'H|| '--'A|| '--'N|| '--'K|     | '--'Y|| '--'O|| '--'U|
    `------'`------'`------'`------'`------'     `------'`------'`------'"""

WINBANNER = """

 |.--------_--_------------_--__--.|
 ||    /\ |_)|_)|   /\ | |(_ |_   ||
 ;;`,_/``\|__|__|__/``\|_| _)|__ ,:|
((_(-,-----------.-.----------.-.)`)
 \__ )        ,'     `.        \ _/
 :  :        |_________|       :  :
 |-'|       ,'-.-.--.-.`.      |`-|
 |_.|      (( (*  )(*  )))     |._|
 |  |       `.-`-'--`-'.'      |  |
 |-'|        | ,-.-.-. |       |._|
 |  |        |(|-|-|-|)|       |  |
 :,':        |_`-'-'-'_|       ;`.;
  \  \     ,'           `.    /._/
   \/ `._ /_______________\_,'  /
    \  / :   ___________   : \,'
     `.| |  |           |  |,'
       `.|  |           |  |
         |  |           |  |"""

print(BANNER)

# Input for users name and to store it
name = str(input("To start, please enter your name:\n"))
print(f"Welcome to the game {name}.")

# Input option for rules or to start game
print("\nPlease select one of following options:")
main_choice = int(input("\n1.Start Game\n2.Read Rules\nChoice:"))

# Test input to ensure it is valid

if main_choice == 1:
    PLAYING = True
    clear()

elif main_choice == 2:
    print("""
    Rules of BlackJack \n
    1. The player and dealer are both dealt two cards \n
    2. The player will get both cards face up and the dealer
    will have one card hidden. \n
    3. The goal of the game is to get as close to 21 without going over \n
    4. You will be given the option to Hit or Stand during your turn \n
    5. Once you are satisfied with your score and stand then its the 
    dealers turn. \n
    6. The dealer must hit and draw a card on 16 but stand on 17\n
    7. If the dealer goes over 21 he loses and you win.\n
    8. If both yourself and the dealer do not exceed 21 then\n
    the closest to 21 wins\n
    9. Good luck
    """)

else:
    print("I am sorry that input is invalid. Please try again.")
    main_choice = int(input("\n1.Start Game\n2.Read Rules\nChoice:"))

rules_choice = input("When you are ready to play press any key to start!")

if rules_choice.lower() == "y":
    PLAYING = True
else:
    print("I am sorry but that option is not recognized. Try Again")
    PLAYING = True
clear()

HIDDEN_CARD = """
    .-------.
    |?.---. |
    | : ? : |
    | '---'?|
    `-------'
            """


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
        if card.rank == "A":
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
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """
    Function to start the loop of asking the payer to hit or stand
    """
    global PLAYING  # Access global scope

    while True:
        game_loop = input("Press H for hit or S for stand: 'H'/ 'S'")

        if game_loop.lower() == "h":
            hit(deck, hand)

        elif game_loop.lower() == "s":
            print("You have chosen Stand. Now its the dealers turn:")
            PLAYING = False

        else:
            print("Invalid entry. Please try again")
            continue
        break


def first_round(player, dealer):
    """
    First round displays both user cards and only one of the
    dealers card
    """
    print("\nDealers Hand:")
    print(HIDDEN_CARD, '', dealer.cards[1])
    print("\nPlayers Hand:", *player.cards, sep="\n")
    print("\nPlayers Score = ", player.value)
    print("\n")


def display_all_cards(player, dealer):
    """
    Final round once player has decided to stand or hit then
    the remaining dealer card is shown and scores can then
    be calculated
    """
    print("\nDealers Hand:", *dealer.cards, sep="\n")
    print("Dealer's Score =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n")
    print("\nPlayers Score = ", player.value)


def player_wins(player, dealer):
    """
    If the player wins then notify player and insert name into message
    """
    print(f"{name} wins!!")
    print(WINBANNER)


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


def dealer_busts(player, dealer):
    """
    If the dealer busts then notify player and insert name into message
    """
    print(f"{name} wins!! The dealer has bust")
    print(WINBANNER)


def push(player, dealer):
    """
    If after the game has reached its conclusion and scores are tied.
    """
    print(f"A tie! {name} & the dealer have the same score.")


# Starting the game

while True:

    deck = Deck()  # set deck = to Deck() function
    deck.shuffle()  # Shuffle deck

    player_hand = Hand()
    player_hand.add_card(deck.deal())  # Assign the player the first card
    player_hand.add_card(deck.deal())  # Assign the player the second card

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())  # Assign the dealer the first card
    dealer_hand.add_card(deck.deal())  # Assign the dealer the second card

    first_round(player_hand, dealer_hand)  # only show 1 dealer card

    # First round of player interaction
    while PLAYING:
        hit_or_stand(deck, player_hand)

        first_round(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show hidden dealer card
        clear()
        display_all_cards(player_hand, dealer_hand)

        # Check winner
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand)

        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)

    new_game = input("Would you like to play again? Y(es) or N(o)")

    if new_game.lower() == 'y':
        clear()
        PLAYING = True
        continue
    else:
        clear()
        print(ENDBANNER)
    break
