#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from src.functions import *
from random import *
from texttable import *

def transform_complex(z):
    while True:
        try:
            complex_number = [0, 0]
            z = z.replace(" ", "").replace("i", "")
            if '+' in z:
                real, imag = z.split('+')
            elif '-' in z[1:]:
                real, imag = z.split('-', 1)
                imag = '-' + imag
            set_real(complex_number, int(real))
            set_imag(complex_number, int(imag))
            return complex_number
        except ValueError:
            print("Invalid input. Please enter a complex number in the form a+bi.")

def display(in_list):
    texttable = Texttable()
    texttable.add_row(["Index","Number"])
    for i in range(len(in_list)):
        texttable.add_row([i, str(get_real(in_list[i])) + "+" + str(get_imag(in_list[i])) + "i"])
    print(texttable.draw())

def start():
    in_list = [[0, 0] for _ in range(10)]
    stack = [in_list.copy()]
    for i in range(10):
        set_real(in_list[i], randint(-1000, 1000))
        set_imag(in_list[i], randint(-1000, 1000))
    tests()
    while True:
        n = input("Enter a command: ")
        prop = n.split()
        if prop[0]=='add':
            try:
                complex_number=transform_complex(prop[1])
                in_list=add(in_list,complex_number)
                stack.append(in_list.copy())
            except:
                print("Please enter a valid input.")
        elif prop[0]=='insert':
            try:
                complex_number=transform_complex(prop[1])
                in_list=insert(in_list,complex_number,int(prop[3]))
                stack.append(in_list.copy())
            except IndexError:
                print("Please enter an index that is within the bounds of the list.")
            except:
                print("Please enter a valid input.")
        elif prop[0]=='remove':
            if len(in_list)==0:
                print("There are no more elements to remove.")
            else:
                if 'to' in prop:
                    try:
                        in_list=remove_multiple(int(prop[1]),int(prop[3]),in_list)
                        stack.append(in_list.copy())
                    except IndexError:
                        print("Please enter values within the list's range.")
                    except:
                        print("Please enter a valid input.")
                else:
                    try:
                        in_list=remove(int(prop[1]),in_list)
                        stack.append(in_list.copy())
                    except:
                        print("Please enter a valid input.")
        elif prop[0]=='replace':
            try:
                replace(transform_complex(prop[1]),transform_complex(prop[3]),in_list)
                stack.append(in_list.copy())
            except:
                print("Please enter a valid input.")
        elif prop[0]=='list':
            if len(in_list)==0:
                print("The list is empty.")
            else:
                if len(prop)==1:
                    display(in_list)
                else:
                    if prop[1]=='real':
                        try:
                            result=list_real(in_list,int(prop[2]),int(prop[4]))
                            if len(result)==0:
                                print("There are no elements that satisfy the condition.")
                            else:
                                display(result)
                        except:
                            print("Please enter a valid input.")
                    elif prop[1]=='modulo':
                        try:
                            result=list_modulo(in_list,prop[2],int(prop[3]))
                            if len(result) == 0:
                                print("There are no elements that satisfy the condition.")
                            else:
                                display(result)
                        except:
                            print("Please enter a valid input.")
        elif prop[0]=='filter':
            if 'real' in prop:
                try:
                    in_list=filter_real(in_list)
                    stack.append(in_list.copy())
                except:
                    print("Please enter a valid input.")
            elif 'modulo' in prop:
                try:
                    in_list=filter_modulo(in_list,prop[2],int(prop[3]))
                    stack.append(in_list.copy())
                except:
                    print("Please enter a valid input.")
            else:
                print("Invalid input")
        elif prop[0]=='undo':
            try:
                stack=undo(stack.copy())
                in_list=stack[-1]
            except IndexError:
                print("There are no more operations to undo.")
        elif prop[0]=='exit':
            exit(0)
        else:
            print("Invalid command. Please try again.")