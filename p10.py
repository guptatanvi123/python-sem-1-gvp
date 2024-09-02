#(10).Collatz Sequence

n=int(input("enter a number"))  #user input
while n!=1: #condition
    if n%2==1: #check the input is even or odd.
       n=3*n+1  #for odd number
    else:       
       n=n//2 #for even number
    print(n)  #output
