# question 9- insert 100 numbers print number of the highest insert.
number_of_inserts = 0
highest_value_of_insert = 0
while number_of_inserts < 5:
    value_of_insert = int(input('Insert a number: '))
    number_of_inserts = highest_value_of_insert
    number_of_inserts += 1
    if value_of_insert > highest_value_of_insert:
        highest_value_of_insert == value_of_insert
print('The highest number you inserted is ' + str(highest_value_of_insert))








