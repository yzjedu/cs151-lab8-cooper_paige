# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

- Input validation
- Roll the dice
- Add the sum to the list
- Print the list
- Main

Purpose: Make sure the number the user inputs is an integer  
Name: roll_amount  
Parameters: None  
Return: Number user inputs as an integer  
Algorithm:
1. Prompt the user to input the number of dice rolls they want
2. While roll amount is not a digit
   1. Output that the input was invalid and prompt the user to input a digit
3. Convert the number of rolls to an integer
4. Output roll amount


Purpose: Get a value for the roll of the dice  
Name: roll_dice  
Parameters: None  
Return: Sum of the two dice rolls  
Algorithm:
1. Get a random number from one to six and store it within a variable such as 'roll1'
2. Get another random number from one to six and store it within a variable such as 'roll2'
3. Add roll1 and roll2 and store it within a variable such as 'sum'


Purpose: Store the amount of times the sum is rolled  
Name: add_to_list  
Parameters: Sum  
Return: None  
Algorithm:
1. Add 1 to the index of the sum in the list


Purpose: Print the list  
Name: print_list  
Parameters: None  
Return: None  
Algorithm:
1. Output the list
2. Set count equal to 2
3. Set total to 12
4. While count is less than total:
   1. Output the sum and its corresponding index
   2. Add 1 to count


Purpose:   
Name: main  
Parameters: None  
Return: None  
Algorithm:  
1. Output purpose
2. Create a list with thirteen spots, all of which are zero
3. Set count equal to zero
4. Call the amount function
5. While count is less than amount:
   1. Call roll_dice function
   2. Call add_to_list function with the sum from the roll_dice function as an argument
   3. Add 1 to count
6. Call the print_list function
7. Output goodbye message