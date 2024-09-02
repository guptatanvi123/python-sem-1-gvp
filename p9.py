#(9).Print Fibonacci sequence.
n = int(input("Please Enter Number:-"))
first=0
second=1

while n>0:
   print(first)

   third= first+second
   first = second
   second= third

   n = n-1
