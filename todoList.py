# run in a while loop until user quits

# create an array to store tasks(dict)
tasks = []

# print lines to format the output


def print_lines():
    print("------------------ \n")

# function that runs in while statement -- takes user #input and runs appropriate function


def chooser(user_input):
    if user_input == "1":
        add_task()
    elif user_input == "2":
        delete_task()
    elif user_input == "3":
        view_all_tasks()
        input("Hit return to continue: ")


def show_menu():
    # show_menu
    print_lines()
    print("To ENTER a new task, enter 1: ")
    print("To DELETE a task, enter 2: ")
    print("To VIEW all tasks, enter 3: ")
    print("To QUIT the app, enter 'q': ")
    print_lines()


def add_task():
    # add task(dict)
    task_name = input("Enter name of task: ")
    task_priority = input("Enter task priority - (low, medium, high): ")
    # store elements in a dictionary, task
    task = {"title": task_name, "priority": task_priority}
    # store dict(task) in an array(tasks)
    tasks.append(task)


def view_all_tasks():
    # view all tasks
    print_lines()
    for i in range(0, len(tasks)):
        # can use task = tasks[i] !!!
        print(f"{i + 1} - {tasks[i]['title']} - {tasks[i]['priority']}")
    print_lines()
    # prints all tasks added by user


def delete_task():
    # show task names
    print("This is the list of tasks to delete from: ")
    view_all_tasks()
    # give user a choice of which task to delete
    to_delete = int(input("Enter the task number to delete the task: "))
    to_delete -= 1

    # delete the task and confirm deletion
    for i in range(len(tasks)):
        if i == to_delete:
            to_go = tasks[i]
            del tasks[i]
            print(f"You just deleted the {to_go['title']}task. ")


# While loop showing main menu
user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Please enter a choice from the menu: ")
    chooser(user_input)
