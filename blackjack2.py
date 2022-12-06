import random 
import pandas as pd

#make deck 
deck = []

for suit in ["\u2663", "\u2660", "\u2665", "\u2666"]:
    for rank in [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
        deck.append(rank+suit)

#create dictionary to assign card values

value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11 }

#Test the dictionary 

# print(value[random.choice(deck)[0]] + value[random.choice(deck)[0]])

#Create Player and Dealer hands

player = []

dealer = [] 

# Create a function to deal out cards from the deck 

def deal (deck):
    y = 0
    while y < 2:
        x = random.choice(deck)
        player.append(x)
        deck.remove(x)
        z = random.choice(deck)
        dealer.append(z)
        deck.remove(z)
        y += 1
    return player, dealer

#Test the Function

# deal(deck)

# print(player)
# print(dealer)

#Create a function to add up score

def hand_value (hand):
    amount = 0 
    value_deck = []
    for card in hand: 
        x = card[:-1]
        y = value[x]
        value_deck.append(y)
    value_deck.sort(reverse = True)
    for number in value_deck: 
        amount += number
        if amount > 21 and number == 11:
          amount += number + 1
    return amount
#Test the function 

# print(hand_value(player))
# print(hand_value(dealer))


#Create a function to hit
def hit (hand): 
    x = random.choice(deck)
    hand.append(x)
    deck.remove(x)
    return x
#Test hit function 

# print(hit(player))
# print(player)
# print(hand_value(player))

# Create dictionary for chip values

chip_value = {"White": 1, "Pink": 2.5, "Red": 5, "Blue": 10, "Green": 25, "Black": 100}
chip_amount = {"White": 50, "Pink": 20, "Red": 10, "Blue": 5, "Green": 2, "Black": 1, "null": 0}

bank = {"Chip": ['White', 'Pink', 'Red', 'Blue', 'Green', 'Black'],
        'Value':[1, 2.5, 5, 10, 25, 100],
        'Amount':[50, 20, 10, 5, 2, 1]}
pd.DataFrame(bank)
print(bank)
#Create Function to bet


def bet (chip): 
    quantity = 1
    chip = input("What would you like to bet?\n(White, Pink, Red, Blue, Green, Black): ")
    if chip_amount[chip] > 1: 
        quantity = int(input("How many? "))
    return chip, quantity
    
# test bet function 

# bet(chip)
# print(chip_amount)

# Create a function to find total cash
def cash_value (): 
     white = chip_amount["White"] * chip_value["White"]
     pink = chip_amount["Pink"] * chip_value["Pink"]
     red = chip_amount["Red"] * chip_value["Red"]
     blue = chip_amount["Blue"] * chip_value["Blue"]
     green = chip_amount["Green"] * chip_value["Green"]
     black = chip_amount["Black"] * chip_value["Black"]
     return white + pink + red + blue + green + black 

# Create A function to win or lose
def win (player, dealer, chip, quantity):
    if hand_value(player) > 21:
        print(f"You lose {chip_value[chip] * quantity}")
        chip_amount[chip] -= quantity
    elif hand_value(dealer) > 21:
        print(f"You win {chip_value[chip] * quantity}")
        chip_amount[chip] += quantity
    elif hand_value(player) > hand_value(dealer):
        print(f"You win {chip_value[chip] * quantity}")
        chip_amount[chip] += quantity 
    elif hand_value(player) == hand_value(dealer):
        print(f"Push")
    else: 
        print(f"You lose {chip_value[chip] * quantity}")
        chip_amount[chip] -= quantity
# Create function to change the value of the A

#Create function to init game
def blackjack():
    cont = input("Would you like to play Blackjack?(Y/N): ")
    while cont == "Y":
        dealer.clear()
        player.clear()
        print(f"Chip values: {chip_value}")
        print(f"Chip amount: {chip_amount}")
        print(f"You have ${cash_value()}")
        chip = "null"
        while chip_amount[chip] < 1: 
            chip = input("What would you like to bet?\n(White, Pink, Red, Blue, Green, Black): ")
            if chip_amount[chip] < 1:
                print("Sorry, you don't have enough to make that bet. Try something else.")
        quantity = 1
        if chip_amount[chip] > 1: 
            quantity = int(input("How many? "))
            while chip_amount[chip] < quantity: 
                print("Sorry, you don't have enough to make that bet. Try something else.")
                quantity = int(input("How many? "))
        deal(deck)
        print(f"The dealer's hand is {dealer[1]}")
        print(f"Your hand is {player}")
        if hand_value(player) == 21 and hand_value(dealer) != 21:
            print("Blackjack!!!! You win")
            win(player, dealer, chip, quantity)
        elif hand_value(dealer) == 21:
            print("The dealer has blackjack. You lose.")
            print(dealer)
            win(player, dealer, chip, quantity)
        else:
            print(f"Your score is: {hand_value(player)}")
            stay = []
            double = []
            if player[0][:-1] == player[1][:-1]:
                double = input("Do you want to double down? (Y/N) ")
                if double == "Y":
                    quantity + 1
                    hit(player)
            while hand_value(player) < 21 and stay != "S" and double != "N":
                stay = input("Whould you like to hit or stay? (H/S) ")
                if stay == "H":
                    hit(player)
                    print(player)
                    print(f"Your score is: {hand_value(player)}")
            print(f"The dealer's hand is: {dealer}")
            print(f"The dealer's score is {hand_value(dealer)}")
            while hand_value(dealer) <= 16:
                hit(dealer)
                print(f"The dealer's hand is: {dealer}")
                print(f"The dealer's score is {hand_value(dealer)}")
            win(player, dealer, chip, quantity)
        cont = input("Would you like to play again?(Y/N): ")



blackjack()


