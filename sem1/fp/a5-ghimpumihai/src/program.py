# setA:3
# setB:3
# Write the implementation for A5 in this file
#

#
# Write below this comment
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
import random
def create_complex(real, imag):
    return [real, imag]

def get_real(c):
    return c[0]

def get_imag(c):
    return c[1]

def set_real_list(c, real):
    c[0] = real

def set_imag_list(c, imag):
    c[1] = imag

def complex_to_str(c):
    if c[1]<0:
        return f"{c[0]} - {abs(c[1])}i"
    else:
        return f"{c[0]} + {c[1]}i"


#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
#
# def create_complex(real, imag):
#     return {'real': real, 'imag': imag}
#
# def get_real(c):
#     return c['real']
#
# def get_imag(c):
#     return c['imag']
#
# def set_real(c, real):
#     c['real'] = real
#
# def set_imag(c, imag):
#     c['imag'] = imag
#
# def complex_to_str(c):
#     if c['imag'] < 0:
#         return f"{c['real']} - {abs(c['imag'])}i"
#     else:
#         return f"{c['real']} + {c['imag']}i"

#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def max_subarray_incr_mod(numbers):
    """
    Finds the longest subarray of complex numbers where the modulus of each number is strictly increasing.

    :param numbers: list of complex numbers represented as lists [real, imag]
    :return: tuple containing the length of the longest subarray and the subarray itself
    """
    start = end = s = 0
    max_length = 1
    last_modulus = get_real(numbers[0])**2 + get_imag(numbers[0])**2

    for i in range(1, len(numbers)):
        modulus = get_real(numbers[i])**2 + get_imag(numbers[i])**2
        if modulus > last_modulus:
            if i - s + 1 > max_length:
                max_length = i - s + 1
                start = s
                end = i
        else:
            s = i
        last_modulus = modulus

    return end - start + 1, numbers[start:end + 1]


def max_subarray_sum_real(numbers):
    """
    Finds the subarray of complex numbers with the maximum sum of real parts.

    :param numbers: list of complex numbers represented as lists [real, imag]
    :return: tuple containing the length of the subarray with the maximum sum and the subarray itself
    """
    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0

    for i in range(len(numbers)):
        current_sum += get_real(numbers[i])

        if max_sum < current_sum:
            max_sum = current_sum
            start = s
            end = i

        if current_sum < 0:
            current_sum = 0
            s = i + 1

    return end - start + 1, numbers[start:end + 1]
#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#
def read_complex_number(n):
    d=[]
    for i in range(n):
        z = input("Enter a complex number (z = a + bi): ")
        z = z.replace(" ", "").replace("i", "")
        if '+' in z:
            real, imag = z.split('+')
        elif '-' in z[1:]:
            real, imag = z.split('-', 1)
            imag = '-' + imag
        d.append(create_complex(int(real), int(imag)))
    return d
def print_complex_number(c):
    print(complex_to_str(c))

def choice_read_ver():
    while True:
        try:
            choice = int(input("Choose an option: "))
            break
        except ValueError:
            print("Invalid option. Please try again.")
    return choice
def menu():
    print("1. Read a list of complex numbers")
    print("2. Display the entire list of numbers")
    print("3. Display the sequence required by the properties")
    print("4. Exit")

def main():
    numbers = [
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000)),
        create_complex(random.randint(-1000,1000), random.randint(-1000,1000))
    ]
    while True:
        menu()
        choice=choice_read_ver()
        if choice == 1:
            n=int(input("Enter the number of complex numbers: "))
            numbers=read_complex_number(n)
        elif choice == 2:
            for number in numbers:
                print_complex_number(number)
        elif choice == 3:
            length , subarray= max_subarray_incr_mod(numbers)
            subarray1=[]
            for i in range(len(subarray)):
               subarray1.append(complex_to_str(subarray[i]))
            print("Set A: " + str(length)+" "+str(subarray1))

            length, subarray = max_subarray_sum_real(numbers)
            subarray1 = []
            for i in range(len(subarray)):
                subarray1.append(complex_to_str(subarray[i]))
            print("Set B: " + str(length) + " " + str(subarray1))
        elif choice == 4:
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
   main()



