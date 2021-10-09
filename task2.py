while True:
    number1 = int(input('input first number:'))
    if number1 != 0:
        number2 = int(input('input second number:'))
        while number2 != 0:
            if number1 > number2:
                print('Bigger')
            else:
                print('Second number was bigger than first')
                break
