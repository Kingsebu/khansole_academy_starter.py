count = 0
while count < 3:

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    sum = num1 + num2
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
