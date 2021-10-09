# input an integer number and print the number of digits
tens = 10
number_of_digits = 1
number = int(input('input an integer number:'))
while number // tens >= 1:
    number_of_digits += 1
    tens *= 10

print('The number of digits is: ' + str(number_of_digits))
