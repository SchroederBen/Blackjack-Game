from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value > 10:
                value += 10
            elif card.value == 1:
                aces += 1
                value += 11
            else:
                value += card.value
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __repr__(self):
        return ", ".join(map(str, self.cards))
