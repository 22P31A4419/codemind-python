a=int(input())
s=list(map(int,input().strip().split()))
x=set(s)
x=sorted(x)
print(x[len(x)-3]) if len(x)>=3 else print(max(x))