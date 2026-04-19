# Functions

# Make a function that prints "Hello World"

def hello_world():
    print("Hello World")

hello_world()

# Make function with parameters

def greeting(name):
    print(f"Good morning {name}")

greeting("John")
greeting("Sarah")


def custom_greeting(first_name, last_name, message):
    print(f"Hey, {first_name} {last_name}, {message}")

custom_greeting("Tareq", "Aziz", "Welconme aboard!")

# Keyword argument ( position does not matter if it is used)

custom_greeting(last_name="Aziz", message="Good evening", first_name="Tareq")

# function with default argument

def smith_family(first_name, last_name = "Smith"):
    print(f"Hello! {first_name} {last_name}, Thanks for joining")

print(smith_family("Bob"))

# fucntion with return statement
# Every function returns a "None" by default

def square (number):
    return number * number

result = square(4)
print(result)
#or
print(square(5))    # without return it will return "None"

# Function that returns cube of a number
def cube(number):
    return number ** 3

# Function that calculates average

def average_cost(total_cost, number_of_items):
    return total_cost / number_of_items

print(average_cost(100, 5))

print(cube(4))  #output - 20

# Emoji converter function

def convert_to_emoji(message):
    words = message.split(" ")

    emojis = {
        "happy": ":)",
        "sad": ":(",
        "angry": "-_-",
        "shy": "^_^"
    }
    output = ""
    for word in words:
        coverted = emojis.get(word, word)
        output += coverted + " "
    return output

message = input("> ")
print(convert_to_emoji(message))














