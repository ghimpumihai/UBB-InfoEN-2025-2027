def bkt(a,k,s,rez,rezp,rez2):
    for i in range(k,len(a)):
        s=s+a[i]
        rez.append(a[i])
        rezp.append(i)
        if s==sum(a)//2:
            print(rez)
            for j in range(len(a)):
                if j not in rezp:
                    rez2.append(a[j])
            print(rez2)
            exit(0)
        elif s<sum(a)//2:
            bkt(a,i+1,s,rez,rezp,rez2)
        s=s-a[i]
        rez.pop()
        rezp.pop()



def main():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    x=sum(a)
    if x%2==1:
        print("Impossible to divide in 2 subsets")
    else:
        bkt(a,0,0,[],[],[])
        print("Impossible to divide in 2 subsets")

main()