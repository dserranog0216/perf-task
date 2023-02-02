#Blackjack game
from random import randint

dealer = randint(0,11)
card1 = randint(0,11)
card2 = randint(0,11)



def Game(card1, card2):
  print("Welcome to this game of Blackjack, your objective is to get 21 or get the closest number to 21 without going over but getting something higher than the dealer good luck with the game you'll need it")
  yes = "true"
  while yes == "true":
    print(" ")
    print("dealers hand:",dealer)
    hand = ("your hand, card 1: ", card1, "card 2: ", card2 )
    total = card1+card2
    print(hand)
    print("total:", total)
    next = (input("Hit or stand?"))
    if next=="stand":
      print("stand")
    else:
      print("dealers hand:", dealer + dealer)
      print("Your hand:",total + card1)
      if total > 21:
        print("You lose")
  
  
    

    
    


Game(card1, card2)