# Built in modules

import random # To generate random number

for i in range(3):
    print(random.randint(1,10))

members = [ "John", "Bob", "Sarah", "Taru", "Josh"]

lucky_member = random.choice(members)
print(lucky_member)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice1 = Dice()
print(dice1.roll())

class Lottery:
    def winner(self, players):
        winner_name = random.choice(players)
        return winner_name


lottery1 = Lottery()
won = lottery1.winner(["Mohammed", "Robin", "Sarah"])
print(won)

