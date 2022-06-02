import random
from random import shuffle

class Card:
    
    cardRank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    cardSuit = ("Club", "Diamond", "Heart", "Spade")
    
    def __init__(self, rank = cardRank[0], suit = cardSuit[0]):
        self.rank = rank
        self.suit = suit
        
    def printCard(self):
        print(f"{self.rank} {self.suit}")
        
    def getCardValue(self):
        self.cardValue = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
        self.cVs = dict(zip(self.cardRank, self.cardValue))
        return self.cVs[self.rank]
    
    def value(self):
        return self.cardValue[self.cardRank.index(self.rank)]
        
        
class Deck:
    
    def __init__(self):
        self.deck = []
        for rank in Card().cardRank:
            for suit in Card().cardSuit:
                self.deck.append(f"{rank} {suit}")
       # self.deck = Card().cardRank * Card().cardSuit
        random.shuffle(self.deck)
        
        
    def dealCard(self):
        str = self.deck.pop(0).split(" ")
        return Card(str[0], str[1])
        
class Hand:
        
        def __init__(self):
            self.hand = []
            
        def takeCard(self, card):
            self.hand.append(card)
            
        def handScore(self):
            aces = 0
            score = 0
            for card in self.hand:
                score += card.getCardValue()
                if "Ace" == card.rank:
                    aces += 1
            if score > 21 and aces > 0:
                score -= 10 * aces
            return score
            
        def showCard(self):
            self.hand[-1].printCard()
            
def playerChoice():
        choice = input("Hit (h) or stand (s)?")
        while choice != "h" and choice != "s":
            choice = input("Hit (h) or stand (s)?")
        return choice == "h"
        
        
def playBJ(deck):
        dealerHand = Hand()
        playerHand = Hand()
        dealerHand.takeCard(deck.dealCard())
        print("Dealer got ")
        dealerHand.showCard()
        dealerHand.takeCard(deck.dealCard())
        playerHand.takeCard(deck.dealCard())
        print("Player got ")
        playerHand.showCard()
        while (playerHand.handScore() < 21) and (playerChoice()):
            playerHand.takeCard(deck.dealCard())
            print("Player got ")
            playerHand.showCard()
        if playerHand.handScore() > 21:
            print(f"Player score is {playerHand.handScore()} and Dealer score is {dealerHand.handScore()}. \nYou lost.")
            return False
        print("Dealer got ")
        dealerHand.showCard()
        while dealerHand.handScore() < 17:
            dealerHand.takeCard(deck.dealCard())
            print("Dealer got ")
            dealerHand.showCard()
        if dealerHand.handScore() > 21 or playerHand.handScore() > dealerHand.handScore():
            print(f"Player score is {playerHand.handScore()} and Dealer score is {dealerHand.handScore()}. \nYou win.")
            return True
        if playerHand.handScore() < dealerHand.handScore():
            print(f"Player score is {playerHand.handScore()} and Dealer score is {dealerHand.handScore()}. \nYou lost.")
            return False
        if playerHand.handScore() == dealerHand.handScore():
            print(f"Player score is {playerHand.handScore()} and Dealer score is {dealerHand.handScore()}. \npush")
            return True
        
cash = 250
while cash > 0:
    if playBJ(Deck()):
        print(f"Your prize is: {cash / 2}$")
        cash += cash / 2
        print(f"Your total is: {cash}$")
    else:
        print(f"You lost: {cash / 2}$")
        cash -= cash / 2
        print(f"Your total is: {cash}$")
    ev = input("Keep playing?")
    while ev != "y" and ev != "n":
        ev = input("Keep playing?")
    if ev == "n":
        cash = 0
    print("Тут был Леха")