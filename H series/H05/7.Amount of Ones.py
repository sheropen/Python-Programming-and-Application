n = int(input())
res = 0
for i in range(n+1):
    s = str(i)
    for c in s:
        if(c == '1'):
            res += 1

print(res)

