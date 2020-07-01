n = int(input())
res = 0;
flag = False
for i in range(n+1):
    s = str(i)
    flag = True
    for j in s:
        if(j == '7'):
            flag = False
            break
    if(i%7==0):
        flag = False
    if(flag):
        res += i
print(res)
