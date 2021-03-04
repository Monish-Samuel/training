a = int(input('Enter the number 1: '))
b = int(input('Enter the number 2: '))

try:
    c = a / b
except Exception as e:
    print('Exception error: ', e)
    c = None

print(f'The division of {a} by {b} is: ', c)
