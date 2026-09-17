import json
print("=========To-Do List=========")
with open("tasks.json", "r") as file:
    tasks = json.load(file)

loop = True

while(loop):
    try:
        user_choice = int(input( 
            "==============\n" 
            "1. Add Task\n"
            "2. Remove Task\n"
            "3. Show Tasks\n"
            "4. Edit task\n"
            "5. Quit\n"
            "==============\n"
            ">"
        ))
    except:
        print("Please enter a number from 1 to 4.")
        continue

    if user_choice == 1:
        task = input("Enter task: ")
        tasks.append({
            "title": task,
            "status": "Incomplete"
        })
    elif user_choice == 2:
        task_position = int(input("Task position (number): "))
        tasks.remove(tasks[task_position-1])
  
    elif user_choice == 3:
        print("=====================================")
        for task in tasks:
            print(task["title"]," - ",task["status"])
        print("=====================================")

    elif user_choice == 4:
        task_to_edit = int(input("Which task would you like to edit (number): "))
        edit_type = int(input("Would like to edit the task name or status (1,2): "))
        if edit_type == 1:
            tasks[task_to_edit - 1]["title"] = input("Enter Task replacement: ")
        elif edit_type == 2:
            status = int(input("Set task status (1)incomplete, (2)complete, (3)in progress"))
            tasks[task_to_edit -1]["status"] = "incomplete" if status == 1 else "complete" if status == 2 else "in progress"
    elif user_choice == 5:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Goodbye")
        loop = False        
    else:
        print("Choice out of bounds")



