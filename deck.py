from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in range(4) for value in range(1, 14)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
