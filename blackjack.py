import random
card = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ten': 10, 'Nine': 9, 'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2, 'One': 1}
bet_amount = int

class Dealer:
    def __init__(self, name):
        self.name = name

    def deal_card(self):
        return random.choice(list(card.keys()))

    def __repr__(self):
        return f'Dealer {self.name} is ready to play.'

class Player_one:
    def __init__(self, name, balance):
        self.name = name
        self.cards = []
        self.balance = balance

    def receive_card(self, card_name):
        self.cards.append(card_name)

    def place_bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            
            return False


    def __repr__(self):
        return f'Player {self.name} with cards: {self.cards}'

# Example usage
d = Dealer('Cyborg Dealer')
print(d)

p = Player_one('You')
p.receive_card(d.deal_card())
print(p)
