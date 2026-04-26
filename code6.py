# game

"""villian = 100
player = 50

print("------Battle Started------")

while villian > 0:
    print(f"Vilian Health : {villian}")
    input("Press Enter to Attack 👊")

    villian -= player

if villian <= 0:
    print("Booom! You Win")
else:
    print("Villian is still standing! keep hitting")

print("--- Game Over -----")
"""

# rock paper scissors

import random
options = ['rock','paper','scissors']
player = True

while True:
    player = input(" Enter rock,paper, or scissors" )

    computer_random = random.choice('rock','paper','scissors')
    print(f"computer chose: {computer_random}")

    if player == computer_random:
        print("tie")
    else:
        print("you win!")

    print("Game over")
    
