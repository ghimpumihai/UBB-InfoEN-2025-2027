#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#

import math
#A
def get_real(c:list[int])->int:
    return c[0]

def get_imag(c:list[int])->int:
    return c[1]

def set_real(c:list[int], real:int)->None:
    c[0] = real

def set_imag(c:list[int], imag:int)->None:
    c[1] = imag

def add(in_list:list, complex_number:list)->list:
    """
    Adds a complex number to the list.

    Parameters:
    in_list (list): The list of complex numbers.
    complex_number (list): The complex number to add, represented as a list [real, imag].

    Returns:
    list: The updated list of complex numbers.
    """
    in_list.append([get_real(complex_number), get_imag(complex_number)])
    return in_list

def insert(in_list:list, complex_number:list, position:int)->list:
    """
    Inserts a complex number at a specified position in the list.

    Parameters:
    in_list (list): The list of complex numbers.
    complex_number (list): The complex number to insert, represented as a list [real, imag].
    position (int): The position at which to insert the complex number.

    Returns:
    list: The updated list of complex numbers.
    """
    in_list.insert(position, [get_real(complex_number), get_imag(complex_number)])
    return in_list

def remove(position:int, in_list:list)->list:
    """
    Removes a complex number from the list at a specified position.

    Parameters:
    position (int): The position of the complex number to remove.
    in_list (list): The list of complex numbers.

    Returns:
    list: The updated list of complex numbers.
    """
    in_list.pop(position)
    return in_list

def remove_multiple(start_position:int, end_position:int, in_list:list)->list:
    """
    Removes multiple complex numbers from the list within a specified range.

    Parameters:
    start_position (int): The starting position of the range.
    end_position (int): The ending position of the range.
    in_list (list): The list of complex numbers.

    Returns:
    list: The updated list of complex numbers.
    """
    i = end_position - start_position + 1
    while i:
        in_list.pop(start_position)
        i -= 1
    return in_list

def replace(old_number:list, new_number:list, in_list:list)->list:
    """
    Replaces an old complex number with a new complex number in the list.

    Parameters:
    old_number (list): The old complex number to replace, represented as a list [real, imag].
    new_number (list): The new complex number to insert, represented as a list [real, imag].
    in_list (list): The list of complex numbers.

    Returns:
    list: The updated list of complex numbers.
    """
    for i in range(len(in_list)):
        if get_real(in_list[i]) == get_real(old_number) and get_imag(in_list[i]) == get_imag(old_number):
            in_list[i] = [get_real(new_number), get_imag(new_number)]
    return in_list



def list_real(in_list:list, start:int, end:int)->list:
    """
    Lists all complex numbers with an imaginary part of zero within a specified range.

    Parameters:
    in_list (list): The list of complex numbers.
    start (int): The starting position of the range.
    end (int): The ending position of the range.

    Returns:
    list: A list of complex numbers with an imaginary part of zero within the specified range.
    """
    result = []
    for i in range(start, end + 1):
        if get_imag(in_list[i]) == 0:
            result.append(in_list[i])
    return result

def list_modulo(in_list:list, comp:str, nr:int)->list:
    """
    Lists all complex numbers based on their modulus and a comparison operator.

    Parameters:
    in_list (list): The list of complex numbers.
    comp (str): The comparison operator ('>', '<', or '=').
    nr (int): The number to compare the modulus against.

    Returns:
    list: A list of complex numbers that satisfy the comparison condition.
    """
    result = []
    if comp == '>':
        for i in in_list:
            if get_real(i) ** 2 + get_imag(i) ** 2 > nr:
                result.append(i)
    elif comp == '<':
        for i in in_list:
            if get_real(i) ** 2 + get_imag(i) ** 2 < nr:
                result.append(i)
    else:
        for i in in_list:
            if get_real(i) ** 2 + get_imag(i) ** 2 == nr:
                result.append(i)
    return result

def filter_real(in_list:list)->list:
    """
    Filters the list to keep only complex numbers with an imaginary part of zero.

    Parameters:
    in_list (list): The list of complex numbers.

    Returns:
    list: The filtered list of complex numbers.
    """
    copy_list=[]
    for i in in_list:
        if get_imag(i) == 0:
            copy_list.append(i)
    return copy_list

def filter_modulo(in_list:list, comp:str, nr:int)->list:
    """
    Filters the list of complex numbers based on their modulus and a comparison operator.

    Parameters:
    in_list (list): The list of complex numbers.
    comp (str): The comparison operator ('>', '<', or '=').
    nr (int): The number to compare the modulus against.

    Returns:
    list: The filtered list of complex numbers.
    """
    copy_list=[]
    if comp == '>':
        for i in in_list:
            if math.sqrt(get_real(i) ** 2 + get_imag(i) ** 2) > nr:
                copy_list.append(i)
    elif comp == '<':
        for i in in_list:
            if math.sqrt(get_real(i) ** 2 + get_imag(i) ** 2) < nr:
                copy_list.append(i)
    else:
        for i in in_list:
            if math.sqrt(get_real(i) ** 2 + get_imag(i) ** 2) != nr:
                copy_list.append(i)
    return copy_list

def undo(stack:list)->list:
    """
    Undoes the last operation that modified the list.

    Parameters:
    stack (list): The stack of previous states of the list.

    Returns:
    None
    """
    stack.pop()
    return stack
def add_test():
    """
    Tests the add function by asserting the expected output for given inputs.
    """
    l = []
    assert add(l, [1, 2]) == [[1, 2]]
    assert add(l, [3, 4]) == [[1, 2], [3, 4]]

def insert_test():
    """
    Tests the insert function by asserting the expected output for given inputs.
    """
    l = []
    assert insert(l, [1, 2], 0) == [[1, 2]]
    assert insert(l, [3, 4], 0) == [[3, 4], [1, 2]]
    assert insert(l, [5, 6], 1) == [[3, 4], [5, 6], [1, 2]]

def remove_test():
    """
    Tests the remove function by asserting the expected output for given inputs.
    """
    l = [[1, 2], [3, 4], [5, 6]]
    assert remove(1, l) == [[1, 2], [5, 6]]
    assert remove(0, l) == [[5, 6]]
    assert remove(0, l) == []

def remove_multiple_test():
    """
    Tests the remove_multiple function by asserting the expected output for given inputs.
    """
    l = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    assert remove_multiple(0, 1, l) == [[5, 6], [7, 8], [9, 10]]
    assert remove_multiple(0, 2, l) == []

def replace_test():
    """
    Tests the replace function by asserting the expected output for given inputs.
    """
    l = [[1, 2], [3, 4], [5, 6]]
    assert replace([1, 2], [7, 8], l) == [[7, 8], [3, 4], [5, 6]]
    assert replace([3, 4], [9, 10], l) == [[7, 8], [9, 10], [5, 6]]
    assert replace([1, 1], [1, 1], l) == [[7, 8], [9, 10], [5, 6]]

def tests():
    """
    Runs all the test functions to validate the program's functionality.
    """
    add_test()
    insert_test()
    remove_test()
    remove_multiple_test()
    replace_test()
