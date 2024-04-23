n=int(input())
t=n*(n-1)
for i in range(2,n-1):
    t=t*(n-i)


print(t)