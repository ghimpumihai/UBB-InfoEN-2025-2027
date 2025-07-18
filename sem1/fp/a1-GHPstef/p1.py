# Solve the problem from the first set here
import math


def verify_prime(input_number):
    if input_number == 0 or input_number == 1:
        return 0
    if input_number == 2:
        return 1
    if input_number % 2 == 0:
        return 0
    for i in range(3, int(math.sqrt(input_number)), 2):
        if input_number % i == 0:
            return 0
    return 1

def solve(input_number):
    for i in range(input_number - 1, 1, -1):
        if verify_prime(i):
            return i
    return 0


def main():
    print("Please enter a number:", end=' ')
    input_number = int(input())
    result = solve(input_number)
    if result == 0:
        print("There is no smaller prime number than {}".format(input_number))
    else:
        print("The largest prime number smaller than {}".format(input_number)+" is {}".format(result))


main()
