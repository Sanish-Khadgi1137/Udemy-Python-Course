#WAP to add 2 digits in a 2 digit number 87= 8+7 =15

#input() function take any data type and assign to variable as string
two_digit_number = input("write a two digit number: ");

# function ""type()" give the "type" of the input(show what is input type)
print(type(two_digit_number))

first_digit  =two_digit_number[0]
second_digit =two_digit_number[1]

print(first_digit)
print(second_digit)

# since input() keep any values as string below give cancatination
result = first_digit + second_digit
print(result)

# changining the datatye of the above variables which results addition
result = int(first_digit) + int(second_digit)
print(result)
