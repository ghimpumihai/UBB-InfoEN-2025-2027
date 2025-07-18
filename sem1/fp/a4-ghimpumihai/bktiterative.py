#bkt
import math
def check_prime(n):
    if n<2:
        return 0
    elif n==2:
        return 1
    elif n%2==0:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return 0
    return 1
def generate_prime(n,primes:list[int]):
    for i in range(1,n):
        if check_prime(i):
            primes.append(i)
def bkt_iterative(n,lista):
    result=[]
    stack=[(0,0,[])]
    while stack:
        current_sum,index,current_decomposition=stack.pop()
        if current_sum==n:
            result.append(current_decomposition)
        for i in range(index,len(lista)):
            new_sum=current_sum+lista[i]
            if new_sum<=n:
                stack.append((new_sum,i,current_decomposition+[lista[i]]))
    print (result)
# current_decomposition list, current_sum tracks the sum of the current try,index tracks the index of the list so that sums cannot repeat to assure uniqueness

def start():
    ok=0
    lista=[]
    while ok==0:
        try:
            n=int(input("Please enter a number: "))
            ok=1
        except ValueError:
            print("Enter a valid number")
    generate_prime(n,lista)
    bkt_iterative(n,lista)
start()