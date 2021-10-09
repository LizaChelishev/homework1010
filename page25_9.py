# question 9- insert 100 numbers print number of the highest insert.
number_of_inserts = 0
highest_value_of_insert = 0
serial_number_of_highest_number = 0
while number_of_inserts < 100:
    value_of_insert = int(input('Insert a number: '))
    number_of_inserts += 1
    if value_of_insert > highest_value_of_insert:
        highest_value_of_insert = value_of_insert
        serial_number_of_highest_number = number_of_inserts
print('The serial number off the highest number you inserted is ' + str(serial_number_of_highest_number))








