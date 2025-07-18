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
def prime(n,primes:list[int]):
    for i in range(1,n):
        if check_prime(i):
            primes.append(i)

def bkt_recursive(n,lista,rez,setrez):
    for i in lista:
        n=n-i
        rez.append(i)
        if n==0 and frozenset(rez) not in setrez:
            print(rez)
            setrez[(frozenset(rez))]=1
        elif n>0:
            bkt_recursive(n,lista,rez,setrez)
        n=n+i
        rez.pop()

def start():
    ok=0
    lista=[]
    rez=[]
    setrez={}
    while ok==0:
        try:
            n=int(input("Please enter a number: "))
            ok=1
        except ValueError:
            print("Enter a valid number")
    prime(n,lista)
    bkt_recursive(n,lista,rez,setrez)
start()