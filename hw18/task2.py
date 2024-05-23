def fuctorial(a):
    m=1
    l=1
    while m<=a:
        l=l*m
        m+=1
    return 1
n=int(input())
k=int(input())
h=fuctorial(n)/(fuctorial(n-k)*fuctorial(k))
print(h) 