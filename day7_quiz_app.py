score = 0
answer1 = input("what is 10 % 3? ")
if answer1 == "1":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!") 
        

answer2 = input("Is python case sensitive? (yes/no): ")
if answer2.lower() == "yes":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer3 = input("what symbol is used for comments? ")
if answer3 =="#":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer4 = input("what does input() always return? ")
if answer4 == "string":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer5 = input("what is '5' == 5? (True/False) ")
if answer5.lower() == "false":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

    
print("your score:", score, "out of 5")


if score == 5:
    print("Perfect! you're mastering in python basics!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("You need more practice.Review week 1!")
          

