to_do = input("Enter your tasks seperated by ',': ")
to_do_list = to_do.split(",")
print (to_do_list)

option = input("add, remove, display: ")

if option == "add":
    add_task = input("Add task seperatd by ',': ")
    to_do_list.append(add_task)
    print(to_do_list)
elif option == "remove":
    rm_task = input("Enter task you want to remove using ',': ")
    remove_task = rm_task.split(",")
    for task in remove_task:
        if task in to_do_list:
            to_do_list.remove(task)
        print(to_do_list)
else:
    print(to_do_list)

