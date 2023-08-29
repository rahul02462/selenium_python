tasks = []

def add_task():
    a = input("Enter the task")
    tasks.append(a)
    print("Task added Successfully..!")

def show_task():
    if len(tasks) == 0:
        print("No task available!")
    else:
        print("Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index},{task}")

while True:
    print("Menu")
    print("1.Add Task")
    print("2.Complete Tasks")
    print("3.Show Task")
    print("4.Quit")

    choice = input("Enter your choice (1-4):")

    if choice == '1':
        add_task()
    elif choice == '2':
        complete_task()
    elif choice == '3':
        show_task()
    elif choice == '4':
        print("Thank you for choicing to do list application!!!!")
        break
    else:
        print("Invalid choice")