import timeit
import random

#3rd homework functions
#best case:omega(n) the list is already sorted so the algorithms does not enter the while loop
#worst case:O(n^2) the list is sorted but in the reverse so the algorithm has to make the maximum number of changes which is n*(n-1)/2
#average case:theta(n^2) let's take all the possible cases of the number of changes done in a list: 1+2+3+...+(n^2-n)/2=(n^2-n)/2*((n^2-n+1)/2+1)/(n^2-n)/2=(n^2-n)/2+1=
def insert_sort(input_list:list[int])->float:
    start=timeit.default_timer()
    for i in range(len(input_list) - 1):
        p = i
        while p > 0 and input_list[p] < input_list[p - 1]:
            input_list[p], input_list[p - 1] = input_list[p], input_list[p - 1]
            p = p - 1
    end=timeit.default_timer()
    return end-start

#best case:omega(nlogn) if we use the heapify function(it creates a max heap,takes the root to the end and repeats the process n times) or O(n) if all the elements are equal and don't use heapify
#worst case:O(nlogn) heap sort doesn't have a worst case because each time it is building a new max heap and adding the root to the end of the list so the worst case=average case=O(nlogn)
#average case:theta(nlogn)
def heapify(input_list:list[int], n:int, node:int):
    largest = node
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    # If left child is larger than root
    if left_child < n and input_list[left_child] > input_list[largest]:
        largest = left_child

    # If right child is larger than largest so far
    if right_child < n and input_list[right_child] > input_list[largest]:
        largest = right_child

    # If largest is not root
    if largest != node:
        input_list[node], input_list[largest] = input_list[largest], input_list[node]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(input_list, n, largest)

