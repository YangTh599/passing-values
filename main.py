# Thayer Yang
# 20 DEC 2024
# Passing Values

from random import randint

def generate_random_number():
    return randint(1,25)

def user_generate_number_input():
    print("Please enter a number between 1 and 25")
    while True:
        num = input("Enter a number:\n")
        if num.isdigit():
            if int(num) >= 1 and int(num) < 25:
                return int(num)
            else:
                print("Out of range!\n")
        else:
            print("Please enter a number!\n")

def square_number(num):
    return num**2

value_random = generate_random_number()
result_random = square_number(value_random)

print(f"The square of {value_random} is {result_random}.")

value_input = user_generate_number_input()
result_input = square_number(value_input)
print(f"The square of {value_input} is {result_input}")

