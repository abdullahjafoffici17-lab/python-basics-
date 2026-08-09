marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

if attendance < 75:
    result = "Fail - Insufficient Attendance"
elif marks >= 90 and attendance >= 75:
    result = "A"
elif marks >= 75:
    result = "B"
elif marks >= 60:
    result = "C"
elif marks >= 40:
    result = "D"
else:
    result = "F"

print("Your Grade is:", result)
