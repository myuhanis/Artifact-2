# Part 1: Credit Card Approval Simulation

# Initialize variable
user_name = 'L'

# Open text document to write user input
with open('CreditCardOutput.txt', mode='w') as userinput:
    while user_name != 'done':
        user_name = input('Applicant Name: ')
        if user_name != 'done':
            user_credit = int(input('Applicant Credit Score: '))
            # Validate user credit score
            while user_credit < 300 or user_credit > 850:
                print('Invalid credit score')
                user_credit = int(input('Applicant Credit Score: '))
            user_multiplier = float(input('Credit Score Multiplier: '))
            # Validate user credit multiplier
            while user_multiplier < -0.20 or user_multiplier > 0.20:
                print('Invalid credit multiplier')
                user_multiplier = float(input('Credit Score Multiplier: '))
            # Write user information to file
            userinput.write(f'{user_name} {user_credit} {user_multiplier}\n')

# Open text document to read user input and perform calculations
with open('CreditCardOutput.txt', mode='r') as userinput:
    line = userinput.readline()
    approved = 0
    decline = 0
    print(f'{"Name":<10}{"Credit Score":<10}{"Multiplier":>15}')
    while line:
        line = line.split()
        score = int(line[1])
        multi = 1 + float(line[2])
        if (score * multi) >= 605:
            approved += 1
        else:
            decline += 1
        print(f'{line[0]:<10}{line[1]:<10}{line[2]:>15}')
        line = userinput.readline()
    # Calculate percentage of approved applicants
    total_applicants = approved + decline
    approval_percentage = (approved / total_applicants) * 100 if total_applicants > 0 else 0
    print(f'Approved Applicants: {approved}\nApplicants Declined: {decline}\nPercentage: {approval_percentage:.2f}%')


# Part 2: Dice Rolling Simulation

# Prompt user to input number of times to roll dice
roll = int(input('Number of times to roll dice: '))
while roll < 1:
    roll = int(input('Number of times to roll dice: '))

import random

# Dictionary to store frequency of each dice roll
freq = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simulate rolling dice and calculate frequency of each number rolled
for x in range(roll):
    num = random.randrange(1, 7)
    freq[num] += 1

print(freq)
