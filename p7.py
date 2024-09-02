#(7.)To read a card as input and output if the card is lucky or not.

print("---:Find Your Card:---")
cards = input("Enter Your Card:- ")   #user input
luckycards = ("king", "queen" , "A")  

if cards in luckycards: #condition
   print("Congrats You Got A Lucky Card") #if true
else:
   print("Better Luck Next Time") #if false
    
