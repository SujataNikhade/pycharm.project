item= str(input("what item would you like to buy?:"))
price= float(input("what price?:"))
quantity= int(input("how many would you like?:"))

total=price*quantity

print(f"you have bought {quantity} x {item}")
print(f"your total is: {total}")