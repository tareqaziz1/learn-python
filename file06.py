# conditions (if, else, elif )

is_sunny = True

if is_sunny:
    print("It's a sunny day!")
else:
    print("It's a cold day!")
print("Have a good day!!") # it will be executed without any condition

''' Qns: Price of a chair is 100.
    If buyer is a returning customer, 10% discount will be given.
    Otherwise 5% discount will be given. Pring the payment.
'''

''''
is_returning_customer = True
price = 100

if is_returning_customer:
    discounted_price = price - (price * 0.1)
    print(discounted_price)
else:
    customer_price = price - (price * 0.05)
    print(customer_price)
print("Check the price above")
''
# When is_returning_customer = True outcome is 90
# When is_returning_customer = False outcome is 95

#using elif for 2 or more conditions

If the customar is older than 50 he gets 20% discount. Print the price.'''

is_returning_customer = False
price = 100
customer_age = 51

if is_returning_customer:
    discounted_price = price - (price * 0.1)
    print(discounted_price)

elif customer_age > 50:    # This condition is fulfilled and it is executed.
    discounted_price = price - (price * 0.2)
    print(discounted_price)

else:
    customer_price = price - (price * 0.05)
    print(customer_price)

'''If temperature is 30, it's a hot day. 
If it is less than 10 then it's a very cold day,
otherwise it's a normal day'''

temperature = 12

if temperature >= 30:
    print("It's a hot day!")
elif temperature <= 10:
    print("It's a cold day!")
else:
    print("It's a normal day!")



'''If name is less than 3 character long, show name must be 3 character.
If it is 10 character long then show - it must be within 10 characters.
 Otherwise show name looks good'''

name = "tareq"

if len(name) < 3:
    print("Name must be at least 3 character")
elif len(name) > 10:
    print("Name must be within 10 character")
else:
    print("Name looks good!")

''''
# Determine discount
if original_price >= 100:
    discount = 0.20 if is_member else 0.10
else:
    discount = 0.0

new_price = original_price * (1 - discount)

# Determine shipping
is_neighbor = country.upper() in ['BELGIUM', 'GERMANY', 'NETHERLANDS']
if is_member:
    shipping = 5 if is_neighbor else 10
else:
    shipping = 10 if is_neighbor else 20

total_cost = new_price + shipping
print(total_cost)

'''


'''
Calculate the final price for a movie ticket based on age, student status, and showtime.

Adults (18+):
Students pay a base price of $12.00.
Showtimes before 17:00 (5 PM) get a $3.00 discount.
Evening showtimes pay the base price.
Non-students pay a base price of $12.00 and extra $6.
Showtimes before 17:00 get a 10% discount base ticket price.
Evening showtimes add a $2.00 prime-time surcharge.

(Time format - 1300 = 1PM, 1400 = 2PM)

'''

ticket_price = 12
age = 10
is_student = False
show_time = 1900

if age >= 18 and is_student:
    if show_time < 1700:
        new_ticket_price = ticket_price - 3
        print(new_ticket_price)
    else:
        new_ticket_price = ticket_price
        print(new_ticket_price)
elif age < 18 or is_student == False:
    new_ticket_price = ticket_price + 6
    print(new_ticket_price)
    if show_time < 1700:
        new_ticket_price = ticket_price * 0.9
        print(new_ticket_price)

