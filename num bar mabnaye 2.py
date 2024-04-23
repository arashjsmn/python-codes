n=int(input())
c=''
while n//2 !=0:
    c+=str(n%2)
    n=n//2
c+=str(n%2)
print(c)
