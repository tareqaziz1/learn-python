# While loop syntax - ( while condition: )
# As long as the condition is true the code will be executed

i = 1
while i <= 5:
    print(i)
    i += 1
print("finished")


# Print half pyramid with asterisks
j = 1
while j <= 5:
    print(j * "*")
    j += 1

# Make a 6 row pyramid

row = 6
z = 1

while z <= row:
    spaces = row - z
    stars = 2 * z - 1

    print(" " * spaces + "*" * stars)
    z += 1

# Guessing game with 3 attempt


secret_number = 7
guess = 0
guess_limit = 3

while guess < guess_limit:
    input_number = int(input("What is the secret number? : "))
    guess += 1

    if input_number == secret_number:
        print("Congratulations ! Your guess is correct.")
        break
    elif guess == guess_limit:
        print("Your guess is wrong! Try again !")
        print("Thanks for playing !")

    else:
        print("Your guess is wrong. Try again ! ")


''''while guess < guess_limit:
    input_number = int(input("What is the secret number? : "))
    guess += 1
    if secret_number == input_number:
        print("Your guess is correct!!!")
        print("Thank you for playing.")
        break
    elif guess == guess_limit:
        print("Your guess is wrong. Try again !")
        print("Thank you for playing.")
    else:
        print("Your guess is wrong. Try again !")'''

# car engine program

command = ""
started = True
stopped = True
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started...")
        else:
            started = True
            print("Car started...")

    elif command == "stop":
        if stopped:
            print("Car already stopped...")
        else:
            stopped = True
            print("Car stopped...")
    elif command == "help":
        print('''
        start - to start the car.
        stop - to stop the car.
        quit - to quit''')
    elif command == "quit":
        print("Game Over!")
        break
    else:
        print("Wrong command! to get help, type - help")



