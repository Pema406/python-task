temp = input("enter temperature")
temp=int(temp)
if temp>=100:
    print("Boiling")
if temp <=32 and temp <=99:
    print("Liquid")
if temp<=32:
    print("Freezing")