todo_list = []
done = False

print('Type "done" at any time to exit')

while not done:
    print("Todo List: " + str(todo_list))
    new_item = input("add an item to the to-do list ")

    if new_item != "done":
        todo_list.append(new_item)

    elif new_item == "done":
        done = True

print(todo_list)
