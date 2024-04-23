n=int(input())
m=int(input())
bmm=0
kmm=0
for i in range(1,n+1):
    if n%i == 0:
        if m%i == 0:
            bmm=i
while kmm%m!=0 or kmm==0:
    kmm+=n
print(f"bmm is: {bmm}")
print(f"kmm is: {kmm}")