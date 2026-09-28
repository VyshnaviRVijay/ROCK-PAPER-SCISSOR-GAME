import random
choice=["rock","paper","scissors"]
player=''
while player not in choice:
    player=input("Enter your choice: ").lower()
computer=random.choice(choice)
print(f"player chose {player} and computer chose {computer} ")
if player==computer:
    print("Tie")
else:
    if player=="rock" and computer=="paper":
        print("Computer wins")
    elif player=="rock" and computer=="scissors":
        print("Player wins")
    elif player=="paper" and computer=="rock":
        print("Player wins")
    elif player=="paper" and computer=="scissors":
        print("Computer wins")
    elif player=="scissors" and computer=="paper":
        print("Player wins")
    else:
        print("Computer wins")
