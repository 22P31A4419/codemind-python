for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=sorted(l)
    if(l==r):
       print(0)
    else:
        print(max(l)-min(l))
    
   