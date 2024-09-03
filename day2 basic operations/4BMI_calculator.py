#BMI calculator

height=input("Enter your heigh (meters): ")
weight=input("Enter your weight (kilogram): ")

bmi = int(weight )/ float(height) **2;

#to get whole(int) not float
BMI=float(bmi)

print(BMI)