rock = 0
paper = 1
scissors = 2

print("Welcome to the Tournement!")
print("1)Rock\n2)Paper\n3)Scissors")
weapon = input("Choose your weapon: ")
print("Your weapon is " + weapon.lower())

"""
random.randrange(0,2)
print("Ready!\n Rock\n Paper\n Scissors\n Shoot)

Use nested dictionary to decide outcome
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
    }
    'scissors' " {
        'rock': 'won',
        'paper': 'lost',
        'scissors": 'tied'
    }
}

ai_move = 'punch'
player_move = 'kick'
print ai[ai_move][player_move] #output: wins


ai_move = 'stab'
player_move = 'punch'
print ai[ai_move][player_move] #output: loses


#You "Blank"
#Blank beats Blank
"""