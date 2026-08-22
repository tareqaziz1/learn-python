# for loop

for letter in "python":
    print(letter)


# List is a list of items. It can be numbers or strings. Syntax - []

for item in ["Tareq", "John", "Tom"]:
    print(item)

for number in [1,2,3,4,5,6]:
    print(number)

#to print a range of 1 to 9 (range has to be until 10) -

for x in range(10):
    print(x)

for z in range(20, 31):
    print(z) # it will print 20 to 30

# Range function can add a step. For example if 2 is given as a third parameter it will be forwaded with 2 steps.

for i in range(20,31,2):
    print(i) # it will print 20,22,24.26,28,30

# A list of prices given, add the total .

prices = [10.5, 14.20, 15.20, 30.10]
total_price = 0

for item_price in prices:
    total_price += item_price

print(f"Total price: {total_price}")

# nested loop (For iterating items and items inside items)

'''
(x,y)
(0,1)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
'''

for i in range(3):
    for j in range(2):
        print(f"({i},{j})")

#make an F shape with asterisks

rows = [5, 2, 5, 2, 2]

for star in rows:
    output = ""
    for star1 in range(star):
        output += "*"
    print(output)

# OR

for star in rows:
    print(star * 'x')

'''
Given the list prices = [12.50, 45.00, 8.00, 100.00, 24.50].

Use a for loop to iterate through prices and calculate the subtotal.

If is_member = True, apply a 10% discount to any single item priced at $20 or higher (items under $20 remain full price). 
If is_member = False, all items are full price.

Calculate and print the final total.
'''

product_prices = [12.50, 45.00, 8.00, 100.00, 24.50]
is_Member = input("Are you a member? (Y/N) ").lower().startswith("y")
subtotal = 0

for i in product_prices:
    if i >= 20 and is_Member:
        subtotal += i * 0.9
    else:
        subtotal += i

print(subtotal)


'''
Write a Python script that calculates the extra fee for a piece of luggage based on its weight and passenger status.

Rules:

Standard Allowances:
Economy: Free up to 23 kg.
Business: Free up to 32 kg.

Overweight Surcharges (Beyond Free Allowance):

First 5 kg over limit: $10 per kg.
Any weight beyond 5 kg over the limit: $20 per kg for those additional kilograms.

VIP & Absolute Limit Conditions:

If has_gold_card = True, the passenger gets an extra 5 kg added to their base free allowance, and receives a flat $15 discount off the total calculated extra fee (the final fee cannot go below $0).

Hard Cap: Any bag strictly over 40 kg is rejected with "REJECTED: Too Heavy" regardless of ticket class or card status (no fee calculated).'''

ticket_class = input("What is your ticket class? : ")
weight = int(input("What's the weight of the luggage : "))
is_goldCardHolder = input("Do you have a gold card? (Yes/No): ").lower().startswith('y')