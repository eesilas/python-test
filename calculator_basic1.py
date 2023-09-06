# define the calculator function
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid operator'

# get user input
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operator = input('Enter the operator (+, -, *, /): ')

# call the calculator function and print the result
result = calculator(num1, num2, operator)
print('Result: ', result)