number1 = 0
number2 = 0
while True:
    while number1 == 0:
        number1 = int(input('input first number:'))
    while number2 == 0:
        number2 = int(input('input second number:'))
    if number1 > number2:
        print('Bigger')
        number1 = 0
        number2 = 0
    else:
        print('Second number was bigger than first')
        break




