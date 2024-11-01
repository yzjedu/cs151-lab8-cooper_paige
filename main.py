# Intro comments

# PLACEHOLDER FOR PRINTING LIST
# print(list[2]*'*')


import random

sum_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num_roll = 0
sum = 0

# Purpose: Make sure the number the user inputs is an integer
# Parameters: None
# Return: Number user inputs as an integer
def roll_amount():
    num_roll = input("How many times do you want to roll the dice? ")
    while not num_roll.isdigit():
        print("Please enter a valid number.")
        num_roll = input("How many times do you want to roll the dice? ")
    num_roll = int(num_roll)
    return num_roll


# Purpose: Get a value for the roll of the dice
# Parameters: None
# Return: Sum of the two dice rolls
def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = roll1 + roll2
    return sum


# Purpose: Store the amount of times the sum is rolled
# Parameters: Sum
# Return: None
def add_to_list(sum):
    sum_list[sum] = sum_list[sum] + 1


# Purpose: Print the list
# Parameters: None
# Return: None
def print_list():
    print(f'Rolling {num_roll} pairs of dice.')
    print(sum_list)
    count_list = 0
    total = 10
    while count_list <= total:
        print(f'Sum of {count_list + 2:02}: {sum_list[count_list + 2]*'*'}')
        count_list += 1


# Purpose:
# Parameters: None
# Return: None
def main():
    print('Enter purpose here')
    num_roll = roll_amount()
    count = 0
    while count < num_roll:
        sum = roll_dice()
        add_to_list(sum)
        count += 1
    print_list()

main()