# Exercise 2: Create a deck of cards class
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit} "


class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
                       'K']
        self.cards = []
        self.reset_deck()

    def reset_deck(self):
        """Helper to fill the deck with a standard set of 52 cards."""
        for s in self.suits:
            for v in self.values:
                self.cards.append(Card(s, v))

    def shuffle(self):
        """Ensures the deck is full and rearranges cards randomly."""
        if len(self.cards) < 52:
            print("Refilling deck before shuffling...")
            self.reset_deck()
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def deal(self):
        """Removes and returns a single card from the deck."""
        if len(self.cards) == 0:
            return "No cards left in the deck!"
        return self.cards.pop()


my_deck = Deck()
my_deck.shuffle()

dealt_card = my_deck.deal()
print(f"Dealt: {dealt_card}")
print(f"Cards remaining: {len(my_deck.cards)}")
my_deck.shuffle()