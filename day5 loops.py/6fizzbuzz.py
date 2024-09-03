#fizzbuzz game one of the most asked question in interview
for num in range (1, 101):

    '''if() check for first condition if it gets true then display 
    without going throug all. If there is a condiontion that
    need to check 2 condition where first codition is same as first if()
    then it will be skipped if put it after first condition 
    so we put "num % 3 ==0 and num % 4 == 0" at first'''
    if num % 3 == 0 and num % 4 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 4 == 0:
        print("buzz")
    else:
        print(num)