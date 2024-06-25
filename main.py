import random
print("Welcome to the pig dice game!")
user_name = input("what is your name?")
print("-"*30)


dice_options = [1,2,3,4,5,6]
user_final_score = 0
computer_final_score = 0
while True:
    input("Click 'enter' to roll the dice")
    print("-" * 30)
    player_value = random.choice(dice_options)
    computer_value = random.choice(dice_options)
    print(f"{user_name} rolled a {player_value}")
    print(f"The computer rolled a {computer_value}")

    if player_value == 1:
        print(f"OOPS {user_name} rolled a 1. Must start score over.")
        user_final_score = 0
    if computer_value == 1:
        print("OOPS...the computer rolled a 1. Must start score over.")
        computer_final_score = 0

    if player_value != 1:
        user_final_score += player_value

    if computer_value != 1:
        computer_final_score += computer_value


    print(f"{user_name}'s score is {user_final_score}")
    print(f"The computer's score is {computer_final_score}")


    if user_final_score >= 30:
        print(f"{user_name} won the pig game!")
        break

    if computer_final_score  >= 30:
        print("The computer won the pig game!")
        break
