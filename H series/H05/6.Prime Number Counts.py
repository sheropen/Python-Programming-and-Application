a = int(input())
b = int(input())
res = 0
for n in range(a,b+1):
    flag = True
    for i in range(2,n):
        if(n % i == 0):
            flag = False
            break
    if(flag and n != 1):
        res += 1
print(res)
