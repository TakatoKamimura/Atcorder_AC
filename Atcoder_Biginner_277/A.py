n,x=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]==x:
        print(i+1)
        exit()