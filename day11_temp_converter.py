def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


temp = celsius_to_fahrenheit(30)
print(temp)

def farhenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return(celsius)

temp = farhenheit_to_celsius(212)
print(temp)


def add(a,b):
    return a + b
result = add(3,4)
print(result)

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

result = is_positive(5)
print(result)

result2 = is_positive(-3)
print(result2)

def greet(name):
    return "Hello," + name

print(greet("Abdul"))
print(greet("Ahamed"))




def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
         return "Underweight"
    elif bmi < 24.9:
        return "Normalweight"
    elif bmi < 29.9:
        return "overweight"
    else:
        return "obese"

result = calculate_bmi(93,1.9)
print(result)

def calculate_grade(marks,attendance):

    if attendance < 75:
        return  "Fail - Insufficient Attendance"
    elif marks >= 90 and attendance >= 75:
        return  "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

result = calculate_grade(78,75)
print("Your Grade is:", result)

def multiply(a,b):
    return a * b

result = multiply(4,5)
print(result)


def is_even(number):
    balance = number % 2

    if balance > 0:
        return "odd number"
    else:
        return "even number"

result = is_even(3)
print(result)


def is_leap_year(year):
    

    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not leap year"

result = is_leap_year(1900)
print(result)



def check_password_length(password):
    
    if len(password) > 8:
        return "GOOD"
    else:
        return "BAD"

result = check_password_length("23")
print(result)



































    
