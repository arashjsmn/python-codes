a=int(input('number?'))
b=int(input('number?'))
try:
    if b>a:
        for i in range(a,b+1):
            if i == 1:
                continue
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
    elif a>b:
        for i in range(b,a+1):
            if i == 1:
                continue
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
    elif a==b:
        for i in range(2,a):
            if i == 1:
                print('this number is smaller than the expected limit number!')
                break
            if a%i==0:
                    break
        else:
            print(i)
except:
    print('these numbers are smaller than the ecxpected limit numbers!')