def heap_sort(input_list:list[int]):
    start=timeit.default_timer()
    n = len(input_list)
    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(input_list, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        # Move root to end
        input_list[0], input_list[i] = input_list[i], input_list[0]
        # Call max heapify on the reduced heap
        heapify(input_list, i, 0)
    end=timeit.default_timer()
    return end-start
#best case: omega(1) if the element we are searching for is right in the middle
#worst case:O(logn) if the elements is the first one or the last one, the algorithm does logn steps to find it
#average case:theta(logn) let's take all the posibilities if the element is found and if it doesn't exist in the list: (1+2+3+..+logn)/n+(logn+logn+....+logn)/n=logn
def binary_search(input_list:list[int], x:int) -> float:
        start=timeit.default_timer()
        left=0
        right=len(input_list)-1
        rez=x
        while left<=right:
            mid=(left+right)//2
            if input_list[mid]==rez:
                end=timeit.default_timer()
                return end-start
            elif input_list[mid]<rez:
                left=mid+1
            else:
                right=mid-1
        end=timeit.default_timer()
        return end-start

def worst_case_generate()->list[list[int]]:
    input_list1 = []
    for i in range(500):
        input_list1.append(random.randint(0, 2 ** 32))
    input_list1.sort(reverse=True)
    input_list2 = []
    for i in range(1000):
        input_list2.append(random.randint(0, 2 ** 32))
    input_list2.sort(reverse=True)
    input_list3 = []
    for i in range(2000):
        input_list3.append(random.randint(0, 2 ** 32))
    input_list3.sort(reverse=True)
    input_list4 = []
    for i in range(4000):
        input_list4.append(random.randint(0, 2 ** 32))
    input_list4.sort(reverse=True)
    input_list5 = []
    for i in range(8000):
        input_list5.append(random.randint(0, 2 ** 32))
    input_list5.sort(reverse=True)
    return [input_list1, input_list2, input_list3, input_list4, input_list5]
def best_case_generate()->list[list[int]]:
    input_list1 = []
    for i in range(500):
        input_list1.append(random.randint(0, 2 ** 32))
    input_list1.sort()
    input_list2 = []
    for i in range(1000):
        input_list2.append(random.randint(0, 2 ** 32))
    input_list2.sort()
    input_list3 = []
    for i in range(2000):
        input_list3.append(random.randint(0, 2 ** 32))
    input_list3.sort()
    input_list4 = []
    for i in range(4000):
        input_list4.append(random.randint(0, 2 ** 32))
    input_list4.sort()
    input_list5 = []
    for i in range(8000):
        input_list5.append(random.randint(0, 2 ** 32))
    input_list5.sort()
    return [input_list1, input_list2, input_list3, input_list4, input_list5]
def average_case_generate()->list[list[int]]:
    input_list1 = []
    for i in range(500):
        input_list1.append(random.randint(0, 2 ** 32))
    input_list2 = []
    for i in range(1000):
        input_list2.append(random.randint(0, 2 ** 32))
    input_list3 = []
    for i in range(2000):
        input_list3.append(random.randint(0, 2 ** 32))
    input_list4 = []
    for i in range(4000):
        input_list4.append(random.randint(0, 2 ** 32))
    input_list5 = []
    for i in range(8000):
        input_list5.append(random.randint(0, 2 ** 32))
    return [input_list1, input_list2, input_list3, input_list4, input_list5]

def worst_case(worst_sort:list[list[int]]):
    rez=[]
    for i in worst_sort:
        ci=i
        insert_sort_time=insert_sort(ci)
        heap_sort_time=heap_sort(i)
        binary_search_time=binary_search(i,i[-1])
        rez.append([insert_sort_time, heap_sort_time, binary_search_time])
    return rez
def average_case(average_sort:list[list[int]]):
    rez=[]
    for i in average_sort:
        ci=i
        insert_sort_time=insert_sort(i)
        heap_sort_time=heap_sort(ci)
        binary_search_time=binary_search(i,random.choice(i))
        rez.append([insert_sort_time, heap_sort_time, binary_search_time])
    return rez
def best_case(best_sort:list[list[int]]):
    rez=[]
    for i in best_sort:
        insert_sort_time=insert_sort(i)
        heap_sort_time=heap_sort(i)
        binary_search_time=binary_search(i,i[len(i)//2])
        rez.append([insert_sort_time, heap_sort_time, binary_search_time])
    return rez

def worst_case_print(rez:list[list[float]])->None:
    x=500
    for i in rez:
        print("Worst case for insert sort with " + str(x) + " elements:" + str(i[0]))
        print("Worst case for heap sort with " + str(x) + " elements:" + str(i[1]))
        print("Worst case for binary search with " + str(x) + " elements:" + str(i[2]))
        x*=2
def best_case_print(rez:list[list[float]])->None:
    x=500
    for i in rez:
        print("Best case for insert sort with " + str(x) + " elements:" + str(i[0]))
        print("Best case for heap sort with " + str(x) + " elements:" + str(i[1]))
        print("Best case for binary search with " + str(x) + " elements:" + str(i[2]))
        x*=2
def average_case_print(rez:list[list[float]])->None:
    x=500
    for i in rez:
        print("Average case for insert sort with " + str(x) + " elements:" + str(i[0]))
        print("Average case for heap sort with " + str(x) + " elements:" + str(i[1]))
        print("Average case for binary search with " + str(x) + " elements:" + str(i[2]))
        x*=2
#2nd homework functions
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
def binary_search_steps(input_list: list[int], x: int) -> int:
    left = 0
    right = len(input_list) - 1
    rez = x
    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == rez:
            return mid
        elif input_list[mid] < rez:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def insert_sort_steps(input_list:list[int],number_of_steps:int) -> None:
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
def heapify_steps(input_list:list[int], list_length:int, node:int, number_of_steps:int, step:list[int])-> None:
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
        heapify_steps(input_list, list_length, largest, number_of_steps, step)
def heap_sort_steps(input_list:list[int],number_of_steps:int) -> None:
    list_length = len(input_list)
    step = [0]  # Step counter stored in a list, passed by reference
    # Build heap (rearrange array)
    for i in range(list_length // 2 - 1, -1, -1):
        heapify_steps(input_list, list_length, i, number_of_steps, step)

    # One by one extract an element from heap
    for i in range(list_length - 1, 0, -1):
        # Move root to end
        input_list[0], input_list[i] = input_list[i], input_list[0]
        step[0] += 1  # Increment the step counter
        if step[0] % number_of_steps == 0:
            print("The list at step " + str(step[0]) + ": " + str(input_list))
        # Call max heapify on the reduced heap
        heapify_steps(input_list, i, 0, number_of_steps, step)

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
        print('5.Worst case for Insert Sort,Heap Sort and Binary Search.')
        print('6.Average case for Insert Sort,Heap Sort and Binary Search.')
        print('7.Best case for Insert Sort,Heap Sort and Binary Search.')
        print('8.Exit program')
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
                insert_sort_steps(input_list,number_of_steps)
                is_sorted = 1
        elif choice == 4:
            if is_generated == 0:
                print("You have to generate the list before you sort!")
            else:
                number_of_steps=verify_steps()
                heap_sort_steps(input_list,number_of_steps)
                is_sorted = 1
        elif choice == 5:
            worst=worst_case_generate()
            rez=worst_case(worst)
            worst_case_print(rez)
        elif choice == 6:
            average=average_case_generate()
            rez=average_case(average)
            average_case_print(rez)
        elif choice == 7:
            best=best_case_generate()
            rez=best_case(best)
            best_case_print(rez)
        elif choice == 8:
            exit(0)
        else:
            print('Please choose a valid option!\n')

menu()
