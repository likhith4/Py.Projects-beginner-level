import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll
value=roll()
print(value)

while True:
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Number must be between 2-4")
    else:
        print("Looks like you have not entered a number !, Try again with number :)")


max_score=25
player_scores=[0 for _ in range(players)]
print(player_scores)

while max(player_scores)<=max_score:
    for player_idx in range(players):
        print("\nPlayer",player_idx+1,"has just started!\n")
        print("Your total score is ",player_scores[player_idx],"\n")
        current_score=0
        while True:
            should_roll=input("Would you like to roll (y)? :")
            if should_roll.lower()!='y':
                break
            else:
                value=roll()
            if value == 1:
                current_score=0
                print("You rolled a 1 ,Turn done")
                break
            else:
                current_score+=value
                print(f"You rolled {value}!")
            print(f"Your current score is {current_score} ")
        player_scores[player_idx]+=current_score
        print("Your total score is ",player_scores[player_idx])
max_score=max(player_scores)
winningidx=player_scores.index(max_score)
print('Player number',winningidx+1,"is the WINNER")
    

