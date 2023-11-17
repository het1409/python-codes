shopping_items = input("Enter Shopping list: ")
shopping_list = shopping_items.split()

option = input("add, remove, display: ")

if option == "add":
    in_list = input("Add item in the list: ")
    shopping_list.append(in_list)
    print(shopping_list)
elif option == "remove":
    rm_item = input("Item to want to remove: ")
    shopping_list.remove(rm_item)
    print(shopping_list)
else:
    print(shopping_list)