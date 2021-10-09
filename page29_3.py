while True:
    number = int(input('Enter a number'))
    if number < 0:
        break
    else:
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += number % 10
            number = number // 10
        print('Sum of digits is: ' + str(sum_of_digits))