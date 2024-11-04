import random

# Create a deck with 4 of each card (standard 52-card deck)
deck = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two'] * 4

# Shuffle the deck
random.shuffle(deck)

card_values = {'Ace': 11, 'King': 10, 'Queen': 10, 'Jack': 10, 'Ten': 10, 'Nine': 9, 'Eight': 8, 'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4, 'Three': 3, 'Two': 2}

class Dealer:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def deal_card(self):
        if deck:  # Check if there are cards left in the deck
            return deck.pop()  # Remove and return the top card
        else:
            print("No more cards in the deck!")
            return None

    def receive_card(self, card_name):
        if card_name:
            self.cards.append(card_name)


    def calculate_hand_value(self):
        total_value = 0
        aces_count = 0

        for card_name in self.cards:
            total_value += card_values[card_name]
            if card_name == 'Ace':
                aces_count += 1

    # Adjust Aces from 11 to 1 if total exceeds 21
        while total_value > 21 and aces_count > 0:
            total_value -= 10  # Change an Ace from 11 to 1
            aces_count -= 1

        return total_value

    def __repr__(self):
        return f'Dealer {self.name} with cards: {self.cards}'


class PlayerOne:
    def __init__(self, name, balance):
        self.name = name
        self.cards = []
        self.balance = balance

    def receive_card(self, card_name):
        self.cards.append(card_name)

    def calculate_hand_value(self):
        total_value = 0
        aces_count = 0

        for card_name in self.cards:
            total_value += card_values[card_name]
            if card_name == 'Ace':
                aces_count += 1

    # Adjust Aces from 11 to 1 if total exceeds 21
        while total_value > 21 and aces_count > 0:
            total_value -= 10  # Change an Ace from 11 to 1
            aces_count -= 1

        return total_value

    def __repr__(self):
        return f'Player {self.name} with cards: {self.cards}'


# Example usage
d = Dealer('Cyborg Dealer')
print(d)

p = PlayerOne('You', 100)
p.receive_card(d.deal_card())
print(p)

while True:
    p.receive_card(d.deal_card())
    print(p)
    if p.calculate_hand_value() >= 21:
        break
    another_card = input("Do you want another card? (yes/no): ").strip().lower()
    if another_card != 'yes':
        break

# Dealer's turn
while d.calculate_hand_value() < 17:
    d.receive_card(d.deal_card())

# Compare hands
player_value = p.calculate_hand_value()
dealer_value = d.calculate_hand_value()

print(f"Player's hand value: {player_value}")
print(f"Dealer's hand value: {dealer_value}")

if player_value > 21:
    print("Player busts! Dealer wins.")
elif dealer_value > 21 or player_value > dealer_value:
    print("Player wins!")
elif player_value < dealer_value:
    print("Dealer wins!")
else:
    print("It's a tie!")
