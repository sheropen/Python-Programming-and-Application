import time
def fib(n):
    if n in (1,2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,35):
    start = time.time()
    res = fib(i)
    print('Time used: %.6f'%(time.time()-start),'seconds,','Fib(%d) ='%i,res)
    
