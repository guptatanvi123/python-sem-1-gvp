#(6).Find the student from CS department where the roll number may be in capital or smallcase Letters.

print("---:Find Your Department:---")
roll = input("Enter your Roll Number In Syntax(CS23B048) :- ")

if (roll[0]=='C' or roll[0]=='c') and(roll[1]=='S' or roll[1]=='s'):
   print("You Are Belongs To COMPUTER SCIENCE Department")
else:
   print("Sorry You Are Not From COMPUTER SCIENCE Department")
    
