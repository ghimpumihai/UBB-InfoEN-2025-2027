# Solve the problem from the third set here
import math


def verifyprime(input_number):
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
    copy_input_number = 1
    while input_number > 0:
        cc_input_number = copy_input_number
        if cc_input_number == 1 or verifyprime(cc_input_number) == 1:
            input_number = input_number - 1
            if input_number <= 0:
                return copy_input_number
        else:
            prime_divisor = 2
            while cc_input_number != 1:
                power = 0
                while cc_input_number % prime_divisor == 0:
                    cc_input_number = cc_input_number // prime_divisor
                    power += 1
                if power > 0:
                    input_number = input_number - prime_divisor
                    if input_number <= 0:
                        return prime_divisor
                prime_divisor = prime_divisor + 1
                if prime_divisor * prime_divisor > cc_input_number:
                    prime_divisor = cc_input_number
        copy_input_number = copy_input_number + 1


def main():
    print("Please enter the position of the element:", end=' ')
    input_number = int(input())
    answer = solve(input_number)
    if input_number%10==1:
        print("The {}st".format(input_number) + " element of the sequence is {}".format(answer) )
    elif input_number%10==2:
        print("The {}nd".format(input_number) + " element of the sequence is {}".format(answer))
    elif input_number%10==3:
        print("The {}rd".format(input_number) + " element of the sequence is {}".format(answer))
    else:
        print("The {}th".format(input_number) + " element of the sequence is {}".format(answer))


main()
