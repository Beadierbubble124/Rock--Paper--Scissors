import random

rock = 0
paper = 1
scissors = 2

weapon_map = {
    0: 'rock',
    1: 'paper',
    2: 'scissors'
}

print("")
print("Welcome to the Tournement!")
print("")
print("1)Rock\n2)Paper\n3)Scissors")
print("")

player_move = input("Choose your weapon: ")
player_move = player_move.lower()
print("Your weapon is " + player_move.lower())
print("")

ai_weapon = random.randint(0,2)
ai_move = weapon_map[ai_weapon]
print("Ready!\n Rock\n Paper\n Scissors\n Shoot!")
print("")

ai = {
    'rock' : {
        'rock': 'tied',
        'paper': 'won',
        'scissors': 'lost'
    },
    'paper' : {
        'rock': 'lost',
        'paper': 'tied',
        'scissors': 'lost'
    },
    'scissors' : {
        'rock': 'won',
        'paper': 'lost',
        'scissors': 'tied'
    }
 }

outcome = ai[ai_move][player_move]

if outcome == 'won':
    print("You won: " + player_move + " beats " + ai_move)

elif outcome == 'tied':
    print("You tied: " + player_move + " can't beat " + ai_move)

else:
    print("You lost: " + ai_move + " beats " + player_move)

print("")

'''
Player can only use the 3 options
'''