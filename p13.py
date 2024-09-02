#(13).Exact change: Given a price identify if you have exact change summing up to that price?
#(Count all combinations of coins to make a given value sum.)

Price=int(input('Enter Price:'))
temp=0

currency1=int(input("Check Currency 1:"))
currency2=int(input("Check Currency 2:"))
currency3=int(input("Check Currency 3:"))

print(f"{currency1}-{currency2}-{currency3}")
for c1 in range(0, 1+Price // currency1):
    for c2 in range(0, 1+Price // currency2):
        for c3 in range(0, 1+Price // currency3):
            if c1*currency1 + c2*currency2 + c3*currency3 == Price:
                temp=temp+1
                print(c1,c2,c3)

print(f"all combinations Count: {temp}")
