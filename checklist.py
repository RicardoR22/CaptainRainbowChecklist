checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    update(index, ("{} {}".format("√", checklist[index])))
    list_all_items()


def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code.lower() == "c":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code.lower() == "r":
        item_index = user_input("Index number? ")
        if int(item_index) < len(checklist):
            print(read(int(item_index)))
        else: print("Invalid Index")
        # Update item
    elif function_code.lower() == "u":
        item_index = user_input("Index number? ")
        if int(item_index) < len(checklist):
            updated_item = user_input("Replace " + checklist[int(item_index)] + " with? ")
            update(int(item_index), updated_item)
        else: print("Invalid Index")

        # Destroy item
    elif function_code.lower() == "d":
        item_index = user_input("Index number? ")
        if int(item_index) < len(checklist):
            destroy(int(item_index))
        else: print("Invalid Index")

        # Print all items
    elif function_code.lower() == "p":
        list_all_items()

        # Stop our while loop
    elif function_code.lower() == "q":
        return False

        # Checkmark an item in list
    elif function_code.lower() == "check":
        item_index = user_input("Index number? ")
        if int(item_index) < len(checklist):
            mark_completed(int(item_index))
        else: print("Invalid Index")

    # Catch all
    else:
        print("Unknown Option")

    return True

def test():
    create("Cats")
    create("Dogs")
    create("CatDog")

test()

running = True
while running:
    selection = user_input(
        """
        Press C to add to list,
        Press R to Read from list,
        Press U to Update an item in list,
        Press D to Delete an item from list,
        Press P to display list,
        Type Check to mark an item as complete,
        Press Q to quit

        """)
    running = select(selection)
