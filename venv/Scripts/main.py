import random

# Welcome
print('Welcome to Rock, Paper Sissors')

#Instrustions
playerChoice = int(input("Choose between 3 choices; (1)Rock, (2)Paper or (3)Scissors "))

#Computer randomised choice
for x in range(1):
    computerChoice = random.randint(1,4)

#Logic (if statements)
#Player chooses 1
if playerChoice == 1 and computerChoice == 1:
    print('Draw, both players picked ROCK')
elif playerChoice == 1 and computerChoice == 2:
    print('Computer wins, PAPER BEATS ROCK')
elif playerChoice == 1 and computerChoice == 3:
    print('Player wins, ROCK BEATS SCISSORS')

#Player chooses 2
elif playerChoice == 2 and computerChoice == 1:
    print('Computer wins, PAPER BEATS ROCK')
elif playerChoice == 2 and computerChoice == 2:
    print('Draw, both players picked PAPER')
elif playerChoice == 2 and computerChoice == 3:
    print('Computer wins, SCISSORS BEATS PAPER')

#Player chooses 3
elif playerChoice == 3 and computerChoice == 1:
    print('Computer wins, ROCK BEATS SCISSORS')
elif playerChoice == 3 and computerChoice == 2:
    print('Player wins, SCISSORS BEATS PAPER')
elif playerChoice == 3 and computerChoice == 3:
    print('Draw, both players picked SCISSORS')
else:
    print('Please enter a valid entry (1, 2 or 3)')


