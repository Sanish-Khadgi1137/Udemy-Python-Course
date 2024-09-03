#WAP sum of even number from 1 to 100
#way1
total=0

#last one inside range "2" is step-size of the number and even start off from 2 so that taking 2 step size will be 4(even) if we had took 1 it would be 3(odd)
for number in range(2, 101 , 2):
    total += number
print(total)

#way2
total2=0

for number2 in range(1, 101):
    if number2 % 2 == 0:
        total2 += number2

print(total2)