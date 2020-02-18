#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: frbvianna
----------------------
--- BlackJack Game ---
----------------------

--- GAME SEQUENCE: ---
Player starts with 1000 chips and must place a bet.
The deck contains 52 shuffled cards.
Both player and dealer (PC) start with two cards. Dealer's second card is hidden.
Player's turn allow to draw more cards to hand, or keep current hand.
If player busts, dealer wins. If player hits BlackJack or skips turn, dealer goes.
Dealer draws cards until his hand is 17 or bigger.

Finally, player wins if dealer busts, or if hand count is bigger than the dealer's.

Good Luck!  
----------------------  
"""

import random as r
import time

class Card():

    face = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suit = ('\u2665', '\u2666', '\u2660', '\u2663')
   
    
class Deck():

    def __init__(self, deck = []):
        self.deck = deck
        
    def __str__(self):
        return f"Deck currently has {len(self.deck)} cards."

    def createDeck(self):
        """
        Creates a classic deck of 52 cards, as a 2D array:
            52 rows, two columns each (face and suit)
            
            Ex.:   [('A', 'Hearts'),
                    ('A', 'Clubs'),
                                 ...]
        """
        
        self.deck = [(face, suit) for face in Card.face for suit in Card.suit]
    
    def shuffle(self):
        """
        Randomly shuffles the entire range of the deck.
        """
        
        for card in range(0,len(self.deck)):
            randomCard = r.randint(0,len(self.deck)-1)
            self.deck[card], self.deck[randomCard] = self.deck[randomCard], self.deck[card]


class Chips():

    def __init__(self, chips):
        self.chips = chips
    
    def winChips(self, amount):
        """
        Adds chips to the total amount.
        """
        
        self.chips += amount
    
    def loseChips(self, amount):
        """
        Subtracts chips from the total amount.
        """
        
        self.chips -= amount

         
class Hand():
    
    def __init__(self, hand, count, choice = ''):
        self.hand = hand
        self.count = count
        self.choice = choice
                
    def handCount(self):
        """
        Counts total hand value.
        """
        
        countDict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

        self.count = 0
        for card in self.hand:
            if card[0] == 'A' and self.count <= 10:
                self.count += 11
            elif card[0] == 'A':
                self.count += 1
            else:
                self.count += countDict[card[0]]


class Player(Chips, Hand):
    
    def __init__(self, chips = 0, hand = [], count = 0):
        Chips.__init__(self, chips)
        Hand.__init__(self, hand, count)
                             
    
def greet():
    """
    Initial greeting.
    """
    
    print("\n----------------------\n--- BlackJack Game ---\n----------------------\n\n--- GAME SEQUENCE: ---\nPlayer starts with 1000 chips and must place a bet.\nThe deck contains 52 shuffled cards.\nBoth player and dealer (PC) start with two cards. Dealer's second card is hidden.\nPlayer's turn allow to draw more cards to hand, or keep current hand.\nIf player busts, dealer wins. If player hits BlackJack or skips turn, dealer goes.\nDealer draws cards until his hand is 17 or bigger.\n\nFinally, player wins if dealer busts, or if hand count is bigger than the dealer's.\n\nGood Luck!\n----------------------\n\n")     
    
def begin():
    """
    Initiates Deck object and creates deck; then, shuffles the cards.
    Initiates Player objects, player (pr) and dealer (pc).
    """
    
    global pr
    global pc
    global d
    
    d = Deck()
    d.createDeck()
    d.shuffle()
    
    pr = Player()
    pc = Player()      

def deal(toWhom):
    """
    Deals cards, from deck stack to hand stack.
    """
    
    global pr 
    global pc
    global d
    
    if toWhom == 'pr':
        pr.hand.append(d.deck.pop())
    elif toWhom == 'pc':
        pc.hand.append(d.deck.pop())
                
def playerBet():
    """
    Places player bet as per input.
    Returns remaining chips.
    """
    
    global bet
    
    print(f"\nYou have {pr.chips} chips available.")
    while True:
        try:
            bet = input("How many chips would you like to bet? ")
            bet = int(bet)
        except ValueError:
            print("Invalid input.")
            continue
        else:
            if bet > pr.chips:
                print(f"Can't bet more than {pr.chips} chips.")
                continue
            else:
                return pr.chips - bet
                break
        
def cardDeal(when):
    """
    Sorts card dealing.
    First deal:   Deals two cards for both player and dealer,
                  Displays one dealer card and two player cards.
    Next deal:    Subsequent card deals for player.
                  Displays one dealer card and all player cards.
    Dealer deal:  Deals cards for dealer until its count reaches 17 or larger.
                  At the end, displays all dealer and player cards.
    """
    
    if when == 'firstDeal':
        print("\n"*3)
        
        for _ in [1,2]:
            deal('pr')
            deal('pc')
        
        print("Dealer's hand:", end = " "*3)
        print("{} {}".format(pc.hand[0][0], pc.hand[0][1]), end = " "*3)
        print("[? ?]")
        pc.handCount()
        
        print("\nPlayer's hand:", end = " "*3)
        for card in pr.hand: 
            print("{} {}".format(card[0], card[1]), end = " "*3)
        pr.handCount()
        print("Player count:"+" "*3+"{}".format(pr.count))
        
        print("\n\n")
    
    elif when == 'nextDeal':
        print("\n"*3)
        
        deal('pr')
        
        print("Dealer's hand:", end = " "*3)
        print("{} {}".format(pc.hand[0][0], pc.hand[0][1]), end = " "*3)
        print("[? ?]")
        
        print("\nPlayer's hand:", end = " "*3)
        for card in pr.hand: 
            print("{} {}".format(card[0], card[1]), end = " "*3)
        pr.handCount()
        print("Player count:"+" "*3+"{}".format(pr.count))
        
        print("\n\n")
        
    elif when == 'dealerDeal':
        print("\n"*3)
    
        while pc.count <= 17:
            deal('pc')
            pc.handCount()

        print("Dealer's hand:", end = " "*3)
        for card in pc.hand: 
            print("{} {}".format(card[0], card[1]), end = " "*3)
        print("Dealer count:"+" "*3+"{}".format(pc.count))
        
        print("\nPlayer's hand:", end = " "*3)
        for card in pr.hand: 
            print("{} {}".format(card[0], card[1]), end = " "*3)
        pr.handCount()
        print("Player count:"+" "*3+"{}".format(pr.count))
        
        print("\n")
    
def nextCard():
    """
    Decides whether or not to deal more cards, as per input.
    """
    
    while True:
        dealMore = input("Would you like to deal more cards? [Y or N] ")
        if dealMore in ['Y', 'y']:
            return True
            break
        elif dealMore in ['N', 'n']:
            return False
            break
        else:
            print("Invalid input.")
            continue
        
def checkBust():
    """
    Checks for player bust, that is, a hand count larger than 21.
    """
    
    if pr.count > 21:
        return True
    else:
        pass
    
def checkBlackJack():
    """
    Checks for player BlackJack, that is, a hand count equal to 21.
    """
    
    if pr.count == 21:
        print("You hit BlackJack!")
        return True
    else:
        pass

def playerTurn():
    """
    Sequentiates player actions.
    """
    
    drawMore = True
    bust = False
    blackJack = False
    
    while True:
        drawMore = nextCard()
        if not drawMore:
            break
        
        cardDeal('nextDeal')
        
        bust = checkBust()
        if bust:
            break
        
        blackJack = checkBlackJack()
        if blackJack:
            break
    
    return bust
        
def dealerTurn():
    """
    Arranges dealer turn, when player doesn't bust.
    """
    
    print("\n"*2)
    dotStr = ""
    print(f"Wait for dealer turn", end = "")
    for _ in range(3):
        print(f"{dotStr}", end = "")
        dotStr += " ."
        time.sleep(1)
    
    cardDeal("dealerDeal")

def matchDecision():
    """
    Outputs winner and loser, rewarding double the bet (only player).
    """
    
    global pc
    global pr
    
    if pc.count > 21 and pr.count <= 21:
        print("Dealer bust and you won the bet!")
        print(f"Congratulations, you've been rewarded {2*bet} chips.")
        pr.winChips(2*bet)
    elif pc.count <= 21 and pr.count > 21:
        print("You just bust!")
        print(f"The dealer won the bet and you lost {bet} chips.")
    elif pc.count == pr.count:
        print(f"It's a tie! You have received your {bet} chips back.")        
    elif pc.count > pr.count:
        print(f"The dealer won the bet and you lost {bet} chips.")
    elif pc.count < pr.count:
        print("You won the bet!")
        print(f"Congratulations, you've been rewarded {2*bet} chips.")
        pr.winChips(2*bet)
    
    print(f"\nPlayer chips left: {pr.chips}")
        
def resetTable():
    """
    Flushes cards, resetting hands and deck.
    """
    
    global pc
    global pr
    global d
    
    pc.hand = []
    pr.hand = []
    
    d.createDeck()
    d.shuffle()
    
def replayBet():
    """
    Decides whether or not to run another bet, as per input.
    """
    
    while True:
        replayChoice = input("Would you like to bet again? [Y or N] ")
        if replayChoice in ['Y', 'y']:
            return True
            break
        elif replayChoice in ['N', 'n']:
            return False
            break
        else:
            continue
        
if __name__ == '__main__':
    
    greet()
    begin()
    pr.winChips(1000)
    replay = True
    
    while True:
        pr.chips = playerBet()
        cardDeal('firstDeal')
        
        bust = playerTurn()
        
        if not bust:
            dealerTurn()
        
        matchDecision()
        resetTable()
        
        if pr.chips == 0:
            print("\nCan't bet again, you've run out of chips.")
            break
            
        replay = replayBet()
        
        if not replay:
            break

    print("\nThanks for playing!")       
