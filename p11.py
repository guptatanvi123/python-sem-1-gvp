#giving a postive number check if it is a prime number or not.

n = int(input("enter number"))  
if n<2:
     print("not a prime number")
else:
    for i in range(2, n):
         if n % i == 0:
             print("not a prime number")
             break
    else:
     print("number is prime")
      
