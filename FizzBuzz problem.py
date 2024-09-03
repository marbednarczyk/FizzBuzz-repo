"""
Program is replacing any number in range between 1 and 100 divisible by three with the word "Fizz", 
and any number divisible by five with the word "Buzz", 
and any number divisible by both three and five with the word "FizzBuzz".
"""

# Declaration of numbner which program are going to check
number = 4

# Loop where division of number is verified and replaced with proper word
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif not number % 5:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)