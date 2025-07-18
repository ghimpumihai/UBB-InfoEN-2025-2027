# Solve the problem from the second set here
import math

def product_of_proper_factors(input_number):
    product = 1
    for i in range(2, int(math.sqrt(input_number)) + 1):
        if input_number % i == 0:
            j = input_number // i
            product = product * i
            if i != j:
                product = product * j
    return product


def main():
    print("Please enter a number:", end=' ')
    input_number = int(input())
    result = product_of_proper_factors(input_number)
    print("The product of proper factors of {}".format(input_number) + " is {}".format(result))


main()
