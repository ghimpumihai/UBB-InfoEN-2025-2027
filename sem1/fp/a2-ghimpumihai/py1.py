# binary search iterative insert sort heap sort
import random

def binary_search(input_list:list[int], x:int) -> int:
    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == x:
            return mid
        elif input_list[mid] > x:
            right = mid - 1
        elif input_list[mid] < x:
            left = mid + 1
    return -1

def verify_steps()->int:
    while True:
        try:
            number_of_steps = int(input("Enter the period of printing partial lists: "))
            if number_of_steps >0:
                break
            else:
                print("Please enter an integer greater than 0.")
        except ValueError:
            print('Please enter a valid number: ')
    return number_of_steps

def insert_sort(input_list:list[int],number_of_steps:int) -> None:
    step = 0
    for i in range(1,len(input_list)):
        p = i
        while p > 0 and input_list[p] < input_list[p - 1]:
            input_list[p], input_list[p - 1] = input_list[p-1], input_list[p]
            step += 1
            if step % number_of_steps == 0:
                print("The list at step " + str(step) + ": " + str(input_list))
            p = p - 1
    print("The list after the final step(" + str(step) + "): " + str(input_list))

def heapify(input_list:list[int], list_length:int, node:int, number_of_steps:int, step:list[int])-> None:
    largest = node
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    # If left child is larger than root
    if left_child < list_length and input_list[left_child] > input_list[largest]:
        largest = left_child

    # If right child is larger than largest so far
    if right_child < list_length and input_list[right_child] > input_list[largest]:
        largest = right_child

    # If largest is not root
    if largest != node:
        input_list[node], input_list[largest] = input_list[largest], input_list[node]  # Swap
        step[0] += 1  # Increment the step counter
        if step[0] % number_of_steps == 0:
            print("The list at step " + str(step[0]) + ": " + str(input_list))
        # Recursively heapify the affected sub-tree
        heapify(input_list, list_length, largest, number_of_steps, step)

def heap_sort(input_list:list[int],number_of_steps:int) -> None:
    list_length = len(input_list)
    step = [0]  # Step counter stored in a list, passed by reference
    # Build heap (rearrange array)
    for i in range(list_length // 2 - 1, -1, -1):
        heapify(input_list, list_length, i, number_of_steps, step)

    # One by one extract an element from heap
    for i in range(list_length - 1, 0, -1):
        # Move root to end
        input_list[0], input_list[i] = input_list[i], input_list[0]
        step[0] += 1  # Increment the step counter
        if step[0] % number_of_steps == 0:
            print("The list at step " + str(step[0]) + ": " + str(input_list))
        # Call max heapify on the reduced heap
        heapify(input_list, i, 0, number_of_steps, step)

    print("The list after the final step (" + str(step[0]) + "): " + str(input_list))

def generate_list() -> list[int]:
    input_list = []
    while True:
        try:
            list_length = int(input('Please enter the length of the list: '))
            if list_length<=0:
                print("Please choose an integer larger than 0!")
            else:
                break
        except ValueError:
            print('Please enter a valid option: ')
    for i in range(list_length):
        input_list.append(random.randint(0, 1000))
    print("The list was generated with success! The list:", input_list)
    return input_list

def menu()->None:
    is_generated=is_sorted=0
    while True:
        print('1.Generate a list of n random natural numbers.')
        print('2.Search for an item in the list using Binary Search.')
        print('3.Sort the list using Insertion Sort.')
        print('4.Sort the list using Heap Sort.')
        print('5.Exit the program')
        while True:
            try:
                choice = int(input('Please choose an option: '))
                break
            except ValueError:
                print('Please enter a valid option!')
        if choice == 1:
            input_list = generate_list()
            is_generated = 1
            is_sorted = 0
        elif choice == 2:
            if is_generated == 0:
                print("You have to generate the list before you search!")
            else:
                if is_sorted == 1:
                    while True:
                        try:
                            target = int(input('Please enter the number you want to find: '))
                            break
                        except ValueError:
                            print('Please enter a valid number: ')
                    target_position = binary_search(input_list, target)
                    if target_position != -1:
                        print("The position of the element is: " + str(target_position))
                    else:
                        print("The element doesn't exist in the list!")
                else:
                    print("You have to sort the list before you search!")
        elif choice == 3:
            if is_generated == 0:
                print("You have to generate the list before you sort!")
            else:
                number_of_steps=verify_steps()
                insert_sort(input_list,number_of_steps)
                is_sorted = 1
        elif choice == 4:
            if is_generated == 0:
                print("You have to generate the list before you sort!")
            else:
                number_of_steps=verify_steps()
                heap_sort(input_list,number_of_steps)
                is_sorted = 1
        elif choice == 5:
            exit(0)
        else:
            print('Please choose a valid option!\n')

menu()
