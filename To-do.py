import json
print("=========To-Do List=========")
with open("tasks.json", "r") as file:
    tasks = json.load(file)

print(tasks)
loop = True

while(loop):
    user_choice = int(input( 
        "==============\n" 
        "1. Add Task\n"
        "2. Remove Task\n"
        "3. Show Tasks\n"
        "4. Quit\n"
        "==============\n"
        ">"
    ))

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
        print("============")
        for task in tasks:
            print(task["title"]," - ",task["status"])
        print("============")
    elif user_choice == 4:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Goodbye")
        loop = False        
    else:
        print("Choice out of bounds")



