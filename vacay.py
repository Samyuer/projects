# trip suggestion program
import random
import time
# roock paper sccissors

opt = ["rock", "paper", "scissors"]

Starting_line = ["rock", "paper", "scissors","shoot"]

for i in Starting_line:
    print(i + "\n")
    time.sleep(0.5)

guess = input()

ai_pick = random.choice(opt)

def rps(guess, ai_pick):
 if guess == ai_pick:
    print("Tie")
 elif guess == "rock" and ai_pick == "scissors":
    print("You win")
 elif guess == "paper" and ai_pick == "rock":
    print("You win")
 elif guess == "scissors" and ai_pick == "paper":
    print("You win")
 else:
    print("You lose")

rps(guess, ai_pick)