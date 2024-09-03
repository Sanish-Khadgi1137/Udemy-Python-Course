#issue of floting point arthematic see https://docs.python.org/3/tutorial/floatingpoint.html
bill=float(input("What was the total Bill :$ "))

tips=int(input("How much tips would you like to give :(in%) "))

people =int(input("How many people would you like to split the bill to : "))

tips_amt = bill * tips / 100

total_bill = bill + tips_amt

bill_per_person= total_bill / people

final_bill = round (bill_per_person,2)

print(final_bill)
# for $150 ,12% and 5 ppl we get 33.6 not in 2 digit so to get in 2 digit we use formating "{:.2f}".format() now answer is 33.60

final_bills="{:.2f}".format(final_bill)

print(f"Bill per person is {final_bills}")