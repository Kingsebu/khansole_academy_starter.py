#importing the random package into python
import random

#setting out to count attempts
count = 0

#as long as count is less than three input from user should continue
while count < 3:

#generating the two random numbers between 10 and 99 and adding them up.
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    sum = num1 + num2

#recieving input from user. Where 3 right responses are entered in a row the program ends with congratulatory message
#where a wrong answer is provided, the program will continue.
    response = int(input(f'What is {num1} + {num2}? '))
    if response == sum:
        count += 1
        print(f"Great!, You got {count} right!")
    elif response != sum:
        count = 0
        print(f"Incorrect!, The right answer is {sum}")
    else:
        print('Invalid answer')
print('Congratulations! You have mastered addition.')
