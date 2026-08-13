tasks = []
tasks.append("Study Python")
tasks.append("Read Quran")
tasks.append("GO to School")
tasks.append("Do Exercise")
tasks.append("Wake up 5 o' clock")
tasks.append("Complete homework")
tasks.append("Play Basketball")
tasks.append("Read Book")
tasks.append("Learn New thing")

my_tasks = []

task1 = input("Enter task 1: ")
my_tasks.append(task1)

task2 = input("Enter task 2: ")
my_tasks.append(task2)

task3 = input("Enter task 3: ")
my_tasks.append(task3)

print("your tasks:")
count = 1
for task in my_tasks:
    print(f"{count}. {task}")
    count = count + 1


