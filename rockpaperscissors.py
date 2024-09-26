#The game rockpaperscissors includes two users 1.User 2.Computer
import random
#the three choices are stored in a list
game=["rock","paper","scissors"]
#the count is initialized to zero
user_count=0
comp_count=0

#thw while is used and the loop runs until any one of the player wins by acquiring 3 points
while user_count<3 and comp_count<3:
    #asks for user to enter a input in three choices
    user_choice=input("Enter your choice:(rock,paper,scissors): ")
    #random is used to pick a choice of computer choice randomly
    comp_choice=random.choice(game)
    #prints the user choice and computer choice 
    print(f"The user choice is {user_choice} and computer choice is {comp_choice}")
    #check whether who gets points according to their choice
    if user_choice == comp_choice:
        print("It's a tie")
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("Point to Computer")
            comp_count+=1
        else:
            print("Point to User")
            user_count+=1
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("Point to User")
            user_count+=1
        else:
            print("Point to Computer")
            comp_count+=1
    else:
        if comp_choice == "rock":
            print("Point to Computer")
            comp_count+=1
        else:
            print("Point to User")
            user_count+=1
    #prints the point of both user and computer
    print(f"User point {user_count}, Computer point {comp_count}")

#prints who wins the game by acquiring maximum points(3)
if comp_count == 3:
    print("Computer won the Game")
else:
    print("User won the Game")


# Rock Paper Scissors Game Test Cases
# User choice    Computer choice    Result
# rock            rock              tie
# rock            paper             computer point
# rock            scissors          user point
# paper           rock              user point
# paper           paper             tie
# paper           scissors          computer point
# scissors        rock              computer point
# scissors        paper             user point
# scissors        scissors          tie