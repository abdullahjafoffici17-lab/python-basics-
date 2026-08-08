weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "Underweight"
elif bmi <= 24.9:
    result = "Normal weight"
elif bmi <= 29.9:
    result = "Overweight"
else:
    result = "Obese"

print("Your BMI is:", bmi)
print("Your Result is:", result)
