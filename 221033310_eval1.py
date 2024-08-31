#Advanced Task Management system



def add_task(t_name, t_id , t_status):
    if t_id in main_task:
        print(f"Task with ID {t_id} already exists.")
    else:
        
        main_task[id] = {
            'Name': t_name,
            'Status': t_status,
           
        }
        print(f"Task '{t_name}' added successfully.")
        
def update_task(t_name, t_id, t_status):
    main_task[id] = {
            'Name': t_name,
            'Status': t_status,
           
        }
    print("Updated")
    

def delete_task(t_id):
    del main_task[t_id]


def list_stack():
    print(main_task)

def search_task(t_id):
    print(main_task[id])

def list_task_last(ch):
    for key, value in main_task.items():
        t_name = value.get("Name")
        if t_name[-1] == ch:
            print(main_task[key])

print("Welcome to Advanced Task Managament System")
main_task = {}
while True:
    print("Choose from the following functions below that you want to perform: ")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. List all tasks")
    print("5. Search a task")
    print("6. List task from the last letter")
    ch = int(input("Enter the index number of the function that you want to perform: "))
    if ch==1:
        
        print("Enter the details of the task that you want to enter: ")
        t_name = input("Enter the name of the task: ")
        t_id = int(input("Ënter the id of the task: "))
        t_status=input("Enter the status of the task: ")
       
        add_task(t_name, t_id, t_status)
    elif ch==2:
            t_id = int(input("Ënter the id of the task: "))
            t_name = input("Enter the name of the task: ")  
            t_status=input("Enter the status of the task: ")
            update_task(t_name, t_id, t_status)
    elif ch==3:
            t_id = int(input("Ënter the id of the task: "))
            delete_task(t_id)
    elif ch==4:
            list_stack()
    elif ch==5:
              t_id = int(input("Ënter the id of the task: "))
              search_task(t_id)
    elif ch==6:
        ch = input("Enter the last letter")
        list_task_last(ch)
